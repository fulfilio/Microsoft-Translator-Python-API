# -*- coding: utf-8 -*-
"""
    __init__
    A translator using the micrsoft translation engine documented here:
    https://docs.microsoft.com/en-us/azure/cognitive-services/translator/
"""

__all__ = ['Translator', 'TranslatorException']

try:
    import simplejson as json
except ImportError:
    import json

import requests
import logging
from datetime import datetime, timedelta

logger = logging.getLogger('microsofttranslator')

class AzureAuthToken:
    """ Class to make sure that .value is always a valid 10-min auth token """
    _token = None
    last_fetched = None

    def __init__(self, api_key):
        self.azure_api_key = api_key

    @property
    def value(self):
        """ The value of the current auth token """
        if self._token is None or self.outdated:
            self.update()
        return self._token

    @property
    def outdated(self):
        """ Returns True if a new token value must be fetched """
        return self.last_fetched is None or \
               datetime.utcnow() > self.last_fetched+timedelta(minutes=9)

    def update(self):
        url = 'https://api.cognitive.microsoft.com/sts/v1.0/issueToken'
        headers = {'Ocp-Apim-Subscription-Key': self.azure_api_key}
        resp = requests.post(url, headers=headers)
        self._token = resp.text
        self.last_fetched = datetime.utcnow()

class TranslatorException(Exception):
    def __init__(self, code, message, *args):
        self.code = code
        self.message = message
        super(TranslatorException, self).__init__('%d-%s' % (self.code, self.message), *args)

class Translator(object):
    """ Implements the Azure Cognitive Services - Translator REST API """

    base_url = 'https://api.cognitive.microsofttranslator.com'

    def __init__(self, client_key):
        self.auth_token = AzureAuthToken(client_key)

    def call(self, path, params, json=None):
        """
        Calls the given path with the params urlencoded.
        Will be POST if json is defined, otherwise a GET.

        :param path: The path of the API call being made
        :param params: The parameters dictionary for the query string
        :param json: JSON data for POST body.
        """
        params = params.copy()
        params.update({'api-version': '3.0'})
        url = self.base_url + '/' + path

        headers = {'Authorization': 'Bearer %s' % self.auth_token.value}
        if json:
            query_params = map(lambda e: '%s=%s' % e, params.items())
            url += '?' + '&'.join(query_params)
            resp = requests.post(url, json=json, headers=headers)
        else:
            resp = requests.get(url, params=params, headers=headers)
        resp.encoding = 'UTF-8-sig'
        rv = resp.json()

        if 'error' in rv:
            error = rv['error']
            raise TranslatorException(error['code'], error['message'])

        return rv

    @staticmethod
    def texts_as_json(texts):
        return [{'Text': text.encode('utf8')} for text in texts]

    def get_languages(self):
        """
        Fetches the languages supported by Microsoft Translator
        Returns list of languages
        """
        return self.call('languages', {})['translation']

    def translate(
            self, texts,
            to_lang, from_lang=None,
            text_type='plain', category='general'):
        """
        Translates one or more text strings from one language to another.

        :param texts:
            A string array representing the texts to translate.
        :param to_lang:
            A string representing the language code to translate the text into.
            Can be many languages separated by comma.
        :param from_lang:
            A string representing the language code of the translation text.
            If left None the response will include
            the result of language auto-detection. (Default: None)
        :param text_type:
            The format of the text being translated.
            The supported formats are "plain" and "html".
            Any HTML needs to be well-formed.
        :param category:
            The category of the text to translate.
            The only supported category is "general".
        """
        params = {
            'to': to_lang,
            'textType': text_type,
            'category': category,
        }
        if from_lang: params['from'] = from_lang
        translated = self.call('translate', params, json=Translator.texts_as_json(texts))
        translated = [[inner['text'] for inner in outer['translations']] for outer in translated]
        return translated

    def detect_language(self, texts):
        """
        Detects language of given string
        Returns two letter language - Example : fr
        :param texts: A string array representing the texts to detect language.
        """
        return self.call('detect', {}, json=Translator.texts_as_json(texts))

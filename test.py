# -*- coding: utf-8 -*-
"""
    test
    Test the translator
"""
import os
import unittest
from . import Translator, TranslatorException

azure_translator_key = os.environ['AZURE_TRANSLATOR_KEY']

default_languages = ['en', 'fr', 'de']

class TestTranslator(unittest.TestCase):
    def test_translate(self):
        client = Translator(azure_translator_key)
        translated = client.translate(['hello', 'how are you?'], 'pt,fr')
        self.assertEqual(translated, [
            [u'Ol\xe1', u'Bonjour'],
            [u'Como est\xe1?', u'Comment vas-tu?'],
        ])

    def test_invalid_translator_key(self):
        client = Translator('invalid_translator_key')
        with self.assertRaises(TranslatorException):
            client.translate(['hello'], 'pt')

    def test_invalid_language(self):
        client = Translator(azure_translator_key)
        with self.assertRaises(TranslatorException):
            client.translate(['hello'], 'abcd')

    def test_get_languages(self):
        client = Translator(azure_translator_key)
        languages = client.get_languages()
        for language in default_languages:
            self.assertIn(language, languages)

    def test_detect_language(self):
        client = Translator(azure_translator_key)
        detected_language = client.detect_language(['how are you?'])[0]
        self.assertEqual(detected_language['language'], 'en')

def test_all():
    loader = unittest.TestLoader()
    suite = unittest.TestSuite()
    suite.addTests(loader.loadTestsFromTestCase(TestTranslator))
    return suite


if __name__ == '__main__':
    unittest.main()

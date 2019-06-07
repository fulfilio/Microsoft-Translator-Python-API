Microsoft Translator V3 -- Python API
=====================================

:Version: 0.9
:Web: http://fulfil.io/
:keywords: Microsoft Translator
:copyright: Fulfil.IO, Openlabs Technologies & Consulting (P) LTD
:license: BSD

.. image:: https://secure.travis-ci.org/fulfilio/Microsoft-Translator-Python-API.png?branch=master
   :target: http://travis-ci.org/#!/fulfilio/Microsoft-Translator-Python-API

.. image:: https://coveralls.io/repos/fulfilio/Microsoft-Translator-Python-API/badge.png?branch=master
  :target: https://coveralls.io/r/fulfilio/Microsoft-Translator-Python-API


This python API implements the Microsoft Translator services which can be used 
in web or client applications to perform language translation operations. The 
services support users who are not familiar with the default language of a page 
or application, or those desiring to communicate with people of a different 
language group.


Create your Azure translation key
---------------------------------

To sign up for Translator Text API, please follow instructions here
https://docs.microsoft.com/en-us/azure/cognitive-services/translator/translator-text-how-to-signup

Installing
----------

::

      pip install microsofttranslator


Features
--------


Translation
+++++++++++

::

        >>> from microsofttranslator import Translator
        >>> translator = Translator('<Your Azure Translator Key>')
        >>> print translator.translate(['hello'], 'es')
        [['Hola']]


Translate multiple phrases and multiple languages at once
+++++++++++++++++++++++++++++++++++++++++++++++++++++++++

::

        >>> from microsofttranslator import Translator
        >>> translator = Translator('<Your Azure Translator Key>')
        >>> print translator.translate(['hello', 'good bye'], 'de,it')
        [
            ['Hallo', 'Ciao'],
            ['Auf Wiedersehen', 'Arrivederci']
        ]

Get supported languages
+++++++++++++++++++++++

::

        >>> from microsofttranslator import Translator
        >>> translator = Translator('<Your Azure Translator Key>')
        >>> print translator.get_languages()
        {
            ...
            'en': {'nativeName': 'English', 'name': 'English', 'dir': 'ltr'},
            'es': {'nativeName': 'Espa\xf1ol', 'name': 'Spanish', 'dir': 'ltr'},
            'et': {'nativeName': 'Eesti', 'name': 'Estonian', 'dir': 'ltr'},
            'fa': {'nativeName': 'Persian', 'name': 'Persian', 'dir': 'rtl'},
            'fi': {'nativeName': 'Suomi', 'name': 'Finnish', 'dir': 'ltr'},
            ...
        }

Detect Language
+++++++++++++++

::

        >>> from microsofttranslator import Translator
        >>> translator = Translator('<Your Azure Translator Key>')
        >>> translator.detect_language('how are you?')
        {
            'language': 'en',
            'score': 1.0,
            'isTranslationSupported': True,
            'isTransliterationSupported': False,
            'alternatives': [
                {'score': 1.0, 'isTranslationSupported': True, 'isTransliterationSupported': False, 'language': 'ro'},
                {'score': 1.0, 'isTranslationSupported': True, 'isTransliterationSupported': False, 'language': 'fil'}
            ]
        }



Bugs and Development on Github
------------------------------

https://github.com/fulfilio/Microsoft-Translator-Python-API

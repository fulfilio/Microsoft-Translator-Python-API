# -*- coding: utf-8 -*-
"""
    Microsoft translator API

    The Microsoft Translator services can be used in web or client
    applications to perform language translation operations. The services
    support users who are not familiar with the default language of a page or
    application, or those desiring to communicate with people of a different
    language group.

    This module implements the AJAX API for the Microsoft Translator service.

    An example::

        >>> from microsofttranslator import Translator
        >>> translator = Translator('<Your API Key>')
        >>> print translator.translate('Hello', 'pt')
        [['Olá']]

    The documentation for the service can be obtained here:
    https://docs.microsoft.com/en-us/azure/cognitive-services/translator/

    The project is hosted on GitHub where your could fork the project or report
    issues. Visit https://github.com/fulfilio/Microsoft-Translator-Python-API
"""

import codecs
from setuptools import setup

setup(
    name='microsofttranslator',
    version='0.9',
    packages=[
        'microsofttranslator',
    ],
    package_dir={
        'microsofttranslator': '.'
    },
    author='Fulfil.IO Inc., Openlabs Technologies & Consulting (P) Limited',
    author_email='info@fulfil.io',
    description='Microsoft Translator V3 - Python API',
    long_description=codecs.open(
        'README.rst', encoding='UTF-8'
    ).read(),
    license='BSD',
    keywords='translation microsoft',
    url='https://www.fulfil.io/',
    include_package_data=True,
    classifiers=[
        'Development Status :: 5 - Production/Stable',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: BSD License',
        'Natural Language :: English',
        'Operating System :: OS Independent',
        'Topic :: Software Development :: Internationalization',
        'Topic :: Utilities',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 2',
    ],
    test_suite='microsofttranslator.test.test_all',
    install_requires=[
        'requests >= 1.2.3',
        'six',
    ]
)

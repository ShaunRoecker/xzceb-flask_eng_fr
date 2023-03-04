import json
from ibm_watson import LanguageTranslatorV3
from ibm_cloud_sdk_core.authenticators import IAMAuthenticator
import os
from dotenv import load_dotenv

load_dotenv()

apikey = os.environ['apikey']
url = os.environ['url']


authenticator = IAMAuthenticator(apikey)
language_translator = LanguageTranslatorV3(
    version='2018-05-01',
    authenticator=authenticator
)

language_translator.set_service_url(url)

language_translator.set_disable_ssl_verification(True)

translation = language_translator.translate(
    text='Hello, how are you today?',
    model_id='en-es').get_result()
print(json.dumps(translation, indent=2, ensure_ascii=False))


def english_to_french(english_text):
    '''Translates english text to french'''
    translation = language_translator.translate(
    english_text,
    model_id='en-fr').get_result()
    return translation

def french_to_english(french_text):
    '''Translates french text to english'''
    translation = language_translator.translate(
    french_text,
    model_id='fr-en').get_result()
    return translation


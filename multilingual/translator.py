# TRANSLATION
from googletrans import Translator

translator = Translator()

def translate_to_english(text):
    return translator.translate(text, dest='en').text

def translate_back(text, lang):
    return translator.translate(text, dest=lang).text

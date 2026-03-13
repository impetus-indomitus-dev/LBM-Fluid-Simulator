# -*- coding: utf-8 -*-
import lang_zh
import lang_en
import lang_es

# Mapping of language codes to their respective module dictionaries
LANGUAGES = {
    "zh": lang_zh.LANG_ZH,
    "en": lang_en.LANG_EN,
    "es": lang_es.LANG_ES
}

# Current global language state
CURRENT_LANG = "zh"

def get_text(key):
    """
    Retrieve text for a given key in the current language.
    Falls back to ZH if key is missing in current language.
    """
    lang_dict = LANGUAGES.get(CURRENT_LANG, LANGUAGES["zh"])
    
    return lang_dict.get(key, LANGUAGES["zh"].get(key, key))

def set_language(lang_code):
    global CURRENT_LANG
    if lang_code in LANGUAGES:
        CURRENT_LANG = lang_code

# config_loader.py

import os
import config

def get_bible_api_key():
    return os.getenv("BIBLE_API_KEY") or config.BIBLE_API_KEY

def get_openai_api_key():
    return os.getenv("OPENAI_API_KEY") or config.OPENAI_API_KEY

def get_notes_directory():
    return os.getenv("BIBLESTUDY_NOTES_DIRECTORY") or config.BIBLESTUDY_NOTES_DIRECTORY

def get_nlt_api_key():
    return os.getenv("NLT_API_KEY") or config.NLT_API_KEY

def get_esv_api_key():
    return os.getenv("ESV_API_KEY") or config.ESV_API_KEY
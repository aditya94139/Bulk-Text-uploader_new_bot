import os

class Config(object):
    BOT_TOKEN = os.environ.get("BOT_TOKEN", "7120497132:AAGWW5GfPgQG0D4fu4llnfY_KY3_GnurtDc")
    API_ID = int(os.environ.get("API_ID", 23291931)
    API_HASH = os.environ.get("API_HASH", "4b11dd648188731fb7c9bc8083e8791c")
    AUTH_USERS = os.environ.get("AUTH_USERS", "6594402123")

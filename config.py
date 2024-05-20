import os

class Config(object):
    BOT_TOKEN = os.environ.get("BOT_TOKEN", "7165589893:AAFv6ySRRhkxq0gRTXIOfysXr4hsBwWq2ac")
    API_ID = int(os.environ.get("API_ID", 25586552))
    API_HASH = os.environ.get("API_HASH", "f265cba9d76dc6ad70914accbe758f47")
    AUTH_USERS = os.environ.get("AUTH_USERS", "1368753935")

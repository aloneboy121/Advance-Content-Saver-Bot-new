from os import environ 

class Config:
    API_ID = environ.get("API_ID", "23881274")
    API_HASH = environ.get("API_HASH", "c867262073a58ccdebcae19601c5bf5f")
    BOT_TOKEN = environ.get("BOT_TOKEN", "6662067892:AAGHRuBY4_A2Vft3VP34H1TnVA_mz5Z8azw") 
    BOT_SESSION = environ.get("BOT_SESSION", "bot") 
    DATABASE_URI = environ.get("DATABASE", "mongodb+srv://24x7repairsericecenter:CKHPNQA8IaEiVGpt@saveee.cbx213c.mongodb.net/")
    DATABASE_NAME = environ.get("DATABASE_NAME", "24x7repairsericecenter")
    BOT_OWNER_ID = [int(id) for id in environ.get("BOT_OWNER_ID", '6964148334').split()]

class temp(object): 
    lock = {}
    CANCEL = {}
    forwardings = 0
    BANNED_USERS = []
    IS_FRWD_CHAT = []
    

from os import environ 

class Config:
    API_ID = environ.get("API_ID", "26395620")
    API_HASH = environ.get("API_HASH", "906cc7e4b4c1ad7f7121efc2244d13ad")
    BOT_TOKEN = environ.get("BOT_TOKEN", "6835498210:AAGrEMgO8TA-4wT1bndrrA3_zcEAepO4_zQ") 
    BOT_SESSION = environ.get("BOT_SESSION", "BQGi8fAAtq_BW6HD8apsFYv-FU9XfCSGdia5xf9xr58VxAHZOnR6qS9rgsp3X2152lMmJxs0dysnodGCulc6s7zvuVTYXKMMzOF-pYdJA6Ib3HRqJkyU_of3gf7HTc1dIyixJncxY_No1teocYA_GO1tfKFf21Hlsnh7vNokmjr814CBQK9dGetS67bvcQTEvjoexcYI55O_r7MnFBfQoFgjA7vbm1HuHbTIoeHyfb1_OpE5DxuX7M8AeUDTnHrl_m-AHT8ZiDtxm3QXrGMpr8QRri5s5j8PQOkcv8nimH2f66qbaWjOY_noGdUzqJ2X5ipLiT-NYPit517mQZMyxudAf5-XZwAAAAF7vQiuAA") 
    DATABASE_URI = environ.get("DATABASE", "mongodb+srv://24x7repairsericecenter:CKHPNQA8IaEiVGpt@saveee.cbx213c.mongodb.net/")
    DATABASE_NAME = environ.get("DATABASE_NAME", "24x7repairsericecenter")
    BOT_OWNER_ID = [int(id) for id in environ.get("BOT_OWNER_ID", '7047183902').split()]

class temp(object): 
    lock = {}
    CANCEL = {}
    forwardings = 0
    BANNED_USERS = []
    IS_FRWD_CHAT = []
    

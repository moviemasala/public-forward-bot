import os
import logging
class Config:                                                                   
    API_ID = int(os.environ.get("API_ID", "16374594"))
    API_HASH = os.environ.get("API_HASH", "ebabe6cf7ba47c82c109fdf4cf553205")       
    BOT_TOKEN = os.environ.get("BOT_TOKEN", "5496479323:AAF5091WC3q4TUaeE247rZBRHgAZfoLEBDc")
    BOT_SESSION = os.environ.get("BOT_SESSION", "forwardbot")
    OWNER_ID = os.environ.get("OWNER_ID", "995932132")                             
    DATABASE_URI = os.environ.get("DATABASE_URI", "mongodb+srv://MM:MM@cluster0.jrwebpe.mongodb.net/?retryWrites=true&w=majority")  
    DATABASE_NAME = os.environ.get("DATABASE_NAME", "Cluste0")
    COLLECTION_NAME = os.environ.get('COLLECTION_NAME', 'Data')
    SESSION = os.environ.get("SESSION", "")   
    TO_CHANNEL = int(os.environ.get("TO_CHANNEL", "-1001551361967"))
    BOT_USERNAME= os.environ.get("BOT_USERNAME", "@STRANGE_45_BOT")


def LOGGER(name: str) -> logging.Logger:
    return logging.getLogger(name)

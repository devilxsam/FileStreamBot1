from os import environ as env
from dotenv import load_dotenv

load_dotenv()

class Telegram:
    API_ID = int(env.get("API_ID", '29689475'))
    API_HASH = str(env.get("API_HASH", 'e550c215a6720df4c747ddf8febf1686'))
    BOT_TOKEN = str(env.get("BOT_TOKEN", '6993152634:AAEc-ztX6jmSeoC81lRpQXhyROJObtI9gYM'))
    OWNER_ID = int(env.get('OWNER_ID', '5882105086'))
    WORKERS = int(env.get("WORKERS", "6"))  # 6 workers = 6 commands at once
    DATABASE_URL = str(env.get('DATABASE_URL', 'mongodb+srv://narcos0017:4pXHYgjaECjVLu9i@cluster0.bottupl.mongodb.net/?retryWrites=true&w=majority'))
    UPDATES_CHANNEL = str(env.get('UPDATES_CHANNEL', "TADxBotz"))
    SESSION_NAME = str(env.get('SESSION_NAME', 'FileStream'))
    FORCE_SUB_ID = env.get('FORCE_SUB_ID', None)
    FORCE_SUB = env.get('FORCE_UPDATES_CHANNEL', False)
    FORCE_SUB = True if str(FORCE_SUB).lower() == "true" else False
    SLEEP_THRESHOLD = int(env.get("SLEEP_THRESHOLD", "60"))
    FILE_PIC = env.get('FILE_PIC', "https://graph.org/file/5bb9935be0229adf98b73.jpg")
    START_PIC = env.get('START_PIC', "https://graph.org/file/290af25276fa34fa8f0aa.jpg")
    VERIFY_PIC = env.get('VERIFY_PIC', "https://graph.org/file/736e21cc0efa4d8c2a0e4.jpg")
    MULTI_CLIENT = False
    FLOG_CHANNEL = int(env.get("FLOG_CHANNEL", "-1002034021960"))   # Logs channel for file logs
    ULOG_CHANNEL = int(env.get("ULOG_CHANNEL", "-1002034021960"))   # Logs channel for user logs
    MODE = env.get("MODE", "primary")
    SECONDARY = True if MODE.lower() == "secondary" else False
    AUTH_USERS = list(set(int(x) for x in str(env.get("AUTH_USERS", "5882105086")).split()))

class Server:
    PORT = int(env.get("PORT", "4040"))
    BIND_ADDRESS = str(env.get("BIND_ADDRESS", "0.0.0.0"))
    PING_INTERVAL = int(env.get("PING_INTERVAL", "1200"))
    HAS_SSL = str(env.get("HAS_SSL", "0").lower()) in ("1", "true", "t", "yes", "y")
    NO_PORT = str(env.get("NO_PORT", "1").lower()) in ("1", "true", "t", "yes", "y")
    FQDN = str(env.get("FQDN", "216.107.138.148:4040"))
    URL = "http{}://{}{}/".format(
        "s" if HAS_SSL else "", FQDN, "" if NO_PORT else ":" + str(PORT)
    )


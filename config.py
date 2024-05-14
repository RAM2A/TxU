import os

API_ID = API_ID = 24665357

API_HASH = os.environ.get("API_HASH", "beb7e4b83ada668fa85f9a9b56338f1d")

BOT_TOKEN = os.environ.get("BOT_TOKEN", "6700540841:AAEzEG75XEQXqfTGmIvy136zVclAUBxQKOI")

PASS_DB = int(os.environ.get("PASS_DB", "721"))

OWNER = int(os.environ.get("OWNER", 1717511106))

LOG = -1002137417670

try:
    ADMINS=[]
    for x in (os.environ.get("ADMINS", "1717511106").split()):
        ADMINS.append(int(x))
except ValueError:
        raise Exception("Your Admins list does not contain valid integers.")
ADMINS.append(OWNER)



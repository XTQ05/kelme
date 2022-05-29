from os import getenv
from dotenv import load_dotenv

load_dotenv()
que = {}
admins = {}

BOT_TOKEN = getenv("BOT_TOKEN", "5311094936:AAHbpGSeys8BjQ5uvm4gCGBhjfHYkWqWGWk")
BOT_NAME = getenv("BOT_NAME", "CrocadilBot") 
API_ID = int(getenv("API_ID" 11742375))
API_HASH = getenv("API_HASH", "0c37f648f2fea4cd39b35579eb7a2f64")
BOT_USERNAME = getenv("BOT_USERNAME", "Corcadildsidhlebot")
MONGO_DB_URI = getenv("MONGO_DB_URI", "mongodb+srv://nusrte:Nusret.2006@cluster0.r8ckx.mongodb.net/myFirstDatabase?retryWrites=true&w=majority")

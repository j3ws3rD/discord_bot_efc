VERSION = "0.0.0"
import os 
from dotenv import load_dotenv

# loading discord token
load_dotenv()
TOKEN = os.getenv("TOKEN")

print(os.listdir())

from lib.bot import BOT

BOT.run(TOKEN)
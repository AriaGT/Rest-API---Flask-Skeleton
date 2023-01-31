from dotenv import load_dotenv

load_dotenv()
import os

config = {
  "api": {
    "port": os.getenv("PORT") or 3000
  }
}

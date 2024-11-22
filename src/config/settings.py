import os
import dotenv

dotenv.load_dotenv()

# Email configuration
EMAIL_ADDRESS = os.getenv("EMAIL_ADDRESS")
EMAIL_PASSWORD = os.getenv("EMAIL_PASSWORD")
SMTP_SERVER = "smtp.gmail.com"
SMTP_PORT = 587
RESUME_PATH = os.getenv("RESUME_PATH")
FILE_PATH = os.getenv("FILE_PATH")

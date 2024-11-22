import os
import sys
import logging

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from src.service import ReferralEmailSender
from src.utils.logger import setup_logging


def main():
    setup_logging()
    try:
        sender = ReferralEmailSender()
        results = sender.send_bulk_emails(
            delay=2, resume_filename="John_Doe_Resume.pdf"
        )
    except Exception as e:
        logging.error(f"Application error: {str(e)}")


if __name__ == "__main__":
    main()

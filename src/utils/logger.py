import logging
from datetime import datetime


def setup_logging():
    """Setup logging configuration"""
    logging.basicConfig(
        filename=f'logs/email_logs_{datetime.now().strftime("%Y%m%d_%H%M%S")}.log',
        level=logging.INFO,
        format="%(asctime)s - %(levelname)s - %(message)s",
    )

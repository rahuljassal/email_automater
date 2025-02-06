import pandas as pd
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.mime.application import MIMEApplication
import time
import logging
from typing import Dict, List

from src.config.settings import *
from src.templates.email_template import create_email_content


class ReferralEmailSender:
    def __init__(self):
        self.excel_path = FILE_PATH
        self.sender_email = EMAIL_ADDRESS
        self.sender_password = EMAIL_PASSWORD
        self.smtp_server = SMTP_SERVER
        self.smtp_port = SMTP_PORT
        self.resume_filename = RESUME_FILENAME

    def read_excel_data(self) -> pd.DataFrame:
        try:
            df = pd.read_excel(self.excel_path)
            required_columns = ["email", "name", "company", "profile", "job link"]
            if not all(col in df.columns for col in required_columns):
                raise ValueError(f"Excel file must contain columns: {required_columns}")
            return df
        except Exception as e:
            logging.error(f"Error reading Excel file: {str(e)}")
            raise

    def send_email(
        self,
        recipient: str,
        subject: str,
        body: str,
        # resume_filename: str = RESUME_FILENAME,
    ) -> bool:
        try:
            msg = MIMEMultipart("alternative")
            msg["From"] = self.sender_email
            msg["To"] = recipient
            msg["Subject"] = subject

            msg.attach(MIMEText(body, "html"))

            # with open(RESUME_PATH, "rb") as f:
            #     resume = MIMEApplication(f.read(), _subtype="pdf")
            #     resume.add_header(
            #         "Content-Disposition",
            #         "attachment",
            #         filename=resume_filename,
            #     )
            #     msg.attach(resume)

            with smtplib.SMTP(self.smtp_server, self.smtp_port) as server:
                server.starttls()
                server.login(self.sender_email, self.sender_password)
                server.send_message(msg)

            return True
        except Exception as e:
            logging.error(f"Error sending email to {recipient}: {str(e)}")
            return False

    def send_bulk_emails(
        self, delay: int = 0, resume_filename: str = RESUME_FILENAME
    ) -> Dict[str, List[str]]:
        """
        Send emails to all contacts in the Excel file

        Args:
            delay: Delay between emails in seconds to avoid spam filters

        Returns:
            Dictionary containing successful and failed email addresses
        """
        results = {"successful": [], "failed": []}

        df = self.read_excel_data()
        total_emails = len(df)

        logging.info(f"Starting to send {total_emails} emails")

        for index, row in df.iterrows():
            try:
                email_content = create_email_content(
                    row["name"], row["company"], row["profile"], row["job link"]
                )

                logging.info(
                    f"Sending email to {row['email']} ({index + 1}/{total_emails})"
                )

                if self.send_email(
                    row["email"],
                    email_content["subject"],
                    email_content["body"],
                    # resume_filename,
                ):
                    results["successful"].append(row["email"])
                    logging.info(f"Successfully sent email to {row['email']}")
                else:
                    results["failed"].append(row["email"])
                    logging.error(f"Failed to send email to {row['email']}")

                # Add delay between emails
                if index < total_emails - 1:  # Don't delay after last email
                    time.sleep(delay)

            except Exception as e:
                results["failed"].append(row["email"])
                logging.error(f"Error processing {row['email']}: {str(e)}")

        logging.info(
            f"Email sending completed. Successful: {len(results['successful'])}, Failed: {len(results['failed'])}"
        )
        return results

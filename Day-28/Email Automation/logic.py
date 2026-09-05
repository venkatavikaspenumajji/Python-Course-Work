import smtplib
import os
import csv
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.base import MIMEBase
from email import encoders


SMTP_SERVER ="smtp.gmail.com"
SMPT_PORT =587
SENDER_EMAIL = "venkatavikaspenumajji@gamil.com"
SENDER_PASSWORD = " givv sjju lvpt qgni"

def send_email(to_email, subject, body, attachments=None):
    try:
        msg = MIMEMultipart()
        msg["From"] = SENDER_EMAIL
        msg["To"] = to_email
        msg["Subject"] = subject
        msg.attach(MIMEText(body, "plain")) 

        if attachments:
            for file_path in attachments:
                if os .path.exists(file_path):
                    with open(file_path," rb") as f:
                        mime_base = MIMEBase("application","octet-stream")
                        mime_base.set_payload(f.read())
                        encoders.encode_base64(mime_base)
                        mime_base.add_header(
                            "Content-Disposition",
                            f"attachment; filename={os.path.basename(file_path)}"
                        )
                        msg.attach(mime_base)
                else:
                    print(f"File '{file_path}' not found. Skipping...")         






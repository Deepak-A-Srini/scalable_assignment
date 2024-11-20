import smtplib
from email.message import EmailMessage
import requests
import json
import requests
import os
from flask import Flask, jsonify, url_for
app = Flask(__name__)
port = int(os.environ.get('PORT', 5000))

@app.route("/email")
def send_email():
    """Sends an email using Gmail's SMTP server."""

    # Gmail credentials
    sender_email = "2023mt93122@wilp.bits-pilani.ac.in"
    password = ""

    try:
        # Create a message
        body = "This is a test email sent using Python."
        msg = EmailMessage()
        msg['Subject'] = "Test Email"
        msg['From'] = sender_email
        msg['To'] = ""
        msg.set_content(body)
    
        # Connect to Gmail's SMTP server
        with smtplib.SMTP_SSL('smtp.gmail.com', 587) as smtp:
            smtp.login(sender_email, password)
            smtp.send_message(msg)
        
        return str(1)
        
    except Exception as error:
        print(error)
        
        return error
    

# Example usage

if __name__ == "__main__":
    app.run(debug=True, host="", port=port)
'''   
url = url_for('send_email')
print(url)
'''
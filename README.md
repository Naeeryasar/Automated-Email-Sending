# Automated Email Sending

A simple Python project demonstrating how to send an email automatically through an SMTP server using Python's built-in `smtplib` and `email` libraries.

## Features

* SMTP email sending with Python
* STARTTLS support
* SMTP authentication
* Plain-text email messages
* Simple and easy-to-understand implementation
* No external Python packages required

## Requirements

* Python 3.8 or newer
* Internet connection
* SMTP account

## Project Structure

```text
Automated-Email-Sending/
├── main.py
└── README.md
```

## Installation

Clone the repository:

```bash
git clone https://github.com/Naeeryasar/Automated-Email-Sending.git
cd Automated-Email-Sending
```

Check your Python installation:

```bash
python --version
```

No additional Python packages are required because the project uses Python's standard library.

## How It Works

The project uses Python's built-in email and SMTP libraries:

* `smtplib` — connects to the SMTP server and sends the email
* `MIMEMultipart` — creates the email message
* `MIMEText` — creates the email body
* `starttls()` — establishes a secure TLS connection
* `login()` — authenticates with the SMTP server
* `sendmail()` — sends the email

## SMTP Configuration

The current example uses **Ethereal Email** for testing.

```text
SMTP Host: smtp.ethereal.email
SMTP Port: 587
Security: STARTTLS
```

## Run the Project

Execute:

```bash
python main.py
```

If the email is sent successfully, the program displays:

```text
Email sent successfully!
```

## Customize the Email

You can change the sender, recipient, subject, and message in `main.py`:

```python
sender_email = "your-email@example.com"
sender_password = "your-password"
receiver_email = "recipient@example.com"

subject = "Your Subject"
body = "Your email message"
```

### HTML Email

To send an HTML email instead of plain text:

```python
MIMEText(html_content, "html")
```

## Security

**Do not store real SMTP passwords or other sensitive credentials directly in source code.**

For testing and learning, credentials may be placed directly in the script. However, for production use, credentials should be stored in environment variables or a secure secret manager.

For example:

```text
SMTP_HOST=smtp.example.com
SMTP_PORT=587
SMTP_USERNAME=your-email@example.com
SMTP_PASSWORD=your-password
RECIPIENT_EMAIL=recipient@example.com
```

If a real password has already been committed to a public repository, it should be changed or revoked immediately.

## Automation

The current program sends an email whenever `main.py` is executed.

It can be scheduled using:

* Windows Task Scheduler
* Linux/macOS Cron
* GitHub Actions
* Other scheduling systems

For example:

```bash
python /path/to/Automated-Email-Sending/main.py
```

can be configured to run automatically at a specific time.

## Troubleshooting

### Authentication Failed

Check:

* SMTP username
* SMTP password
* SMTP server
* SMTP port
* Whether the provider requires an app password
* Whether SMTP authentication is enabled

### Connection Failed

Check:

* Internet connection
* SMTP hostname
* SMTP port
* Firewall settings
* Network restrictions

### TLS/SSL Error

Make sure the security method matches the SMTP provider.

Port `587` commonly uses STARTTLS, while port `465` commonly uses implicit SSL/TLS.

### Email Not Received

Check:

* Recipient email address
* Spam/junk folder
* SMTP delivery status
* SMTP provider restrictions
* Sending limits

## Future Improvements

Possible improvements include:

* Environment-variable configuration
* HTML email templates
* Multiple recipients
* CC/BCC support
* File attachments
* Error handling
* Logging
* Retry mechanism
* Database-based recipient management
* CSV recipient import
* Scheduled email campaigns
* Reusable email templates

## Author

**Naeer Yasar**

GitHub: https://github.com/Naeeryasar

## Repository

https://github.com/Naeeryasar/Automated-Email-Sending

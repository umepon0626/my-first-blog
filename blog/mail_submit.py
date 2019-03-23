from email.mime.text import MIMEText
from email.utils import formatdate


def create_message(subject, content, user):
    content_list = [subject, content, user]
    msg = MIMEText(
        "Subject:{0[subject]}\n Body: {0[content]}\n from:{0[user]}")
    msg["Subject"] = subject
    msg["From"] = ACCOUNT
    msg["To"] = ALIAS
    msg["Date"] = formatdate(localtime=True)
    return msg

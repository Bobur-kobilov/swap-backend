import config
import smtplib
import base64
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from .templates import success_template, kyc_error, already_swapped, expired_error, admin_error,kyc, error, kyc_duplicate


def send(txHash, address, requesterEmail, code):

    if code == '0':
        content = MIMEText(success_template.SUCCESS_TEMPLATE.format(tx_hash=txHash, address=address), 'html', _charset='utf-8')

    if code == '65545':
        content = MIMEText(already_swapped.MAIN_TEMPLATE.format(address=address), 'html', _charset='utf-8')    
    
    if code == '65540' or code == '65544':
       content = MIMEText(expired_error.MAIN_TEMPLATE.format(address=address), 'html', _charset='utf-8')    
    
    if code == '65538':
        content = MIMEText(kyc_error.MAIN_TEMPLATE.format(address=address), 'html', _charset='utf-8')
    
    if code == '65542' or code == '65537':
        content = MIMEText(admin_error.MAIN_TEMPLATE.format(address=address), 'html', _charset='utf-8')
    
    if code == '6' or code == '9':
        print(code)
        content = MIMEText(error.MAIN_TEMPLATE.format(address=address), 'html', _charset='utf-8')    
    
    msg = MIMEMultipart('alternative')
    msg['Subject'] = "Hdac-Atolo Coin Swap Information"
    msg['From'] = 'no-reply@hdactech.com'  # email change
    msg['To'] = requesterEmail
    msg.attach(content)

    a = smtplib.SMTP(config.MAILER_INFO['host'])
    a.ehlo()
    a.starttls()
    a.login(config.MAILER_INFO["sender"], config.MAILER_INFO["password"])
    a.sendmail("no-reply@hdac.io", requesterEmail, msg.as_string())
    a.quit()

def send_kyc(txHash,address,requesterEmail,success):
    if success == False:
        content = MIMEText(kyc_error.MAIN_TEMPLATE.format(tx_hash=txHash, address=address), 'html', _charset='utf-8')
    else:
        content = MIMEText(kyc.MAIN_TEMPLATE.format(tx_hash=txHash, address=address), 'html', _charset='utf-8')

    msg = MIMEMultipart('alternative')
    msg['Subject'] = "Hdac-Atolo Coin Swap Information"
    msg['From'] = 'no-reply@hdactech.com'  # email change
    msg['To'] = requesterEmail
    msg.attach(content)

    a = smtplib.SMTP(config.MAILER_INFO['host'])
    a.ehlo()
    a.starttls()
    a.login(config.MAILER_INFO["sender"], config.MAILER_INFO["password"])
    a.sendmail("no-reply@hdac.io", requesterEmail, msg.as_string())
    a.quit()

def send_kyc_duplicate(requesterEmail):
    
    content = MIMEText(kyc_duplicate.MAIN_TEMPLATE.format(), 'html', _charset='utf-8')

    msg = MIMEMultipart('alternative')
    msg['Subject'] = "Hdac-Atolo Coin Swap Information"
    msg['From'] = 'no-reply@hdactech.com'  # email change
    msg['To'] = requesterEmail
    msg.attach(content)

    a = smtplib.SMTP(config.MAILER_INFO['host'])
    a.ehlo()
    a.starttls()
    a.login(config.MAILER_INFO["sender"], config.MAILER_INFO["password"])
    a.sendmail("no-reply@hdac.io", requesterEmail, msg.as_string())
    a.quit()

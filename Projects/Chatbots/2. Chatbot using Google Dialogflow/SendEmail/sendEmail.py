import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.base import MIMEBase
from config_reader import ConfigReader


class EmailSender:
    # For sending an email you require certain things
    # 1) To: customer email
    # 2) From:The account from which you'll send the email(Basically your mail)
    # 2.1) For your account(ex. gmail) you'll need it's usernmame & pswrd
    # 3) You'll also need email subject, email body and email attachment

    def send_email_to_student(self, recepient_email, message):
        try:
            self.config_reader = ConfigReader()
            self.configuration = self.config_reader.read_config()

            # instance of MIMEMultipart
            self.msg = MIMEMultipart()

            # storing the senders email address
            self.msg['From'] = self.configuration['SENDER_EMAIL']

            # storing the receivers email address
            self.msg['To'] = ",".join(recepient_email)

            # storing the subject
            self.msg['Subject'] = self.configuration['EMAIL_SUBJECT']

            # string to store the body of the mail
            # body = "This will contain attachment"
            body = message

            # attach the body with the msg instance
            self.msg.attach(MIMEText(body, 'html'))

            # instance of MIMEBase and named as p
            self.p = MIMEBase('application', 'octet-stream')

            # creates SMTP session
            self.smtp = smtplib.SMTP('smtp.gmail.com', 587)

            # start TLS for security
            self.smtp.starttls()

            # Authentication
            self.smtp.login(self.msg['From'], self.configuration['PASSWORD'])

            # Converts the Multipart msg into a string
            self.text = self.msg.as_string()

            # sending the mail
            self.smtp.sendmail(self.msg['From'], recepient_email, self.text)

            # terminating the session
            self.smtp.quit()
        except Exception as e:
            print('the exception is '+str(e))


def send_email_to_support(self, cust_name, cust_email, cust_contact,
                          course_name, body):
    try:
        self.config_reader = ConfigReader()
        self.configuration = self.config_reader.read_config()

        # instance of MIMEMultipart
        self.msg = MIMEMultipart()

        # storing the senders email address
        self.msg['From'] = self.configuration['SENDER_EMAIL']

        # storing the subject
        self.msg['Subject'] = self.configuration['SALES_TEAM_EMAIL_SUBJECT']

        # string to store the body of the mail
        # body = "This will contain attachment"

        body = body.replace('cust_name', cust_name)
        body = body.replace('cust_contact', cust_contact)
        body = body.replace('cust_email', cust_email)
        body = body.replace('course_name', course_name)

        # attach the body with the msg instance
        self.msg.attach(MIMEText(body, 'html'))

        # instance of MIMEBase and named as p
        self.p = MIMEBase('application', 'octet-stream')

        # creates SMTP session
        self.smtp = smtplib.SMTP('smtp.gmail.com', 587)

        # start TLS for security
        self.smtp.starttls()

        # Authentication
        self.smtp.login(self.msg['From'], self.configuration['PASSWORD'])

        # Converts the Multipart msg into a string
        self.text = self.msg.as_string()

        # sending the mail

        self.support_team_email = self.configuration['SALES_TEAM_EMAIL']

        self.smtp.sendmail(self.msg['From'], self.support_team_email,
                           self.text)

        # terminating the session
        self.smtp.quit()
    except Exception as e:
        print('the exception is ' + str(e))

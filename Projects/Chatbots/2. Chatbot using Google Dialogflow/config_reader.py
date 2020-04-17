import configparser


class ConfigReader:
    def __init__(self):
        self.filename = 'config.ini'

    def read_config(self):
        self.config = configparser.ConfigParser()
        self.config.read(self.filename)
        self.configuration = self.config['DEFAULT']
        # self.sender_email=self.configuration['SENDER_EMAIL']
        # self.password = self.configuration['PASSWORD']
        # self.email_body = self.configuration['EMAIL_BODY']
        # self.email_subject = self.configuration['EMAIL_SUBJECT']

        return self.configuration
        # configuration is a dict containing key-value pair of the config.ini

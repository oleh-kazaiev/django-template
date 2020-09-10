from logging import Handler

from core.helper import send_email


DEV_EMAILS_LIST = []


class SendEmailToDevelopersHandler(Handler):
    def emit(self, record):
        log_entry = self.format(record)
        send_email('ERROR {{ files.0 }}', log_entry, DEV_EMAILS_LIST)

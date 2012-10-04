#!/usr/bin/env python
# vim: ai ts=4 sts=4 et sw=4
import string
from django.conf import settings
from rapidsms.apps.base import AppBase
from models import *
from datetime import timedelta
from django.utils.translation import ugettext as _

PUNCTUATIONS = filter(lambda s: s not in settings.ALLOWED_PUNCTUATIONS, string.punctuation) + ' '
TRANS_TABLE = dict((ord(fro), ord(to)) for fro, to in settings.CHARACTER_TRANSLATIONS)

RANGE_ERROR = _('Invalid response(s) for question(s): "%(attributes)s". You sent: %(text)s')
ATTRIBUTE_ERROR = _('Unknown question codes: "%(attributes)s". You sent: %(text)s')
UNKNOWN_OBSERVER = _('Observer ID not found. Please resend with valid Observer ID. You sent: %(text)s')
INVALID_MESSAGE = _('Invalid message: "%(message)s". Please check and resend!')
SUBMISSION_RECEIVED = _('Your submission was received! You sent: %(message)s')


class App(AppBase):
    def handle(self, message):
        working_text = unicode(message.text)
        # strip all unwanted whitespace and punctuation marks
        at_position = working_text.find('@')
        working_text = filter(lambda s: s not in PUNCTUATIONS, working_text[:at_position]).translate(TRANS_TABLE) + working_text[at_position:] \
            if at_position != -1 else filter(lambda s: s not in PUNCTUATIONS, working_text).translate(TRANS_TABLE)

        at_position = working_text.find('@')
        message.text = working_text[:at_position] if at_position != -1 else working_text

        try:
            submission, observer = Form.parse(working_text)
            if not observer:
                return message.respond(UNKNOWN_OBSERVER % {'text': message.text}) or True
            else:
                # Find submission for observer and persist valid data
                try:
                    if submission['form'].autocreate_submission:
                        entry, dummy = Submission.objects.get_or_create(observer=observer, date=message.date,
                            form=submission['form'])
                    else:
                        entry = Submission.objects.get(observer=observer, form=submission['form'],
                            date__range=(message.date - timedelta(settings.BACKLOG_DAYS), message.date))
                    entry.data.update(submission['data'])
                    entry.save()
                except Submission.DoesNotExist:
                    pass

                if 'range_error_fields' in submission and submission['range_error_fields']:
                    return message.respond(RANGE_ERROR % \
                        {'attributes': ', '.join(submission['range_error_fields']), 'text': message.text})
                elif 'attribute_error_fields' in submission and submission['attribute_error_fields']:
                    return message.respond(ATTRIBUTE_ERROR % \
                        {'attributes': ', '.join(submission['attribute_error_fields']), 'text': message.text})
                else:
                    return message.respond(SUBMISSION_RECEIVED % {'message': message.text})
        except Form.DoesNotExist:
            # We couldn't parse the message hence it's invalid
            return self.default(message)

    def default(self, message):
        return message.respond(INVALID_MESSAGE % {'message': message.text})
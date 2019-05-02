import re

# need to strip out the envelope apparently so that python email library can parse it...
# python 2 and 3 email libraries silently skips emails with an envelope
# https://github.com/python/cpython/blob/2.7/Lib/email/feedparser.py#L226
#  and
# https://github.com/python/cpython/blob/3.7/Lib/email/feedparser.py#L228
# see const.py for non-bytes version of regex; can't include this one there or python2 complains

EMAIL_ENVELOPE_PATTERN_BYTES = re.compile(rb'(?:MAIL FROM:|RCPT TO:).*\n', re.IGNORECASE)

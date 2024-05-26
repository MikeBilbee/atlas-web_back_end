#!/usr/bin/env python3
"""
A function called filter_datum that returns the log message obfuscated:
Arguments:
    fields: a list of strings representing all fields to obfuscate
    redaction: a string representing by what the field will be obfuscated
    message: a string representing the log line
    separator: a string representing by which character is separating
        all fields in the log line (message)
"""

import re
import logging
from typing import List


def filter_datum(fields: List[str],
                redaction: str,  # noqa: E128
                message: str,  # noqa: E128
                separator: str) -> str:  # noqa: E128

    """Filters and returns obfuscated data"""

    regex = f'({"|".join(fields)})=([^{separator}]*)'
    return re.sub(regex, fr'\1={redaction}', message)


class RedactingFormatter(logging.Formatter):
    """ Redacting Formatter class
        """

    REDACTION = "***"
    FORMAT = "[HOLBERTON] %(name)s %(levelname)s %(asctime)-15s: %(message)s"
    SEPARATOR = ";"

    def __init__(self, fields: List[str]):
        """Initializes the class RedactingFormatter"""
        super().__init__(self.FORMAT)
        self.fields = fields

    def format(self, record: logging.LogRecord) -> str:
        """Formats the log and returns redacted data"""
        record.msg = filter_datum(
            self.fields, self.REDACTION, record.msg, self.SEPARATOR
        )
        return super().format(record)

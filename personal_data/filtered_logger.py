#!/usr/bin/env python3
"""
An obfuscating logging system
"""

import re
import logging
import os
import mysql.connector
from typing import List
PII_FIELDS = ('name', 'email', 'phone', 'ssn', 'password')


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


def get_logger() -> logging.Logger:
    """Creates a log of user data"""

    logger = logging.getLogger("user_data")
    logger.setLevel(logging.INFO)
    logger.propagate = False
    handler = logging.StreamHandler()
    handler.setFormatter(RedactingFormatter(PII_FIELDS))
    logger.addHandler(handler)

    return logger


def get_db() -> mysql.connector.connection.MySQLConnection:
    """Connects to the Holberton database and returns a connection object."""
    return mysql.connector.connect(
        host=os.environ.get('PERSONAL_DATA_DB_HOST', 'localhost'),
        database=os.environ.get('PERSONAL_DATA_DB_NAME', 'root'),
        user=os.environ.get('PERSONAL_DATA_DB_USERNAME'),
        password=os.environ.get('PERSONAL_DATA_DB_PASSWORD', '')
        )


def main():
    """

    """


if __name__ == "__main__":
    main()

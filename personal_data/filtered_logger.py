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
from typing import List


def filter_datum(fields: List[str],
                redaction: str,  # noqa: E128
                message: str,  # noqa: E128
                separator: str) -> str:  # noqa: E128

    """Filters and returns obfuscated data"""

    regex = f'({"|".join(fields)})=([^{separator}]*)'
    return re.sub(regex, fr'\1={redaction}', message)

#!/usr/bin/env Python3

""" a function that returns a log message"""

import re
from typing import List


def filter_datum(fields: list[str],
                 redaction: str,
                 message: str,
                 separator: str) -> str:
    """returns a log message obfuscated"""

    for field in fields:
        message = re.sub(
            f"{field}=[^{separator}]*",
            f"{field}={redaction}",
            message
        )

    return message

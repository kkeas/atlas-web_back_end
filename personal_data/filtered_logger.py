#!/usr/bin/env Python3

""" a function that returns a log message"""

import re
import os
from typing import List
import logging


def filter_datum(fields: List[str],
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


class RedactingFormatter(logging.Formatter):
    """ Redacting Formatter class
        """

    REDACTION = "***"
    FORMAT = "[HOLBERTON] %(name)s %(levelname)s %(asctime)-15s: %(message)s"
    SEPARATOR = ";"

    def __init__(self, fields: List[str]):
        super(RedactingFormatter, self).__init__(self.FORMAT)
        self.fields = fields

    def format(self, record: logging.LogRecord) -> str:
        """filter values in incoming log records"""
        OG_message = filter_datum(self.fields, self.REDACTION,
                                  super().format(record), self.SEPARATOR)
        return OG_message


    PII_FIELDS: tuple = ("name", "email", "phone", "ssn", "password")

def get_logger() -> logging.Logger:
    """creates logger object and configures it with a custom formatter"""

    new_logger: logging.Logger = logging.getLogger("user_data")
    new_logger.setLevel(logging.INFO)
    new_logger.propogate = False
    handler: logging.StreamHandler = logging.StreamHandler()
    handler.setFormatter(RedactingFormatter(PII_FIELDS))
    new_logger.addHandler(handler)

    return new_logger

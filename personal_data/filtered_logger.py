#!/usr/bin/env Python3

""" a function that returns a log message"""

import re
import os
from typing import List
import logging
import mysql.connector


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
    new_logger.propagate = False
    handler: logging.StreamHandler = logging.StreamHandler()
    handler.setFormatter(RedactingFormatter(PII_FIELDS))
    new_logger.addHandler(handler)

    return new_logger


def get_db() -> mysql.connector.connection.MySQLConnection:
    """a function that returns a connector to the database"""

    user = os.getenv(PERSONAL_DATA_DB_USERNAME, "root")
    password = os.getenv(PERSONAL_DATA_DB_PASSWORD, "")
    host = os.getenv(PERSONAL_DATA_DB_HOST, "localhost")
    db = os.getenv(PERSONAL_DATA_DB_NAME)

    connector = mysql.connector.connect(
        user=user, password=password, host=host, database=db
    )
    return connector


def main():
    """obtains database connection and retrieves all rows in the users table"""
    db_connector = get_db()
    cursor = db_connector.cursor()
    logger = get_logger()

    cursor.execute("SELECT * FROM users;")
    field_names = [column[0] for column in cursor.description]
    for row in cursor.fetchall():
        user_dict = dict(zip(field_names, row))
        user_str = RedactingFormatter.SEPARATOR.join(
            f"{key}={value}" for key, value in user_dict.items()
        )
        logger.info(user_str)

    db_connector.close()


if __name__ == '__main__':
    main()

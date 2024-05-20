#!/usr/bin/env python3

"""method get_page that takes args
page=1 and page_size=10"""

import csv
import math
from typing import List


def index_range(page, page_size):
    """function returns a tuple for pagination parameters"""
    start_index = (page - 1) * page_size
    end_index = start_index + page_size
    return start_index, end_index


class Server:
    """Server class to paginate a database of popular baby names.
    """
    DATA_FILE = "Popular_Baby_Names.csv"

    def __init__(self):
        self.__dataset = None

    def dataset(self) -> List[List]:
        """Cached dataset
        """
        if self.__dataset is None:
            with open(self.DATA_FILE) as f:
                reader = csv.reader(f)
                dataset = [row for row in reader]
            self.__dataset = dataset[1:]

        return self.__dataset

    def get_page(self, page: int = 1, page_size: int = 10) -> List[List]:
        """assert values are greater than 0, read csv file,
        ensure the start and end are within bounds of dataset,
        extract page of dataset based on indices"""

        assert isinstance(page, int) and isinstance(page_size, int)
        assert page > 0 and page_size > 0
        self.dataset()
        begin, end = index_range(page, page_size)
        if begin >= len(self.__dataset):
            return []
        return self.__dataset[begin:min(end, len(self.__dataset))]

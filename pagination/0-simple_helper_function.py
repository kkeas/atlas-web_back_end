#!/usr/bin/env python3

"""simple helper function index_range that takes
two integer args page and page size"""


def index_range(page, page_size):
    """function returns a tuple for pagination parameters"""
    start_index = (page - 1) * page_size
    end_index = start_index + page_size
    return start_index, end_index

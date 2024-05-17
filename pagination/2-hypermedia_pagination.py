#!/usr/bin/env python3
"""
a get_hyper method that takes the same arguments (and defaults)
as get_page and returns a dictionary containing the
following key-value pairs:

page_size: the length of the returned dataset page
page: the current page number
data: the dataset page (equivalent to return from previous task)
next_page: number of the next page, None if no next page
prev_page: number of the previous page, None if no previous page
total_pages: the total number of pages in the dataset as an integer
Make sure to reuse get_page in your implementation.
"""

import csv
import math
from typing import List, Dict
index_range = __import__('0-simple_helper_function').index_range


class Server:
    """Server class to paginate a database of popular baby names."""

    DATA_FILE = "Popular_Baby_Names.csv"

    def __init__(self):
        self.__dataset = None

    def dataset(self) -> List[List]:
        """Cached dataset"""

        if self.__dataset is None:
            with open(self.DATA_FILE) as f:
                reader = csv.reader(f)
                dataset = [row for row in reader]
            self.__dataset = dataset[1:]

        return self.__dataset

    def get_page(self, page: int = 1, page_size: int = 10) -> List[List]:
        """Gets page number"""

        assert type(page) == int and page > 0
        assert type(page_size) == int and page_size > 0

        page, page_size = index_range(page, page_size)
        try:
            return self.dataset()[page:page_size]
        except IndexError:
            return []

    def get_hyper(self, page: int = 1, page_size: int = 10) -> Dict:
        """Args:
            page: Page number
            page_size: Size of Page

            Returns: A Dictionary of value pairs
        """

        data = self.get_page(page, page_size)
        total_items = len(self.dataset()) - 1

        total_pages = math.ceil(total_items / page_size)

        hyper_dict = {
            "page_size": len(data),
            "page": page,
            "data": data,
            "next_page": page + 1 if page < total_pages else None,
            "prev_page": page - 1 if page > 1 else None,
            "total_pages": total_pages,
        }

        return hyper_dict

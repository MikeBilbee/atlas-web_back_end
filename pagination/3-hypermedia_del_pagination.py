#!/usr/bin/env python3
"""
Deletion-resilient hypermedia pagination
"""

import csv
import math
from typing import List, Dict


class Server:
    """Server class to paginate a database of popular baby names.
    """
    DATA_FILE = "Popular_Baby_Names.csv"

    def __init__(self):
        self.__dataset = None
        self.__indexed_dataset = None

    def dataset(self) -> List[List]:
        """Cached dataset
        """
        if self.__dataset is None:
            with open(self.DATA_FILE) as f:
                reader = csv.reader(f)
                dataset = [row for row in reader]
            self.__dataset = dataset[1:]

        return self.__dataset

    def indexed_dataset(self) -> Dict[int, List]:
        """Dataset indexed by sorting position, starting at 0
        """
        if self.__indexed_dataset is None:
            dataset = self.dataset()
            truncated_dataset = dataset[:1000]
            self.__indexed_dataset = {
                i: dataset[i] for i in range(len(dataset))
            }
        return self.__indexed_dataset

    def get_hyper_index(self, index: int = None, page_size: int = 10) -> Dict:
        """
        A get_hyper_index method with two integer arguments: index with a None
        default value and page_size with default value of 10.
        """

        assert index is None or (
            type(index) == int and index >= 0
        )
        assert type(page_size) == int and page_size > 0

        indexed_dataset = self.indexed_dataset()
        total_items = len(indexed_dataset)
        data = []

        if index is None:
            index = 0
        else:
            assert index < total_items

        next_index = index + page_size

        while index < total_items and len(data) < page_size:
            if index in indexed_dataset:
                data.append(indexed_dataset[index])
            index += 1

        return {
            "index": index,
            "next_index": next_index if next_index < total_items else None,
            "page_size": page_size,
            "data": data,
        }

#!/usr/bin/env python3
"""
A function named index_range that takes two integer arguments page
and page_size.

The function should return a tuple of size two containing a start
index and an end index corresponding to the range of indexes to return
in a list for those particular pagination parameters.

Page numbers are 1-indexed, i.e. the first page is page 1.
"""


def index_range(page, page_size):
    """
    Args:
        page: Page number
        page_size: Leangth of page

    Returns: Tuple containing start and end indices
    """

    if page or page_size < 1:
        pass

    start_index = (page - 1) * page_size  # Calculate the start index
    end_index = start_index + page_size   # Calculate the end index
    index_range = (start_index, end_index) # Tuple of indeces

    return index_range

#!/usr/bin/env python3
"""
   This module defines the function: index_range and the
   class: Server
"""
import csv
import math
from typing import List, Dict, Optional


def index_range(page: int, page_size: int) -> tuple:
    """
    Calculate the start and end index for pagination.

    Args:
        page (int): The current page number (1-indexed).
        page_size (int): The number of items per page.

    Returns:
        tuple: A tuple containing the start and end indexes
        for the given page.
    """
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
        """
        Get a page of the dataset.

        Args:
            page (int): The current page number (1-indexed).
            page_size (int): The number of items per page.

        Returns:
            List[List]: A list of rows corresponding to the requested page.
        """
        # Validate input arguments
        assert isinstance(
            page, int) and page > 0, "page must be a positive integer."
        assert isinstance(page_size, int) and page_size > 0, \
            "page_size must be a positive integer."

        # Calculate start and end indexes
        start_index, end_index = index_range(page, page_size)

        # Retrieve the dataset
        dataset = self.dataset()

        # Return the requested page or an empty list if out of range
        return dataset[start_index:end_index]

    def get_hyper(
      self, page: int = 1, page_size: int = 10) -> Dict[str, Optional[int]]:
        """
        Get a hypermedia dictionary for pagination.

        Args:
            page (int): The current page number (1-indexed).
            page_size (int): The number of items per page.

        Returns:
            Dict[str, Optional[int]]: A dictionary with pagination details.
        """
        # Get the page data
        data = self.get_page(page, page_size)

        # Calculate total pages
        total_items = len(self.dataset())
        total_pages = math.ceil(total_items / page_size)

        # Determine next and previous pages
        next_page = page + 1 if page < total_pages else None
        prev_page = page - 1 if page > 1 else None

        # Return the hypermedia dictionary
        return {
            "page_size": len(data),
            "page": page,
            "data": data,
            "next_page": next_page,
            "prev_page": prev_page,
            "total_pages": total_pages,
        }

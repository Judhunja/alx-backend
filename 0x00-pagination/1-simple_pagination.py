#!/usr/bin/env python3
"""This module contains a function index_range"""

from typing import Tuple, List
import csv
import math


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

    @staticmethod
    def index_range(page: int, page_size: int) -> Tuple[int, int]:
        """Returns tuple containing start and end index that corresponds to the
        range of indexes to return in a list for those particular pagination
        parameters"""
        start_ind = (page - 1) * page_size
        end_ind = start_ind + page_size
        return [start_ind, end_ind]

    def get_page(self, page: int = 1, page_size: int = 10) -> List[List]:
        """returns the appropriate list of rows for the specified range"""
        assert isinstance(page, int) and page > 0
        assert isinstance(page_size, int) and page_size > 0
        data = []
        with open("./Popular_Baby_Names.csv", "r", encoding="utf-8") as f:
            csvreader = csv.reader(f)
            for row in csvreader:
                data.append(row)

        try:
            start, end = self.index_range(page, page_size)
            return data[start:end]
        except IndexError:
            return []

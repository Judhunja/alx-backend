#!/usr/bin/env python3
"""This module contains a function index_range"""

from typing import Tuple


def index_range(page: int, page_size: int) -> Tuple[int, int]:
    """Returns tuple containing start and end index that corresponds to the
    range of indexes to return in a list for those particular pagination
    parameters"""
    start_ind = (page - 1) * page_size
    end_ind = start_ind + page_size
    return (start_ind, end_ind)

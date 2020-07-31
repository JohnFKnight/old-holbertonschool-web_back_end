#!/usr/bin/env python3
""" Pagination function
"""

import csv
import math
from typing import List, Tuple, Dict


def index_range(page: int, page_size: int) -> Tuple[int, int]:
    """Return 2 member tuple of start, end index
    """

    res: tuple
    res = ((page - 1) * page_size, page * page_size)
    return res


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
        """Paginate csv file
        """
        assert isinstance(page, int)
        assert isinstance(page_size, int)
        assert page > 0
        assert page_size > 0

        idx_range: tuple
        idx_range = index_range(page, page_size)

        names = self.dataset()
        return names[idx_range[0]:idx_range[1]]

    def get_hyper(self, page: int = 1, page_size: int = 10) -> Dict[str, str]:
        """Return pagination dictionary data of csv file
        """
        assert isinstance(page, int)
        assert isinstance(page_size, int)
        assert page > 0
        assert page_size > 0

        dset = self.dataset()
        tot_pages = math.ceil(len(dset) / page_size)

        d: Dict[str, str] = {}
        d["page_size"] = page_size if page <= tot_pages and page_size <= tot_pages else 0
        d["page"] = page
        d["data"] = self.get_page(page, page_size)
        d["next_page"] = page + 1 if page + 1 <= tot_pages else None
        d["prev_page"] = page - 1 if page - 1 >= 0 else None
        d["total_pages"] = tot_pages

        return d

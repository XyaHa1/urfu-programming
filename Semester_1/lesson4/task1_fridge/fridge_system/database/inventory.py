from pathlib import Path
from typing import List

import pandas as pd

from exceptions import *
from ..core import Product
from ..trie_prefix import TriePrefix


class ProductTable:
    def __init__(self, file: str = ""):
        self.df = None
        self.trie = None
        self._data_dir = Path(__file__).parent.parent / "data"
        self.load(file)

    def load(self, file: str):
        self.df = pd.DataFrame(columns=["title", "amount", "expiration_date"])
        self.trie = TriePrefix([])
        if not file:
            return

        file_path = self._data_dir / file
        if not file_path.is_file():
            raise FileNotFoundError()

        if file.endswith(".csv"):
            self.df = pd.read_csv(file_path)
        elif file.endswith(".json"):
            self.df = pd.read_json(file_path)
        else:
            raise InvalidFormatFileError()

        self.trie = TriePrefix(self.df["title"].str.lower().tolist())

    def save(self, product: Product):
        new_data = pd.DataFrame(
            {
                "title": [product.title.get()],
                "amount": [product.amount.get()],
                "expiration_date": [product.expiration_date.get()],
            },
            index=[0],
        )
        self.df = pd.concat([self.df, new_data], ignore_index=True)
        self.trie.insert(product.title.get().lower())

    def delete_items_by_title(self, title: str):
        if self.df["title"].isin([title]).any():
            self.df = self.df[self.df["title"] != title].reset_index(drop=True)
            self.trie.delete(title.lower())
        else:
            raise TitleNotFoundError()

    def delete_item_by_index(self, index: int):
        if index >= len(self.df) or index < 0:
            raise InvalidIndexError()

        title = self.df.iloc[index]["title"]
        count_title_items = len(self.df[self.df["title"] == title]) - 1
        if count_title_items == 0:
            self.trie.delete(title.lower())

        self.df = self.df.drop(index).reset_index(drop=True)

    def find_titles(self, prefixes: List[str]):
        result_titles = []
        for prefix in prefixes:
            result_titles.extend(self.trie.search(prefix.lower().strip()))
        return result_titles

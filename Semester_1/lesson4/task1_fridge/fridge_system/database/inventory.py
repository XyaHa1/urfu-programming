from pathlib import Path

import pandas as pd

from exceptions import *
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

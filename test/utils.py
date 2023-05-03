import json
from typing import List
from bs4 import BeautifulSoup


def read_json_data(path: str) -> json:
    f = open(path)
    json_data = json.load(f)
    return json_data


def read_html_to_soup(file_path: str) -> BeautifulSoup:
    with open(file_path, "r") as f:
        contents = f.read()
        soup = BeautifulSoup(contents, "lxml")
    return soup


def get_round_embeddings(embeddings: List[float], num: int) -> List[float]:
    round_embeddings = list(map(lambda x: round(x, num), embeddings))
    return round_embeddings

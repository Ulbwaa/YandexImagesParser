import json
from typing import Literal, NamedTuple

import requests
from fake_headers import Headers
from bs4 import BeautifulSoup as bs4


SIZES = Literal["small", "medium", "large"]


class Size(NamedTuple):
    height: int
    width: int


class Result(NamedTuple):
    title: str
    description: str
    domain: str
    url: str
    size: Size


class YandexImage:
    _URL = "https://yandex.ru/images/search"

    def __init__(self, sizes: SIZES) -> None:
        self.headers = Headers(headers=True).generate()
        self.sizes = sizes

    @staticmethod
    def _parse_result_page(page_text: str) -> list[str]:
        output = []

        soup = bs4(page_text, "html.parser")
        items_place, *__ = soup.find_all("div", {"class": "serp-list"})
        items = items_place.find_all("div", {"class": "serp-item"})

        for item in items:
            data = json.loads(item.get("data-bem"))
            image_url = data["serp-item"]["img_href"]
            snippet = data["serp-item"]["snippet"]

            img_size = Size(
                data["serp-item"]["preview"][0]["w"],
                data["serp-item"]["preview"][0]["h"],
            )

            result = Result(
                snippet.get("title", ""),
                snippet.get("text", ""),
                snippet.get("domain", ""),
                image_url,
                img_size,
            )

            output.append(result)

        return output

    def search(self, query: str) -> list[str]:
        request = requests.get(
            self._URL,
            params={"text": query, "nomisspell": 1, "noreask": 1, "isize": self.sizes},
            headers=self.headers,
        )

        if request.ok:
            return self._parse_result_page(request.text)

        return []

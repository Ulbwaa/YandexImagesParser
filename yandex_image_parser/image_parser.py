import json
from typing import Literal, NamedTuple

import requests
from fake_headers import Headers
from bs4 import BeautifulSoup as bs4


SIZES = Literal["small", "medium", "large"]


class Size(NamedTuple):
    height: int
    width: int


class Preview(NamedTuple):
    url: str
    size: Size


class Result(NamedTuple):
    title: str
    description: str
    domain: str
    url: str
    size: Size
    preview: Preview


class YandexImage:
    _URL = "https://yandex.ru/images/search"

    def __init__(self):
        self.headers = Headers(headers=True).generate()

    def search(self, query: str, sizes: SIZES = "large") -> list[str]:
        request = requests.get(
            self._URL,
            params={"text": query, "nomisspell": 1, "noreask": 1, "isize": sizes},
            headers=self.headers,
        )

        output = []

        soup = bs4(request.text, "html.parser")
        items_place, *__ = soup.find_all("div", {"class": "serp-list"})
        items = items_place.find_all("div", {"class": "serp-item"})

        for item in items:
            data = json.loads(item.get("data-bem"))
            image = data["serp-item"]["img_href"]
            image_width = data["serp-item"]["preview"][0]["w"]
            image_height = data["serp-item"]["preview"][0]["h"]

            snippet = data["serp-item"]["snippet"]

            preview = "https:" + data["serp-item"]["thumb"]["url"]
            preview_width = data["serp-item"]["thumb"]["size"]["width"]
            preview_height = data["serp-item"]["thumb"]["size"]["height"]

            result = Result(
                snippet.get("title", ""),
                snippet.get("text", ""),
                snippet.get("domain", ""),
                image,
                Size(image_width, image_height),
                Preview(preview, Size(preview_width, preview_height)),
            )

            output.append(result)

        return output

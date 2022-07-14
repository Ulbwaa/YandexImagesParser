import requests
import json
from fake_headers import Headers
from bs4 import BeautifulSoup as bs4


class Size:
    def __init__(self):
        self.large = "large"
        self.medium = "medium"
        self.small = "small"


class Preview:
    def __init__(self, url: str, width: int, height: int):
        self.url = url
        self.width = width
        self.height = height
        self.size = str(width) + "*" + str(height)


class Result:
    def __init__(
        self,
        title: (str, None),
        description: (str, None),
        domain: str,
        url: str,
        width: int,
        height: int,
        preview: Preview,
    ):
        self.title = title
        self.description = description
        self.domain = domain
        self.url = url
        self.width = width
        self.height = height
        self.size = str(width) + "*" + str(height)
        self.preview = preview


class YandexImage:
    def __init__(self):
        self.size = Size()
        self.headers = Headers(headers=True).generate()
        self.version = "1.0-release"
        self.about = "Yandex Images Parser"

    def search(self, query: str, sizes: Size = "large") -> list:
        request = requests.get(
            "https://yandex.ru/images/search",
            params={"text": query, "nomisspell": 1, "noreask": 1, "isize": sizes},
            headers=self.headers,
        )

        soup = bs4(request.text, "html.parser")
        items_place = soup.find("div", {"class": "serp-list"})
        output = list()
        try:
            items = items_place.find_all("div", {"class": "serp-item"})
        except AttributeError:
            return output

        for item in items:
            data = json.loads(item.get("data-bem"))
            image = data["serp-item"]["img_href"]
            image_width = data["serp-item"]["preview"][0]["w"]
            image_height = data["serp-item"]["preview"][0]["h"]

            snippet = data["serp-item"]["snippet"]
            try:
                title = snippet["title"]
            except KeyError:
                title = None
            try:
                description = snippet["text"]
            except KeyError:
                description = None
            domain = snippet["domain"]

            preview = "https:" + data["serp-item"]["thumb"]["url"]
            preview_width = data["serp-item"]["thumb"]["size"]["width"]
            preview_height = data["serp-item"]["thumb"]["size"]["height"]

            output.append(
                Result(
                    title,
                    description,
                    domain,
                    image,
                    image_width,
                    image_height,
                    Preview(preview, preview_width, preview_height),
                )
            )

        return output

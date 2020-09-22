<div align="center">
  <h1>Yandex Images Parser</h1>
  <p>Python-модуль для парсинга фото с <a href="https://yandex.ru/images/">Яндекс.Картинок</a></p>

  <img align="center" src="https://img.shields.io/github/repo-size/Ulbwaa/YandexImagesParser" alt="GitHub repo size">
  <img align="center" src="https://img.shields.io/github/stars/Ulbwaa/YandexImagesParser" alt="GitHub Repo stars">
  <img align="center" src="https://img.shields.io/github/watchers/Ulbwaa/YandexImagesParser" alt="GitHub watchers">
  <img align="center" src="https://img.shields.io/github/last-commit/Ulbwaa/YandexImagesParser" alt="GitHub last commit">
  <img align="center" src="https://img.shields.io/codacy/grade/7733fc868fbc4da180e781d90cb30694" alt="Codacy grade">
  <img align="center" src="https://img.shields.io/github/languages/top/Ulbwaa/YandexImagesParser" alt="GitHub top language">
  <img align="center" src="https://img.shields.io/website?down_color=red&down_message=Down&label=Yandex.Images%20Uptime&up_color=blue&up_message=Up&url=https%3A%2F%2Fyandex.ru%2Fimages%2F" alt="Yandex.Images Uptime">
</div>

## Навигация

* [Начало работы](#начало-работы)
  * [Установка зависимостей](#инициализация-скрипта)
  * [Инициализация скрипта](#инициализация-скрипта)
* [Поиск фото по ключевому слову](#получение-информации-о-фильме-по-id-кинопоиска)
  * [Возвращаемые параметры функцией YandexImage.search](#возвращаемые-параметры-функцией-kpget_film)
* [Фильтры для поиска](#поиск-фильма-на-кинопоиске-по-ключевому-слову)
  * [Выборочный размер фото](#возвращаемые-параметры-функцией-kpsearch)
    * [Возвращаемые параметры функцией YandexImage.size](#возвращаемые-параметры-функцией-kpsearch)

## Начало работы
Для работы Вам нужно установить или скачать модуль. Установить модуль можно двумя способами:
* Установка в качестве подмодуля:
```
$ git submodule add https://github.com/Ulbwaa/YandexImagesParser
```

* Клонирование репозитория в Ваш проект:
```
$ git clone https://github.com/Ulbwaa/YandexImagesParser
```

> Для удобной работы рекомендуется использовать первый способ.

### Установка зависимостей
```
$ pip install -r requirements.txt
```

### Инициализация скрипта
```python
from ImageParser import YandexImage

parser = YandexImage()

print(parser.about, parser.version)
```

```
>>> Yandex Images Parser 1.0-release
```

## Поиск фото по ключевому слову
```python
from ImageParser import YandexImage

parser = YandexImage()

for item in parser.search("Hello world!"):
    print(item.title)
    print(item.url)
    print(item.preview.url)
    print("(", item.size, ")", sep='')
```

```
>>> Hello world! - SYNDICATE
>>> https://access.viasyndicate.com/wp-content/uploads/helloworld.jpg
>>> https://im0-tub-ru.yandex.net/i?id=f4c8a1308fd44579344172c874f228a4&n=13
>>> (1900*800)
```

### Возвращаемые параметры функцией `YandexImage.search`
`YandexImage.search` возвращает список элементов, имеющих следующие параметры:

* Заголовок материнского сайта - `self.title` (Сокращается до определенного количества символов)
* Описание материнского сайта - `self.description` (Сокращается до определенного количества символов)
* Домен материнского сайта - `self.domain`
* URL полноразмерного изображения - `self.url`
* Ширина полноразмерного изображения - `self.width` (В пикселях)
* Высота полноразмерного изображения - `self.height` (В пикселях)
* Размер полноэкранного изображения - `self.size` (Вид: 1280*720)
* URL сжатого изображения - `self.preview.url`
* Ширина сжатого изображения - `self.preview.width` (В пикселях)
* Высота сжатого изображения - `self.preview.height` (В пикселях)
* Размер сжатого изображения - `self.preview.size` (Вид: 1280*720)

> Для получения информации в формате dict используйте `self.__dict__`

## Фильтры для поиска
Для фильтрации поиска вы можете использовать следующие функции:

### Выборочный размер фото
```python
from ImageParser import YandexImage

parser = YandexImage()

for item in parser.search("Hello world!", sizes=parser.size.large):
    print(item.title)
    print(item.url)
    print(item.preview.url)
    print("(", item.size, ")", sep='')
```

#### Возвращаемые параметры функцией `YandexImage.size`
* Большие фото - `self.large`
* Средние фото - `self.medium`
* Маленькие фото - `self.small`

> Для получения информации в формате dict используйте `self.__dict__`

В будущем будут добавлены и другие фильтры.

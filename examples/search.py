from ImageParser import YandexImage

parser = YandexImage()

for item in parser.search("Hello world!", parser.size.large):
    print(item.title)
    print(item.url)
    print(item.preview.url)
    print("(", item.size, ")", sep='')

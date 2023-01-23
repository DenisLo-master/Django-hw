import json


def get_json(file, **options):
    with open(file, "rb") as f:
        return json.load(f)


def get_news_data():
    data = get_json("./content/news_from_GPTChat.json")
    news_on_page = 2
    news = []
    page_num = 1
    page_content = []
    i = 0
    for news_item in data:
        page_num = i // news_on_page + 1
        page_content.append(news_item)
        i += 1
        if i >= (news_on_page * page_num):
            news.append(page_content)
            page_content = []
    news.append(page_content)
    return news

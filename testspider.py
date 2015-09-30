from grab.spider import Spider, Task


class ExampleSpider(Spider):
    def task_generator(self):
        for lang in ('python', 'ruby', 'perl'):
            url = 'https://www.google.com/search?q={}'.format(lang)
            yield Task('search', url=url, lang=lang)

    def task_search(self, grab, task):
        print('{}: {}'.format(
            task.lang,
            grab.doc('//div[@class="s"]//cite').text()
        ))


bot = ExampleSpider()
bot.run()

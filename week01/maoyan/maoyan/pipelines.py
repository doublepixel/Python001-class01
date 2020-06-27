import pandas


class MaoyanPipeline:

    def process_item(self, item, spider):
        print(item.values())
        work02_movie = pandas.DataFrame(item.values())
        work02_movie.to_csv('./work02_movie.csv', mode='a', encoding='utf-8', index=False, header=False)
        return item

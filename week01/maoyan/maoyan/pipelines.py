import pandas

class MaoyanPipeline:

    def process_item(self, item, spider):

        work02_movie = pandas.DataFrame(item.values())
        work02_movie.to_csv('./work02_movie.csv', encoding='utf8', index=False, header=False)
        return item

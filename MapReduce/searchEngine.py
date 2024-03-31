from mrjob.job import MRJob
import re

WORD_RE = re.compile(r"[\w']+")

class SearchEngine(MRJob):
    def mapper(self, _, line):
        article = line.split(',')
        yield article[0], len(WORD_RE.findall(article[3]))

    def reducer(self, key, value):
        yield key, sum(value)

if __name__ == '__main__':
    SearchEngine.run()
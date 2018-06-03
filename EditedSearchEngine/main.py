import time
import argparse

from EditedSearchEngine.core.searchEngine import SearchEngine
from EditedSearchEngine.utils.parser import parse_csv_file, get_data

import pygtrie

if __name__ == "__main__":

    # # Instantiate the parser
    # parser = argparse.ArgumentParser(description='Edited Search Engine')
    #
    # # Json file to be loaded
    # parser.add_argument('--index', type=str,
    #                 help='CSV file to build index', default="../data/search_dataset.csv")
    #
    # parser.add_argument('--search', type=str,
    #                 help='CSV file for different searches', default='')
    #
    # args = parser.parse_args()
    # print(args.load, args.index)

    # Ingest data
    index = parse_csv_file("../data/search_dataset.csv")
    data = get_data("../data/search_dataset.csv")
    search_engine = SearchEngine(index, data)
    # Seconds
    start_time = time.time()

    rank = search_engine.search("green top")
    print("--- {} Milliseconds ---".format((time.time() - start_time) / 1000))

    # t = pygtrie.CharTrie()
    #
    # t['richard'] = ['fe', 'fefe', 'rob']
    # t['reddish'] = [1,2,3,4,]
    # t['red'] = [5,6,7,8,9]
    # t['green'] = [10]
    # t['greeny'] = [11]
    #
    # print(t.keys('red'))
    # print(t.keys('green'))
    # print(t.keys('greeny'))
    #
    # print(t.get('reddish'))
    #
    # values = t.keys("red")
    #
    # for word in values:
    #     print(word)
    #
    #
    #
    # # print(t)
    #
    # # print(t.get('red'))













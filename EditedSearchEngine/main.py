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
    index = parse_csv_file("../data/test.csv")
    data = get_data("../data/test.csv")
    search_engine = SearchEngine(index, data)
    # Seconds
    start_time = time.time()

    rank = search_engine.search("red blouse")
    print("--- {} Milliseconds ---".format((time.time() - start_time) / 1000))














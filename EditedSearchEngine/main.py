import pprint
import time


from EditedSearchEngine.core.searchEngine import SearchEngine
from EditedSearchEngine.utils.parser import parse_csv_file, get_data

if __name__ == "__main__":

    index = parse_csv_file("../data/search_dataset.csv")
    data = get_data("../data/search_dataset.csv")
    #
    # # print(data)
    #
    search_engine = SearchEngine(index, data)

    #

    start_time = time.time()
    rank = search_engine.search("rich")
    # pprint.pprint(rank)
    # print("Number of products: {}".format(len(rank.keys())))
    print("--- {} Milliseconds ---".format((time.time() - start_time)/1000))





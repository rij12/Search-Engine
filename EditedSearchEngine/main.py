import pprint
import time


from EditedSearchEngine.core.searchEngine import SearchEngine
from EditedSearchEngine.utils.parser import parse_csv_file

if __name__ == "__main__":

    index = parse_csv_file("/home/richard/git/EditedInterview/data/search_dataset.csv")

    search_engine = SearchEngine(index)

    start_time = time.time()
    results_free = search_engine.free_text_query("Jumper")
    print("Results: {}".format(len(results_free)))
    pprint.pprint(results_free)
    # print(results_free)
    print("--- %s seconds ---" % (time.time() - start_time))





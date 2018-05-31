import csv
import pprint

from EditedSearchEngine.core.searchEngine import SearchEngine
from EditedSearchEngine.utils.parser import parse_csv_file

if __name__ == "__main__":

    index = parse_csv_file("/home/richard/git/EditedInterview/data/search_dataset.csv")

    search_engine = SearchEngine(index)
    results = search_engine.single_word_query("richard")
    print("Results: {}".format(len(results[0])))
    pprint.pprint(results)

    # Free text search
    print("------ FREE TEXT ---------- \n")
    results_free = search_engine.free_text_query("ralph lauren vest")
    print("Results: {}".format(len(results_free.keys())))
    pprint.pprint(results_free)






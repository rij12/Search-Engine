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
    # start_time = time.time()
    # answer = search_engine.free_text_query("green jumper")
    # print("Results: {}".format(len(answer)))
    # pprint.pprint(answer)
    # # print(results_free)
    # print("--- %s seconds ---" % (time.time() - start_time))

    string_list = "hello my name is richard richard"

    search_engine.cosine_similarity("He is the hero Gotham deserves", "but not the one it needs right now.")

    # print(term_count)




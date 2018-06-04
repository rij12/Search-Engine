import argparse
import time


from EditedSearchEngine.core.searchEngine import SearchEngine
from EditedSearchEngine.utils.parser import parse_csv_file, get_data

SECONDS_TO_MILLISECONDS = 1000


if __name__ == "__main__":

    # Instantiate the parser
    parser = argparse.ArgumentParser(description='Edited Search Engine')

    # Json file to be loaded
    parser.add_argument('--index', type=str,
                    help='CSV file to build index', default="../data/search_dataset.csv")

    parser.add_argument('--search', type=str,
                    help='CSV file for different searches', default='../data/test_search.txt')

    args = parser.parse_args()

    # Ingest data
    index = parse_csv_file(args.index)
    data = get_data(args.index)
    search_engine = SearchEngine(index, data)

    # Read and perform search for each csv line
    with open(args.search) as f:
        content = f.readlines()

        for query in content:
            query = query.lower().strip()
            # Execute each query
            start_time = time.time()
            rank = search_engine.search(query)
            print("--- {} Milliseconds ---".format((time.time() - start_time) / SECONDS_TO_MILLISECONDS))
















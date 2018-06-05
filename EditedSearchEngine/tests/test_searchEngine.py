import unittest

from EditedSearchEngine.core.search_engine import SearchEngine
from EditedSearchEngine.utils.parser import parse_csv_file, get_data

test_data = "data/test.csv"


class SearchEngineTestCase(unittest.TestCase):
    search_engine = None

    def init(self):
        index = parse_csv_file(test_data)
        data = get_data(test_data)

        self.search_engine = SearchEngine(index=index, data=data)

    def test_search_query(self):
        query_string = "red blouse"

        product_1 = "1.0, 666, red, blouse"
        product_2 = "0.63, 11280, red checked blouse, ann harvey"
        product_3 = "0.5, 32651, red imperial lily print shell sleeveless blouse, topshop"
        product_4 = "0.5, 555, reddish, blouse"

        expected_output = list()

        expected_output.append(product_1)
        expected_output.append(product_2)
        expected_output.append(product_3)
        expected_output.append(product_4)

        # Generate a search engine with an index and data
        self.init()

        results = self.search_engine.search(query_string)
        length = set(expected_output) & set(results)

        self.assertEqual(len(length), len(results))
        self.assertEqual(len(length), len(expected_output))


if __name__ == '__main__':
    unittest.main()

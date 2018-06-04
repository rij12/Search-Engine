import unittest

from EditedSearchEngine.core.searchEngine import SearchEngine
from EditedSearchEngine.utils.parser import parse_csv_file, get_data

test_data = "../../data/test.csv"


class SearchEngineTestCase(unittest.TestCase):
    search_engine = None

    def init(self):
        index = parse_csv_file(test_data)
        data = get_data(test_data)

        self.search_engine = SearchEngine(index=index, data=data)

    def test_parse_csv_file(self):

        expected_text_file_size = 48

        # Build Index
        self.init()

        index_size = len(self.search_engine.index)
        self.assertEquals(index_size, expected_text_file_size)

    def test_get_data(self):
        self.init()

        expected_output = dict()
        expected_output['8524'] = 'green distressed hibiscus print tankini top,mantaray'
        expected_output['67228'] = 'viva la diva contrast trim court shoes e,simply be'
        expected_output['51147'] = 'animal-print silk-chiffon gown,d&g'
        expected_output['9015'] = 'knot-front stretch-jersey maxi dress,kelly bergin'
        expected_output['32617'] = 'wool varsity jacket,alexander wang'
        expected_output['666'] = 'red, blouse'
        expected_output['555'] = 'reddish, blouse'
        expected_output['11280'] = 'red checked blouse,ann harvey',
        expected_output['32651'] = 'red imperial lily print shell sleeveless blouse,topshop'

        data = self.search_engine.data

        data_set_ids = set(data) & set(expected_output)

        self.assertEquals(len(data_set_ids), len(expected_output))
        self.assertEquals(data_set_ids, data.keys())
        self.assertEquals(data_set_ids, expected_output.keys())


if __name__ == '__main__':
    unittest.main()

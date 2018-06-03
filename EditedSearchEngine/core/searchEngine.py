import math
import re

import depq as DEPQ
from nltk.stem import PorterStemmer

from EditedSearchEngine.utils.parser import clean_string

ps = PorterStemmer()

"""


"""


class SearchEngine:

    def __init__(self, index, data):
        self.index = index
        self.data = data

    def free_text_query(self, query_string):
        """
        Takes a query string and converts to
        :param query_string: String of text containing the query
        :return: List of the r
        """
        # Clean query
        pattern = re.compile('[\W_]+')
        query_string_clean = pattern.sub(' ', query_string)
        query_string_clean = query_string_clean.lower()

        results = list()

        # Check if query token are in index
        for index, word in enumerate(query_string_clean.split()):
            word = ps.stem(word)
            # Only use words that are indexed
            # todo fix
            # if word not in self.index:
            #     results = []
            #     break

            # Calculate the intersection between the results
            # Adds a tuple of results to the current result
            current_index = self.index.items(word)
            # print(current_index)

            # Matching products from the prefix tuples
            matching_products = list()
            for x in range(0, len(current_index)):
                _, ids = current_index[x]
                matching_products += ids

            print(len(matching_products))
            print(matching_products)

            if index == 0:
                results = matching_products
            else:
                # Only get the product that all the query token appear
                results = set(results) & set(matching_products)

        print("Result data:")
        print(len(results))
        print(results)
        return results

    def single_word_query(self, word):

        # Clean Query

        pattern = re.compile('[\W_]+')
        word_clean = pattern.sub(' ', word)
        word_clean = word_clean.lower()
        results = list()

        # Is the word indexed?
        for query in self.index.keys():
            if word_clean.startswith(query):
                # print(self.index[word_clean])
                results.append(self.index[word_clean])

        return results



    def cosine_similarity(self, query, index_text):
        """
        Cosine Similarity(https://en.wikipedia.org/wiki/Cosine_similarity)
        is used to ranked the search result provided by the query function.

        :param query: Search query string
        :param index_text: A given product string of tokens
        :return: A ranking score that determines how similar the query and the provided product is.
        """

        # ensure the input strings are clean

        query = clean_string(query)
        index_text = clean_string(index_text)

        query_count = self.get_term_frequency(query.lower())
        index_text_count = self.get_term_frequency(index_text)

        print(query_count.keys())
        print(index_text_count.keys())

        # Get unique words from both sequences

        # intersection_set = set(query_count.keys()) & set(index_text_count.keys())
        intersection_set = [value for value in query_count.keys() if value in index_text_count.keys()]

        dot_product = 0

        # Get the dot product of the two vectors
        for intersection_word in intersection_set:
            dot_product += query_count[intersection_word] * index_text_count[intersection_word]

        # Calculate the magnitude for the query

        magnitude_query = 0
        for word in query_count:
            magnitude_query += math.pow(query_count[word], 2)

        magnitude_index_string = 0
        for word in index_text_count:
            magnitude_index_string += math.pow(index_text_count[word], 2)

        # return cosine similarity
        return dot_product / math.sqrt(magnitude_query * magnitude_index_string)

    def get_term_frequency(self, query):
        """
        Given an array of string return a dict of the terms and their count in each string
        :param string: A string of text
        :return: Python dict detailing all words and their frequency.
        """

        # words = query[0] + query[1]

        words = query.split()
        term_count = dict()

        for word in words:


            if word not in term_count.keys():
                term_count[word] = 1
            else:
                term_count[word] = term_count[word] + 1

        return term_count

    def search(self, query):

        """
        Procresses a user's query to the engine and returns the most relevant products (10 max)
        :param query: A query string provided by the user and print the results to the console
        :return: None
        """
        depq = DEPQ.DEPQ(iterable=None, maxlen=10)

        # Get a dict of matching product indexed by their id
        results = self.free_text_query(query)
        print(results)

        # Rank Results

        ranking = dict()

        # Find the relevance for each product to the query
        for product in results:
            ranking[product] = self.cosine_similarity(query, self.data[product])
            # item, priority
            depq.insert(product, ranking[product])

        print(depq.size())
        for product in depq:

            # Unpacking score, id.
            name, brand = self.data[product[0]].split(',')
            print("{}, {}, {}, {}".format(round(product[1], 2), product[0], name, brand))


import math
import re
import operator
import pprint as pprint
import depq as DEPQ


class SearchEngine:

    def __init__(self, index, data):
        self.index = index
        self.data = data
        # self.results = None

    def free_text_query(self, query_string):
        # Clean query
        pattern = re.compile('[\W_]+')
        query_string_clean = pattern.sub(' ', query_string)
        query_string_clean = query_string_clean.lower()

        results = []

        for index, word in enumerate(query_string_clean.split()):
            # results[word] = self.single_word_query(word)

            # Only use words that are indexed
            if word not in self.index:
                results = []
                break

            # Calculate the intersection between the results
            current_index = self.index[word]
            if index == 0:
                results = current_index
            else:
                results = set(results) & set(current_index)

        return results

    def single_word_query(self, word):

        # Clean Query

        pattern = re.compile('[\W_]+')
        word_clean = pattern.sub(' ', word)
        word_clean = word_clean.lower()
        results = list()
        keys = self.index.keys()
        # Is the word indexed?
        for query in self.index.keys():
            if word_clean == query:
                # print(self.index[word_clean])
                results.append(self.index[word_clean])

        self.results = results
        return results

    def rank_results(self, result):

        # Get terms frequency of terms for a given string
        pass


    # todo add reference to the cosine matching wikie page or something
    def cosine_similarity(self, query, index_text):
        """

        :param query:
        :param index_text:
        :return:
        """

        # Get string vectors
        # todo refactor
        a = self.get_term_frequency(query.lower())
        b = self.get_term_frequency(index_text.lower())

        # Get unique words from both sequences

        intersection_set = set(a) & set(b)

        dot_product = 0

        # Get the dot product of the two vectors
        for intersection_word in intersection_set:
            dot_product += a[intersection_word] * b[intersection_word]

        # Calculate the magnitude for the query

        magnitude_query = 0
        for word in a:
            magnitude_query += math.pow(a[word], 2)

        magnitude_index_string = 0
        for word in b:
            magnitude_index_string += math.pow(b[word], 2)

        # return cosine similarity
        return dot_product / math.sqrt(magnitude_query * magnitude_index_string)

    def get_term_frequency(self, string):
        """
        Given an array of string return a hash map of the terms and their count in each string
        :param String: A string of text
        :return: Python dict detailing all words and their count.
        """

        words = string.split()
        term_count = dict()

        for word in words:

            if word not in term_count.keys():
                term_count[word] = 1
            else:
                term_count[word] = term_count[word] + 1

        # todo remove this print line
        # print(term_count)
        return term_count

    def search(self, query):
        depq = DEPQ.DEPQ(iterable=None, maxlen=10)

        # Get a dict of matching product indexed by their id
        results = self.free_text_query(query)

        # Rank Results

        ranking = dict()


        # Find the relevance for each product to the query
        for product in results:
           ranking[product] = self.cosine_similarity(query, self.data[product])
           # item, priority
           depq.insert(product, ranking[product])


           # print(queue)

        # print("Size: 10, highest scoring product: {}".format(queue.popfirst()))
        # print(queue)
        # print(depq.high(), depq.low())
        # print(depq)

        # print(self.data)
        print(depq.size())
        for product in depq:


            # unpacking score, id.
            name, brand = self.data[product[0]].split(',')
            # pprint.pprint(product[0], product[1], name, " ", brand)

            print("{}, {}, {}, {} \n".format(product[1], product[0], name, brand))



        # print(ranking)






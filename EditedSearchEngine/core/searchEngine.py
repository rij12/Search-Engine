import re



class SearchEngine:

    def __init__(self, index):
        self.index = index

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

        return results

    def rank_queries(self):
        pass

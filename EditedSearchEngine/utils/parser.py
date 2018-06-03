import csv
import string
import re
# import nltk
# nltk.download('punkt')

from nltk.stem import PorterStemmer

import pygtrie


ps = PorterStemmer()

def parse_csv_file(file):
    """
    loads CSV file and creates an inverted index that stores all tokens in the csv files as a key
    and value: all the products that the token appears in.
    :return: Inverted index
    """
    inverted_index = dict()

    with open(file) as csvfile:
        csv_data = csv.reader(csvfile, delimiter=',')

        for row in csv_data:

            # Strip the string!
            pattern = re.compile('[\W_]+')
            name_string = pattern.sub(' ', row[1])
            brand_string = pattern.sub(' ', row[2])

            name_tokens = name_string.split(" ")
            brand_tokens = brand_string.split(" ")

            #
            for word in name_tokens:
                index = word.lower()
                index = ps.stem(index)

                if index not in inverted_index:
                    inverted_index[index] = list()
                    inverted_index.setdefault(index, []).append(row[0])
                else:
                    inverted_index.setdefault(index, []).append(row[0])

            for brand in brand_tokens:
                index = brand.lower()

                if index not in inverted_index:
                    inverted_index[index] = list()
                    inverted_index.setdefault(index, []).append(row[0])
                else:
                    inverted_index.setdefault(index, []).append(row[0])

    return inverted_index


def get_data(file):

    data = dict()

    with open(file) as csvfile:
        csv_data = csv.reader(csvfile, delimiter=',')
        for row in csv_data:

            blob = row[1].lower() + "," + row[2].lower()
            data[row[0]] = blob

    return data








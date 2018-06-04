import csv
import re

import pygtrie
from nltk.stem import PorterStemmer

ps = PorterStemmer()


def parse_csv_file(file):
    """
    loads CSV file and creates an inverted index that stores all tokens in the csv files as a key
    and value: all the products that the token appears in.
    :return: Inverted index
    """
    inverted_index = pygtrie.CharTrie()

    with open(file) as csvfile:
        csv_data = csv.reader(csvfile, delimiter=',')

        for row in csv_data:

            # Strip the string! = [^a-zA-Z0-9_]
            pattern = re.compile('[\W_]+')
            name_string = pattern.sub(' ', row[1])
            brand_string = pattern.sub(' ', row[2])

            name_tokens = name_string.split(" ")
            brand_tokens = brand_string.split(" ")

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
    """
    Dict containing the data from CSV file used for look up when printing the data
    :param file: csv file containing the data
    :return: dict containing the CSV data
    """

    data = dict()

    with open(file) as csvfile:
        csv_data = csv.reader(csvfile, delimiter=',')
        for row in csv_data:

            blob = row[1].lower() + "," + row[2].lower()
            data[row[0]] = blob

    return data









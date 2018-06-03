import csv
import string
import re
import nltk
nltk.download('punkt')

from nltk.stem import PorterStemmer
from nltk.tokenize import sent_tokenize, word_tokenize

ps = PorterStemmer()

# stop_words = get_stop_words('english')
def parse_csv_file(file):
    """
    loads CSV file from file
    :return: CSV file object
    """
    inverted_index = dict()
    translator = str.maketrans('', '', string.punctuation)

    # s = 'string with "punctuation" inside of it! Does this work? I hope so.&'
    # print(s.translate(translator))

    with open(file) as csvfile:
        csv_data = csv.reader(csvfile, delimiter=',')

        for row in csv_data:

            # row[1] = row[1].translate(translator)
            # row[2] = row[2].translate(translator)


            # Strip the string!
            pattern = re.compile('[\W_]+')
            name_string = pattern.sub(' ', row[1])
            brand_string = pattern.sub(' ', row[2])

            # Stem name and brand string

            # name_string = word_tokenize(row[1])
            # brand_string = word_tokenize(row[2])

            # print(name_string)
            # print(brand_string)

            name_tokens = name_string.split(" ")
            brand_tokens = brand_string.split(" ")

            for word in name_tokens:
                index = word.lower()
                index = ps.stem(index)

                # Do add stop words
                # if word in stop_words:
                #     break

                if index not in inverted_index:
                    inverted_index[index] = list()
                    inverted_index.setdefault(index, []).append(row[0])
                else:
                    inverted_index.setdefault(index, []).append(row[0])

            for brand in brand_tokens:
                index = brand.lower()

                # Do not add stop words
                # if brand in stop_words:
                #     break

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

            blob = row[1].lower() + " " + row[2].lower()
            # blob = blob.split()

            data[row[0]] = blob

    # print(data)

    return data



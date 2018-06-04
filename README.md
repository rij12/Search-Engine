# Edited Interview Search Engine


## How to run

#### Program Arguments:
**--search** File that contains searches on each new line (DEFAULT: "../data/test_search.txt")
**--index** A CSV file to be index (DEFAULT: "../data/search_dataset.csv")

* Export root path, see below for an example command:

```
export PYTHONPATH=$PWD
pip3 install -r requirements.txt --user
python3 EditedSearchEngine/main.py --search data/test_search.txt --index data/search_dataset.csv
```

#### Tests

```
export PYTHONPATH=$PWD
pip3 install -r requirements.txt --user
python3 EditedSearchEngine/tests/test_parser.py
python3 EditedSearchEngine/tests/test_searchEngine.py

```

## Process

Due to the performance requirements I chosse to an inverted index(https://en.wikipedia.org/wiki/Inverted_index) implemented using a Trie (https://en.wikipedia.org/wiki/Trie) to index the CSV input data. The reason I chosse to use a Trie for the implementation of the inverted index over the standard method of dictionary(hash map) because a dictionary only allows exact matches for words. Where as a Trie allows for prefix matches which is what was required by the chaalenge. It also allows for very fast look up.

### Processing the query string
Once the data was indexed, I processed the string into tokens separated via a space, converted each token to lower case and filtered out special charaters. I create two lists: a temp list that obtained the current product matches for the token currently being processed and a "results" list holding the product matching the query search. Each time a token return a list of product id's I found the intersection of the tmp list and the "results" list so that only products that all the required tokens in remained.


### Ranking the results from the query.

The result was a list of id's, for each product queried the data store for name and brand information using its product's id and converted into a vector A. The vector consisted of a dict containing all the unique words and their frequency. The query search string into a vector B. Now I used the Cosine Similarity rule (https://en.wikipedia.org/wiki/Cosine_similarity) to get score of how similar the query and the product's name and brand fields were. This score was used as ranking score for search.

This took into account the amount of words of the query and the index product string so for example a query of "red bag" would yield, product A with "red bag asos" and product B "super crazy red Burton bag". In this case product A would be ranked higher becuse even though both index terms have "red bag" product A has very few words so its words hold higher weight and therefore produces a higher score.

I used dict to store the score and the id as its index, however this wasn't the best choice because I want the id, score and it needed to be ordered by the score of similarity between the query and the index. So I changed the dict to a DEPQ (Double End Priority Queue) because it was ordered using score from the cosine Similarity. I set the Queue to have a maximun length of 10 so that once the queue was full it would pop the element with the lowest score, to result in a list of the 10 top highest scoring elements.

I then printed each element in the DEPQ starting from the highest priority(score) as per the requirements.

### Sample Input

yellow toywatch
asos skinny jeans
toyota car
floral dress
red prada clutch
prada perforated runway duffel bag
guess top
ralph lauren vest

### Sample Output <br />

1 <br />
0.58, 4838, jelly time only watch yellow, toywatch <br />
--- 3.4689903259277345e-07 Milliseconds --- <br />
10 <br />
0.87, 50657, asos skinny carrot jeans, asos <br />
0.87, 19579, asos diamante skinny jeans, asos <br />
0.82, 41460, asos side zip skinny jeans, asos <br />
0.82, 19584, asos lace up skinny jeans, asos <br />
0.77, 50698, asos premium tuxedo tab skinny jeans, asos <br />
0.77, 38097, asos premium washed camo skinny jeans, asos <br />
0.77, 21883, asos petite rich indigo skinny jeans, asos <br />
0.77, 40267, asos petite silver grey skinny jeans, asos <br />
0.77, 41401, asos curve foil armour skinny jeans, asos <br />
0.58, 17898, asos petite mini diamante skinny jean, asos<br />
--- 1.1932849884033203e-06 Milliseconds --- <br />
0 <br />
--- 6.580352783203126e-08 Milliseconds ---
10
0.82, 42719, floral dress, boudicca
0.71, 34217, floral lace dress, unknown
0.71, 30186, floral print dress, linea
0.71, 51983, floral bodycon dress, topshop
0.71, 20406, floral dress, wal-g
0.71, 2836, floral fantasy dress, lanebryant
0.71, 34740, floral spray dress, eastex
0.71, 55109, floral chiffon dress, lanebryant
0.71, 46154, floral strapless dress, jarlo
0.71, 21761, floral lace dress, cc
--- 6.37507438659668e-06 Milliseconds ---
0
--- 4.2009353637695313e-07 Milliseconds ---
1
1.0, 44050, perforated runway duffel bag, prada
--- 6.017684936523438e-07 Milliseconds ---
10
0.87, 57744, guess classic top, guess
0.82, 21843, jody top, guess
0.82, 61175, ornament top, guess
0.82, 26237, patricia top, guess
0.75, 31426, guess sequin animal tunic top, guess
0.75, 13107, guess logo ribbed vest top, guess
0.71, 30148, lydia print top, guess
0.71, 26393, rumer fringe top, guess
0.71, 18892, solid barb top, guess
0.71, 8957, marilyn corset top, guess
--- 1.524209976196289e-06 Milliseconds ---
6
0.75, 26907, rlx ralph lauren ocean down vest, rlx ralph lauren
0.75, 26763, rlx ralph lauren ac targa vest, rlx ralph lauren
0.66, 58504, ralph lauren childrenswear toddler girls' plain vest - sizes 2t-4t, ralph lauren childrenswear
0.65, 22604, ralph lauren childrenswear toddler boys' fairisle sweater vest - sizes 2t-4t, ralph lauren childrenswear
0.65, 2042, ralph lauren childrenswear toddler boys' "ascent" down vest - sizes 2t-4t, ralph lauren childrenswear
0.61, 15244, fair isle knitted sweater vest, polo ralph lauren
--- 7.26938247680664e-07 Milliseconds ---


### Final thoughts

It was Very fun and interesting interview challenge. I actually learned a lot from the challenge, I've never built a search engine before and learned about indexing in particular: Cosine Simularity, inverted index and Trie data structure.








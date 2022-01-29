import re

example_sentence = "This is a string! It contains a price of $12.99"

# regular expression to find a price
price_regex = re.compile(r'\$\d+\.\d\d')

# print the dollar amount that was found
print(price_regex.findall(example_sentence))

# the result is: ['$12.99']



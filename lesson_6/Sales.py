# You have a database on sales of an online store. Every line of an input file is a string containing a
# “Buyer product number of product”. A Buyer is a customer name (a string with no spaces), product is a
# product name (a string with no spaces), number of product is a number of product purchased.
#
# Create a list of buyers, for each buyer count the number of product purchased and the number of each product
# purchased. The list of buyers, as well as the list of all products purchased by each buyer,
# should be output in Lexicographical order.
#
# Input
# [
#      ['Ivanov', 'paper', 10],
#      ['Petrov', 'pens', 5],
#      ['Ivanov', 'marker', 3],
#      ['Ivanov', 'paper', 7],
#      ['Petrov', 'envelope', 20],
#      ['Ivanov', 'envelope', 5]
# ]
#
# Output
# [
#     {
#         'Ivanov': {
#             'envelope': 5,
#             'marker': 3,
#             'paper': 7
#         }
#     },
#     {
#         'Petrov': {
#             'envelope': 20,
#             'pens': 5
#         }
#     }
# ]


def sales(data):
    result = []
    for item in data:
        is_included = False
        buyer_index = None
        index = 0
        while index < len(result):
            buyer = result[index]
            if buyer.get(item[0]) is not None:
                is_included = True
                buyer_index = index
            index += 1
        if not is_included:
            result.append({
                item[0]: {
                    item[1]: item[2]
                }
            })
        else:
            result[buyer_index][item[0]][item[1]] = item[2]
    return result


print(sales(
    [
         ['Ivanov', 'paper', 10],
         ['Petrov', 'pens', 5],
         ['Ivanov', 'marker', 3],
         ['Ivanov', 'book', 7],
         ['Petrov', 'envelope', 20],
         ['Ivanov', 'envelope', 5]
    ]
))

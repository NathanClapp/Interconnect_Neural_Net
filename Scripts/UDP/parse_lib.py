import re
#remove square brackets and space delimit data
def parse_tensor(decoded_tensor):
    #remove [ or ] if encountered in string
    regular_expression = re.compile('([|])')
    return regular_expression.sub('', decoded_tensor)

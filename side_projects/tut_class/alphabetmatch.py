import string

# def alphabet_position(text):
#     text_index = []
    
#     for i in text.lower():
#         if i in string.ascii_lowercase:

#             letter_index = string.ascii_lowercase.index(i)
#             text_index.append(letter_index + 1)
#     index_strings = [str(x) for x in text_index] 
#     result = " ".join(index_strings)
#     print(result)

def alphabet_position_better(text):
    return ' '.join(str(string.ascii_lowercase.index(n.lower()) + 1) for n in text if n.isalpha())




print(alphabet_position_better("The sunset sets at twelve o' clock."))
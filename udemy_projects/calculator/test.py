def do_something(a_list):
    my_string=""
    for element in a_list:
        my_string += element[1]
    return my_string

aladdin_characters = ["Jasmine", "Aladdin", "Fazahl", "Abu", "Razoul"]
print(do_something(aladdin_characters))
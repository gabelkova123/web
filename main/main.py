#number_1: int = 12
#number_2 = 16
#print(number_1,
#      number_2,
#      )
#string_1 = 'hello "world"'
#string_2 = "hello 'world'"
#string_3 = "hello \"world\""
#string_4 = "\n"
#print(string_1,
#      string_4,
#      string_2,
#    string_4,
#    string_3
#      )

def add_numbers(a,b):
    return a + b
result = add_numbers(25, 6)
print(result)

def sum_of_list(numbers):
    return sum(numbers)
result = sum_of_list([1, 23, 3, 41, 58])
print(result)

def join_strings(separator, *strings):
    return separator.join(strings)
result = join_strings(", ", "киви", "банан", "апельсин")
print(result)

def split_string(input_string, delimiter):
    return input_string.split(delimiter)
result = split_string("киви, банан, апельсин", ", ")
print(result)

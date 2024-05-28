#[12:28 PM] Satyam Singh (Unverified)
def ascii_concatenation(input_string):

    concatenated_ascii = ""

    for char in input_string:
        ascii_value = str(ord(char))
        concatenated_ascii += ascii_value

    return concatenated_ascii
 
input_string  = 'ABCDEFG'#= input("Enter the String for the ascii_concatenation: ")

output = ascii_concatenation(input_string)

print(output) 
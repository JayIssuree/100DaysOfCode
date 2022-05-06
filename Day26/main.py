import pandas

alphabetDF = pandas.read_csv("nato_phonetic_alphabet.csv")

alphabet_dict = {row.letter:row.code for (index, row) in alphabetDF.iterrows()}
# print(alphabet_dict)

def convert_string():
    string = input("What would you like to translate into the nato phonetic alphabet?: ")
    try:
        phonetic_array = [alphabet_dict[letter.upper()] for letter in string]
    except KeyError:
        print("Sorry, only letters in the alphabet please.")
        convert_string()
    else:
        print(phonetic_array)

convert_string()
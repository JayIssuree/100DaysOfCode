import pandas

alphabetDF = pandas.read_csv("nato_phonetic_alphabet.csv")

alphabet_dict = {row.letter:row.code for (index, row) in alphabetDF.iterrows()}
print(alphabet_dict)

string = input("What would you like to translate into the nato phonetic alphabet?: ")
phonetic_array = [alphabet_dict[letter.upper()] for letter in string]
print(phonetic_array)
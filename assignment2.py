# Tian Lan

from data import countries_and_capitals, countries, capitals, countries_capitals_dictionary
import re


def main():
    print("I should not be called.")


def write_countries_capitals_to_file(filename):
    """
    This function validates the given filename first and writes country & capital data in certain format to the file.
    If the given filename is not valid, prompt user over and over again until enter a valid filename.
    Valid filename: only contain letters or digits, 1-8 characters long, plus ".txt" file extension.
    :param filename: The given filename.
    :return: The file with valid filename that contains country & capital data in certain format.
    """
    # ".txt" extension, escape special meaning of "."
    while True:
        if re.search("^[A-Za-z0-9]{1,8}[.](txt)$", filename):
            print("Your valid filename is " + str(filename))
            file = open(filename, "w")
            for country, capital in countries_capitals_dictionary.items():  # return key-value pairs
                print_line = f"The capital of {country} is {capital}.\n"  # \n: print each data pair in each line
                file.write(print_line)
            file.close()
            break  # jump out of the loop
        else:
            print("Not a valid filename.")
            filename = input("Enter a file name: ")  # re-assign the variable


def save_capitals():
    vowel_pattern = "[aeiou]{3}"
    cons_pattern = "[bcdfghjklmnpqrstvwxyz]{3}"
    ie_pattern = "i.*e"
    aa_pattern = "^a.*a$"
    end_vowel_pattern = ".*[aeiou]$"
    weird_pattern = "[' *]"
    not_start_pattern = "^[^a-el-ps]"

    file_1 = open("vowel_vowel_vowel.txt", "w")
    for capital in capitals:
        if re.search(vowel_pattern, capital, re.IGNORECASE):  # case insensitive
            file_1.write(capital.lower() + "\n")  # write capitals in lowercase, one capital name each line
    file_1.close()

    file_2 = open("cons_cons_cons.txt", "w")
    for capital in capitals:
        if re.search(cons_pattern, capital, re.IGNORECASE):
            file_2.write(capital.lower() + "\n")
    file_2.close()

    file_3 = open("i_before_e.txt", "w")
    for capital in capitals:
        if re.search(ie_pattern, capital, re.IGNORECASE):
            file_3.write(capital.lower() + "\n")
    file_3.close()

    file_4 = open("a_a.txt", "w")
    for capital in capitals:
        if re.search(aa_pattern, capital, re.IGNORECASE):
            file_4.write(capital.lower() + "\n")
    file_4.close()

    file_5 = open("end_with_vowel.txt", "w")
    for capital in capitals:
        if re.search(end_vowel_pattern, capital, re.IGNORECASE):
            file_5.write(capital.lower() + "\n")
    file_5.close()

    file_6 = open("weird.txt", "w")
    for capital in capitals:
        if re.search(weird_pattern, capital, re.IGNORECASE):
            file_6.write(capital.lower() + "\n")
    file_6.close()

    file_7 = open("not_start.txt", "w")
    for capital in capitals:
        if re.search(not_start_pattern, capital, re.IGNORECASE):
            file_7.write(capital.lower() + "\n")
    file_7.close()


if __name__ == "__main__":
    main()

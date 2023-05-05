from bdflib import reader
from curses import ascii
import sys

def get_hex(number):
    """
    This function return number as hex byte string.
    :number: Number to return as string
    :return: String with number 
    """

    hex_string = hex(number).upper()
    if len(hex_string) == 3:
        hex_string = hex_string[0:2] + "0" + hex_string[2]
    return hex_string.replace("X", "x")


def get_letter(letter):
    """
    This function return description as letter.
    :letter: Number of letter in ASCII
    :return: String with description for comment
    """

    if letter == 0x20:
        return "' ' SP"
    if letter < len(ascii.controlnames):
        return "\"" + ascii.unctrl(letter) + "\" " + ascii.controlnames[letter]
    if ascii.isprint(letter): 
        if letter == ord("'"): return "'\\''"
        if letter == ord("\\"): return "'\\\\'"
        return "'" + chr(letter) + "'"
    return ascii.unctrl(letter)

def get_comment(letter):
    """
    This function return description line for letter.
    :letter: Letter to create description for
    :return: Description line
    """

    return "# " + get_hex(letter) + " " + get_letter(letter)



def get_bitmap(letter):
    """
    This function create bitmat in CSV format.
    :ltter: Letter as bool array.
    :return: CSV format bitmap
    """

    result = ""

    for line in letter:
        for pixel in line:
            result += str(int(pixel)) + ","
        result += "\n"

    return result


def main():
    if len(sys.argv) <= 1:
        print("Run bdf2csv.py [bdf filename] > [csv filename]")
        exit(0)

    filename = sys.argv[1]

    with open(filename, "rb") as font_file:
        font = reader.read_bdf(font_file)

    width = font.glyphs[0].bbW
    height = font.glyphs[0].bbH

    for letter_number in range(256):
        try:
            letter = font[letter_number]
            letter_array = list()
            for line in letter.iter_pixels():
                letter_array.append(list())
                for pixel in line:
                    letter_array[-1].append(pixel)

            while len(letter_array) < height:
                letter_array.append(list())

            for count in range(len(letter_array)):
                while len(letter_array[count]) < width:
                    letter_array[count].append(False)
            
        except:
            letter_array = list([list([False] * width)] * height)  
    
        print(get_comment(letter_number))
        print(get_bitmap(letter_array))


if __name__ == "__main__":
    main()

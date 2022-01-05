# Write your solution here
import string 
# from string import ascii_letters,punctuation
def separate_characters(text):
    ascii_letters=punctuation=characters=""
    # parts = ()
    for letter in text:
        # print(letter)
        if letter in string.ascii_letters:
            ascii_letters+=letter
        elif letter in string.punctuation:
            punctuation+=letter
        else:
            characters+=letter

    parts=(ascii_letters,punctuation,characters)
    return parts

if __name__ == "__main__":
    parts= separate_characters("Olé!!! Hey, are ümläüts wörking?")
    print(parts[0])
    print(parts[1])
    print(parts[2])

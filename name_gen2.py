import random, string

vowels = "aeiouy"
consonants = "bcdfghjklmnpqrstvwxz"
letters = string.ascii_lowercase

letterimport1 = input("Please indicate the first type of letter you'd like (Enter 'v' for a vowel, 'c' for a consonant, and 'l' for any letter): ")
letterimport2 = input("Please indicate the second type of letter you'd like (Enter 'v' for a vowel, 'c' for a consonant, and 'l' for any letter): ")
letterimport3 = input("Please indicate the third type of letter you'd like (Enter 'v' for a vowel, 'c' for a consonant, and 'l' for any letter): ")

def generator():
    if letterimport1 == "v":
        letter1 = random.choice(vowels)
    elif letterimport1 == "c":
        letter1 = random.choice(consonants)
    elif letterimport1 == "l":
        letter1 = random.choice(letters)
    else:
        letter1 = letterimport1


    if letterimport2 == "v":
        letter2 = random.choice(vowels)
    elif letterimport2 == "c":
        letter2 = random.choice(consonants)
    elif letterimport2 == "l":
        letter2 = random.choice(letters)
    else:
        letter2 = letterimport2


    if letterimport3 == "v":
        letter3 = random.choice(vowels)
    elif letterimport3 == "c":
        letter3 = random.choice(consonants)
    elif letterimport3 == "l":
        letter3 = random.choice(letters)
    else:
        letter3 = letterimport3

    name = letter1+letter2+letter3

    return name

for i in range(10):
    print(generator())

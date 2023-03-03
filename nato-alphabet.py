# Define the NATO phonetic alphabet dictionary
nato_alphabet = {
    'A': 'Alpha',
    'B': 'Bravo',
    'C': 'Charlie',
    'D': 'Delta',
    'E': 'Echo',
    'F': 'Foxtrot',
    'G': 'Golf',
    'H': 'Hotel',
    'I': 'India',
    'J': 'Juliet',
    'K': 'Kilo',
    'L': 'Lima',
    'M': 'Mike',
    'N': 'November',
    'O': 'Oscar',
    'P': 'Papa',
    'Q': 'Quebec',
    'R': 'Romeo',
    'S': 'Sierra',
    'T': 'Tango',
    'U': 'Uniform',
    'V': 'Victor',
    'W': 'Whiskey',
    'X': 'Xray',
    'Y': 'Yankee',
    'Z': 'Zulu'
}

# Define a function to translate a word to the NATO alphabet
def translate_word(word):
    translated_word = []
    for letter in word.upper():
        if letter in nato_alphabet:
            translated_word.append(nato_alphabet[letter])
    return translated_word

# Test the function
word = input("Enter a word to translate to the NATO alphabet: ")
translated_word = translate_word(word)
print(" ".join(translated_word))

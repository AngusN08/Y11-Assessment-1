import requests

# You can ignore how this function works, it's just used to get the list of words in all_words
def get_valid_wordle_words():
    str_words = []
    words_text = requests.get("https://raw.githubusercontent.com/tabatkins/wordle-list/refs/heads/main/words") \
                        .content
    words = words_text.split()
    for word in words:
        str_words.append(str(word.decode('ascii')))
    return str_words

# all_words will contain a list of all valid words that you can use
all_words = get_valid_wordle_words()

letter_freq = {}

# Count the frequency of each letter
for word in all_words:
    for letter in word:
        if letter in letter_freq:
            letter_freq[letter] += 1
        else:
            letter_freq[letter] = 1

# Manually find the most used letter
most_used_letter = ''
highest_count = 0

for letter in letter_freq:
    count = letter_freq[letter]
    if count > highest_count:
        highest_count = count
        most_used_letter = letter

print(f"The most used letter is '{most_used_letter}' with {highest_count} occurrences.")
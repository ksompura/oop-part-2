def single_letter_count(words,letter):
    words = words.lower()
    letter = letter.lower()
    count = 0
    for i in words:
        if letter == i:
            count +=1
    return count

print(single_letter_count("It's a tuesday Ian", "A"))

##Another solution
def single_letter_count(string,letter):
    return string.lower().count(letter.lower())
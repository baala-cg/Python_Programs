def align_vowels_and_consonants(text):

    result = []

    for word in text.split():

        vowels = ''.join(ch for ch in word if ch.lower() in 'aeiou')

        consonants = ''.join(ch for ch in word if ch.lower() not in 'aeiou')

        result.append(vowels + consonants)

    return ' '.join(result)


print(align_vowels_and_consonants("Sample run"))
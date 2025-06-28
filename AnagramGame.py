from collections import defaultdict

def group_anagrams(a):

    dfdict = defaultdict(list)

    for i in a:
        convert_i = "".join(filter(str.isalpha, i)).lower()

        sorted_i = "".join(sorted(convert_i))

        dfdict[sorted_i].append(i)
    return dfdict.values()

if __name__ == "__main__":
    words = []
    print("Let's play Anagram!")

    
    while True:
        word = input("Enter a word: ")
        if word.lower() == 'done':
          break
        elif word:
            words.append(word)
        else:
            print("Please enter a word or 'done' to finish")

    anagram_groups = group_anagrams(words)
    print(anagram_groups)
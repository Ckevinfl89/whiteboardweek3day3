# Given two strings ransomNote and magazine, return true if ransomNote can be constructed from magazine and false otherwise.
# Each letter in magazine can only be used once in ransomNote.

# Example 1:				
# Input: ransomNote = "a", magazine = "b"
# Output: false
# Example 2:
# Input: ransomNote = "aa", magazine = "ab"
# Output: false
# Example 3:
# Input: ransomNote = "aa", magazine = "aab"
# Output: true

def solution(ransomNote, magazine):
    for chr in set(ransomNote):
        if ransomNote.count(chr) > magazine.count(chr):
            return False
        return True
    



    
def solution1(ransom_note, magazine ):
    words= {}
    for letters in ransom_note:
        if letters not in words:
            words[letters] = 1
        else:
            words[letters] += 1
    print(words,"getting count needed")
    for letters in magazine:
        if letters in words:
            words[letters] -= 1
    print(words,"take away what i found")
    for x in words.values():
        print(x)
        if x > 0:
            return False
    return True

print(solution1("aa",'ab'))



def solution(ransom, magazine):
    magazine_letters = list(magazine)
    for letter in ransom:
        if letter in magazine_letters:
            magazine_letters.remove(letter)
        else:
            return False
    return True

from collections import Counter
def solution(ransom, magazine):
    ransom_count = Counter(ransom)
    magazine_count = Counter(magazine)
    for letter, count in ransom_count.items():
        if magazine_count.get(letter, 0) < count:
            return False
    return True
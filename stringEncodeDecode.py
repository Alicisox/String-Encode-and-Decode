# Learned about UTF-8, ASCII, Encoding and decoding using multiple methods
# Change string to integer length = 0 -> length*10 + integer 
# While can use to loop increment variables instead of multiple if-else (complicated)
# Careful checking outofrange of an index
# Fix pattern safes time

# Learning

def basic_encode(text):
    shift = 50
    hashval = ''
    for s in text:
        hashval += chr((ord(s) + shift)%256)
        print((ord(s) + shift)%256)
    return hashval

def basic_decode(text):
    shift = -50
    hashval = ''
    for s in text:
        hashval += chr((ord(s) + shift)%256)
    return hashval

def is_digit(s):
    return '0' <= s <= '9'

# Problem solution start here

class Solution:

    def encode(self, strs) -> str:
        for i in range(len(strs)):
            strs[i] = str(len(strs[i])) + "#" + strs[i]
        strs = "".join(strs)
        return strs

    def decode(self, s: str):
        res = []
        i = 0
        while i < len(s):
            length = 0
            while i < len(s) and s[i].isdigit():
                length = length*10 + int(s[i])
                i += 1
            if i < len(s) and s[i] == "#" and i + length < len(s):
                i += 1
                j = length
                word = ""    
                while j > 0:
                    word += s[i]
                    j -= 1
                    i += 1
                res.append(word)
            else:
                break
        return res
    
    def decode_shortversion(self, s: str):
        res = []
        i = 0
        while i < len(s):
            length = 0
            while i < len(s) and s[i].isdigit():
                length = length*10 + int(s[i])
                i += 1
            if i < len(s) and s[i] == "#" and i + length < len(s):
                i += 1
                res.append(s[i:i+length])
                i += length
        return res
    
    def encode_optimal(self, strs) -> str:
        res = ""
        for s in strs:
            res += str(len(s)) + "#" + s # Imbue word count and delimitor #
        return res

    def decode_optimal(self, s: str):
        res = []
        i = 0
        while i < len(s):
            j = i # Iterator
            while s[j] != "#": # Find the delimitor '#'
                j += 1
            length = int(s[i:j])
            i = j + 1 # (first index)
            j = i + length # word index (1+last index)
            res.append(s[i:j])
            i = j # shift index to new word
        return res
    
# Testing
strs = ["neet#","3code","4love","#you#"]

x = Solution().encode_optimal(strs)

print(x)

print(Solution().decode_optimal(x))

print(Solution().decode_shortversion(x))

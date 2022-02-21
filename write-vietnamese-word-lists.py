import urllib.request
import re

ignore_chars = {'!','"',"'",'(',')','*',',','-','.','/','0','1','2','3','4','7','8',':',';','<','>','[',']','f','j','w','z' }

# https://gist.github.com/jarvisluong/f01e108e963092336f04c4b7dd6f7e45
def sanitize_word(s:str):
    s = re.sub(r'à|á|ạ|ả|ã|â|ầ|ấ|ậ|ẩ|ẫ|ă|ằ|ắ|ặ|ẳ|ẵ', "a", s)
    s = re.sub(r'è|é|ẹ|ẻ|ẽ|ê|ề|ế|ệ|ể|ễ', "e", s)
    s = re.sub(r'ì|í|ị|ỉ|ĩ', "i", s)
    s = re.sub(r'ò|ó|ọ|ỏ|õ|ô|ồ|ố|ộ|ổ|ỗ|ơ|ờ|ớ|ợ|ở|ỡ', "o", s)
    s = re.sub(r'ù|ú|ụ|ủ|ũ|ư|ừ|ứ|ự|ử|ữ', "u", s)
    s = re.sub(r'ỳ|ý|ỵ|ỷ|ỹ', "y", s)
    s = re.sub(r'đ', "d", s)
    return s

data = urllib.request.urlopen('https://github.com/duyet/vietnamese-wordlist/raw/master/Viet11K.txt').read().decode('utf-8')
words_5_11k = set()
for line in data.split('\n'):
    words = line.rstrip().split(' ')
    for word in words:
        word = sanitize_word(word.lower())
        if any([c in word for c in ignore_chars]):
            continue
        if len(word) == 5:
            words_5_11k.add(word)
with open('words_5_11k.txt', 'w') as f:
    for word in words_5_11k:
        f.write(f"'{word}',\n")

data = urllib.request.urlopen('https://github.com/duyet/vietnamese-wordlist/raw/master/Viet74K.txt').read().decode('utf-8')
words_5_74k = set()
chars = set()
for line in data.split('\n'):
    words = line.rstrip().split(' ')
    for word in words:
        word = sanitize_word(word.lower())
        if any([c in word for c in ignore_chars]):
            continue
        for char in word:
            chars.add(char)
        if len(word) == 5:
            words_5_74k.add(word)
with open('words_5_74k.txt', 'w') as f:
    for word in words_5_74k:
        f.write(f"'{word}',\n")

with open('chars.txt', 'w') as f:
    for char in chars:
        f.write(f"'{char}',\n")

file = open("stopwords.txt")
stopwordsRaw = file.readlines()
stopwords = []

for word in stopwordsRaw:
    stopwords.append(word.strip())

# removes stopwords from input
def filter(input):
    print stopwords
    words = input.split(' ')
    for word in words:
        if word in stopwords:
            print "stopword: " + word
            words.remove(word)
    return ' '.join(words)

while True:
    input = raw_input("Say something interesting: ")
    filtered = filter(input)
    print('filtered: ' + filtered)
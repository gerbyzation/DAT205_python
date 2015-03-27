# read stopwords file
file = open("stopwords.txt")
stopwordsRaw = file.readlines()
stopwords = []

# read countries file
countries = []
countriesRaw = open("countries.txt").readlines()
for country in countriesRaw:
    countries.append(country.split('|')[1].strip())

person = {}

for word in stopwordsRaw:
    stopwords.append(word.strip())


def ask(question):
    input = raw_input(question + " ")
    words = input.split(' ')
    for word in words:
        if word in stopwords:
            print "stopword: " + word
            words.remove(word)
    return ' '.join(words)

##########
# Asking for name
##########
nameInput = ask("Hi! What's your name?")
# assuming people always mention their name last
name = nameInput.split(' ')[-1]
person['name'] = name
print "Nice to meet you " + name + "!"

locationInput = ask("In what country do you live?")
locWords = locationInput.split(' ')
for word in locWords:
    print locWords
    if locWords in countries:
        print "I have always wanted to go to " + word + "! Have a few friends who live there."
    else:
        print "Cool!"

input = raw_input("Say something interesting: ")
filtered = filter(input)
print('filtered: ' + filtered)

# List of countries foudn at: https://gist.github.com/marijn/396531
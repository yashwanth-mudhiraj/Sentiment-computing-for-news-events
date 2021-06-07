import nltk
from nltk.tokenize import sent_tokenize, word_tokenize
from nltk.corpus import stopwords
from nltk.stem import PorterStemmer
from nltk.stem import WordNetLemmatizer


raw_news = open("hi.txt", "r")
news = raw_news.read()
stop_words = set(stopwords.words("english"))

words = word_tokenize(news)

filtered_news = []

for i in words:
    if i not in stop_words:
        filtered_news.append(i)

print(filtered_news)

# words = ["cats","geese"]

lemmatizer = WordNetLemmatizer()
lemmatized_news = []
for l in filtered_news:
    lemmatized_news.append(lemmatizer.lemmatize(l))

print(lemmatized_news)

tagged_news = []

def process_tag():
    try:
        for i in lemmatized_news:
            words = word_tokenize(i)
            tagged_news.append(nltk.pos_tag(words))

    except Exception as e:
        print(str(e))


process_tag()
print(tagged_news)



# def process_chunk():
#     try:
#         for j in lemmatized_news:
#             words1 = nltk.word_tokenize(j)
#             tagged_news1 =  nltk.pos_tag(words1)
#             chunkGram = r"""Chunk: {<RB.?>*<VB.?>*<NNP>+<NN>?}"""
#             chunkParser = nltk.RegexpParser(chunkGram)
#             chunked_news = chunkParser.parse(tagged_news1)
#             chunked_news.draw()
#
#     except Exception as e:
#         print(str(e))
#
# process_chunk()



ps = PorterStemmer()
stemmed_news = []

for w in lemmatized_news:
    stemmed_news.append(ps.stem(w))

print(stemmed_news)



# def process_content():
#     try:
#         for i in lemmatized_news:
#             words = nltk.word_tokenize(i)
#             tagged = nltk.pos_tag(words)
#
#             namedEnt = nltk.ne_chunk(tagged)
#
#             namedEnt.draw()
#
#     except Exception as e:
#         print(str(e))
#
#
# process_content()






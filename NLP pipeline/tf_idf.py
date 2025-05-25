import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
import scipy.sparse.csr



data = pd.read_json("/home/milad/python projects/twittercrawler/fa1tweetes.json")
NewCorpus = list(data['text'])
print(NewCorpus)

stop_words = ['با', 'و', 'از', 'تا', 'به' , 'را']
corpusTest = [

    'سلام به همه',
    'من با شما کاری ندارم',
    'این وقت روز هوا چقدر ابری است',

]

vectorizer = TfidfVectorizer(stop_words=stop_words)
x = vectorizer.fit_transform(NewCorpus)

print(x.shape)


#print(vectorizer.get_feature_names())
#print(type(x))
#print(x)
#print(x.todense())
#print(x[0,:].toarray())

from gensim.models import KeyedVectors
import numpy as np
from gensim.models import Word2Vec
import random
from gensim.test.utils import datapath, get_tmpfile
from gensim.models import word2vec

w2v25 = word2vec.Word2Vec.load('w2v25')
w2v50 = word2vec.Word2Vec.load('w2v50')
w2v75 = word2vec.Word2Vec.load('w2v75')
w2v100 = word2vec.Word2Vec.load('w2v100')
w2v200 = word2vec.Word2Vec.load('w2v200')
glo25 = KeyedVectors.load_word2vec_format('glove_model25d.txt',binary=False)
w2vsg25=word2vec.Word2Vec.load('w2vsg25')
w2vsg50=word2vec.Word2Vec.load('w2vsg50')
w2vsg75=word2vec.Word2Vec.load('w2vsg75')
w2vsg100=word2vec.Word2Vec.load('w2vsg100')
w2vsg200=word2vec.Word2Vec.load('w2vsg200')
w2vhs200=word2vec.Word2Vec.load('w2vhs200')
w2vcbowsum200=word2vec.Word2Vec.load('w2vcbowsum200')
w2v10epo200=word2vec.Word2Vec.load('w2vc10epo200')

with open('analogy_dataset.txt', 'r') as fh:
    word = fh.read()


def analogy(vec1,a,b,c,d):
    temp=vec1.most_similar([a,b],[c],topn=3)
    if d==temp[0][0]:
        return 3
    elif d==temp[1][0]:
        return 2
    elif d==temp[2][0]:
        return 1
    else:
        return 0

def analogyscore(vec1,wordlist):
    total=0
    n=len(wordlist)/4
    for i in range (n):
        total+=analogy(vec1,wordlist[4*i],wordlist[4*i+1],wordlist[4*i+2],wordlist[4*i+3])
    return total

if __name__ == "__main__":


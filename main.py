import spacy
from spacy.lang.en.stop_words import STOP_WORDS
from string import punctuation
from heapq import nlargest


text = """  """

def summerycalc(rawdocs):
    
   

# GET STOP WORDS
 stopword = list(STOP_WORDS)
# print(stopword)

# now we load the text in nlp
 nlp = spacy.load('en_core_web_sm')
 doc = nlp(rawdocs)
# print(doc)

# now we create the list and insert doc data
 tokens = [token.text for token in doc]
# print(tokens)

# Now word count and add to the dictionary
 word_freq = {}

 for word in doc:
     if word.text.lower() not in stopword and word.text.lower()  not in punctuation:
         if word.text not in word_freq.keys():
             word_freq[word.text] = 1
         else:
            word_freq[word.text] +=1

# print(word_freq)
# print max frequency values
 max_freq = max(word_freq.values())
# print(max_freq)

# set make sentence and divede the coresponding word frequency to max frequebcy count

 for word in word_freq.keys():
     word_freq[word] = word_freq[word]/max_freq

# print(word_freq)

# Make sentense list based array

 sent_tokens = [sent for sent in doc.sents]
# print(sent_tokens)

 sent_scores = {}

 for sent in sent_tokens:
     for word in sent:
         if word.text in word_freq.keys():
             if sent not in sent_scores.keys():
                sent_scores[sent] = word_freq[word.text]
             else:
                 sent_scores[sent]+=word_freq[word.text]

# print(sent_scores)

 select_len = int(len(sent_tokens) * 0.3)

# make summery
 summery = nlargest(select_len,sent_scores,key = sent_scores.get)

# print(summery)

 final_summery = [word.text for word in summery]
 summery = ' '.join(final_summery)

#  print(summery)
#  print("length of original text",len(text.split(' ')))
#  print("length of summery text",len(summery.split(' ')))

#  return summery,doc,len(text.split(' ')),len(summery.split(' '))
 swc = len(summery.split(' '))
 dwc = len(rawdocs.split(' '))

 return summery,swc,dwc





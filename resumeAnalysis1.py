import textract
import re
from nltk.stem import PorterStemmer
from nltk.tokenize import word_tokenize

document = textract.process('bold_cv-converted.docx')
import  pdb; pdb.set_trace()
ps = PorterStemmer()

words = word_tokenize(document)
email = ''
# for word in words:
email = re.findall('\S+@\S+', document)

start_length = document.find(ps.stem('experi'))
# for word in words:
#     if 'experi' in ps.stem(word):
#         import pdb; pdb.set_trace()
#         print word

print document
print re.split('\s{4}', document)

print 'email : {}'.format(email[0])

# import re 

# patterns='welcome'
# text='wel dhruvin hello'
# a=re.search(patterns,text)
# print(a)

import re

s='A paragraph is a series of related sentences developing a central idea, called the topic. Try to think about paragraphs in terms of thematic unity: a paragraph is a sentence or a group of sentences that supports one central, unified idea. Paragraphs add one idea at a time to your broader argument.'

pattern='a' 

b=re.search(pattern,s)

print(b)
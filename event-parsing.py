from __future__ import unicode_literals
import spacy
from spacy import displacy

text = u"Puts the key into door"

nlp = spacy.load('en_core_web_sm')
doc = nlp(text)

event_formula =[]
for token in doc:
    if token.pos_ is 'VERB':
        event_formula.append(token.text)
        event_formula.append('(')
        for child in token.children:
            print(child)
            if child.dep_ is 'dobj':
                event_formula.append('x')
            if child.dep_ is 'prep':
                event_formula.append(',')
                event_formula.append(child.text)
                event_formula.append('(y)')
            if child.dep_ is 'conj':
                event_formula.append(' and ')
event_formula.append(')')
print(event_formula)

#options = {'collapse_phrases': True}
#displacy.serve(doc, style='dep', options=options)

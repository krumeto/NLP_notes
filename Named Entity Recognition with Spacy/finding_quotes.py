import spacy
import re
from spacy import displacy

with open("./data/alice.txt", 'r', encoding="utf-8") as file:
    text = file.read().replace("\n\n", " ").replace('\n', " ")
    chapters = text.split("CHAPTER ")[1:]
    chapter1 = chapters[0]

def find_sents(text = chapter1):
    nlp = spacy.load('en_core_web_sm')
    doc = nlp(text)
    sentences = list(doc.sents)
    return sentences

def get_quotes(text):
    quotes = re.findall(r'[“](.*?)[”]', text)
    return quotes


found_sents = find_sents()
for sent in found_sents:
    str_sent = str(sent)
    found_quotes = get_quotes(str_sent)

    if len(found_quotes) > 0:
        print(found_quotes)

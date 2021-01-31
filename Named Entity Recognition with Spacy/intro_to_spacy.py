### Small intro to spaCy, following the Python for Digital Humanities tutorial
import spacy
import textacy
from spacy import displacy

#Breaking into chapters
with open("./data/alice.txt", 'r', encoding="utf-8") as f:
    text = f.read().replace("\n\n", " ").replace("\n", " ")
    chapters = text.split('CHAPTER ')[1:]

chapter1 = chapters[12]

nlp = spacy.load('en_core_web_md')

doc = nlp(chapter1)
sentences = list(doc.sents)

# for i, sent in enumerate(sentences[:15]):
#     if 'considering' in sent.text:
#         print(i, sent)

sentence = sentences[9]


# print(sentence)
# ents = list(sentence.ents)
# print(ents)
# print(ents[1].label)
# print(ents[1].label_)
# print(ents[1].text)

# people = []

# full_ents = list(doc.ents)
# for ent in full_ents:
#     if ent.label_ == "PERSON":
#         people.append(ent.text)

# print(set(people))

# nouns = []
# for token in sentence:
#     if token.pos_ == 'NOUN':
#         nouns.append(token)

# print(nouns)

## Noun chunks are groups that are linked to a noun "the book", "a very small cake", "New York City Police Station"
# chunks = list(doc.noun_chunks)

# for chunk in chunks:
#     if "watch" in chunk.text:
#         print(chunk)

## Verbs - find patterns

# patterns = [{"POS": 'ADV'}, {"POS":"VERB"}]

# verb_phrases = textacy.extract.matches(doc, patterns=patterns)

# for verb_phrase in verb_phrases:
#     print(verb_phrase)

# patterns = [[{"POS": 'NOUN'}, {"POS":"VERB"}, {"POS": 'ADV'}], [{"POS": 'PRON'}, {"POS":"VERB"}, {"POS": 'ADV'}]]

# verb_phrases = textacy.extract.matches(doc, patterns=patterns)

# for verb_phrase in verb_phrases:
#     print(verb_phrase)

### Lemmatization

# for word in sentence:
#     if word.pos_ == 'VERB':
#         print(word, word.lemma_)

### Displacy

colors = {"PERSON": "4E0000"}
options = {'ents': ['PERSON'], 'colors': colors}

html = displacy.render(
    sentence, 
    style="ent",
    options = options
    )

with open("dataviz.html", "w") as f:
    f.write(html)

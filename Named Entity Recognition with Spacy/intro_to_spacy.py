### Small intro to spaCy, following the Python for Digital Humanities tutorial
import spacy

#Breaking into chapters
with open("./data/alice.txt", 'r', encoding="utf-8") as f:
    text = f.read().replace("\n\n", " ").replace("\n", " ")
    chapters = text.split('CHAPTER ')[1:]

chapter1 = chapters[12]

nlp = spacy.load('en_core_web_md')

doc = nlp(chapter1)
sentences = list(doc.sents)


sentence = sentences[0]
print(sentence)
ents = list(sentence.ents)
print(ents)
print(ents[1].label)
print(ents[1].label_)
print(ents[1].text)

people = []

full_ents = list(doc.ents)
for ent in full_ents:
    if ent.label_ == "PERSON":
        people.append(ent.text)

print(set(people))

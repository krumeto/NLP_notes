### Small intro to spaCy, following the Python for Digital Humanities tutorial
import spacy

#Breaking into chapters
with open("./data/alice.txt", 'r', encoding="utf-8") as f:
    text = f.read()
    chapters = text.split('CHAPTER ')[1:]
    print(chapters[1])


nlp = spacy.load('en_core_web_sm')

doc = nlp(chapters[0])

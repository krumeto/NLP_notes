import json
import requests

print("This is a flowed, bad, rule-based NER used to educate")
print("This code follows a YouTube tutorial https://www.youtube.com/watch?v=O_2uq0sdCQo&list=PL2VXyKi-KpYs1bSnT8bfMFyGS-wMcjesM&index=2&ab_channel=PythonTutorialsforDigitalHumanities")

hp_link = 'https://raw.githubusercontent.com/wjbmattingly/ner_youtube/main/data/hp.txt'

# Download and read the hp text file
with requests.get(hp_link) as page:
    download = page.text

with open('hp.txt', 'w', encoding='utf-8') as f:
    f.write(download)

with open ("hp.txt", "r", encoding="utf-8") as f:
    text = f.read().split("\n\n\n")
    print(text[3:4])

text = text[3:4]
#Download and read the json characters file

char_list_link = 'https://raw.githubusercontent.com/wjbmattingly/ner_youtube/main/data/hp_characters.json'

with requests.get(char_list_link) as char_page:
    characters = char_page.json()
    print(characters)

character_names = []
for char in characters:
    names = char.split()
    for name in names:
        if 'and' != name and 'the' != name and 'The' != name:
            name = name.replace(",", " ").strip()
            character_names.append(name)

for segment in text:
    print(segment)
    segment = segment.strip()
    segment = segment.replace("\n", " ")
    #TODO remove punctuation
    
    words = segment.split()
    print(words)


    i = 0
    for word in words:
        if word in character_names:
            if words[i-1][0].isupper():
                print(f"Found Characters: {words[i-1]} {word}")
            else:
                print(f"Found Charachters: {word}")

        i=i+1
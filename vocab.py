import json

with open('vocab_files/nouns.json', 'r') as fp:
    nouns = json.load(fp)
with open('vocab_files/verbs.json', 'r') as fp:
    verbs = json.load(fp)
with open('vocab_files/adjectives.json', 'r') as fp:
    adjectives = json.load(fp)

vocab = {
    "nouns": nouns, 
    "verbs": verbs, 
    "adjectives": adjectives}



import re
import json
import random

def process_sentence(original_sentence):
    words = re.findall(r'@[\w\$]+|[\w\*]+|[\,\.\'@\$]+', original_sentence)
    ori = ' '.join(words)
    return ori

def random_deletion(sentence, p=0.2):
    words = sentence.split()
    if len(words) == 1:
        return sentence
    remaining = list(filter(lambda x: random.random() > p or x in ["@DRUG1", "@DRUG2"], words))
    if len(remaining) == 0:
        return random.choice(words)
    return ' '.join(remaining)

with open('dataset/DDI/k-shot/1-1/aaaaaa.txt', 'r') as file, open('dataset/DDI/k-shot_RaDe/1-1/train_da.txt', 'w') as output_file:
    for line in file:
        data = json.loads(line)

        ori = process_sentence(' '.join(data["token"]))
        processed_sentence = random_deletion(ori)

        data["token"] = processed_sentence.split()
        words = data["token"]

        e1_start, e1_end, e2_start, e2_end = None, None, None, None

        for idx, word in enumerate(words):
            if word == "@DRUG1":
                e1_start, e1_end = idx, idx + 1
            elif word == "@DRUG2":
                e2_start, e2_end = idx, idx + 1

        token = words
        e1_pos = [e1_start, e1_end]
        e2_pos = [e2_start, e2_end]
        relation = data["relation"]
        d = {
            "token": words,
            "h": {
                "name": "@DRUG1",
                "pos": e1_pos
            },
            "t": {
                "name": "@DRUG2",
                "pos": e2_pos
            },
            "relation": relation
        }

        json.dump(d, output_file)
        output_file.write('\n')

from Google_Text_TransAPI import GoogleTrans
from tqdm import tqdm
import re
import json

#读取token
def process_sentence(original_sentence):

    sentence_1 = original_sentence

    words = re.findall(r'@[\w\$]+|[\w\*]+|[\,\.\'@\$]+', original_sentence)
    sentence_1 = ' '.join(words)

    return sentence_1

trans = GoogleTrans()
def translate_google(text):
    global trans
    return  trans.backTrans(text)

with open('dataset/DDI/k-shot/1-1/aaaaaa.txt', 'r') as file, open('dataset/DDI/k-shot_TranDA/1-1/train_da.txt', 'w') as output_file:
    for line in file:
        data = json.loads(line)

        sentence_1= process_sentence(' '.join(data["token"]))

        processed_sentences = [sentence_1]
        for idx, processed_sentence in enumerate(processed_sentences):

            processed_sentence = str(processed_sentence)
            processed_sentence = re.sub(r'(@DRUG[12])', r'[\1]', processed_sentence)

            processed_sentence = trans.backTrans(processed_sentence)
            print('processed_sentence:',processed_sentence)

            processed_sentence = re.sub(r'\[|\]', '', processed_sentence)

            print('processed_sentence:',processed_sentence)



            data["token"] = processed_sentence.split()
            words = data["token"]

            e1_start = None
            e1_end = None
            e2_start = None
            e2_end = None

            for idx, word in enumerate(words):
                if word == "@DRUG1":
                    e1_start = idx
                    e1_end = idx + 1
                elif word =="@DRUG2":
                    e2_start = idx
                    e2_end = idx + 1


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
import nlpaug.augmenter.word as naw
import re
import json


aug = naw.SynonymAug(aug_src='wordnet')


def process_sentence(original_sentence):

    ori = original_sentence

    words = re.findall(r'@[\w\$]+|[\w\*]+|[\,\.\'@\$]+', original_sentence)
    ori = ' '.join(words)

    return ori


with open('dataset/DDI/k-shot/1-1/aaaaaa.txt', 'r') as file, open('dataset/DDI/k-shot_SyDA/1-1/train_da.txt', 'w') as output_file:
    for line in file:
        data = json.loads(line)

        ori = process_sentence(' '.join(data["token"]))

        processed_sentences = [ori]
        exclude_words = ["@DRUG1", "@DRUG2"]

        augmentation_factor = 1

        augmented_texts = []
        for _ in range(augmentation_factor):
            words = ori.split()
            augmented_words = []

            for word in words:

                if word in exclude_words:
                    augmented_words.append(word)
                else:
                    augmented_word = aug.augment(word)
                    if isinstance(augmented_word, list):
                        augmented_word = augmented_word[0]
                    augmented_words.append(augmented_word)

            augmented_text = " ".join(augmented_words)
            augmented_texts.append(augmented_text)

        for idx, processed_sentence in enumerate(augmented_texts):

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
                elif word == "@DRUG2":
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


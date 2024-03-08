import re
import json
import openai

def process_sentence(original_sentence):

    words = re.findall(r'@[\w\$]+|[\w\*]+|[\,\.\'@\$]+', original_sentence)
    ori = ' '.join(words)
    return ori

def gpt_prompt(data):

    sentence = ' '.join(data["token"])
    prompt = (f"The above are a few examples of structural relational statements. "
              f"“Token” is the original biomedical statement, “h” and “t” are entity information, "
              f"where “name” represents the name of the entity and “pos” represents the position "
              f"in the sentence. Abstract relationships are implicit between pairs of entities. "
              f"Now, please help convert the following sentence into an expression with the same text format.\n\n{sentence}")
    return prompt

def augment_data_with_gpt(file_path, output_path):

    with open(file_path, 'r') as file, open(output_path, 'w') as output_file:
        for line in file:
            data = json.loads(line)

            ori = process_sentence(' '.join(data["token"]))
            prompt = gpt_prompt(data)

            # response = openai.Completion.create(
            #     engine="text-davinci-003",
            #     prompt=prompt,
            #     max_tokens=100
            # )
            augmented_text = "This is an example of augmented text based on the GPT-generated response."

            output_file.write(augmented_text + '\n')


openai.api_key = 'your_api_key_here'
augment_data_with_gpt('dataset/DDI/k-shot/1-1/train.txt', 'dataset/DDI/k-shot_GPT/1-1/train_gpt.txt')

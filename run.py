import re
from input_tokenizer_scratch import InputTokenizer

f = open("datasets/the-verdict.txt", "r")
input_text = f.read()
processed = re.split(r'([,.?_!"()\']|--|\s)', input_text)
processed = [
    item.strip() for item in processed if item.strip()
]

vocabulary = sorted(set(processed))
vocabulary.extend(["<|endoftext|>", "<|unk|>"])
print("length of vocabulary: ", len(vocabulary))

tokenizer = InputTokenizer(vocabulary)

test = "Hello World!, how are you?"
print("Test case")
print(tokenizer.encode(test))
print(tokenizer.decode(tokenizer.encode(test)))
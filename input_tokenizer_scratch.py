import re


class InputTokenizer:
    def __init__(self, vocabulary):
        self._str_to_int = {word: index for index, word in enumerate(vocabulary)}
        self._int_to_str = {index: word for index, word in enumerate(vocabulary)}

    def encode(self, text) -> list:
        processed = re.split(r'([,.?_!"()\']|--|\s)', text)

        processed = [item if item in self._str_to_int else "<|unk|>" for item in processed]
        ids = [self._str_to_int[each] for each in processed]
        return ids

    def decode(self, ids) -> str:
        text = " ".join([self._int_to_str[i] for i in ids])
        text = re.sub(r'\s+([,.?!"()\'])', r'\1', text)
        return text

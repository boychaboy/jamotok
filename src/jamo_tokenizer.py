import jamotools
from transformers import BasicTokenizer


class JamoTokenizer(object):
    def __init__(self):
        # Split punctuation & Tokenize Chinese Character & Clean Text
        self.basic_tokenizer = BasicTokenizer(do_lower_case=False, tokenize_chinese_chars=True)

    def tokenize(self, text: str):
        text = " ".join(self.basic_tokenizer.tokenize(text))
        text_ptr = 0
        is_first_token = True
        tokenized = []

        # jamotok
        jamo_split = jamotools.split_syllables(text).split(" ")
        return jamo_split

if __name__ == "__main__":
    text = "본 OKC 페이퍼에는, 이번 emnlp findings에 억셉된 두 개의 한국어 nlp dataset들이 수록되어 있습니다. 左衝右突"
    print(text)
    tokenizer = JamoTokenizer()
    tokenized = tokenizer.tokenize(text)
    print(tokenized)
    
    # test joinability
    joined = ""
    for word in tokenized:
        joined += jamotools.join_jamos(word) + " "
    
    print(joined)

    print(text==joined)
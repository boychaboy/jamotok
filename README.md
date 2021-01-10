# Korean Jamo Tokenizer

Korean Tokenizer using Consonents & Vowels to do BERT wordpiece tokenizing. 

## Requirements

```
$ pip3 install -r requirements.txt
```

## How to

1. Prepare corpus file (e.g. `corpus.txt`)

2. Split corpus file (for multiprocessing)

```bash
$ mkdir corpus
$ split -a 4 -l {$NUM_LINES_PER_FILE} -d {$CORPUS_FILE} ./corpus/data_
```

3. Pretokenize corpus with Jamo Tokenizer

```bash
$ python3 src/jamo_pretokenize.py --input_dir corpus --output_dir pretokenized_corpus --num_processes 16
```

4. Train Wordpiece

```bash
$ mkdir -p vocab
$ python3 src/train_bertwordpiece.py --files 'pretokenized_corpus/*' --out vocab
```

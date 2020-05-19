import os
import jieba
import markovify

corpus_file = []
for file in os.listdir():
    if file.endswith('txt'):
        corpus_file.append(file)

print(corpus_file)
raw = ''
for file in corpus_file:
    with open(file, 'r', encoding='utf-8') as f:
        raw += f.read()

split = ''
for i in raw.splitlines():
    split += " ".join(jieba.cut(i)) + '\n'


split = split.replace('\n \n', '\n')
try:
    markovify.Text(split)
except:
    for i in split.splitlines():
        try:
            markovify.Text(i)
        except:
            print(i)
            if i != '' and i != ' ':
                split = split.replace(f'{i}\n', '')


with open('../split.txt', 'w', encoding='utf-8') as f:
    f.write(split)

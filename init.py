import jieba
import markovify


with open('鲁迅全集.txt', 'r', encoding='utf-8') as f:
    luxun_raw = f.read()

luxun_text = luxun_raw
for i in ['。', '？', '！', '……', '——', '；', '：']:
    luxun_text = luxun_text.replace(i, f'{i}\n')

luxun_split = " ".join(jieba.cut(luxun_text))
luxun_split = luxun_split.replace('\n ', '\n')
luxun_split = luxun_split.replace('\n　　 ', '\n')

escape = ' ○＂＃＄％＆＇（）＊＋，－／：；＜＝＞＠［＼］＾＿｀｛｜｝～｟｠｢｣､　、〃〈〉《》「」『』【】〔〕〖〗〘〙〚〛〜〝〞〟〰〾〿–—‘’‛“”„‟…‧﹏﹑﹔·！？｡。'


def normal(char):
    if char in escape:
        return True
    if '\u3400' <= char <= '\u9FFF':
        return True
    if '\u0000' <= char <= '\u007F':
        return True
    if '\uFF00' <= char <= '\uFF5A' or char in 'áéǒ①—×＝１２３４５６７８９０':
        return True
    return False


for i in luxun_split.splitlines():
    for j in i:
        if not normal(j):
            print(j, '\n', i)
            luxun_split = luxun_split.replace(i, '')
            break

for i in luxun_split.splitlines():
    try:
        luxun_model = markovify.Text(i)
    except:
        print(i)
        luxun_split = luxun_split.replace(f'{i}\n', '')


with open('luxun_split.txt', 'w', encoding='utf-8') as f:
    f.write(luxun_split)

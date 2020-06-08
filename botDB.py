import os
from botInfo import twi_id


images = {
    'blank': {
        '001': {'path': 'images/blank_001.jpg'},
        '002': {'path': 'images/blank_002.jpg'},
    },
    'greet': {
        'morning': {
            'path': 'images/morning.jpg',
            'id': 1262414213156233216,
        },
        'night': {
            'path': 'images/night.jpg',
            'id': 1262416125117095936,
        },
    }
}

blacklist = [twi_id]

corpus = []
for i in os.listdir('corpus'):
    if i.endswith('.txt'):
        corpus.append(i)


tg_start = '欢迎使用鲁迅 Bot @LuXunRobot 。\n\n' \
           '您可以使用 /say 生成一句话，或者 /luxun 读取一句原文。'


update_cmd = 'kill (ps -A | grep python | tail -n 1 | cut -b 1-7); git pull; python3.8 -m compileall .; rm nohup.out; nohup python3.8 -u main.py &; disown (ps -A | grep python | tail -n 1 | cut -b 1-7)'

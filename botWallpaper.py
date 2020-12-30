import json
import requests
from datetime import datetime, timedelta, timezone
from botSession import lx_twi, logger


market = 'zh-CN'
bing_url = f'https://www.bing.com/HPImageArchive.aspx?format=js&idx=0&n=1&mkt={market}'


def get_wallpaper(locale=market):
    api_url = f'https://www.bing.com/HPImageArchive.aspx?format=js&idx=0&n=1&mkt={locale}'
    wp_result = requests.get(api_url)
    wp_json = json.loads(wp_result.content)
    wp_url = 'https://www.bing.com' + wp_json['images'][0]['url'].replace('1366x768', '1920x1080')
    wp_copyright = wp_json['images'][0]['copyright']
    return wp_url, wp_copyright


def send_wallpaper(comment='呐，早安。'):
    wp_url, wp_copyright = get_wallpaper()
    wp_path = 'tmp/' + datetime.now(timezone(timedelta(hours=8))).strftime('%Y%m%d%H%M%S') + '.jpg'
    with open(wp_path, 'wb') as f:
        f.write(requests.get(wp_url).content)
    wp_id = lx_twi.media_upload(wp_path)
    text = f'{comment}\n\n#今日壁纸：{wp_copyright}'
    logger.info(f'Sending:\n{text}')
    return lx_twi.update_status(text, media_ids=[wp_id.media_id])

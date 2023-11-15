import re as _re
from pathlib import Path as _Path

API_HEROPAGE = 'https://pvp.qq.com/web201605/herodetail/{hero_id}.shtml'
API_SKINURL = (
    'http://game.gtimg.cn/images/yxzj/img201606/skin/hero-info/'
    '{hero_id}/{hero_id}-bigskin-{skin_id}.jpg'
)
# SKIN_SIZE = ('big', 'mobile', 'small')
REGEX_SKINLIST = _re.compile(r'\s*(.+?)\s*(?:(?:&\d+\|)|(?:&\d+)|\|)')

SAVE_PATH_FILE = _Path('savepath.txt')
if SAVE_PATH_FILE.exists():
    _c = SAVE_PATH_FILE.read_text(encoding='utf-8')
    ROOT_PATH = _Path(_c)
else:
    ROOT_PATH = _Path('./wzry-skin-imag')
if not ROOT_PATH.exists():
    ROOT_PATH.mkdir()

import time
from dataclasses import dataclass
from pathlib import Path
from typing import List


@dataclass
class HeroInfo:
    title: str
    cname: str
    ename: int


def gen_hereinfo(data: List[dict]) -> List[HeroInfo]:
    return [HeroInfo(hero['title'], hero['cname'], hero['ename']) for hero in data]


def mkdir(path: Path):
    if not path.exists():
        path.mkdir()


LOG_ROOT = Path('log')
mkdir(LOG_ROOT)


def get_log_name():
    now = time.strftime("%Y-%m-%d", time.localtime())
    name = f'{now}.log'
    return LOG_ROOT / name

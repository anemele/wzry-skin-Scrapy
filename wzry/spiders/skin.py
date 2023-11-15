import json
from typing import Optional

import scrapy
from scrapy import Request
from scrapy.http import Response

from ..const import *
from ..utils import HeroInfo, gen_hereinfo


class SkinSpider(scrapy.Spider):
    name = "skin"
    allowed_domains = ["pvp.qq.com", "game.gtimg.cn"]
    start_urls = ["http://pvp.qq.com/web201605/js/herolist.json"]

    def parse(self, response: Response):
        data = json.loads(response.body)
        heroinfo = gen_hereinfo(data)
        # yield heroinfo

        for hero in heroinfo:
            heropage = API_HEROPAGE.format(hero_id=hero.ename)
            yield Request(heropage, callback=self.parse_page, cb_kwargs=dict(hero=hero))

    def parse_page(self, response: Response, **cb):
        hero: Optional[HeroInfo] = cb.get('hero')
        if hero is None:
            raise ValueError(f'expect {HeroInfo}')

        heropath = ROOT_PATH / f'{hero.cname}_{hero.title}'
        if not heropath.exists():
            heropath.mkdir()

        skinlist = response.css('div.pic-pf > ul::attr(data-imgname)').get()
        skinlist = REGEX_SKINLIST.findall(skinlist)
        # yield skinlist

        for sid, skin in enumerate(skinlist):
            sid += 1
            skinpath = heropath / f'{sid}_{skin}.jpg'
            if skinpath.exists():
                continue

            skinurl = API_SKINURL.format(hero_id=hero.ename, skin_id=sid)
            yield Request(
                skinurl, callback=self.save_imag, cb_kwargs=dict(path=skinpath)
            )

    def save_imag(self, response: Response, **cb):
        yield dict(data=response.body, path=cb.get('path'))

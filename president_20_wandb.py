import requests
import time
import numpy as np
from bs4 import BeautifulSoup as bs

import wandb
wandb.init(project='president', entity='jason2133')


def p():
    page = requests.get("https://search.naver.com/search.naver?where=nexearch&sm=tab_etc&mra=bjFY&x_csa=%7B%22isMapTab%22%3Afalse%7D&pkid=7001&qvt=0&query=%EC%A0%9C20%EB%8C%80%20%EB%8C%80%ED%86%B5%EB%A0%B9%EC%84%A0%EA%B1%B0%20%EC%A0%84%EA%B5%AD%20%EA%B0%9C%ED%91%9C%ED%98%84%ED%99%A9")
    soup = bs(page.text, "html.parser")

    elements = soup.select('div.rate_per > span')
    gap = soup.select('div.gap_area > span')
    rate = soup.select('div.turnout_info > div')

    r = rate[0].text[23:29]

    time = elements[2].text[:5]
    lee = elements[3].text[3:]
    yoon = elements[5].text[3:]

    gap_cnt = gap[0].text[3:]
    lee_cnt = gap[1].text[9:]
    yoon_cnt = gap[3].text[9:]

    print(f"시간:{time}\t개표율:{r}%")
    print(
        f"이재명:{lee}%\tvs\t윤석열:{yoon}%\tLoss : {np.float32(lee) - np.float32(yoon)}")
    print('\n')

    # WandB
    wandb.log({'open': float(r), 'Loss': np.float32(lee)-np.float32(yoon)})


if __name__ == '__main__':
    while True:
        p()
        time.sleep(60)

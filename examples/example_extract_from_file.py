# 展示如何从打水印的文本文件中提取盲水印
from text_blind_watermark import TextBlindWatermark

password = '20190808'
with open('file.txt', 'r') as f:
    text_embed = f.read()

twm_new = TextBlindWatermark(password=password)
wm_extract = twm_new.extract(text_embed)
print("解出的盲水印：")
print(wm_extract)

assert wm_extract == '绝密：两点老地方见！'

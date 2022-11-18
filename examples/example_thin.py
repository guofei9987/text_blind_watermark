import random

from text_blind_watermark import TextBlindWatermarkThin

password = '20190808'
watermark = 'github.com/guofei9987'
text_blind_wm = TextBlindWatermarkThin(password=password)

wm = text_blind_wm.embed(watermark=watermark)
# This is example，you can put wm everywhere
text_embed = '上' + wm + '下文'
print('打入盲水印后的文本:', text_embed)

# %%

text_blind_wm_new = TextBlindWatermarkThin(password=password)
wm_extract = text_blind_wm_new.extract(text_embed)
print(wm_extract)

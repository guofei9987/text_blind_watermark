from text_blind_watermark import TextBlindWatermarkThin

password = '20190808'
watermark = 'github.com/guofei9987'
text_blind_wm = TextBlindWatermarkThin(password=password)

wm = text_blind_wm.embed(watermark=watermark)
# This is example，you can put wm everywhere
text_embed = '这句话中有盲' + wm + '水印，你能提取出来吗？'
print(text_embed)

# %%

text_blind_wm_new = TextBlindWatermarkThin(password=password)
wm_extract = text_blind_wm_new.extract(text_embed)
print('提取内容：', wm_extract)

# %%
assert watermark == wm_extract

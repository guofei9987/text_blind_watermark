from text_blind_watermark import TextBlindWatermark2

password = '20190808'
text = '这句话中有盲水印，你能提取出来吗？'
watermark = 'github.com/guofei9987'

text_blind_wm = TextBlindWatermark2(password=password)

text_with_wm = text_blind_wm.embed(text=text, watermark=watermark)
print(text_with_wm)

# %%

text_blind_wm2 = TextBlindWatermark2(password=password)
wm_extract = text_blind_wm2.extract(text_with_wm)
print('提取内容：', wm_extract)

assert watermark == wm_extract

# %% put watermark by index
text_blind_wm3 = TextBlindWatermark2(password=password)

text_with_wm = text_blind_wm2.embed(text=text, watermark=watermark, idx=0)
assert text_blind_wm2.extract(text_with_wm) == wm_extract

text_with_wm = text_blind_wm2.embed(text=text, watermark=watermark, idx=len(text))
assert text_blind_wm2.extract(text_with_wm) == wm_extract

# %%

text_blind_wm4 = TextBlindWatermark2(password=password, chr_type=(3, 4))
text_with_wm = text_blind_wm.embed(text=text, watermark=watermark)
print(text_with_wm)

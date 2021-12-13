from text_blind_watermark import embed, extract

wm = "绝密：两点老地方见！"
password = '20190808'
sentence = "这句话中有盲水印，你能提取出来吗？" * 16

# %%
# 打入盲水印
sentence_embed = embed(sentence, wm, password)
print("打上盲水印之后")
print(sentence_embed)

# %% 解出盲水印
wm_extract = extract(sentence_embed, password)
print("解出的盲水印")
print(wm_extract)


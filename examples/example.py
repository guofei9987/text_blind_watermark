from text_blind_watermark import TextBlindWatermark

watermark = "绝密：两点老地方见！"
password = '20190808'
text = '''这句话将会被嵌入暗水印，嵌入后的文本会被 print 出来。
print 出来的文本从外观上看不出里面有隐藏信息，可以复制到微信、钉钉等发送。
接收方获取文本后，用 wm_extract 可以提取出暗水印中的内容。
经过测试，此程序不仅仅可以在微信、钉钉使用，也可以在知乎等网站使用。
B站介绍视频：https://www.bilibili.com/video/BV1m3411s7kT
（相关项目）把盲水印打入图片中： https://github.com/guofei9987/blind_watermark
欢迎对本项目提意见以及 Star： https://github.com/guofei9987/text_blind_watermark
'''

# %% 打入盲水印
twm = TextBlindWatermark(password=password)
twm.read_wm(watermark=watermark)
twm.read_text(text=text)
text_embed = twm.embed()
print("打上盲水印之后:")
print(text_embed)

# %% 解出盲水印
twm_new = TextBlindWatermark(password=password)
wm_extract = twm_new.extract(text_embed)
print("解出的盲水印：")
print(wm_extract)


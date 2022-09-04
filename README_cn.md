# text_blind_watermark

文本隐水印

经测试，可以用于
- [x] 微信
- [x] 钉钉
- [x] pages
- [x] 知乎  
- [x] 欢迎补充


在线演示: [https://www.guofei.site/pictures_for_blog/app/text_watermark/v1.html](https://www.guofei.site/pictures_for_blog/app/text_watermark/v1.html)

视频展示：[https://www.bilibili.com/video/BV1m3411s7kT](https://www.bilibili.com/video/BV1m3411s7kT)

## 如何使用

安装

```bash
>pip install text_blind_watermark
```

### 张三：把隐秘消息嵌入到另一段文本中

```python
from text_blind_watermark import TextBlindWatermark

wm = "绝密：两点老地方见！"
sentence = "这句话中有盲水印，你能提取出来吗？" * 16

twm = TextBlindWatermark(password='20190808')
twm.read_wm(watermark=watermark)
twm.read_text(text=text)
text_embed = twm.embed()

print("打上盲水印之后:")
print(text_embed)
```

显示的明文可以粘贴到任何地方

*It uses AES to encrypt*

### 李四：拿到明文，解出暗文

```python
from text_blind_watermark import TextBlindWatermark

twm_new = TextBlindWatermark(password='20190808')
wm_extract = twm_new.extract(text_embed)
print("解出的盲水印：")
print(wm_extract)
```


# text_blind_watermark

文本隐水印

经测试，可以用于
- [x] 微信
- [x] 钉钉
- [x] 欢迎补充

## 如何使用

安装

```bash
>pip install text_blind_watermark
```

### 张三：把隐秘消息嵌入到另一段文本中

```python
from text_blind_watermark import embed, extract

wm = "绝密：两点老地方见！"
password = '20190808'
sentence = "这句话中有盲水印，你能提取出来吗？" * 16

sentence_embed = embed(sentence, wm, password)
print("打上盲水印之后")
print(sentence_embed)
```

显示的明文可以粘贴到任何地方

*It uses AES to encrypt*

### 罗老师：拿到明文，解出暗文

```python
from text_blind_watermark import embed, extract
password = '20190808'
wm_extract = extract(sentence_embed, password)
print("解出的盲水印")
print(wm_extract)
```


# text_blind_watermark

Put blind watermark into a text.

[![PyPI](https://img.shields.io/pypi/v/text_blind_watermark)](https://pypi.org/project/text_blind_watermark/)
[![Build Status](https://travis-ci.com/guofei9987/text_blind_watermark.svg?branch=master)](https://travis-ci.com/guofei9987/text_blind_watermark)
[![codecov](https://codecov.io/gh/guofei9987/text_blind_watermark/branch/master/graph/badge.svg)](https://codecov.io/gh/guofei9987/text_blind_watermark)
[![License](https://img.shields.io/pypi/l/text_blind_watermark.svg)](https://github.com/guofei9987/text_blind_watermark/blob/master/LICENSE)
![Python](https://img.shields.io/badge/python->=3.5-green.svg)
![Platform](https://img.shields.io/badge/platform-windows%20|%20linux%20|%20macos-green.svg)
[![stars](https://img.shields.io/github/stars/guofei9987/text_blind_watermark.svg?style=social)](https://github.com/guofei9987/text_blind_watermark/)
[![fork](https://img.shields.io/github/forks/guofei9987/text_blind_watermark?style=social)](https://github.com/guofei9987/text_blind_watermark/fork)
[![Downloads](https://pepy.tech/badge/text_blind_watermark)](https://pepy.tech/project/text_blind_watermark)


- Online demo: [https://www.guofei.site/pictures_for_blog/app/text_watermark/v1.html](https://www.guofei.site/pictures_for_blog/app/text_watermark/v1.html)


Can be used in 
- [x] Wechat
- [x] dingding
- [x] pages
- [x] zhihu.com 
- [x] ...

## How to Use

install

```bash
>pip install text_blind_watermark
```

### Alice Put her text watermark into a text:

```python
from text_blind_watermark import embed, extract

wm = "绝密：两点老地方见！"
password = '20190808'
sentence = "这句话中有盲水印，你能提取出来吗？" * 16

sentence_embed = embed(sentence, wm, password)
print("打上盲水印之后")
print(sentence_embed)
```

Then, you can paste this text to where you need.


*It uses AES to encrypt*

### Bob Extract the invisible watermark

```python
from text_blind_watermark import embed, extract
password = '20190808'
wm_extract = extract(sentence_embed, password)
print("解出的盲水印")
print(wm_extract)
```


# text_blind_watermark

文本隐水印，用来把一段信息嵌入到一段明文中，使信息隐密不可见，并且旁人无法察觉到嵌入后明文的变化。


[![PyPI](https://img.shields.io/pypi/v/text_blind_watermark)](https://pypi.org/project/text_blind_watermark/)
[![Build Status](https://app.travis-ci.com/guofei9987/text_blind_watermark.svg?branch=main)](https://app.travis-ci.com/guofei9987/text_blind_watermark)
[![codecov](https://codecov.io/gh/guofei9987/text_blind_watermark/branch/main/graph/badge.svg?token=85EAN4IVM6)](https://codecov.io/gh/guofei9987/text_blind_watermark)
[![License](https://img.shields.io/pypi/l/text_blind_watermark.svg)](https://github.com/guofei9987/text_blind_watermark/blob/master/LICENSE)
![Python](https://img.shields.io/badge/python->=3.5-green.svg)
![Platform](https://img.shields.io/badge/platform-windows%20|%20linux%20|%20macos-green.svg)
[![stars](https://img.shields.io/github/stars/guofei9987/text_blind_watermark.svg?style=social)](https://github.com/guofei9987/text_blind_watermark/)
[![fork](https://img.shields.io/github/forks/guofei9987/text_blind_watermark?style=social)](https://github.com/guofei9987/text_blind_watermark/fork)
[![Downloads](https://pepy.tech/badge/text_blind_watermark)](https://pepy.tech/project/text_blind_watermark)


- Video demo：[https://www.bilibili.com/video/BV1m3411s7kT](https://www.bilibili.com/video/BV1m3411s7kT)
- Online demo(from old version, for demo only): [https://www.guofei.site/pictures_for_blog/app/text_watermark/v1.html](https://www.guofei.site/pictures_for_blog/app/text_watermark/v1.html)
- **中文 readme** [README_cn.md](README_cn.md)
- **源码:** [https://github.com/guofei9987/text_blind_watermark](https://github.com/guofei9987/text_blind_watermark)
- **Rust 版本:** [https://github.com/guofei9987/hidden_watermark](https://github.com/guofei9987/hidden_watermark)



经测试，在这些场景下信息隐藏比较完美
- [x] MacBook 版本的 Chrome 浏览器，包括知乎网页版、微博网页版等。
- [x] 微信、钉钉。Mac/Iphone 版均可
- [x] 苹果备忘录
- [x] 用 Chrome 打开 github.com 上的代码文件和文本文件（但md文件不行）
- [x] 用复制/黏贴 (ctrl+c/v) 的方式在上述平台之间黏贴
- [x] 欢迎补充


在线演示(旧版算法，仅用于展示效果): [https://www.guofei.site/pictures_for_blog/app/text_watermark/v1.html](https://www.guofei.site/pictures_for_blog/app/text_watermark/v1.html)

视频展示：[https://www.bilibili.com/video/BV1m3411s7kT](https://www.bilibili.com/video/BV1m3411s7kT)

## 如何使用

安装

```bash
>pip install text_blind_watermark
```


### 把信息不可见地嵌入到文本中

```python
from text_blind_watermark import TextBlindWatermark2

password = '20190808'
text = '这句话中有盲水印，你能提取出来吗？'
watermark = 'github.com/guofei9987'

text_blind_wm = TextBlindWatermark2(password=password)

text_with_wm = text_blind_wm.embed(text=text, watermark=watermark)
print(text_with_wm)
```


### 从文本中提取不可见的信息

```python
text_blind_wm2 = TextBlindWatermark2(password=password)
wm_extract = text_blind_wm2.extract(text_with_wm)
print('提取内容：', wm_extract)
```

>github.com/guofei9987

### `chr_type`

可以指定 `chr_type` 使其在不同的系统环境中有更好的表现

```python
from text_blind_watermark import TextBlindWatermark2

password = '20190808'
text = '这句话中有盲水印，你能提取出来吗？'
watermark = 'github.com/guofei9987'

text_blind_wm = TextBlindWatermark2(password=password, chr_type=(3, 4))

text_with_wm = text_blind_wm.embed(text=text, watermark=watermark)
print(text_with_wm)

text_blind_wm2 = TextBlindWatermark2(password=password, chr_type=(3, 4))
wm_extract = text_blind_wm2.extract(text_with_wm)
print('提取内容：', wm_extract)
assert watermark == wm_extract
```



## 更稳定的版本
### 张三：把隐秘消息嵌入到另一段文本中

```python
from text_blind_watermark import TextBlindWatermark

watermark = "绝密：两点老地方见！"
text = "这句话中有盲水印，你能提取出来吗？" * 16
password = "20190808"

twm = TextBlindWatermark(password=password)
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
password = "20190808"

twm_new = TextBlindWatermark(password=password)
wm_extract = twm_new.extract(text_embed)
print("解出的盲水印：")
print(wm_extract)
```

## 相关项目

HideInfo：[https://github.com/guofei9987/HideInfo](https://github.com/guofei9987/HideInfo)


| 算法   | 说明                |
|------|-------------------|
| [幻影坦克](https://github.com/guofei9987/HideInfo/blob/main/example/example_mirage_tank.py) | 使图片在不同的背景下显示不同的图片 |
| [化物为图](https://github.com/guofei9987/HideInfo/blob/main/example/example_hide_as_img.py) | 把数据以图片形式存放        |
| [藏物于图](https://github.com/guofei9987/HideInfo/blob/main/example/example_hide_in_img.py) | 把数据藏在一个图片中          |
| [图种](https://github.com/guofei9987/HideInfo/blob/main/example/example_img_seed.py)   | 把图片和文件黏在一起，并存为图片  |
| [EXIF](https://github.com/guofei9987/HideInfo/blob/main/example/example_img_exif.py) | 把一段信息放到图片的EXIF中   |
| [化物为音](https://github.com/guofei9987/HideInfo/blob/main/example/example_hide_as_music.py) | 把数据以音频的形式存放       |
| [藏物于音](https://github.com/guofei9987/HideInfo/blob/main/example/example_hide_in_music.py) | 把数据隐藏在一个音频中       |
| [化物为文](https://github.com/guofei9987/HideInfo/blob/main/example/example_hide_as_txt.py) | 把数据以文本文件的形式存放 |
| [藏物于文](https://github.com/guofei9987/HideInfo/blob/main/example/example_hide_in_txt.py) | 把数据隐藏在一段文本中 |


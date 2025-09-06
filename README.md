# text_blind_watermark

Embed an invisible message (blind watermark) into text, without altering its readability or appearance.

[![PyPI](https://img.shields.io/pypi/v/text_blind_watermark)](https://pypi.org/project/text_blind_watermark/)
[![Build Status](https://app.travis-ci.com/guofei9987/text_blind_watermark.svg?branch=main)](https://app.travis-ci.com/guofei9987/text_blind_watermark)
[![codecov](https://codecov.io/gh/guofei9987/text_blind_watermark/branch/main/graph/badge.svg?token=85EAN4IVM6)](https://codecov.io/gh/guofei9987/text_blind_watermark)
[![License](https://img.shields.io/pypi/l/text_blind_watermark.svg)](https://github.com/guofei9987/text_blind_watermark/blob/master/LICENSE)
![Python](https://img.shields.io/badge/python->=3.5-green.svg)
![Platform](https://img.shields.io/badge/platform-windows%20|%20linux%20|%20macos-green.svg)
[![stars](https://img.shields.io/github/stars/guofei9987/text_blind_watermark.svg?style=social)](https://github.com/guofei9987/text_blind_watermark/)
[![fork](https://img.shields.io/github/forks/guofei9987/text_blind_watermark?style=social)](https://github.com/guofei9987/text_blind_watermark/fork)
[![Downloads](https://pepy.tech/badge/text_blind_watermark)](https://pepy.tech/project/text_blind_watermark)
<a href="https://hellogithub.com/repository/guofei9987/text_blind_watermark" target="_blank"><img src="https://abroad.hellogithub.com/v1/widgets/recommend.svg?rid=e746d0a33c5f471aac65642e173e3dd0&claim_uid=se0WHo8cbiLv2w1&theme=small" alt="Featured｜HelloGitHub" /></a>

- **Try it online**：[https://www.guofei.site/os/text_wm.html](https://www.guofei.site/os/text_wm.html)
- Video demo：[https://www.bilibili.com/video/BV1m3411s7kT](https://www.bilibili.com/video/BV1m3411s7kT)
- **Rust Version:** [https://github.com/guofei9987/hidden_watermark](https://github.com/guofei9987/hidden_watermark)
- **中文 readme** [README_cn.md](README_cn.md)
- **Source code:** [https://github.com/guofei9987/text_blind_watermark](https://github.com/guofei9987/text_blind_watermark)


## ✨ Features

- Invisible watermark embedding in plain text  
- No visible difference in appearance
- Verified in platforms: macOS, Windows, Linux, WeChat, DingTalk, Zhihu, Chrome, etc


## 📦 Installation

```bash
pip install text_blind_watermark
```


---

## 🛠 Usage

### Embed a watermark into text

```python
from text_blind_watermark import TextBlindWatermark

password = b"p@ssw0rd"
watermark = b"This is watermark"
original_text_file = 'files/file_txt.txt'
file_with_watermark = 'files/file_txt_with_watermark.txt'

with open(original_text_file, 'r') as f:
    text = f.read()

twm = TextBlindWatermark(pwd=password)

# embed watermark into the text
text_with_wm = twm.add_wm_rnd(text=text, wm=watermark)

# write into a new file
with open(file_with_watermark, 'w') as f:
    f.write(text_with_wm)
```


### Extract the watermark

```python
from text_blind_watermark import TextBlindWatermark

password = b"p@ssw0rd"
file_with_watermark = 'files/file_txt_with_watermark.txt'

with open(file_with_watermark, 'r') as f:
    text_with_wm_new = f.read()

twm = TextBlindWatermark(pwd=password)
watermark_extract = twm.extract(text_with_wm_new)
print(watermark_extract)
```

> Output: `This is watermark`


## 🔗 Related Project: [HideInfo](https://github.com/guofei9987/HideInfo)


| 算法   | 说明                                                |
|------|---------------------------------------------------|
| [migrate tank](https://github.com/guofei9987/HideInfo/blob/main/example/example_mirage_tank.py) | Show different images under different backgrounds |
| [hide as image](https://github.com/guofei9987/HideInfo/blob/main/example/example_hide_as_img.py) | Store data as an image                            |
| [hide in image](https://github.com/guofei9987/HideInfo/blob/main/example/example_hide_in_img.py) | Hide data inside an image                         |
| [image seed](https://github.com/guofei9987/HideInfo/blob/main/example/example_img_seed.py)   | Merge image and file together                     |
| [EXIF](https://github.com/guofei9987/HideInfo/blob/main/example/example_img_exif.py) | Embed data in image EXIF metadata                                   |
| [hide as music](https://github.com/guofei9987/HideInfo/blob/main/example/example_hide_as_music.py) | Store data as audio                                      |
| [hide in music](https://github.com/guofei9987/HideInfo/blob/main/example/example_hide_in_music.py) | Hide data inside audio                                       |
| [hide as text](https://github.com/guofei9987/HideInfo/blob/main/example/example_hide_as_txt.py) | Store data as plain text                                     |
| [hide in text](https://github.com/guofei9987/HideInfo/blob/main/example/example_hide_in_txt.py) | Hide data within readable text                                       |


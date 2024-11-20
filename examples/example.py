from text_blind_watermark import TextBlindWatermark
import os

os.chdir(os.path.dirname(__file__))

password = b"p@ssw0rd"
watermark = b"This is a watermark"
original_text_file = 'files/file_txt.txt'
file_with_watermark = 'files/file_txt_with_watermark.txt'

with open(original_text_file, 'r') as f:
    text = f.read()

twm = TextBlindWatermark(pwd=password)

# add watermark into the text
text_with_wm = twm.add_wm_rnd(text=text, wm=watermark)

# write into a new file
with open(file_with_watermark, 'w') as f:
    f.write(text_with_wm)

# %% read and extract watermark

with open(file_with_watermark, 'r') as f:
    text_with_wm_new = f.read()

twm = TextBlindWatermark(pwd=password)
watermark_extract = twm.extract(text_with_wm_new)
print(watermark_extract)

# %% assert

assert watermark == watermark_extract

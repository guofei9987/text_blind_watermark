from text_blind_watermark import TextBlindWatermarkDeprecated
import os

os.chdir(os.path.dirname(__file__))

password = "p@ssw0rd"
watermark = "This is a watermark"

original_text_file = 'files/file_txt.txt'
file_with_watermark = 'files/file_txt_with_watermark_old.txt'

with open(original_text_file, 'r') as f:
    text = f.read()

twm = TextBlindWatermarkDeprecated(password=password)

twm.read_wm(watermark=watermark)
twm.read_text(text=text)
text_with_wm = twm.embed()

# write into a new file
with open(file_with_watermark, 'w') as f:
    f.write(text_with_wm)

print("text with ")

# %% read and extract watermark


with open(file_with_watermark, 'r') as f:
    text_with_wm = f.read()

text_blind_wm2 = TextBlindWatermarkDeprecated(password=password)
wm_extract = text_blind_wm2.extract(text_with_wm)
print('watermark extracted：', wm_extract)
# %% assert
assert watermark == wm_extract

# -*- coding: utf-8 -*-

import random


class TextBlindWatermarkDeprecated:
    def __init__(self, password):
        self.password = password
        self.text, self.wm_bin = None, None

    def read_wm(self, watermark):
        random.seed(self.password)
        # wm_bin = [format(i ^ random.randint(0, 255), '08b') for i in watermark.encode('utf-8')]  # 8位2进制格式
        wm_bin = [format(i, '08b') for i in watermark.encode('utf-8')]  # 8位2进制格式
        self.wm_bin = ''.join(wm_bin)
        return self

    def read_text(self, text):
        self.text = text
        return self

    def embed(self, repeat=False):
        wm_bin, text = self.wm_bin, self.text
        # 打入水印
        len_wm_bin, len_text = len(self.wm_bin), len(self.text)
        assert len_text > len_wm_bin, "文本长度至少{}，实际{}".format(len_wm_bin, len_text)

        # TODO:循环嵌入
        if repeat:
            pass
            # wm_bin = wm_bin * ((len_text - 2) // len_wm_bin)

        # 头尾各放一个1。提取过程中把首尾的0去掉。
        wm_bin = '1' + wm_bin + '1'
        sentence_embed = ""
        for idx in range(len_text):
            sentence_embed += text[idx]
            if idx < len(wm_bin):
                if wm_bin[idx] == "1":
                    sentence_embed += chr(0x200C)

        return sentence_embed

    def extract(self, text_embed):
        wm_extract_bin = ""

        idx = 0
        while idx < len(text_embed):
            if text_embed[idx] != chr(0x200C):
                idx += 1
                wm_extract_bin += '0'
            else:
                idx += 2
                wm_extract_bin += '1'

        first_zero = wm_extract_bin.find("1")
        last_zero = len(wm_extract_bin) - wm_extract_bin[::-1].find("1")
        wm_extract_bin = wm_extract_bin[first_zero + 1:last_zero - 1]

        random.seed(self.password)
        # return bytes([int(wm_extract_bin[8 * i:8 * i + 8], base=2) ^ random.randint(0, 255) for i in
        #               range(len(wm_extract_bin) // 8)]).decode('utf-8')
        #
        return bytes([int(wm_extract_bin[8 * i:8 * i + 8], base=2) for i in
                      range(len(wm_extract_bin) // 8)]).decode('utf-8')


# class TextBlindWatermark2:
#     def __init__(self, password, chr_type=(4, 5)):
#         all_chr_wm_hex = ('1d', '7F', '200B', '200C', '200D', 'FEFF')
#         chr_wm = [chr(int(all_chr_wm_hex[chr_idx], base=16)) for chr_idx in chr_type]
#
#         self.bit2char_dict = {'0': chr_wm[0], '1': chr_wm[1]}
#         self.char2bit_dict = {chr_wm[0]: '0', chr_wm[1]: '1'}
#         self.password = password
#
#     def get_wm(self, watermark: str):
#         random.seed(self.password)
#         wm_bin = [format(i ^ random.randint(0, 255), '08b') for i in watermark.encode('utf-8')]  # 8位2进制格式
#         wm_bin = ''.join(wm_bin)
#         return ''.join(self.bit2char_dict[i] for i in wm_bin)
#
#     def embed(self, text: str, watermark: str, idx: int = None) -> str:
#         text = self.remove_watermark(text)  # remove existing watermark before add new one
#         wm = self.get_wm(watermark)
#         if idx is None:
#             idx = random.randint(0, len(text))
#         else:
#             assert idx <= len(text)
#
#         return text[:idx] + wm + text[idx:]
#
#     def extract(self, text_embed: str) -> str:
#
#         idx_left, idx_right = None, None
#
#         for idx, char in enumerate(text_embed):
#             if char in self.char2bit_dict:
#                 if idx_left is None:
#                     idx_left = idx
#             else:
#                 if idx_left is not None and idx_right is None:
#                     idx_right = idx
#                     break
#         else:
#             idx_right = len(text_embed)
#
#         if idx_left is None or idx_right is None:
#             raise IOError("There is no watermark!")
#
#         wm_extract_bin = ''.join(self.char2bit_dict[i] for i in text_embed[idx_left:idx_right])
#
#         random.seed(self.password)
#
#         return bytes([int(wm_extract_bin[8 * i:8 * i + 8], base=2) ^ random.randint(0, 255) for i in
#                       range(len(wm_extract_bin) // 8)]).decode('utf-8')
#
#     def remove_watermark(self, text_embed: str) -> str:
#         return (text_embed
#                 .replace(self.bit2char_dict["0"], "")
#                 .replace(self.bit2char_dict["1"], ""))

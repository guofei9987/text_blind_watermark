# -*- coding: utf-8 -*-

from crypt_tool import CryptConverter, system_random


class TextBlindWatermark:
    def __init__(self, pwd: bytes, chr0=0x2060, chr1=0xFEFF):
        self.crypt_converter = CryptConverter(pwd)
        self.chr0 = chr(chr0)
        self.chr1 = chr(chr1)

    def generate_watermark(self, wm):
        wm_bin = self.crypt_converter.encode(wm)
        return ''.join(self.chr0 if bit == 0 else self.chr1 for bit in wm_bin)

    def add_wm_at_idx(self, text, wm: bytes, byte_idx):
        text = self.remove_watermark(text)
        wm_dark = self.generate_watermark(wm)
        if byte_idx >= len(text):
            byte_idx = len(text)

        return text[:byte_idx] + wm_dark + text[byte_idx:]

    def add_wm_at_last(self, text, wm: bytes):
        return self.add_wm_at_idx(text, wm, len(text))

    def add_wm_rnd(self, text, wm: bytes):
        idx = system_random() % len(text)
        return self.add_wm_at_idx(text, wm, idx)

    def remove_watermark(self, text):
        return ''.join(char for char in text if char != self.chr0 and char != self.chr1)

    def extract(self, text_with_wm):
        bits = []
        found_left = False
        for c in text_with_wm:
            if c == self.chr0 or c == self.chr1:
                if not found_left:
                    found_left = True
                bits.append(0 if c == self.chr0 else 1)

            elif found_left:
                break

        return self.crypt_converter.decode(bits)

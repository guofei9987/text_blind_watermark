import crypto
import sys

sys.modules['Crypto'] = crypto

from Crypto.Cipher import AES


def embed(sentence, wm, password):
    # 对水印做AES加密
    wm = wm.encode('utf-8')
    cryptor = AES.new(key='{:0<16}'.format(password).encode('utf-8'),
                      mode=AES.MODE_ECB)  # key 长度必须是16,24,32 长度的 byte 格式
    ciphertext_tmp = cryptor.encrypt(wm + b' ' * (16 - len(wm) % 16))  # 明文的长度必须是16的整数倍
    ciphertext_hex = ciphertext_tmp.hex()  # 转为16进制

    bin_text = bin(int(ciphertext_hex, base=16))[2:]

    # 打入水印
    len_bin_text = len(bin_text)
    len_sentence = len(sentence)
    assert len_sentence > len_bin_text, "文本长度太短了,至少{}".format(len_bin_text)

    sentence_embed = ""
    for idx in range(len_sentence):
        sentence_embed += sentence[idx]
        if idx < len_bin_text:
            if bin_text[idx] == "1":
                sentence_embed += chr(127)

    # print("打入水印后的结果：")
    # print("水印长度{}".format(len(bin_text)))
    # print(sentence_embed)
    return sentence_embed


# %%提取水印

def extract(sentence_embed, password):
    bin_wm_extract = ""
    previous_is_char = False
    for i in sentence_embed:
        if previous_is_char:
            if ord(i) == 127:
                bin_wm_extract += "1"
                previous_is_char = False
            else:
                bin_wm_extract += "0"
                previous_is_char = True
        else:
            previous_is_char = True

    #  去掉末尾的0

    last_zero = len(bin_wm_extract) - bin_wm_extract[::-1].find("1")

    last_zero = ((last_zero - 1) // 128 + 1) * 128
    bin_wm_extract = bin_wm_extract[:last_zero]

    # 解密

    hex_wm_extract = hex(int(bin_wm_extract, base=2))

    return AES.new(key='{:0<16}'.format(password).encode('utf-8'), mode=AES.MODE_ECB) \
        .decrypt(bytes.fromhex(hex_wm_extract[2:])).decode('utf-8')  # key 长度必须是16,24,32 长度的 byte 格式

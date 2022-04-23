import random


def embed(sentence, wm, password):
    random.seed(password)

    wm_bin = [format(i ^ random.randint(0, 255), '08b') for i in wm.encode('utf-8')]  # 8位2进制格式

    # wm_bin = [format(i, '08b') for i in wm.encode('utf-8')]  # 8位2进制格式
    # 头尾各放一个1。提取过程中把首尾的0去掉。
    wm_bin = '1' + ''.join(wm_bin) + '1'

    # 打入水印
    len_bin_text = len(wm_bin)
    len_sentence = len(sentence)
    assert len_sentence > len_bin_text, "文本长度太短了,至少{}".format(len_bin_text)

    # TODO:循环嵌入
    # 嵌入水印
    sentence_embed = ""
    for idx in range(len_sentence):
        sentence_embed += sentence[idx]
        if idx < len_bin_text:
            if wm_bin[idx] == "1":
                sentence_embed += chr(127)

    return sentence_embed


def extract(sentence_embed, password):
    wm_extract_bin = ""

    idx = 0
    while idx < len(sentence_embed):
        if sentence_embed[idx] != chr(127):
            idx += 1
            wm_extract_bin += '0'
        else:
            idx += 2
            wm_extract_bin += '1'

    first_zero = wm_extract_bin.find("1")
    last_zero = len(wm_extract_bin) - wm_extract_bin[::-1].find("1")
    wm_extract_bin = wm_extract_bin[first_zero + 1:last_zero - 1]

    random.seed(password)
    s_out = bytes([int(wm_extract_bin[8 * i:8 * i + 8], base=2) ^ random.randint(0, 255) for i in
                   range(len(wm_extract_bin) // 8)]).decode('utf-8')

    return s_out

no = [
    '1d', '7F'  # mac-word/excel 不可用
    , '0x202E'  # 会让字符方向颠倒
    , '0x202A', '0x202B', '0x202C', '0x202D'  # 这些 mac-ppt 不行
    , '0x00AD'  # 不行：win-excel，win-word
    , '200C', '200D'  # 不行：mac-excel
]

chrs_may_useful = [

    '200B'
    , 'FEFF'
    , '0x2060'
]

sentences = []

for i in no+chrs_may_useful:
    sentences.append(
        "这里插入"
        + chr(int(i, base=16)) + chr(int(i, base=16)) + chr(int(i, base=16))
        + "一段含零字符" + i
    )

all_sentence = "\n".join(sentences)
with open("find_chr.txt", "w") as f:
    f.write(all_sentence)

print(all_sentence)


"""
检查项目：
平台：mac、win、ios、安卓、Linux
软件：（重要性按大小排序）
- chrome
- 系统自带浏览器
- 系统自带的文本编辑器
- Office 套件
- Mac 自带办公软件
- wps等
- 命令行
- IDE、vscode
- GitHub 代码页、readme 页
"""

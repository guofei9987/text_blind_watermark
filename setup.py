import os

this_directory = os.path.abspath(os.path.dirname(__file__))


def read_file(filename):
    with open(os.path.join(this_directory, filename), encoding='utf-8') as f:
        long_description = f.read()
    return long_description


# 获取依赖
def read_requirements(filename):
    return [line.strip() for line in read_file(filename).splitlines()
            if not line.startswith('#')]


from setuptools import setup, find_packages

setup(
    name='text_blind_watermark',  # 包的名字，也是将来用户使用 pip install scikit-opt 来安装
    version='0.0.1',  # 版本号，每次上传的版本号应当不一样，可以用类似 sko.__version__ 去自动指定
    python_requires='>=3.5',
    description='Text Blind Watermark in Python',
    long_description=read_file('README.md'),
    long_description_content_type="text/markdown",
    url='https://github.com/guofei9987/text_blind_watermark',  # 随意填写，一般是项目的 github 地址
    author='Guo Fei',
    author_email='guofei9987@foxmail.com',
    license='MIT',
    packages=find_packages(),  # 也可以是一个列表，例如 ['sko']
    platforms=['linux', 'windows', 'macos'],
    install_requires=['pycryptodome'],  # 指定此包的依赖
    zip_safe=False,  # 为了兼容性，一般填 False
)

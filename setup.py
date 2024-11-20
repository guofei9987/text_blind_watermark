import os
import text_blind_watermark

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
    name='text_blind_watermark',
    version=text_blind_watermark.__version__,
    python_requires='>=3.5',
    description='Text Blind Watermark in Python',
    long_description=read_file('README.md'),
    long_description_content_type="text/markdown",
    url='https://github.com/guofei9987/text_blind_watermark',
    author='Guo Fei',
    author_email='guofei9987@foxmail.com',
    license='MIT',
    packages=find_packages(),
    platforms=['linux', 'windows', 'macos'],
    install_requires=["crypt_tool>=0.1.3"],
    zip_safe=False,
)

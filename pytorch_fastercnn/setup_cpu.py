import codecs
import os.path

from setuptools import setup


def get_version(rel_path):
    with codecs.open(
        os.path.join(os.path.abspath(os.path.dirname(__file__)), rel_path), "r",
    ) as fp:
        for line in fp.read().splitlines():
            if line.startswith("__version__"):
                delim = '"' if '"' in line else "'"
                return line.split(delim)[1]
        else:
            raise RuntimeError("Unable to find version string.")


packages = [
    "pytorch_fastercnn",
]

package_data = {
    "": ["*"],
    "pytorch_fastercnn": ["checkpoints/*"],
}

install_requires = [
    "Pillow>=8.2.0",
    "torch==1.5.0+cpu",
    "torchvision==0.6.0+cpu",
    "modelplace-api@https://github.com/opencv-ai/modelplace-api/archive/v0.4.12.zip",
]

setup_kwargs = {
    "name": "pytorch-fastercnn",
    "version": get_version("pytorch_fastercnn/__init__.py") + "+cpu",
    "description": "",
    "long_description": None,
    "author": "",
    "author_email": "",
    "maintainer": "OpenCV.AI",
    "maintainer_email": "modelplace@opencv.ai",
    "url": None,
    "packages": packages,
    "package_data": package_data,
    "install_requires": install_requires,
    "python_requires": ">=3.7,<4.0",
}

setup(**setup_kwargs)

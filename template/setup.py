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
    "template",
]

package_data = {
    "": ["*"],
    "template": ["checkpoints/*"],
}

install_requires = [
    "modelplace-api@https://github.com/opencv-ai/modelplace-api/archive/v0.4.7.zip",
]

setup_kwargs = {
    "name": "template",
    "version": get_version("template/__init__.py"),
    "description": "",
    "long_description": None,
    "author": "Author Name",
    "author_email": "author.email@example.com",
    "maintainer": None,
    "maintainer_email": None,
    "url": None,
    "packages": packages,
    "package_data": package_data,
    "install_requires": install_requires,
    "python_requires": ">=3.7,<4.0",
}

setup(**setup_kwargs)

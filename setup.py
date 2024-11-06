import os
from setuptools import setup, find_packages

# Utility function to read the README file
def read(fname):
    with open(os.path.join(os.path.dirname(__file__), fname), encoding="utf-8") as f:
        return f.read()

setup(
    name="pacific_CodeSwitch",
    version="0.1",
    author="Jonathan Dunn",
    author_email="jonathan.dunn@canterbury.ac.nz",
    description="Detect code switching in Pacific languages",
    license="LGPL 3.0",
    url="https://github.com/jonathandunn/pacific_CodeSwitch",
    keywords=["language id", "code switching", "mri"],
    packages=find_packages(exclude=["*.pyc", "__pycache__"]),
    package_data={'': ['eng_mri.*']},
    install_requires=[
        "cytoolz",
        "numpy",
        "scikit-learn",
            "fasttext @ git+https://github.com/user/fasttext-wheel.git"

    ],
    include_package_data=True,
    long_description=read('README.md'),
    long_description_content_type='text/markdown',
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: GNU Lesser General Public License v3 (LGPLv3)",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
)

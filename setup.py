from setuptools import setup, find_packages

with open("README.md", "r") as fh:
    long_description = fh.read()

setup(
    name="pybiplot",
    version="0.0.4",
    author="Carlos A. Adames Ramos",
    author_email="carlos.adames.ramos@gmail.com",
    description="R's BiPlot visual for PCA in Python",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/adames-ouro/pybiplot",
    packages=find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.11',
    install_requires=[
        'pandas>=2.2.2',
        'matplotlib>=3.9.0'
    ],
)
import setuptools

REQUIRED = ['pandas']

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setuptools.setup(
    name="lambdata-keilayb",
    version="0.0.1",
    author="keilayb",
    description="A collection of data science functions.",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/keilayb/lambdata-23",
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    packages=setuptools.find_packages(),
    install_requires = REQUIRED,
    python_requires=">=3.6",
)
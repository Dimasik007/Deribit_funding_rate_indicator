import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="Deribit_funding_rate_indicator-Dimasik007",
    version="0.0.1",
    author="Dmytro Vnukov",
    author_email="d-vnukov@mail.ru",
    description="Real time 8h funding rate vs 4h rolling rate indicator for Deribit exchange",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/Dimasik007/Deribit_funding_rate_indicator",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
)
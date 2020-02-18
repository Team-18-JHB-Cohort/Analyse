from setuptools import setup

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="AnalysePredict",
    version="0.0.1",
    author="Marcus Moeng",
    author_email="marcusmoeng@yahoo.com",
    description="This package contains metric functions",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/Team-18-JHB-Cohort/Analyse",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
)

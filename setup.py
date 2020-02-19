import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="A_Predict_module",
    version="0.0.1",
    author="Team_18_JHB_2020",
    author_email="marcusmoeng@yahoo.com",
    description="This package contains metric functions",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/Team-18-JHB-Cohort/Analyse.git",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "Operating System :: OS Independent",
    ],
)

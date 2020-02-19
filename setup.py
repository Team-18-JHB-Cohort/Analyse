import setuptools

setuptools.setup(
    name="Analyse",
    version="0.0.1",
    license = 'MIT',
    author="Team_18_JHB_2020",
    install_requires = ['numpy', 'pandas'],
    author_email="marcusmoeng@yahoo.com",
    description="This package contains metric functions",
    long_description=open("README.md", "r").read(),
    long_description_content_type="text/markdown",
    url="https://github.com/Team-18-JHB-Cohort/Analyse",
    packages=setuptools.find_packages(exclude=['tests*'])
)

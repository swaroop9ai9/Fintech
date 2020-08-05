import setuptools

with open("README.md","r") as fh:
	long_description = fh.read()
INSTALL_REQUIRES = (
    ['pandas', 'requests']
)


setuptools.setup(
    name="raptor_finance_api",
    version="0.0.1",
    author="Swaroop Manchala",
    author_email="swaroop9ai9@gmail.com",
    description="finance api especially for Indian NSE/BSE Stock Data",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/swaroop9ai9/Fintech/raptor_finance_api",
    packages=setuptools.find_packages(),
    install_requires=INSTALL_REQUIRES,
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
)

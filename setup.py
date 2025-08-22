import setuptools

__version__ = "0.1.0"


with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()


setuptools.setup(
    name="scrapy-vectors",
    version=__version__,
    license="ISC",
    description="Vector embeddings generation and storage for Scrapy",
    long_description=long_description,
    long_description_content_type="text/markdown",
    author="Kyle Kai Hang Tan",
    author_email="",
    url="https://github.com/kyleissuper/scrapy-vectors",
    packages=["scrapy_vectors"],
    classifiers=[
        "Development Status :: 0.1.0",
        "License :: OSI Approved :: ISC License (ISCL)",
        "Programming Language :: Python",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
        "Programming Language :: Python :: 3.11",
        "Programming Language :: Python :: 3.12",
        "Programming Language :: Python :: 3.13",
        "Framework :: Scrapy",
        "Intended Audience :: Developers",
        "Topic :: Internet :: WWW/HTTP",
        "Topic :: Software Development :: Libraries :: Application Frameworks",
        "Topic :: Software Development :: Libraries :: Python Modules",
    ],
    python_requires=">=3.9",
    install_requires=[
        "scrapy>=2.0",
        "litellm>=1.0.0",
        "boto3>=1.20.0",
    ],
)

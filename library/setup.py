from setuptools import setup, find_packages

setup(
    name="rankwise",
    version="0.1.0",
    author="Your Name",
    author_email="your.email@example.com",
    description="A Python library to rank texts using LLMs.",
    long_description=open("README.md").read(),
    long_description_content_type="text/markdown",
    url="https://github.com/yourusername/rankwise",
    packages=find_packages(),
    install_requires=[
        "openai>=0.27.0",
        "pydantic>=1.10.0"
    ],
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
)

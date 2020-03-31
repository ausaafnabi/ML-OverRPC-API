import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="Over-RPC", 
    version="0.0.1",
    author="Ausaaf Nabi",
    author_email=" ",
    description="Machine Learning package over RPC calls",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/ausaafnabi/Over-RPC-API",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
)

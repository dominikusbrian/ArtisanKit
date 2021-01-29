import setuptools

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setuptools.setup(
    name="ArtisanKit", # Replace with your own username
    version="0.0.2",
    author="dominikusbrian",
    author_email="dominikusbrian@nyu.com",
    description="A Productivity Toolkit for Craftsman/woman Doing Research in Computational Chemistry, Machine Learning, and Beyond.",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/xiangsunlab/ArtisanKit",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: GNU Lesser General Public License v3 (LGPLv3)",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.8',
)


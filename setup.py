import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="lifetracker-sgrady", # Replace with your own username
    version="0.0.1",
    author="Sean Grady",
    author_email="vedicmonk@gmail.com",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/SeanGrady/life_tracker",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.8',
)
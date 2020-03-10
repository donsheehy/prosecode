import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="prosecode",
    version="0.1.0",
    author="Donald R. Sheehy",
    author_email="don.r.sheehy@gmail.com",
    description="Literate programming in Python from markdown to LaTeX.",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://donsheehy.github.io/prosecode/",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
    include_package_data=True,
    install_requires =[
        'Markdown',
        'Click',
        'Pygments',
    ],
    entry_points='''
        [console_scripts]
        prosecode=prosecode.cli:cli
    ''',
)

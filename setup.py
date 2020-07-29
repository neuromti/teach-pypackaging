import setuptools

from pathlib import Path

# with (Path(__file__).parent / "readme.md").open() as f:
#     long_description = f.read()
with (Path(__file__).parent / "requirements.txt").open() as f:
    install_requires = f.readlines()


setuptools.setup(
    name="example-pkg",  # Replace with your own username
    version="0.0.1",
    # author="Example Author",
    # author_email="author@example.com",
    # description="A small example package",
    # long_description=long_description,
    # long_description_content_type="text/markdown",
    install_requires=install_requires,
    # url="",
    # license="MIT",
    packages=setuptools.find_packages(),
    entry_points={"console_scripts": ["packmod=pack.module:foo"],},
    classifiers=["Programming Language :: Python :: 3"],
    #     "License :: OSI Approved :: MIT License",
    #     "Operating System :: OS Independent",
    # ],
    python_requires=">=3",
)

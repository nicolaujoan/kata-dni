import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="kata DNI",
    version="0.0.1",
    author="nicolaujoan",
    author_email="joannicolau23@gmail.com",
    description="kata dni to practice oop using python",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/nicolaujoan/kata-dni/",
    packages=setuptools.find_packages(),
    include_package_data=True,
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires=">=3.6",
    install_requires=[
        "attrs==21.2.0",
        "backports.entry-points-selectable==1.1.1",
        "distlib==0.3.4",
        "filelock==3.4.0",
        "iniconfig==1.1.1",
        "packaging==21.3",
        "platformdirs==2.4.0",
        "pluggy==1.0.0",
        "py==1.11.0",
        "pyparsing==3.0.6",
        "pytest==6.2.5",
        "six==1.16.0",
        "toml==0.10.2",
        "tox==3.24.4",
        "virtualenv==20.10.0",
    ],
)

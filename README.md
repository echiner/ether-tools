# Ethereum Tools

## Introduction

Useful tools for Ethereum:
* **send_ether.py**: Send ether to a list of addresses.

## Setup

Follow these steps to run the scripts:

* Download and install python: https://www.python.org/downloads/
* Install required libraries

```
pip install web3
```

## Troubleshooting

### Error installing web3

In Windows you might get an error when installing web3 ("pip install web3") realted to "lru-dict".
This is how you solve it:

The error you're encountering is due to the lru-dict package requiring Microsoft Visual C++ 14.0 or greater to be installed on your system. To resolve this issue, follow these steps:

* Install Microsoft C++ Build Tools from the following link:  [Microsoft C++ Build Tools](https://visualstudio.microsoft.com/visual-cpp-build-tools/)
* During the installation process, make sure to check the "C++ build tools" checkbox, and also select the "Windows 10 SDK" and "MSVC v142 - VS 2019 C++ x64/x86 build tools (v14.2)" components under the "C++ build tools" section.
* After the installation is complete, you might need to restart your computer.
* Open a new command prompt or terminal and try installing the web3 package again using pip install web3.

The installation should now proceed without any errors. If you still encounter issues, make sure that the build tools are correctly installed and that you're using an updated version of Python (3.7 or higher is recommended).

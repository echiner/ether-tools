# Ethereum Tools

## Introduction

Useful tools for Ethereum:
* **send_ether.py**: Send ether to a list of addresses.

## Initial setup

Follow these steps to run the scripts:

* Download and install python: https://www.python.org/downloads/
* Install required libraries

```
pip install web3
```

## Config and run

### send_ether.py

* Setup `send_ether.ini` by adding sender private key and the provider URL
* Add the list of addresses to `send_ether.addresses`
  * Duplicated addresses will be automatically removed
  * Commented addresses will be automatically skipped
  * Incorrect addreses will be automatically skipped
* Execute the code
  * A confirmation is required prior to sending the funds.

```
python send_ether.py 0.1
```

Sample execution:

```
---------------------------------------------------
Sender address: 0xXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX
Amount to be sent: 0.1
---------------------------------------------------
About to send 0.1 Ether to the following 2 addresses:
 - 0xYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYY
 - 0xZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZ

Are you sure you want to proceed? (yes/no): yes

1: Sent 0.1 Ether to 0xYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYY. Transaction hash: 0x429487e3ffd4159fbb7c24b2625a7abade343216c7bc3ca21ea127067e534c5b
2: Sent 0.1 Ether to 0xZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZ. Transaction hash: 0x4372d9e6d34dbf476454390526d5eea8a49a3bbb73d423d38d8bd9febfbd9236
```

## Troubleshooting

### Error installing web3 in Windows

In Windows you might get an error when installing web3 ("pip install web3") related to "lru-dict".
This is how you solve it:

The error you're encountering is due to the lru-dict package requiring Microsoft Visual C++ 14.0 or greater to be installed on your system. To resolve this issue, follow these steps:

* Install Microsoft C++ Build Tools from the following link:  [Microsoft C++ Build Tools](https://visualstudio.microsoft.com/visual-cpp-build-tools/)
* During the installation process, make sure to check the "C++ build tools" checkbox, and also select the "Windows 10 SDK" and "MSVC v142 - VS 2019 C++ x64/x86 build tools (v14.2)" components under the "C++ build tools" section.
* After the installation is complete, you might need to restart your computer.
* Open a new command prompt or terminal and try installing the web3 package again using pip install web3.

The installation should now proceed without any errors. If you still encounter issues, make sure that the build tools are correctly installed and that you're using an updated version of Python (3.7 or higher is recommended).

<h1 align="center" style="font-size:36px;font-weight:bold;">
        WHOISxss
</h1>
<h4 align="center">
    <strong>Powered by BINIT GHIMIRE (<a href='https://twitter.com/WHOISbinit' target="_blank">@WHOISbinit</a>)</strong>
</h4>
<p align="center">
    <img src="src/screenshot.png">
</p>
<h3 align="center">Real-time <strong>XSS</strong> Detection Suite!</h3><hr/>
<h2 align="center">Find XSS in Real-time with WHOISxss!</h2>
<p align="center">
    <a href="https://www.python.org/" target="_blank"><img src="https://ForTheBadge.com/images/badges/made-with-python.svg"></a>
</p>

## Requirements
1. **Python** (3.x)
2. **PIP** for **Python3**
3. **GeckoDriver** [[Download Here](https://github.com/mozilla/geckodriver/releases)]
4. **Required Modules:** **selenium**, **argparse**
    #### Install from **requirements.txt**
    > **`pip3 install -r requirements.txt`**
    #### Manual Installation
    > **`pip3 install selenium argparse`**

**Mozilla Firefox** and **GeckoDriver** are required to be installed for using **WHOISxss** since everything is performed in real-time, just in front of you, and a version of **ChromeDriver** isn't available as of now.

<hr>

## Installation
1. Download/clone the repository to your local machine:
   
    **`git clone https://github.com/TheBinitGhimire/WHOISxss`**
2. Switch to the **WHOISxss** directory!

    **`cd WHOISxss`**

<hr>

## Usage
There are two ways to make use of WHOISxss;

1. Single URL
2. Multiple URLs 
   
> ### Using WHOISxss for Single URL:
> **`python3 main.py -u URL`**<br><br>
> For example:<br>
> **`python3 main.py -u https://xss-quiz.int21h.jp/`**<br><br>
<p align="center">
    <img src="src/single.png">
</p>

> ### Using WHOISxss for Multiple URLs:
> Create a text file with any name, with a list of URLs, separated by new lines.<br>
> **`python3 main.py -f FILENAME`**<br><br>
> For example:<br>
> **`python3 main.py -f list.txt`**<br><br>

<hr>

## Contributors
<table>
    <tr>
        <td align="center">
            <a href="https://github.com/TheBinitGhimire">
                <img src="https://avatars0.githubusercontent.com/u/20013689" style="width:100px;"><br />
                <strong>Binit Ghimire</strong><br>
                <span>@WHOISbinit</span>
            </a>
        </td>
        <td align="center">
            <a href="https://github.com/cimplesid">
                <img src="https://avatars0.githubusercontent.com/u/29953052" style="width:100px;"><br />
                <strong>Siddhartha Joshi</strong><br>
                <span>@cimplesid</span>
            </a>
        </td>
    </tr>
</table>

## Feature Requests
<p align="center">
    <a href="https://github.com/TheBinitGhimire/WHOISxss/pulls"><img src="https://img.shields.io/badge/PRs-welcome-brightgreen.svg?style=flat-square"></a>
</p>

If you are interested in contributing in the development of <strong>WHOISxss</strong>, you can feel free to create a <strong>Pull Request</strong> with modifications in the original code, or you shall open up a new <strong>issue</strong>, and I will try to include the feature as requested.

There is no restriction on anyone for contributing to the development of <strong>WHOISxss</strong>. If you would like to contribute, you can feel free to do so.

<p align="center"><strong>~~~ ___***___~~~</strong></p>

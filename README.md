# To God be the glory

This project was to scrap the twi(Akan) version of the Seventh-day Adventist hymnal from [link](https://www.hymnalaccompanist.com/twi/twinumber.html).

## Objective
The church wanted to present the twi version of the hymnal during church service and I decided to scrap the text that I will use later to build a presentation application for the church.

## Tech tools
- Python
- Selenium

## Installation
I assume you have already installed python and that selenium chrome/firefox driver is also on your system path. check python and selenium documentation

- Open the utilities/driver.py and change the driver to either chrome/firefox to suit your needs.
- Refer to selenium documentation for more information
Example: Linux
```sh
sudo apt update
sudo apt install -y unzip wget # if unzip and wget is not installed
wget https://dl.google.com/linux/direct/google-chrome-stable_current_amd64.deb
sudo apt install -y ./google-chrome-stable_current_amd64.deb
google-chrome --version # result 127.0.6533.119
```
- go to [chrome driver](https://sites.google.com/chromium.org/driver/downloads?authuser=0), download the chrome driver that matches your version of installed chrome
- move the chromedriver to drivers directory

create a virtual environment
```sh
python -m venv venv
```
instal requirements
```sh
pip install -r requirements.txt
```

## Usage
```sh
python main.py
```

## Result
The text are saved as json in a directory called data
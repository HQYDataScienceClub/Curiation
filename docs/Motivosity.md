# Motivosity Scraper

For scraping Motivosity, we use the Selenium package:

#### Selenium

[Selenium](http://selenium-python.readthedocs.io) uses a webdriver to navigate websites.

Run these commands in PowerShell to download the chrome webdriver programmatically:

```PowerShell
cd D:\codebase\sandbox\Curiation
$url = "https://chromedriver.storage.googleapis.com/2.38/chromedriver_win32.zip"
Invoke-WebRequest -Uri $url -OutFile ".\env\chromedriver_win32.zip"
Expand-Archive .\env\chromedriver_win32.zip -DestinationPath .\env\
Remove-Item .\env\chromedriver_win32.zip
```

Alternately, download manually from [sites.google.com/a/chromium.org](https://sites.google.com/a/chromium.org/chromedriver/) and save under the `env` directory:

```
Curiation
    ├─ docs
    ├─ env
    |   ├─ venv
    |   └─ chromedriver  <–– save chrome webdriver here
    ├─ src
    |   └─ Motivosity.py
    └── README.md
```
#### Credentials
Create a credentials file: `.\env\credentials.json` with your credentials.
See: `.\env\credentials_example.json` as an example.

#### Scrape

To scrape Motivosity, run the scrape script:
```PowerShell
.\env\venv\Scripts\activate.ps1
python .\src\Motivosity.py
deactivate
```

This will scrape data and save to files:
`data\Motivosity-Appreciation.json` and `data\Motivosity-Departments.json`

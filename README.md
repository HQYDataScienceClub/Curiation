# Curiation


## Developer Quickstart

Start by cloning this project locally:
```
git clone https://github.com/oliolafsson/Curiation.git
```
#### Virtualenv

```PowerShell
# Install virtual environment: venv
cd D:\codebase\sandbox\Curiation  # /path/may/vary/
python3 -m virtualenv env/venv
. .\env\venv\Scripts\activate.ps1
pip install -r .\env\requirements.txt
deactivate
```

#### Selenium

Selenium uses a webdriver to navigate websites.

Download manually from [sites.google.com/a/chromium.org](https://sites.google.com/a/chromium.org/chromedriver/) and save under the `env` directory:

```
Curiation
    ├─ env
    |   ├─ venv
    |   └─ chromedriver  <–– save chrome webdriver here
    ├─ src
    |   └─ scrape.py
    └── README.md
```

#### Scrape

First, you'll need to add authentication credentials to the `src\scrape.py` script.The variables are called `un` and `pw`, and are d efined at the top of the script.

Now, run the scrape script:
```PowerShell
python .\src\scrape.py
```

This will scrape data and save to a file:
`src\appreciation.json`

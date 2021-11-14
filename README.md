# Impfstatus Fortschritt Twitter Bot

This is the code that runs the account [@impf_progress](https://twitter.com/impf_progress) on Twitter, tweeting German vaccination updates with an ASCII-art style loading bar, inspired by [@year_progress](https://twitter.com/year_progress).

>▓▓▓▓▓▓▓▓▓▓░░░░░ 70,0% mind. eine Impfdosis  
>▓▓▓▓▓▓▓▓▓▓░░░░░ 67,5% vollständig Geimpfte  
>▓░░░░░░░░░░░░░░ 4,6% Booster Geimpfte

## Script Setup

- Create an app at the [Twitter Developer site](https://developer.twitter.com/) and create app tokens and keys
- Edit [twitter.cfg](./twitter.cfg) and put in your Twitter Consumer and Access tokens/keys
- Change `DRY_RUN` to `yes` if you just want to test the script without actually sending any tweets
- Make sure [state.cfg](./state.cfg) is writable, this is where the last Tweet and its values are stored so to not Tweet repeated messages
- Install the Tweepy library

```
# Create venv
py -3 venv venv

# Activate venv: Windows
venv\Scripts\activate.bat 

# Activate venv: Linux / MacOS
source venv/bin/activate

# Install tweepy directly
pip3 install tweepy

# Alternatively, use requirements.txt
pip install -r requirements.txt
```

The script can now simply be called like this:

```
python bot.py
# or
py -3 bot.py
```

## Crontab Setup

Running a cronjob with virtualenv:

```
0 12 * * * cd /home/you/impf-progress-bot/ && /home/you/impf-progress-bot/venv/bin/python /home/you/impf-progress-bot/bot.py
```

## Data Source

The script uses data from [Aktuell_Deutschland_Impfquoten_COVID-19.csv](https://github.com/robert-koch-institut/COVID-19-Impfungen_in_Deutschland/blob/master/Aktuell_Deutschland_Impfquoten_COVID-19.csv), provided by the Robert Koch-Institut under [CC-BY 4.0 International](https://creativecommons.org/licenses/by-sa/4.0/legalcode.de).

## License

All source code and documentation in this repository is licensed under the [MIT license](LICENSE).

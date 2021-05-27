# Impfstatus Fortschritt Twitter Bot

This is the code that runs the account [@impf_progress](https://twitter.com/impf_progress) on Twitter, tweeting German vaccination updates with an ASCII-art style loading bar, inspired by [@year_progress](https://twitter.com/year_progress).

>▓▓▓▓▓░░░░░░░░░░ 31,5% Erstimpfung  
>▓░░░░░░░░░░░░░░ 8,8% vollständig geimpft

## Script Setup

- Create an app at the [Twitter Developer site](https://developer.twitter.com/) and create app tokens and keys
- Edit [twitter.cfg](./twitter.cfg) and put in your Twitter Consumer and Access tokens/keys
- Make sure [state.cfg](./state.cfg) is writable, this is where the last Tweet and its values are stored so to not Tweet repeated messages
- Change `DRY_RUN = True` in [bot.py](./bot.py) to `False` when you are done testing
- Install the Tweepy library, using virtualenv

```
# Create venv
py -3 venv venv

# Activate venv: Windows
venv\Scripts\activate.bat 

# Activate venv: Linux
venv\bin\activate

# Activate venv: MacOS
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

The script uses [germany_vaccinations_timeseries_v2.tsv](https://impfdashboard.de/static/data/germany_vaccinations_timeseries_v2.tsv) from [impfdashboard.de](https://impfdashboard.de/).

> Quelle: impfdashboard.de, RKI, BMG.

## License

MIT

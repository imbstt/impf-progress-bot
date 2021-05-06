# Impfstatus Fortschritt Twitter Bot

Account [@impf_progress](https://twitter.com/impf_progress) on Twitter

## Script Setup

- Edit [twitter.cfg](twitter.cfg) and put in your Twitter Consumer and Access tokens/keys
- Make sure [state.cfg](state.cfg) is writable
- Change `DRY_RUN = True` in [bot.py](bot.py) to `False`

## Script Setup

Install the Tweepy library, using virtualenv:

```
# Create venv
py -3 venv venv

# Activate venv: Windows
venv\Scripts\activate.bat 

# Activate venv: Linux
venv\bin\activate

# Install tweepy directly
pip3 install tweepy

# Alternatively, use requirements.txt
pip install -r requirements.txt
```

## Crontab Setup

Running a cronjob with virtualenv:

```
0 12 * * * cd /home/you/twitter-impf-progress-bot/ && /home/you/twitter-impf-progress-bot/venv/bin/python /home/you/twitter-impf-progress-bot/bot.py
```

## Data Source

The script uses [germany_vaccinations_timeseries_v2.tsv](https://impfdashboard.de/static/data/germany_vaccinations_timeseries_v2.tsv) from [impfdashboard.de](https://impfdashboard.de/).

> Quelle: impfdashboard.de, RKI, BMG.

## License

MIT

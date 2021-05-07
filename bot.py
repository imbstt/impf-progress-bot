import csv
import urllib.request
import tweepy
from datetime import datetime
import configparser

DRY_RUN = True

twitter_config = configparser.ConfigParser()
twitter_config.read('twitter.cfg')
CONSUMER_KEY    = twitter_config.get('TWITTER', 'CONSUMER_KEY')
CONSUMER_SECRET = twitter_config.get('TWITTER', 'CONSUMER_SECRET')
ACCESS_KEY      = twitter_config.get('TWITTER', 'ACCESS_KEY')
ACCESS_SECRET   = twitter_config.get('TWITTER', 'ACCESS_SECRET')
auth = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
auth.set_access_token(ACCESS_KEY, ACCESS_SECRET)

TSV_URL = "https://impfdashboard.de/static/data/germany_vaccinations_timeseries_v2.tsv"

CONFIG_FILENAME = 'state.cfg'

config = configparser.ConfigParser()
config.read(CONFIG_FILENAME)

def generateProgressbar(percentage):
	num_chars = 15
	num_filled = round(percentage*num_chars)
	num_empty = num_chars-num_filled
	display_percentage = str(round(percentage*100, 1)).replace('.', ',')
	msg = '{}{} {}%'.format('▓'*num_filled, '░'*num_empty, display_percentage)
	return msg

def getCurrentdata(url):
	tsvstream = urllib.request.urlopen(url)
	tsv_file_lines = tsvstream.read().decode('utf-8').splitlines()
	tsv_data_lines = csv.DictReader(tsv_file_lines, delimiter='\t')
	# skip to last line
	for line_dict in tsv_data_lines:
		pass
	return line_dict

def sendTweet(the_tweet):
	twitter_API = tweepy.API(auth)
	print('tweeting with handle @{}'.format(twitter_API.me().screen_name))
	if DRY_RUN:
		print("DRY RUN not actually sending tweet!")
		return
	twitter_API.update_status(the_tweet)

def checkIfShouldTweet(data):
	last_date = datetime.strptime(config.get('LAST_TWEET', 'date'), '%Y-%m-%d')
	curr_date = datetime.strptime(data.get('date'), '%Y-%m-%d')
	print("date: {} / {}".format(config.get('LAST_TWEET', 'date'), data.get('date')))

	if last_date < curr_date:
		impf_quote_erst_old = float(config.get('LAST_TWEET', 'impf_quote_erst'))
		impf_quote_voll_old = float(config.get('LAST_TWEET', 'impf_quote_voll'))
		impf_quote_erst_new = float(data.get('impf_quote_erst'))
		impf_quote_voll_new = float(data.get('impf_quote_voll'))
		
		print("erst: {} / {}".format(round(impf_quote_erst_old*100, 1), round(impf_quote_erst_new*100, 1)))
		print("voll: {} / {}".format(round(impf_quote_voll_old*100, 1), round(impf_quote_voll_new*100, 1)))
		
		if round(impf_quote_erst_old*100, 1) < round(impf_quote_erst_new*100, 1):
			return True
		if round(impf_quote_voll_old*100, 1) < round(impf_quote_voll_new*100, 1):
			return True
		return False
	else:
		print("date is same or older: do not tweet")
		return False

def saveState(data):
	config.set('LAST_TWEET', 'date', data.get('date'))
	config.set('LAST_TWEET', 'impf_quote_erst', data.get('impf_quote_erst'))
	config.set('LAST_TWEET', 'impf_quote_voll', data.get('impf_quote_voll'))
	with open(CONFIG_FILENAME, 'w') as configfile:
		config.write(configfile)
		print("saved cfg")

def generateMessage(data):
	bar_erst = generateProgressbar(float(data.get('impf_quote_erst')))
	bar_voll = generateProgressbar(float(data.get('impf_quote_voll')))
	msg = '{} mind. eine Impfdosis\n{} vollständig Geimpfte'.format(bar_erst, bar_voll)
	return msg

def runAll():
	data = getCurrentdata(TSV_URL)
	should_send = checkIfShouldTweet(data)
	print("send tweet?", should_send)
	if should_send:
		# need to tweet
		print('send tweet:')
		print('')
		progress_msg = generateMessage(data)
		print(progress_msg)
		print('')
		sendTweet(progress_msg)
	else:
		print('do not tweet')
	saveState(data)

try:
	runAll()
except:
	raise

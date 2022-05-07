import configparser
import csv
import sys
import tweepy
import urllib.request
from datetime import datetime

"""
Set up config values and constants
"""
twitter_config = configparser.ConfigParser()
twitter_config.read("twitter.cfg")
DRY_RUN         = twitter_config.getboolean("TWITTER", "DRY_RUN")
CONSUMER_KEY    = twitter_config.get("TWITTER", "CONSUMER_KEY")
CONSUMER_SECRET = twitter_config.get("TWITTER", "CONSUMER_SECRET")
ACCESS_KEY      = twitter_config.get("TWITTER", "ACCESS_KEY")
ACCESS_SECRET   = twitter_config.get("TWITTER", "ACCESS_SECRET")
auth = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
auth.set_access_token(ACCESS_KEY, ACCESS_SECRET)

CSV_URL = "https://raw.githubusercontent.com/robert-koch-institut/COVID-19-Impfungen_in_Deutschland/master/Aktuell_Deutschland_Impfquoten_COVID-19.csv"
CSV_COLUMN_ERST = "Impfquote_gesamt_min1"
CSV_COLUMN_VOLL = "Impfquote_gesamt_gi"
CSV_COLUMN_BOOST = "Impfquote_gesamt_boost1"
CSV_COLUMN_BOOST2 = "Impfquote_gesamt_boost2"

CONFIG_FILENAME = "state.cfg"

config = configparser.ConfigParser()
config.read(CONFIG_FILENAME)

def generate_progressbar(percentage):
	"""
	Generates the ASCII-art style progress bar, and appends the percentage number in German locale number format
	"""
	num_chars = 15
	num_filled = round((percentage/100)*num_chars)
	num_empty = num_chars-num_filled
	display_percentage = str(percentage).replace(".", ",")
	msg = "{}{} {}%".format("▓"*num_filled, "░"*num_empty, display_percentage)
	return msg

def get_current_data(url):
	"""
	Downloads the CSV from the data source and extracts data of interest: Vaccination progress for the whole of Germany
	"""
	csvstream = urllib.request.urlopen(url)
	csv_file_lines = csvstream.read().decode("utf-8").splitlines()
	csv_data_lines = csv.DictReader(csv_file_lines, delimiter=',')
	for line_dict in csv_data_lines:
		if line_dict.get("Bundesland") == "Deutschland":
			return line_dict
	return None

def send_tweet(the_tweet):
	"""
	Sends tweet using the tweepy library
	"""
	if DRY_RUN:
		print("[DRY RUN] Not actually sending tweet")
		return

	twitter_API = tweepy.API(auth)
	print("Tweeting with handle @{}".format(twitter_API.me().screen_name))
	twitter_API.update_status(the_tweet)

def check_if_should_tweet(data):
	"""
	Performs several tests to check if a tweet should be sent or not:
	- Current data's date must be newer than the one saved in the state configuration
	- Any of the percentage values must have changed and be higher as well
	"""
	print("Checking old / new values")
	last_date = datetime.strptime(config.get("LAST_TWEET", "date"), "%Y-%m-%d")
	curr_date = datetime.strptime(data.get("Datum"), "%Y-%m-%d")
	print("date: {} / {}".format(config.get("LAST_TWEET", "date"), data.get("Datum")))

	if last_date < curr_date:
		impf_quote_erst_old = float(config.get("LAST_TWEET", "impf_quote_erst"))
		impf_quote_voll_old = float(config.get("LAST_TWEET", "impf_quote_voll"))
		impf_quote_boost_old = float(config.get("LAST_TWEET", "impf_quote_boost"))
		impf_quote_boost2_old = float(config.get("LAST_TWEET", "impf_quote_boost2"))

		impf_quote_erst_new = float(data.get(CSV_COLUMN_ERST))
		impf_quote_voll_new = float(data.get(CSV_COLUMN_VOLL))
		impf_quote_boost_new = float(data.get(CSV_COLUMN_BOOST))
		impf_quote_boost2_new = float(data.get(CSV_COLUMN_BOOST2))

		print("erst: {} / {}".format(impf_quote_erst_old, impf_quote_erst_new))
		print("voll: {} / {}".format(impf_quote_voll_old, impf_quote_voll_new))
		print("boost: {} / {}".format(impf_quote_boost_old, impf_quote_boost_new))
		print("boost2: {} / {}".format(impf_quote_boost2_old, impf_quote_boost2_new))

		if impf_quote_erst_old < impf_quote_erst_new:
			return True
		if impf_quote_voll_old < impf_quote_voll_new:
			return True
		if impf_quote_boost_old < impf_quote_boost_new:
			return True
		if impf_quote_boost2_old < impf_quote_boost2_new:
			return True
		print("Values have not changed: Do not tweet")
		return False
	else:
		print("Date is same or older: Do not tweet")
		return False

def save_state(data):
	"""
	Saves the date and percentages from the current CSV data to a state configuration file
	"""
	config.set("LAST_TWEET", "date", data.get("Datum"))
	config.set("LAST_TWEET", "impf_quote_erst", data.get(CSV_COLUMN_ERST))
	config.set("LAST_TWEET", "impf_quote_voll", data.get(CSV_COLUMN_VOLL))
	config.set("LAST_TWEET", "impf_quote_boost", data.get(CSV_COLUMN_BOOST))
	config.set("LAST_TWEET", "impf_quote_boost2", data.get(CSV_COLUMN_BOOST2))

	if DRY_RUN:
		print("")
		print("[DRY RUN] Not updating the state configuration")
		print("")
		config.write(sys.stdout)
		return

	with open(CONFIG_FILENAME, "w") as configfile:
		config.write(configfile)
		print("Saved state configuration")

def generate_message(data):
	"""
	Concatenates the three progress bars into the final tweet message text
	"""
	bar_erst = generate_progressbar(float(data.get(CSV_COLUMN_ERST)))
	bar_voll = generate_progressbar(float(data.get(CSV_COLUMN_VOLL)))
	bar_boost = generate_progressbar(float(data.get(CSV_COLUMN_BOOST)))
	bar_boost2 = generate_progressbar(float(data.get(CSV_COLUMN_BOOST2)))
	msg = "{} mind. eine Impfdosis\n{} grundimmunisiert\n{} erste Auffrischimpfung\n{} zweite Auffrischimpfung".format(bar_erst, bar_voll, bar_boost, bar_boost2)
	return msg

def run_all():
	data = get_current_data(CSV_URL)
	if not data:
		print("No matching data found in the CSV")
		raise
	should_send = check_if_should_tweet(data)
	print("")
	print("Send tweet?", should_send)
	if should_send:
		print("Sending tweet:")
		print("")
		progress_msg = generate_message(data)
		print(progress_msg)
		print("")
		send_tweet(progress_msg)
	save_state(data)

try:
	run_all()
except:
	raise

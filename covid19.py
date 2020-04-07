# coding=UTF-8
"""
COVID-19 Stats

Author: ZmEu (zmeu@whitehat.ro)
Date: Tue Apr  7 22:02:26 UTC 2020

v0.1 - First version
v0.2 - Fix lowercase on country
v0.3 - Added function spam as auto trigger per channel
v0.4 - Added short name in country: ro
v0.5 - Fixed function country

https://whitehat.ro
"""

from __future__ import unicode_literals, absolute_import, print_function, division
import requests
from sopel.module import commands
from sopel import module
from requests.exceptions import SSLError

def spam(chan, bot):
	if chan in bot.channels:
		try:
			response = requests.get("https://whitehat.ro/api/covid/?c=world", verify=True)
			if response.json()["country"].lower() == "world":
				bot.say("(AUTO) \x02COVID-19\x02 Stats -- \x02" + response.json()['country'] +"\x02 -- Total Cases: \x02" + response.json()['total_cases'] + "\x02, New Cases: \x02\x0302" + response.json()['new_cases'] + "\x03\x02, Total Deaths: \x02" + response.json()['total_deaths'] + "\x02, New Deaths: \x02\x0304" + response.json()['new_deaths'] + "\x03\x02, Recovered: \x02\x0303" + response.json()['total_recovered'] + "\x03\x02, Active Cases: \x02" + response.json()['active_cases'] + "\x02, Critical: \x02" + response.json()['serious_critical'] + "\x02, Total Cases/1M pop: \x02" + response.json()['total_cases_1m_pop'] + "\x02.", chan)
		except SSLError:
			return
		except Exception:
			return

@commands("covid")
def covid(bot, trigger):
	country = trigger.group(2)
	if not country:
		country = "world"
	elif country == "ro":
		country = "romania"
	try:
		response = requests.get("https://whitehat.ro/api/covid/?c=" + country.replace(" ", "_").lower(), verify=True)
		if response.json()["country"]: pass
	except SSLError:
		bot.say("SSL Error")
		return
	except Exception:
		bot.say("We try to help, you try to cheat, guess who won ?")
		return
	if response.json()["country"].lower() == "romania":
		bot.say("\x02COVID-19\x02 Stats -- \x02\x1F\x0304RO\x0308MAN\x0312IA\x03\x1F\x02 -- Total Cases: \x02" + response.json()['total_cases'] + "\x02, New Cases: \x02\x0302" + response.json()['new_cases'] + "\x03\x02, Total Deaths: \x02" + response.json()['total_deaths'] + "\x02, New Deaths: \x02\x0304" + response.json()['new_deaths'] + "\x03\x02, Recovered: \x02\x0303" + response.json()['total_recovered'] + "\x03\x02, Active Cases: \x02" + response.json()['active_cases'] + "\x02, Critical: \x02" + response.json()['serious_critical'] + "\x02, Total Cases/1M pop: \x02" + response.json()['total_cases_1m_pop'] + "\x02.")
	else:
		bot.say("\x02COVID-19\x02 Stats -- \x02" + response.json()['country'] +"\x02 -- Total Cases: \x02" + response.json()['total_cases'] + "\x02, New Cases: \x02\x0302" + response.json()['new_cases'] + "\x03\x02, Total Deaths: \x02" + response.json()['total_deaths'] + "\x02, New Deaths: \x02\x0304" + response.json()['new_deaths'] + "\x03\x02, Recovered: \x02\x0303" + response.json()['total_recovered'] + "\x03\x02, Active Cases: \x02" + response.json()['active_cases'] + "\x02, Critical: \x02" + response.json()['serious_critical'] + "\x02, Total Cases/1M pop: \x02" + response.json()['total_cases_1m_pop'] + "\x02.")

@module.interval(3600)
def spam_every_second(bot):
	spam("#whitehat", bot)

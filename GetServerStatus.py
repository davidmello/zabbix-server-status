#!/usr/bin/python
# -*- coding: utf-8 -*-
# author: David Mello <david.mello@gmail.com>
# Relase: 0.1
# Date: 2017-04-21

# import urllib2
import requests
import json
import argparse
import collections

# Parameters that can be used
if __name__ == '__main__':
	parser = argparse.ArgumentParser()
	parser.add_argument('-s', '--server', help='tell from what server to get server-status')
	parser.add_argument('-k', '--key', help='key to retrieve value')
args = parser.parse_args()

# Check if the parameter was used, case it was, has to be the Apache Server Status URL
if not args.server:
	parser.error('You need to use with -s option.')
else:
	myzabbixurl = args.server + "?auto"

try:
	# Apache Server to be verified... it can be https
	site = requests.get(myzabbixurl, verify=False).content
	
	# Array that will store server-status parameters
	criarJson = []

	# Line by line from the server-status
	for linha in site.splitlines():
		# Breaks the line in two, key and value
		separado = linha.split(":")
		# Adiciona o # que eh necessario para as variaveis do Zabbix
		chave = "#" + separado[0].replace(' ','_').upper()
		valor = separado[1].strip()

		apache_values = {	"_": { "TOTAL": 0, "CODE": "#SCOREBOARD_WAITING_CONNECTION" }, 	# Waiting for Connection
							"S": { "TOTAL": 0, "CODE": "#SCOREBOARD_STARTING_UP" }, 		# Starting up
							"R": { "TOTAL": 0, "CODE": "#SCOREBOARD_READING_REQUEST" }, 	# Reading Request
							"W": { "TOTAL": 0, "CODE": "#SCOREBOARD_SENDING_REPLY" }, 		# Sending Reply
							"K": { "TOTAL": 0, "CODE": "#SCOREBOARD_KEEPALIVE" }, 			# Keepalive (read)
							"D": { "TOTAL": 0, "CODE": "#SCOREBOARD_DNS_LOOKUP" }, 			# DNS Lookup
							"C": { "TOTAL": 0, "CODE": "#SCOREBOARD_CLOSING_CONNECTION" }, 	# Closing connection
							"L": { "TOTAL": 0, "CODE": "#SCOREBOARD_LOGGING" }, 			# Logging
							"G": { "TOTAL": 0, "CODE": "#SCOREBOARD_GRACEFULLY_FINISHING" },# Gracefully finishing
							"I": { "TOTAL": 0, "CODE": "#SCOREBOARD_IDLE_WORKER_CLEANUP" }, # Idle cleanup of worker
							".": { "TOTAL": 0, "CODE": "#SCOREBOARD_OPEN_SLOT" }  			# Open slot with no current process
						}
		# Conta quantos caracteres tem no SCOREBOARD
		if (chave == "#SCOREBOARD"):
			contador = dict(collections.Counter(valor))
			valor = len(valor)
			criarJson.append({chave: valor})
			
			for av in apache_values:
				for c in contador:
					# print c
					if c == av:
						apache_values[av].update({"TOTAL": contador[c]})
				# print apache_values[av]
				criarJson.append({ apache_values[av]["CODE"]: apache_values[av]["TOTAL"]} )
		# Gera e adiciona na variavel os valores	
		final = {chave: valor}
		criarJson.append(final)
	# print "{ \"data\": "
	# print json.dumps(criarJson)
	# print "}"
except Exception as e:
	print e

print criarJson
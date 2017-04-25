# zabbix-server-status
Script python and template for Zabbix server-status

Python Pre-reqs:

requests

json

argparse


On Python 2.6:

backport_collections

On Python 2.7:

collections

Comment the lines with backport_collections and uncoment collections, depends on your Python version

QUICK USE:

Import template to Zabbix (tested on 3.2 only)

Copy apache-server-status.conf to /etc/zabbix/ or wherever your zabbix-agente gets external UserParameter config files

Copy GetApacheStatus.py to /etc/zabbix/scripts/

Reload Zabbix Agent

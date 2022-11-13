#! /usr/bin/env python3
path = r'/home/bitrix/cp_2022_06'
import os,datetime
last_create = datetime.datetime.strptime('13.11.2022 8:50', '%d.%m.%Y %H:%M')

def test_time_create(path_x):
		global last_time
		time_create_isch = os.path.getmtime(path_x)
		time_create = datetime.datetime.fromtimestamp(time_create_isch)
		if time_create > last_create:
			return True
		else:
			return False


def walk(path):
	for p,d,l in os.walk(path):
		if not os.path.islink(p):
			if test_time_create(p):
				print(p)

walk(path)
#!/usr/bin/python 
#    get_shell_cmd_stats.py 
#    script to get the statistics on the most used commands by a certain user
#    Copyright (C) 2011  Satish Eerpini
#
#    This program is free software; you can redistribute it and/or modify
#    it under the terms of the GNU General Public License as published by
#    the Free Software Foundation; either version 2 of the License, or
#    (at your option) any later version.
#
#    This program is distributed in the hope that it will be useful,
#    but WITHOUT ANY WARRANTY; without even the implied warranty of
#    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#    GNU General Public License for more details.
#
#    You should have received a copy of the GNU General Public License along
#    with this program; if not, write to the Free Software Foundation, Inc.,
#    51 Franklin Street, Fifth Floor, Boston, MA 02110-1301 USA.
import os


fh = file(os.getenv("HOME")+"/.bash_history", "r")
stat_dict = {}

for line in fh:
	command = line.strip().split()[0]
#	print command
	if stat_dict.has_key(command):
		stat_dict[command] = stat_dict[command]+1
	else:
		stat_dict[command] = 1

items = [(v,k) for k, v in stat_dict.items()]
items.sort()
items.reverse()
items = [(k,v) for v,k in items]

for k,v in items:
	if(v>5):
		print k+" ==> "+str(v)


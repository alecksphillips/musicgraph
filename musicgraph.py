#!/usr/bin/env python
#
# music graph
# Copyright (C) 2014  Alex Phillips
#

#########################
# GPL Information
#########################
#
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# See <http://www.gnu.org/licenses/> for more information
#
#########################


__author__ = 'Alex Phillips (alecks.phillips@gmail.com)'
__version__ = '$ 16 June 2014 $'
__date__ = '$ Date: 2014/06/16 $'
__copyright__ = 'Copyright (c) 2014 Alex Phillips'
__license__ = 'GPL'

#Key for last.fm api - change to your own personal key
api_key='8cf8b8f0778a606621666c2152df79db'

try:
    from urllib.request import urlopen
except ImportError:
    from urllib2 import urlopen
from xml.dom import minidom
import os.path
import sys
from getopt import getopt
from graphviz import Digraph

def getData(username,number):
    #Get users top artists
    
    url="
    
    
    
def download(url,filename)

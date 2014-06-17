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
try:
    from urllib.parse import urlquote as quote
except ImportError:
    from urllib import quote
from xml.dom import minidom
import os.path
import sys
import time
from getopt import getopt
import pydot

def makeGraph(username,number,cache,Local):
    #Get users top artists
    
    # make cache if doesn't exist
    if not os.path.exists(cache):
        print("cache directory ("+cache+") doesn't exist. I'm creating it.")
        os.mkdir(cache)
        os.mkdir(cache+os.sep+'similar')
        
    url=('http://ws.audioscrobbler.com/2.0/?method=user.gettopartists&user='+username+
         '&api_key='+api_key+'&limit=20')
        
        
    # Make a local copy of the charts
    local_copy = cache+os.sep+'charts_'+username+'.xml'
    if Local=='no' or (Local=='yes' and not os.path.isfile(local_copy)):
        try:
            print("Downloading from ",url)
            download(url, local_copy)
        except Exception as err:
            print("#"*20)
            print("I couldn't download the profile or make a local copy of it.")
            print("#"*20)
    else:
        print("Reading from local copy:  ",local_copy)
        
    print("Parsing list of top artists...")
    
    try:
        data=open(local_copy,'rb')
        xmldoc=minidom.parse(data)
        data.close()

    except Exception as err:
        print('#'*20)
        print("Error while parsing your profile. Your username might be "
              "misspelt or your charts empty.")
        print('#'*20)
        sys.exit()

    artistlist=[]
    for item in xmldoc.getElementsByTagName('artist'):
        artist = item.getElementsByTagName('name')[0].firstChild
        if artist is not None:
            artistlist.append(artist.nodeValue)

    # Stop if charts are empty
    if len(artistlist)==0:
        print('#'*20)
        print("Your charts are empty. I can't proceed.")
        print('#'*20)
        sys.exit()

    #Create graph with artists as nodes and create edges between similar artists
    #graph = pydot.Graph('graphname', graph_type='graph')
    
    time.sleep(2)
    
    for artist in artistlist[:]:
        
        getSimilar(artist.encode('utf8').replace(' ','%20').replace('/','%2F'),cache)
        #graph.add_node(pydot.Node(artist))
    
    #edgelist=[]
    output = open('test.dot','a')
    #Edges
    for artist in artistlist[:]:
        try:
            data=open(cache + os.sep + 'similar' + os.sep + artist.encode('utf8').replace(' ','%20').replace('/','%2F') + '.xml','rb')
            xmldoc=minidom.parse(data)
            data.close()
        except Exception as err:
            print('#'*20)
            print("Error while parsing your profile. Your username might be "
              "misspelt or your charts empty.")
            print('#'*20)
            sys.exit()
            
        simlist=[]
        
        for item in xmldoc.getElementsByTagName('artist'):
            sim = item.getElementsByTagName('name')[0].firstChild
            if sim is not None:
                simlist.append(sim.nodeValue)
        
        
        for sim in simlist[:]:
            if sim in artistlist:
                t = artist, sim
                output.write(artist.encode('utf8').replace('/','').replace('\'','').replace(' ','').replace('?','').replace('!','') + ' -> ' + sim.encode('utf8').replace('/','').replace('\'','').replace(' ','').replace('?','').replace('!','') + '\n')
                #edgelist.append(t)
            
    #output = pydot.Dot(pydot.graph_from_edges(edgelist))
    #output.write('out.dot', prog='none', format='raw')

        
    
    
    
    
    
    
def getSimilar(artist,cache):
    filename = (cache + os.sep + 'similar' + os.sep + artist + '.xml')
    if not os.path.exists(filename):
        url = ('http://ws.audioscrobbler.com/2.0/?method=artist.getsimilar&artist=' + artist + '&api_key=' + api_key)
        #url = quote(url)
        download(url, filename)
        time.sleep(1)
    
def download(url,filename):
    """ download the binary file at url """
    print("Downloading:  " + url)
    instream=urlopen(url)
    outfile=open(filename,'wb')
    for chunk in instream:
        outfile.write(chunk)
    instream.close()
    outfile.close()
    
    
########################
## main
########################
def main():
    makeGraph('alecksphillips',20,'cache','yes')

if __name__=="__main__":
    main()

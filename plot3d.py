#!/usr/bin/env python
#writing by Clement Hottier 
#script in order to plot fast some data file


import argparse
import sys
import os
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
import numpy as np


#--------------#
#User interface#
#--------------#
parser = argparse.ArgumentParser(description=''' Script in order to plot two column from a data file ''')

parser.add_argument('-f',action='store',type=str,default=None,
    help='File which you want to plot')

parser.add_argument('--type',action='store',type=str,default='line',
    help='precise the type of plot you want : line | scatter, default line')

parser.add_argument('-c',action='store',type=int,nargs=3,default=[0,1,2],
    help='column you want to plot (begin at 0), first for x axes and second for yaxes, default : 0 1')

parser.add_argument('-d',action='store',type=str,default=None,
        help='delimiter of column in the file. by default this is any whitespace')

parser.add_argument('--xlim',action='store',type=float,nargs=2,default=None,
    help='X bound of the plot, default : matplotlib auto')

parser.add_argument('--ylim',action='store',type=float,nargs=2,default=None,
    help='Y bound of the plot, default : matplotlib auto')

parser.add_argument('--zlim',action='store',type=float,nargs=2,default=None,
    help='Z bound of the plot, default : matplotlib auto')

parser.add_argument('--xlabel',action='store',type=str,default=None,
    help='label of x axes, default None')

parser.add_argument('--ylabel',action='store',type=str,default=None,
    help='label of y ayes, default None')

parser.add_argument('--zlabel',action='store',type=str,default=None,
    help='label of z azes, default None')

parser.add_argument('--title',action='store',type=str,default=None,
    help='add a title on top of the plot, Default None')

parser.add_argument('--save',action='store',type=str,default=None,
    help='if you prefer to save the plot instead of display it use "--save name_of_file.pdf"')

args=parser.parse_args()
#--------------#

#-----------------#
#Checking argument#
#-----------------#
if args.f==None :
  sys.exit('Error : no input file')

if (not os.path.isfile(args.f)) :
  sys.exit('Error : file '+args.f+' not found')

type_list = ['line','scatter']
if (not args.type in type_list) :
  sys.exit('Error : type '+args.type+' not recognize')
#-----------------#

#-----------------#
#Cheking delimiter#
#-----------------#
#if the data file has .csv extension, the separator is automaticaly set by ','
#-----------------#
if (args.d != None) :
    delim=args.d
else :
    if ('.csv' in args.f):
        delim=','
    else :
        delim=None
#-----------------#

#------------#
#Reading data#
#------------#
data=np.genfromtxt(args.f,usecols=tuple(args.c),delimiter=delim)
#------------#

#---------#
#Plot data#
#---------#
fig=plt.figure()
ax=fig.add_subplot(111,projection='3d')
if (args.type == 'line') :
  ax.plot(data[:,0],data[:,1],data[:,2])
elif (args.type == 'scatter') :
  ax.scatter(data[:,0],data[:,1],data[:,2])


if(args.xlim != None) :
  ax.set_xlim(args.xlim)
if(args.ylim != None) :
  ax.set_ylim(args.ylim)
if(args.zlim != None) :
  ax.set_zlim(args.zlim)

if(args.xlabel != None) :
  ax.set_xlabel(args.xlabel)
if(args.ylabel != None) :
  ax.set_ylabel(args.ylabel)
if(args.zlabel != None) :
  ax.set_zlabel(args.zlabel)

#title
if(args.title != None):
  fig.suptitle(args.title)

#save
if (args.save != None) :
  fig.savefig(args.save)
else :
  plt.show()
#---------#

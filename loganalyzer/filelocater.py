#!/usr/bin/env python3.7
# -*- coding: utf-8 -*-
"""
Created on Wed Aug  5 21:10:14 2020

@author: wazhen
"""
import os
import datetime
import operator
from fnmatch import fnmatch
import prehandle


class FindFile(prehandle.ParaValid):
    """
    gt:greater than
    lt:less than
    tp:time point
	comp: compare
	fname: file name regex
    """
    _fields=["tp","path", "comp", "fname"]
    opt={"gt": operator.__gt__,
     "lt": operator.__lt__,
    "add": operator.__add__,
    "sub": operator.__sub__
 }

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
            
    def path_walker(self):
        try:
            walker = os.walk(self.path)
            while True:
                pth,dirs,fs=walker.__next__()
                yield os.path.join(self.path,pth)
        except StopIteration:
                pass


    def file_filter(self, fileter_func=None, *args):
        self.fileter_func=getattr(self, fileter_func)
        for dirs in self.path_walker():
            for file in os.listdir(dirs):
                fullpath=os.path.join(dirs,file)
                if os.path.isfile(fullpath):
                   yield self.fileter_func(fullpath)

    def by_mod_time(self, fullpath):
        mtime = datetime.datetime.fromtimestamp(os.path.getmtime(fullpath))
        if self.opt[self.comp](mtime, self.tp):
            return fullpath

    def by_name(self, fullpath):
        if fnmatch(fullpath, self.fname):
            return fullpath
                
                
# -*- coding: utf-8 -*-
"""
Created on Wed Aug  2 17:03:11 2020

@author: wazhen
"""

import re
import prehandle
import os

p=os.path.dirname(os.path.abspath(__file__))+'\keywords.txt'

class Xlook(prehandle.ParaValid):
    _fields=["kwords","lookw", "pat"]
    def __init__(self, flags=0, **kwargs):
        super().__init__(**kwargs)
        with open(p) as keywords:
            kl=[]
            for kw in keywords.readlines():
                kl.append(kw.rstrip('\n'))
            self.kwords=("|").join((map(re.escape,kl)))
            
    def do_match(self, content):
        pd={"lookahead":r'{}(?={})'.format(self.lookw,self.kwords),
            "lookbehind":r'(?<={}){}'.format(self.kwords, self.lookw), 
            "match":r'{}'.format(self.kwords)}
        pattern=re.compile(pd[self.pat])
        results=pattern.findall(content)
        return results

x=Xlook()
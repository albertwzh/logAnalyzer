"""
Created on Wed Aug  2 16:13:10 2020

@author: wazhen
"""
class ParaValid():
    def __init__(self, **kwargs):
        for name in list(kwargs):
            if name not in self._fields:
                raise TypeError('Invalid argument(s): {}'.format(name))
            setattr(self, name, kwargs.pop(name))
        if kwargs:
            raise TypeError('Duplicate values {}'.format(name))
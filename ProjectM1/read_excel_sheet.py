#!/usr/bin/env python3

"""
Simple Excel read utility.
This module will read an excel sheet provided.
Based on the requirement we can get the details.
"""

__version__ = "0.1"
__all__ = ["BBB23"]
__author__ = "kunaljha5"
__home_page__ = "I need to buy one."


import xlrd
import os
import glob


class BBB23:
    """
    I think there should be input in the means of
    :argument - Path + Filename + Action
    :return -  Return Value based on action.
    """
    def __init__(self, path, filename):
        self.full_path = str(path) + str(filename)
        if not glob.glob(full_path):
            raise ValueError("Either Path or Filename is missing '{}'".format(full_path))
        if not os.chdir(path):
            raise ValueError("Path '{}' does not exists".format(path))
        if not os.path.isfile(filename):
            raise ValueError("File '{}' does not exists".format(filename))
        self.filename = filename
        self.path = path
        self.wb = xlrd.open_workbook(self.full_path)
        self.sheet = self.wb.sheet_by_index(0)
        self._ncolumns = self.sheet.ncols
        self._nrows = self.sheet.nrows

        print(self._ncolumns)
        print(self._nrows)


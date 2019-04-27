
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
        """ Creating Full path with filename and path"""
        self.filename = filename
        self.path = path
        self.full_path = str(self.path) + '\\' + str(self.filename)
        """Checking filename and path provided are valid or not"""
        # # if not glob.glob(self.full_path):
        # #     raise ValueError("Either Path or Filename is missing '{}'".format(self.full_path))
        # if not os.chdir(self.path):
        #     raise ValueError("Path '{}' does not exists".format(self.path))
        if not os.path.isfile(self.full_path):
            raise ValueError("File '{}' does not exists".format(self.full_path))

        """ This init function will define few basic outputs like
        nc = number of columns
        nr = number of rows
        """
        self.wb = xlrd.open_workbook(self.full_path)
        self.sheet = self.wb.sheet_by_index(0)
        self.nc = self.sheet.ncols
        self.nr = self.sheet.nrows


    def first_row_value(self, default_col=0):
        """
        This function will return first row values
        :param default_col:  if no column values is sent then column value will be 0
        :return: returns the first row and x column values.
        """
        self.rowv = []
        for i in range(self.sheet.ncols):
             self.rowv.append(self.sheet.cell_value(default_col,i))
        return self.rowv

    def first_col_value(self, default_row=0 ):
        """
        This function will return first column value
        :param default_row:  if no row value provided it will use 0 as row value by default.
        :return: return the first column and x row values.
        """
        self.colv = []
        for i in range(self.sheet.ncols):
             self.colv.append(self.sheet.cell_value(i,default_row))
        return self.colv

    def search_rows(self, pattern):
        """
        This function search for the string and pattern end user have shared. if its matches to any cell vales. row value will be returned.
        :param pattern: can be any string or integer.
        :return:  return the row number
        """
        for i in range(self.nr):
            for j in range(self.nc):
                if pattern ==  self.sheet.cell_value(i,j):
                    return i


student = BBB23("D:\\Testing", 'Students_Details.xls')
print(student.first_row_value())
print(student.first_row_value(student.search_rows("Vanya Jha")))

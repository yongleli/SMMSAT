#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Jul 17 09:54:59 2018

@author: bruce
"""

class Application(object):
    def __init__(self,System):
        System.build_TimeList()
        System.check_TimeScheme()
        System.build_DataFrameIndex()
        System.build_TimeGapList()
        System.check_SpeciesSetting()
        System.check_TrjFormat()
        self.System=System
        self.AnalysisGroup=[]
    
    def add(self,analysis):
        self.AnalysisGroup.append(analysis)

    def remove(self,analysis):
        self.Analysisgroup.remove(analysis)

    def run(self):
        for analysisii in range(self.AnalysisGroup.__len__()):
            self.AnalysisGroup[analysisii].excute()
    

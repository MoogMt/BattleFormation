#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Dec 12 17:57:07 2020

@author: moogmt
"""


import simpleAgent

class simpleGame:
    
    agents = np.empty(0, dtype=simpleAgent)
    board = np.zeros( (1,1), dtype=float )
    status = "not_started"

    def play_turn( self ):
        return

    def run( self ):
        while( not game.status ):
            self.play_turn()
        return 
    
    
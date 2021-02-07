#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Dec 12 16:36:11 2020

@author: moogmt
"""

import numpy as np

class simpleAgent:
    
    " Internal Variables "
    "--------------------------------------"
    position = np.zeros( (3), dtype=float )
    max_scan_radius = 5.0
    sigma_score     = 1.0
    score           = 0.0
    "-------------------------------------"
    
    "------------------------------------"
    def getPosition( self ):
        return self.position
    def getScore( self ):
        return self.score
    def getMaxScanRadius( self ):
        return self.max_scan_radius
    def getSigmaScore( self ):
        return self.getSigmaScore
    "------------------------------------"
    
    "------------------------------------"
    def scanNeighbors(self, agents ):
        dist = []
        dist_coor = []
        for agent in agents:
            diff = self.getPosition() - agent.getPosition() 
            distance = np.sum( diff ) 
            if distance < self.getMaxScanRadius() :
                dist = np.append( dist, distance )
                dist_coor = np.append( dist_coor, diff )
        return dist, dist_coor
    def computeScoreDistances( distances, alpha ) : 
        return np.sum( np.exp( -alpha*distances  ) )
    "------------------------------------"
    
    "------------------------------------------"
    def setPosition( self, new_position ):
        self.position = new_position
        return
    def setScore( self, new_score ):
        self.score = new_score
        return 
    def setMaxScanRadius( self, new_max_scan_radius ):
        self.max_scan_radius_ = new_max_scan_radius
        return 
    def setSigmaScore( self, new_sigma_score ):
        self.sigma_score = new_sigma_score
    "------------------------------------------"
    
    
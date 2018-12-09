#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Jesus Maximino Hernandez
CS 2302 Data Structures - Diego Aguirre
TA - Manoj Saha
Lab 7 - Option A 

Program intended to implemet edit distance algorithm 
            
"""
import numpy as np

class editDistance:

    
    def edit(s1, s2):
    """
    Runs the edit distance algorithm and prints the 2D array
    Takes two strings
    Returns the amount of steps to edit the strings
    """
        word_matrix = [[0 for r in range(len(s2)+1)] for c in range(len(s1)+1)]
        
        for i in range(len(s1)+1):
            for j in range(len(s2)+1):
                if (i == 0):
                    word_matrix[i][j] = j
                elif (j == 0):
                    word_matrix[i][j] = i
                elif (s1[i-1] == s2[j-1]):
                    word_matrix[i][j] = word_matrix[i-1][j-1];
                else:
                    word_matrix[i][j] = 1 + min(word_matrix[i][j-1],
                                                word_matrix[i-1][j],
                                                word_matrix[i-1][j-1])
        print("\nMatrix: \n", np.array(word_matrix))
        print("\nNumber of steps to complete distance: ", word_matrix[i][j])





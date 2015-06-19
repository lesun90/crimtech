#!/usr/bin/python

########################################################################
# Author: Duong Le
# Email: lesun90@gmail.com
# Solve the puzzle challenge
# Using A Star search algorithm
# key 21617e2726de4511bd7cc2c27c8d4939
########################################################################

import json
import requests
import Queue as Q
from copy import copy
from copy import deepcopy
import math
import time
import sys
import random

class Solver:
    API_KEY = '21617e2726de4511bd7cc2c27c8d4939'
    # CHANGE THIS VALUE
    # The environment, either 'trial' for practicing and debugging, or 'contest'
    # for actual submissions that count.
    ENV = 'contest'
    BASE_URL = 'http://techchallenge.cimpress.com'

    # Retrieve a puzzle from the server. Returns JSON.
    def getPuzzle(self):
        url = '{0}/{1}/{2}/puzzle'.format(self.BASE_URL, self.API_KEY, self.ENV)
        return requests.get(url).text

    # BEGIN MY SOLUTION ALGORITHM !

    # Solve the puzzle using A Star algorithm
    def solveAstar(self, puzzle):
	solution = []
	h = s.numberOfPossibleSquares(puzzle)*1.1
	g = 0
	f = g + h
	startNode = {'f':f, 'puzzle': puzzle, 'solution': solution}
	frontier = Q.PriorityQueue()
        frontier.put(startNode,f)
    	while not frontier.empty():
	    # Get the node with lowest f score also remove it from queue
	    currentNode = copy(frontier.get())
	    # Return solution if puzzle is finished
	    if (s.puzzleFinished(currentNode['puzzle']) == True):
		return currentNode['solution']
	    # Get the list of corners in current puzzle
	    cornerList = s.getCorner(currentNode['puzzle'])
	    # Generate child nodes
	    for childID in range(0,len(cornerList)):
	        dirRow = cornerList[childID]['dirRow']
	        dirCol = cornerList[childID]['dirCol']
		startRow = cornerList[childID]['row']
		startCol = cornerList[childID]['col']
		#
	        childNodePuzzle =  [row[:] for row in currentNode['puzzle']]
    	        childSol = []
		# Get the squares had to be removed to get this node
	        childSol.extend(currentNode['solution'])
	        childSol.append(s.makeLargestSquare(childNodePuzzle,startRow,startCol,dirRow,dirCol))
		# Find the nmber_future_squares, scale it by 1.1
		h = s.numberOfPossibleSquares(childNodePuzzle)*1.1
		g = len(childSol)
		f = g + h
	        childNode = {'f':f, 'puzzle': childNodePuzzle, 'solution': childSol}
		# Add child node to queue
	        frontier.put(childNode,f)

    # Find the estimate minimun number of squares that can fit into the puzzle
    # Return the estimate minimun number of squares that can fit into the puzzle
    # This function alone can be modified to find the puzzle solution, 
    # however, it is does not give the best solution for the puzzle.
    # For each kind of corner (8 kind of corners), remove the largest square from 
    # that corner, count the number of square has been removed, repeat until 
    # the grid is empty, or the number of square is greater than the minNumberOfSquare

    def numberOfPossibleSquares(self,puzzle):	
	minNumberOfSquare = puzzleWidth * puzzleHeight
	# clone puzzle
	puzzle1 = [row[:] for row in puzzle]
	puzzle2 = [row[:] for row in puzzle]
	puzzle3 = [row[:] for row in puzzle]
	puzzle4 = [row[:] for row in puzzle]
	puzzle5 = [row[:] for row in puzzle]
	puzzle6 = [row[:] for row in puzzle]
	puzzle7 = [row[:] for row in puzzle]
	puzzle8 = [row[:] for row in puzzle]
	#corner 1:
	count = 0
	row = 0
	col = 0
	dirRow = 1
	dirCol = 1
	while (row < puzzleHeight) and (count < minNumberOfSquare):
	    col = 0
	    while (col < puzzleWidth) and (count < minNumberOfSquare):
		if puzzle1[row][col]:
		    square = s.makeLargestSquare(puzzle1,row,col,dirRow,dirCol)
		    count += 1
		    col += square['Size'] * dirCol
		else:
		    col += dirCol
	    row += dirRow
	minNumberOfSquare = count
	#print'case 1: {0}'.format(minNumberOfSquare)

	#corner 2:
	count = 0
	row = 0
	col = 0
	dirRow = 1
	dirCol = 1
	while (col < puzzleWidth) and (count < minNumberOfSquare):
	    row = 0
	    while (row < puzzleHeight) and (count < minNumberOfSquare):
		if puzzle2[row][col]:
		    square = s.makeLargestSquare(puzzle2,row,col,dirRow,dirCol)
		    count += 1
		    row += square['Size'] * dirRow
		else:
		    row += dirRow
	    col += dirCol
	minNumberOfSquare = count
	#print'case 2: {0}'.format(minNumberOfSquare)

	#corner 3: 
	count = 0
	row = 0
	col = puzzleWidth - 1
	dirRow = 1
	dirCol = -1
	while (row < puzzleHeight) and (count < minNumberOfSquare):
	    col = puzzleWidth - 1
	    while (col >= 0) and (count < minNumberOfSquare):
		if puzzle3[row][col]:
		    square = s.makeLargestSquare(puzzle3,row,col,dirRow,dirCol)
		    count += 1
		    col += square['Size'] * dirCol
		else:
		    col += dirCol
	    row += dirRow
	minNumberOfSquare = count
	#print'case 3: {0}'.format(minNumberOfSquare)

        #corner 4:
	count = 0
	row = 0
	col = puzzleWidth - 1
	dirRow = 1
	dirCol = -1
	while (col >= 0) and (count < minNumberOfSquare):
	    row = 0
	    while (row < puzzleHeight) and (count < minNumberOfSquare):
		if puzzle4[row][col]:
		    square = s.makeLargestSquare(puzzle4,row,col,dirRow,dirCol)
		    count += 1
		    row += square['Size'] * dirRow
		else:
		    row += dirRow
	    col += dirCol
	minNumberOfSquare = count
	#print'case 4: {0}'.format(minNumberOfSquare)

        #corner 5:
	count = 0
	row = puzzleHeight - 1 
	col = 0
	dirRow = -1
	dirCol = 1
	while (row >= 0) and (count < minNumberOfSquare):
	    col = 0
	    while (col < puzzleWidth) and (count < minNumberOfSquare):
		if puzzle5[row][col]:
		    square = s.makeLargestSquare(puzzle5,row,col,dirRow,dirCol)
		    count += 1
		    col += square['Size'] * dirCol
		else:
		    col += dirCol
	    row += dirRow
	minNumberOfSquare = count
	#print'case 5: {0}'.format(minNumberOfSquare)

        #corner 6:
	count = 0
	row = puzzleHeight - 1 
	col = 0
	dirRow = -1
	dirCol = 1
	while (col < puzzleWidth) and (count < minNumberOfSquare):
	    row = puzzleHeight - 1
	    while (row >= 0) and (count < minNumberOfSquare):
		if puzzle6[row][col]:
		    square = s.makeLargestSquare(puzzle6,row,col,dirRow,dirCol)
		    count += 1
		    row += square['Size'] * dirRow
		else:
		    row += dirRow
	    col += dirCol
	minNumberOfSquare = count
	#print'case 6: {0}'.format(minNumberOfSquare)

        #corner 7:
	count = 0
	row = puzzleHeight -1
	col = puzzleWidth - 1
	dirRow = -1
	dirCol = -1
	while (row >= 0) and (count < minNumberOfSquare):
	    col = puzzleWidth - 1
	    while (col >= 0) and (count < minNumberOfSquare):
		if puzzle7[row][col]:
		    square = s.makeLargestSquare(puzzle7,row,col,dirRow,dirCol)
		    count += 1
		    col += square['Size'] * dirCol
		else:
		    col += dirCol
	    row += dirRow
	minNumberOfSquare = count
	#print'case 7: {0}'.format(minNumberOfSquare)

        #corner 8:
	count = 0
	row = puzzleHeight -1
	col = puzzleWidth - 1
	dirRow = -1
	dirCol = -1
	while (col >= 0) and (count < minNumberOfSquare):
	    row = puzzleHeight -1
	    while (row >= 0) and (count < minNumberOfSquare):
		if puzzle8[row][col]:
		    square = s.makeLargestSquare(puzzle8,row,col,dirRow,dirCol)
		    count += 1
		    row += square['Size'] * dirRow
		else:
		    row += dirRow
	    col += dirCol
	minNumberOfSquare = count
	#print'case 8: {0}'.format(minNumberOfSquare)
	return minNumberOfSquare

    # Make the largest square starts at a position (startRow, startCol) 
    # with expansion direction (dirRow, dirCol)
    # Also remove that square in puzzle
    # Return the info of the largest square
    def makeLargestSquare(self,puzzle, startRow, startCol, dirRow, dirCol):
	size = 1
	endRow = startRow
	endCol = startCol
	hasHole = False
	while hasHole == False:
	    endRow += dirRow
	    endCol += dirCol
	    if endRow == puzzleHeight or endRow < 0 or endCol == puzzleWidth or endCol < 0:
		endRow -= dirRow
		endCol -= dirCol
		break
	    if puzzle[endRow][endCol] and s.checkRow(puzzle,endRow,startCol,endCol) and s.checkCol(puzzle,endCol,startRow,endRow):
		size += 1
	    else:
		hasHole = True
	#
	X = startCol
	Y = startRow
	if dirCol == -1:
	    X = X - size + 1
	if dirRow == -1:
	    Y = Y - size + 1
	# Delete the square in puzzle
	for row in range(Y,Y + size):
	    for col in range(X,X + size):
		puzzle[row][col] = False
	# Return square info
	return ({'X': X, 'Y': Y, 'Size': size})

    # Get corners of puzzle
    # There are possible of 8 corners
    # corner0 is top left, check row first
    # corner1 is top left, check col first
    # corner2 is top right, check row first
    # corner3 is top right, check col first
    # corner4 is bottom left, check row first
    # corner5 is bottom left, check col first
    # corner6 is bottom right, check row first
    # corner7 is bottom right, check col first
    # corner0 and corner 1 can be the same, similarly for corner2 and corner3, 4 and 5, 6 and 7
    # return list of corners coordinate and the direction of expansion from that corner
    def getCorner(self,puzzle):
	corner0Found = False
	corner1Found = False
	corner2Found = False
	corner3Found = False
	corner4Found = False
	corner5Found = False
	corner6Found = False
	corner7Found = False
	# Init array of corner
	corner = [0] * 8
        cornerWithDir = []
	# Find corner 0 and 2
	row = 0
	while (row < puzzleHeight) and (corner0Found) == False and (corner2Found == False):
	    col = 0
	    while (col < puzzleWidth) and (corner0Found) == False:
		if puzzle[row][col]:
		    corner0Found = True
		    corner[0] = (row,col)
		    cornerWithDir.append({'row': row, 'col': col, 'dirRow': 1, 'dirCol': 1 })
		col +=1
	    col = puzzleWidth - 1
	    while (col >= 0) and (corner2Found) == False:
		if puzzle[row][col]:
		    corner2Found = True
		    corner[2] = (row,col)
		    cornerWithDir.append({'row': row, 'col': col, 'dirRow': 1, 'dirCol': -1})
		col -=1
	    row += 1
	# Find corner 4 and 6
	row = puzzleHeight -1
	while (row >= 0) and (corner4Found) == False and (corner6Found == False):
	    col = 0
	    while (col < puzzleWidth) and (corner4Found) == False:
		if puzzle[row][col]:
		    corner4Found = True
		    corner[4] = (row,col)
		    cornerWithDir.append({'row': row, 'col': col, 'dirRow': -1, 'dirCol': 1 })
		col +=1
	    col = puzzleWidth - 1
	    while (col >= 0) and (corner6Found) == False:
		if puzzle[row][col]:
		    corner6Found = True
		    corner[6] = (row,col)
		    cornerWithDir.append({'row': row, 'col': col, 'dirRow': -1, 'dirCol': -1})
		col -=1
	    row -= 1
	# Find corner 1 and 5
	col = 0
	while (col < puzzleWidth) and (corner1Found) == False and (corner5Found == False):
	    row = 0
	    while (row < puzzleHeight) and (corner1Found) == False:
		if puzzle[row][col]:
		    corner1Found = True
		    corner[1] = (row,col)
		    if (corner[1] != corner[0]):
			cornerWithDir.append({'row': row, 'col': col, 'dirRow': 1, 'dirCol': 1})
		row +=1
	    row = puzzleHeight - 1
	    while (row >= 0) and (corner5Found) == False:
		if puzzle[row][col]:
		    corner5Found = True
		    corner[5] = (row,col)
		    if (corner[5] != corner[4]):
		        cornerWithDir.append({'row': row, 'col': col, 'dirRow': -1, 'dirCol': 1 })
		row -=1
	    col += 1
	# Find corner 3 and 7
	col = puzzleWidth - 1
	while (col >= 0) and (corner3Found) == False and (corner7Found == False):
	    row = 0
	    while (row < puzzleHeight) and (corner3Found) == False:
		if puzzle[row][col]:
		    corner3Found = True
		    corner[3] = (row,col)
		    if (corner[3] != corner[2]):
		        cornerWithDir.append({'row': row, 'col': col, 'dirRow': 1, 'dirCol': -1 })
		row +=1
	    row = puzzleHeight - 1
	    while (row >= 0) and (corner7Found) == False:
		if puzzle[row][col]:
		    corner7Found = True
		    corner[7] = (row,col)
		    if (corner[7] != corner[6]):
		        cornerWithDir.append({'row': row, 'col': col, 'dirRow': -1, 'dirCol': -1 })
		row -=1
	    col -= 1
	return cornerWithDir

    #function to check if a succesive row from startCol to endCol
    def checkRow(self,puzzle, row, startCol, endCol):
	if startCol < endCol:
	    incre = 1
	else:
	    incre = -1
        for col in range(startCol, endCol, incre):
	    if puzzle[row][col] == False:
		return False
	return True

    #function to check if a succesive col from startRow to endRow
    def checkCol(self,puzzle, col, startRow, endRow):
	if startRow < endRow:
	    incre = 1
	else:
	    incre = -1
        for row in range(startRow, endRow, incre):
	    if puzzle[row][col] == False:
		return False
	return True

    #check if puzzle is finish
    def puzzleFinished(self, puzzle):
        for row in range(0, puzzleHeight):
            for col in range(0, puzzleWidth):
                if puzzle[row][col]:
                    return False
        return True
    # END MY ALGORITHM!!
    # Here is a naive solution that just covers each grid cell with a square of size 1.
    # Returns an array of arrays for convenient conversion to JSON.
    def solve(self, puzzle):
        solution = []
        for row in range(0, puzzle['height']):
            for col in range(0, puzzle['width']):
                if puzzle['puzzle'][row][col]:
                    solution.append({'X': col, 'Y': row, 'Size': 1})
        return solution

    # Submit the solution. Returns JSON results.
    def submitSolution(self, id, squares):
        url = '{0}/{1}/{2}/solution'.format(self.BASE_URL, self.API_KEY, self.ENV)
        solution = {'id': id, 'squares': squares}
        return requests.post(url, data=json.dumps(solution)).text

puzzleWidth = 0
puzzleHeight = 0
# Main program
#print 'Using API key: {0}'.format(Solver.API_KEY)
s = Solver()
#start = time.time()
# Get a puzzle, and convert the returned JSON to a Python dictionary
jsonResult = s.getPuzzle()
puzzle = json.loads(jsonResult)

# Demonstrate some of the returned values
#print 'You retrieved a puzzle with {0} width x {1} height and ID={2}'.format(
#    puzzle['width'],
#    puzzle['height'],
#    puzzle['id'])

puzzleWidth = puzzle['width']
puzzleHeight = puzzle['height']

#print 'Generating solution'

nPuzzle = [row[:] for row in puzzle['puzzle']]
squares = s.solveAstar(nPuzzle)

#end = time.time()
#print end - start
#print 'Submitting solution'
jsonResult = s.submitSolution(puzzle['id'], squares)

# Describe the response
response = json.loads(jsonResult);
if len(response['errors']) > 0:
	print 'Your solution failed with {0} problems and used {1} squares.'.format(
	       len(response['errors']),
	       response['numberOfSquares'])
else:
	print 'solution succeeded: {0} squares,score: {1},time penalty: {2}.'.format(
	       response['numberOfSquares'],
	       response['score'],
	       response['timePenalty'])

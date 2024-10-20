# -*- coding: utf-8 -*-
import copy


class GameStatus:


	def __init__(self, board_state, turn_O):

		self.board_state = board_state
		self.turn_O = turn_O
		self.oldScores = 0

		self.winner = ""


	def is_terminal(self):
		"""
        YOUR CODE HERE TO CHECK IF ANY CELL IS EMPTY WITH THE VALUE 0. IF THERE IS NO EMPTY
        THEN YOU SHOULD ALSO RETURN THE WINNER OF THE GAME BY CHECKING THE SCORES FOR EACH PLAYER 
    """
		for row in self.board_state:
			for square in row:
				if square == 0:
					return False
		return self.get_scores()
		

	# Removing terminal for now because im confused by that
	def get_scores(self): 
		"""
        YOUR CODE HERE TO CALCULATE THE SCORES. MAKE SURE YOU ADD THE SCORE FOR EACH PLAYER BY CHECKING 
        EACH TRIPLET IN THE BOARD IN EACH DIRECTION (HORIZONAL, VERTICAL, AND ANY DIAGONAL DIRECTION)
        
        YOU SHOULD THEN RETURN THE CALCULATED SCORE WHICH CAN BE POSITIVE (HUMAN PLAYER WINS),
        NEGATIVE (AI PLAYER WINS), OR 0 (DRAW)
        
        """        
		rows = len(self.board_state)
		cols = len(self.board_state[0])
		scores = 0
		# check_point = 3 if terminal else 2 

		# Check rows
		for row in range(rows):
			for col in range(cols - 2):
				if self.board_state[row][col] != 0 and \
				(self.board_state[row][col] == self.board_state[row][col + 1] == self.board_state[row][col + 2]): 
					if self.board_state[row][col] == 1:
						scores -= 1
					else:
						scores += 1
						

		# Check columns
		for row in range(rows - 2):
			for col in range(cols):
				if self.board_state[row][col] != 0 and \
				(self.board_state[row][col] == self.board_state[row + 1][col] == self.board_state[row + 2][col]): 
					if self.board_state[row][col] == 1:
						scores -= 1
					else:
						scores += 1
		
		# Check diagonals from the left
		for row in range(rows - 2):
			for col in range(cols - 2):
				if self.board_state[row][col] != 0 and \
				(self.board_state[row][col] == self.board_state[row + 1][col + 1] == self.board_state[row + 2][col + 2]): 
					if self.board_state[row][col] == 1:
						scores -= 1
					else:
						scores += 1
		
		# Reverse rows and check diagonals from the right side
		reversed_board_state = [list(reversed(row)) for row in self.board_state]
		for row in range(rows - 2):
			for col in range(cols - 2):
				if reversed_board_state[row][col] != 0 and \
				(reversed_board_state[row][col] == reversed_board_state[row + 1][col + 1] == reversed_board_state[row + 2][col + 2]): 
					if reversed_board_state[row][col] == 1:
						scores -= 1
					else:
						scores += 1

		return scores
		
	    

	def get_negamax_scores(self, terminal):
		"""
        YOUR CODE HERE TO CALCULATE NEGAMAX SCORES. THIS FUNCTION SHOULD EXACTLY BE THE SAME OF GET_SCORES UNLESS
        YOU SET THE SCORE FOR NEGAMX TO A VALUE THAT IS NOT AN INCREMENT OF 1 (E.G., YOU CAN DO SCORES = SCORES + 100 
                                                                               FOR HUMAN PLAYER INSTEAD OF 
                                                                               SCORES = SCORES + 1)
        """
		rows = len(self.board_state)
		cols = len(self.board_state[0])
		scores = 0
		check_point = 3 if terminal else 2
	    

	def get_moves(self):
		moves = []
		"""
        YOUR CODE HERE TO ADD ALL THE NON EMPTY CELLS TO MOVES VARIABLES AND RETURN IT TO BE USE BY YOUR
        MINIMAX OR NEGAMAX FUNCTIONS
        """
		for col in range(len(self.board_state)):
			for row in range(len(self.board_state[0])):
				if (self.board_state[col][row] == 0):
					moves.append([row, col])

		return moves


	def get_new_state(self, move):
		new_board_state = copy.deepcopy(self.board_state)
		x, y = move[0], move[1]
		new_board_state[y][x] = 1 if self.turn_O else -1
  
		return GameStatus(new_board_state, not self.turn_O)

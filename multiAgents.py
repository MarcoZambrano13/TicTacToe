from GameStatus_5120 import GameStatus


def minimax(game_state: GameStatus, depth: int, maximizingPlayer: bool, alpha=float('-inf'), beta=float('inf')):
	"""
		YOUR CODE HERE TO FIRST CHECK WHICH PLAYER HAS CALLED THIS FUNCTION (MAXIMIZING OR MINIMIZING PLAYER)
		YOU SHOULD THEN IMPLEMENT MINIMAX WITH ALPHA-BETA PRUNING AND RETURN THE FOLLOWING TWO ITEMS
		1. VALUE
		2. BEST_MOVE

		THE LINE TO RETURN THESE TWO IS COMMENTED BELOW WHICH YOU CAN USE
	"""
    
	# Check for terminal state (win, loss, or draw) or depth limit
	terminal = game_state.is_terminal()
	if (depth == 0) or terminal:
		# Return the evaluation score and no move, as the game is terminal
		return game_state.get_scores(), None
	
	# Check if maximizing or minimizing
	if (maximizingPlayer):
		best_move = float('-inf')

		# Maximizing agent
		for move in game_state.get_moves():
			new_game_state = game_state.get_new_state(move)
			value = minimax(new_game_state, depth + 1, False, alpha, beta)
			best_move = max(best_move, value)
			if best_move >= beta:
				return best_move
			alpha = max(alpha, best_move)
	else:
		best_move = float('inf')

		# Minimizing agent
		for move in game_state.get_moves():
			new_game_state = game_state.get_new_state(move)
			value = minimax(new_game_state, depth + 1, False, alpha, beta)
			best_move = min(best_move, value)
			if best_move <= alpha:
				return best_move
			beta = min(beta, best_move)
	      
	return value, best_move

def negamax(game_status: GameStatus, depth: int, turn_multiplier: int, alpha=float('-inf'), beta=float('inf')):
	terminal = game_status.is_terminal()
	if (depth==0) or (terminal):
		scores = game_status.get_negamax_scores(terminal)
		return scores, None

	"""
    YOUR CODE HERE TO CALL NEGAMAX FUNCTION. REMEMBER THE RETURN OF THE NEGAMAX SHOULD BE THE OPPOSITE OF THE CALLING
    PLAYER WHICH CAN BE DONE USING -NEGAMAX(). THE REST OF YOUR CODE SHOULD BE THE SAME AS MINIMAX FUNCTION.
    YOU ALSO DO NOT NEED TO TRACK WHICH PLAYER HAS CALLED THE FUNCTION AND SHOULD NOT CHECK IF THE CURRENT MOVE
    IS FOR MINIMAX PLAYER OR NEGAMAX PLAYER
    RETURN THE FOLLOWING TWO ITEMS
    1. VALUE
    2. BEST_MOVE
    
    THE LINE TO RETURN THESE TWO IS COMMENTED BELOW WHICH YOU CAN USE
    """
	for move in game_status.get_moves():
		value = -negamax(game_status.get_new_state(), depth + 1, True, alpha, beta)
		best_move = min(best_move, value)
		return value, best_move

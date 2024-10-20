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
	
	if maximizingPlayer:
		best_value = float('-inf')
		best_move = None
		moves = game_state.get_moves()
		for move in moves:
				# Simulate move and get new game state
				new_game_state = game_state.get_new_state(move)
				# Recursively call minimax on the new state with depth reduced and the minimizing player
				value, _ = minimax(new_game_state, depth - 1, False, alpha, beta)
				# Compare value to find the best one for maximizing player
				if value > best_value:
						best_value = value
						best_move = move
				# Update alpha and check for pruning
				alpha = max(alpha, best_value)
				if beta <= alpha:
						break
		return best_value, best_move

	else:
		best_value = float('inf')
		best_move = None
		moves = game_state.get_moves()
		for move in moves:
				# Simulate move and get new game state
				new_game_state = game_state.get_new_state(move)
				# Recursively call minimax on the new state with depth reduced and the maximizing player
				value, _ = minimax(new_game_state, depth - 1, True, alpha, beta)
				# Compare value to find the best one for minimizing player
				if value < best_value:
						best_value = value
						best_move = move
				# Update beta and check for pruning
				beta = min(beta, best_value)
				if beta <= alpha:
						break
		return best_value, best_move

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
"""
PLEASE READ THE COMMENTS BELOW AND THE HOMEWORK DESCRIPTION VERY CAREFULLY BEFORE YOU START CODING

 The file where you will need to create the GUI which should include (i) drawing the grid, (ii) call your Minimax/Negamax functions
 at each step of the game, (iii) allowing the controls on the GUI to be managed (e.g., setting board size, using 
                                                                                 Minimax or Negamax, and other options)
 In the example below, grid creation is supported using pygame which you can use. You are free to use any other 
 library to create better looking GUI with more control. In the __init__ function, GRID_SIZE (Line number 36) is the variable that
 sets the size of the grid. Once you have the Minimax code written in multiAgents.py file, it is recommended to test
 your algorithm (with alpha-beta pruning) on a 3x3 GRID_SIZE to see if the computer always tries for a draw and does 
 not let you win the game. Here is a video tutorial for using pygame to create grids http://youtu.be/mdTeqiWyFnc
 
 
 PLEASE CAREFULLY SEE THE PORTIONS OF THE CODE/FUNCTIONS WHERE IT INDICATES "YOUR CODE BELOW" TO COMPLETE THE SECTIONS
 
"""
import pygame
import pygame_gui
import numpy as np
from GameStatus_5120 import GameStatus
# from multiAgents import minimax, negamax
import sys, random

mode = "player_vs_ai" # default mode for playing the game (player vs AI)

class RandomBoardTicTacToe:
    def __init__(self, size = (600, 600)):

        self.size = self.width, self.height = size
        # Define some colors
        self.BLACK = (0, 0, 0)
        self.WHITE = (255, 255, 255)
        self.GREEN = (0, 255, 0)
        self.RED = (255, 0, 0)

        # Grid Size
        self.GRID_SIZE = 3
        self. OFFSET = 5

        self.CIRCLE_COLOR = (140, 146, 172)
        self.CROSS_COLOR = (140, 146, 172)

        # This sets the WIDTH and HEIGHT of each grid location
        self.WIDTH = self.size[0]/self.GRID_SIZE - self.OFFSET
        self.HEIGHT = self.size[1]/self.GRID_SIZE - self.OFFSET

        # This sets the margin between each cell
        self.MARGIN = 5

        # Initialize pygame
        pygame.init()
        self.game_reset()

    # Draw game menu, set variables
    def draw_menu(self):
        manager = pygame_gui.UIManager(self.size, enable_live_theme_updates=True)

        started = False
        turn_O = False
        mode = "player_vs_ai"
        algorithm = "Negamax"
        grid = "3x3"
        
        # Draw the grid
        board_state = [
            [0, 0, 0],
            [0, 0, 0],
            [0, 0, 0]
        ]

        # Create GUI buttons
        nought_button = pygame_gui.elements.UIButton(
            relative_rect=pygame.Rect((0, 0), (100, 50)),
            text='Nought (O)',
            manager=manager
        )

        cross_button = pygame_gui.elements.UIButton(
            relative_rect=pygame.Rect((100, 0), (100, 50)),
            text='Cross (x)',
            manager=manager
        )

        opponent_dropdown = pygame_gui.elements.UIDropDownMenu(
            object_id="human-v-human-dropdown",
            options_list=["Human vs Human", "Human vs AI"],
            starting_option='Human vs Human',
            relative_rect=pygame.Rect((200, 0), (200, 50)),
            manager=manager
        )
        
        algo_dropdown = pygame_gui.elements.UIDropDownMenu(
            object_id="algo-dropdown",
            options_list=["Negamax", "Minimax"],
            starting_option='Negamax',
            relative_rect=pygame.Rect((400, 0), (200, 50)),
            manager=manager
        )
        
        grid_dropdown = pygame_gui.elements.UIDropDownMenu(
            object_id="grid-dropdown",
            options_list=["3x3", "4x4", "5x5"],
            starting_option='3x3',
            relative_rect=pygame.Rect((600, 0), (100, 50)),
            manager=manager
        )
        
        start_game_button = pygame_gui.elements.UIButton(
            relative_rect=pygame.Rect((700, 0), (100, 50)),
            text='Start Game',
            manager=manager
        )
        
        clock = pygame.time.Clock()
        time_delta = clock.tick(60) / 1000.0

        while not started:
            for event in pygame.event.get():  # User did something
                if event.type == pygame_gui.UI_BUTTON_PRESSED:
                    ui_elem: pygame_gui.elements.UIButton | pygame_gui.elements.UIDropDownMenu = event.ui_element
                     
                    # Handles symbol assignment
                    if ui_elem == cross_button:
                        turn_O = False
                    if ui_elem == nought_button:
                        turn_O = True
                        
                    # implement grid size
                    
                    if ui_elem == start_game_button:
                        started = True
                        
                        
                # Handle dropdown event
                if event.type == pygame_gui.UI_DROP_DOWN_MENU_CHANGED:
                    if event.ui_element == opponent_dropdown:
                        mode = event.text
                        # The dropdown will automatically close, no need to manually close it       
                    if event.ui_element == algo_dropdown:
                        algorithm = event.text
                        
                    if event.ui_element == grid_dropdown:
                        grid = event.text
                        self.GRID_SIZE = int(grid[0])
                        board_state = [[0 for _ in range(self.GRID_SIZE)] for _ in range(self.GRID_SIZE)]
                                                
                # Checking what button the user clicked
                manager.process_events(event)
                
                manager.update(time_delta)
                manager.draw_ui(self.screen)

            pygame.display.update()

        return { "turn_O": turn_O, "mode": mode, "algorithm": algorithm, "started": started, "board_state": board_state }
    
    def draw_board(self, screen):
        board_items = []
        row_offset = 100                            # init for default edge spacing

        for _ in range(self.GRID_SIZE):             # board cols
            rect = None
            prevRect = None
            nested_items = []
            for row in range(self.GRID_SIZE):       # board rows
                if (row == 0):
                    rect = pygame.draw.rect(
                        self.screen,
                        (255, 0, 0),
                        pygame.Rect(
                            30,
                            row_offset, 
                            self.WIDTH / (self.GRID_SIZE + 1), 
                            self.HEIGHT / (self.GRID_SIZE + 1)
                        )
                    )
                else:
                    rect = pygame.draw.rect(
                        screen,
                        (255, 0, 0),
                        pygame.Rect(
                            prevRect.topright[0] + self.OFFSET, 
                            row_offset, 
                            self.WIDTH / (self.GRID_SIZE + 1), 
                            self.HEIGHT / (self.GRID_SIZE + 1)
                        )
                    )

                prevRect = rect
                nested_items.append(rect)
            board_items.append(nested_items) 

            row_offset = rect.bottomleft[1] + self.OFFSET

        pygame.display.update()
        return board_items

    def draw_game(self):
        # Create a 2 dimensional array using the column and row variables
        pygame.init()
        self.screen = pygame.display.set_mode(self.size)
        pygame.display.set_caption("Tic Tac Toe Random Grid")
        self.screen.fill(self.BLACK)

        screen=pygame.display.set_mode((self.WIDTH,self.HEIGHT))
        screen.fill(self.WHITE)
        pygame.display.flip()


        """
        YOUR CODE HERE TO DRAW THE GRID OTHER CONTROLS AS PART OF THE GUI
        """   

        # -- RENDER MAIN MENU --
        settings = self.draw_menu()
        
        # -- CREATE BOARD GRID --     
        board_items = self.draw_board(screen=screen)

        # -- INIT GAMESTATUS WITH EMPTY BOARD AND TURN_0 SETTINGS FROM MENU --
        self.game_state = GameStatus(board_state=settings["board_state"], turn_O=settings["turn_O"]) # player_one.get("symbol", "") == O
 
        # -- PASS PYGAME RECT ARRAY ALONG WITH GAME STATE TO KEEP TRACK OF CLICKED GRID ITEMS -- 
        self.play_game(mode=settings["mode"], board_items=board_items)       # create players list [player_1_dict, player_2_dict]

    def change_turn(self):
        if(self.game_state.turn_O):
            pygame.display.set_caption("Tic Tac Toe - O's turn")
        else:
            pygame.display.set_caption("Tic Tac Toe - X's turn")


    def draw_circle(self, x, y):
        """
        YOUR CODE HERE TO DRAW THE CIRCLE FOR THE NOUGHTS PLAYER
        """
        font = pygame.font.Font(None, 150)
        rendered_text = font.render("O", True, (0, 0,255))
        self.screen.blit(
            rendered_text, 
            (
                x - (self.OFFSET * (self.GRID_SIZE * 2)), 
                y - (self.OFFSET * (self.GRID_SIZE * 3))
            )
        )
        

    def draw_cross(self, x, y):
        """
        YOUR CODE HERE TO DRAW THE CROSS FOR THE CROSS PLAYER AT THE CELL THAT IS SELECTED VIA THE gui
        """
        font = pygame.font.Font(None, 150)
        rendered_text = font.render("X", True, (0, 0,255))
        self.screen.blit(
            rendered_text, 
            (
                x - (self.OFFSET * (self.GRID_SIZE * 2)), 
                y - (self.OFFSET * (self.GRID_SIZE * 3))
            )
        )
        

    def is_game_over(self):

        """
        YOUR CODE HERE TO SEE IF THE GAME HAS TERMINATED AFTER MAKING A MOVE. YOU SHOULD USE THE IS_TERMINAL()
        FUNCTION FROM GAMESTATUS_5120.PY FILE (YOU WILL FIRST NEED TO COMPLETE IS_TERMINAL() FUNCTION)
        
        YOUR RETURN VALUE SHOULD BE TRUE OR FALSE TO BE USED IN OTHER PARTS OF THE GAME
        """
        # False until a stalemate or a winner
        stalemate_or_winner = False
        if(self.game_state.is_terminal()):
            score = self.game_state.is_terminal()
            if score > 0:
                "Human won!"
            elif score < 0:
                "AI won..."
            else:
                "Its a draw."
        return stalemate_or_winner
        
    

    def move(self, move):
        self.game_state = self.game_state.get_new_state(move)


    def play_ai(self):
        """
        YOUR CODE HERE TO CALL MINIMAX OR NEGAMAX DEPENDEING ON WHICH ALGORITHM SELECTED FROM THE GUI
        ONCE THE ALGORITHM RETURNS THE BEST MOVE TO BE SELECTED, YOU SHOULD DRAW THE NOUGHT (OR CIRCLE DEPENDING
        ON WHICH SYMBOL YOU SELECTED FOR THE AI PLAYER)
        
        THE RETURN VALUES FROM YOUR MINIMAX/NEGAMAX ALGORITHM SHOULD BE THE SCORE, MOVE WHERE SCORE IS AN INTEGER
        NUMBER AND MOVE IS AN X,Y LOCATION RETURNED BY THE AGENT
        """
        
        self.change_turn()
        pygame.display.update()
        terminal = self.game_state.is_terminal()
        """ USE self.game_state.get_scores(terminal) HERE TO COMPUTE AND DISPLAY THE FINAL SCORES """



    def game_reset(self):
        self.draw_game()
        """
        YOUR CODE HERE TO RESET THE BOARD TO VALUE 0 FOR ALL CELLS AND CREATE A NEW GAME STATE WITH NEWLY INITIALIZED
        BOARD STATE
        """
        
        pygame.display.update()

    def play_game(
            self, 
            board_items: list[pygame.Rect], 
            mode = "player_vs_ai"
        ):

        done = False

        while not done:
            if(self.is_game_over() != False):
                done = True
            for event in pygame.event.get():  # User did something
                """
                YOUR CODE HERE TO CHECK IF THE USER CLICKED ON A GRID ITEM. EXIT THE GAME IF THE USER CLICKED EXIT
                """

                # TODO: Handle exit button clicked
                
                """
                YOUR CODE HERE TO HANDLE THE SITUATION IF THE GAME IS OVER. IF THE GAME IS OVER THEN DISPLAY THE SCORE,
                THE WINNER, AND POSSIBLY WAIT FOR THE USER TO CLEAR THE BOARD AND START THE GAME AGAIN (OR CLICK EXIT)
                """
                    
                """
                YOUR CODE HERE TO NOW CHECK WHAT TO DO IF THE GAME IS NOT OVER AND THE USER SELECTED A NON EMPTY CELL
                IF CLICKED A NON EMPTY CELL, THEN GET THE X,Y POSITION, SET ITS VALUE TO 1 (SELECTED BY HUMAN PLAYER),
                DRAW CROSS (OR NOUGHT DEPENDING ON WHICH SYMBOL YOU CHOSE FOR YOURSELF FROM THE gui) AND CALL YOUR 
                PLAY_AI FUNCTION TO LET THE AGENT PLAY AGAINST YOU
                """
                
                if event.type == pygame.MOUSEBUTTONUP:
                    # Get the click position
                    xy_pos = event.dict['pos']
                    
                    row_number = 0
                    for row in board_items:
                        rect_number = 0
                        for rect in row:
                            if rect.collidepoint(xy_pos[0], xy_pos[1]):
                                if self.game_state.turn_O:
                                    self.draw_circle(rect.centerx, rect.centery)
                                    # Using row and col number to update board state value
                                    self.game_state.board_state[row_number][rect_number] = 1
                                    self.game_state.turn_O = False
                                else:
                                    self.draw_cross(rect.centerx, rect.centery)
                                    # Using row and col number to update board state value
                                    self.game_state.board_state[row_number][rect_number] = 2
                                    self.game_state.turn_O = True
                            rect_number += 1
                        row_number += 1

                    self.change_turn()

                    # Check if the game is human vs human or human vs AI player from the GUI. 
                    # If it is human vs human then your opponent should have the value of the selected cell set to -1
                    # Then draw the symbol for your opponent in the selected cell
                    # Within this code portion, continue checking if the game has ended by using is_terminal function
                    
            # Update the screen with what was drawn.
            pygame.display.update()

        pygame.quit()

tictactoegame = RandomBoardTicTacToe(size = (2400, 2400))
"""
YOUR CODE HERE TO SELECT THE OPTIONS VIA THE GUI CALLED FROM THE ABOVE LINE
AFTER THE ABOVE LINE, THE USER SHOULD SELECT THE OPTIONS AND START THE GAME. 
YOUR FUNCTION PLAY_GAME SHOULD THEN BE CALLED WITH THE RIGHT OPTIONS AS SOON
AS THE USER STARTS THE GAME
"""

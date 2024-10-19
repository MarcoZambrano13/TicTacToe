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
    def __init__(self, size = (2400, 2400)):

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
        clock = pygame.time.Clock()

        manager = pygame_gui.UIManager((600, 600))

        # Create GUI buttons
        nought_button = pygame_gui.elements.UIButton(
            relative_rect=pygame.Rect((0, 0), (100, 50)),
            text='Nought (O)',
            manager=manager
        )

        cross_button = pygame_gui.elements.UIButton(
            relative_rect=pygame.Rect((0, 0), (150, 50)),
            text='Cross (x)',
            manager=manager
        )

        human_human_button = pygame_gui.elements.UIButton(
            relative_rect=pygame.Rect((0, 0), (200, 50)),
            text='Human vs Human',
            manager=manager
        )

        huam_ai_button = pygame_gui.elements.UIButton(
            relative_rect=pygame.Rect((0, 0), (300, 50)),
            text='Human vs (AI)',
            manager=manager
        )

        start_game_button = pygame_gui.elements.UIButton(
            relative_rect=pygame.Rect((0, 0), (100, 50)),
            text='Start Game',
            manager=manager
        )

        for event in pygame.event.get():  # User did something
            # Checking what button the user clicked
            manager.process_events(event)

            if event.type == pygame_gui.UI_BUTTON_PRESSED:
                if event.ui_element == cross_button:
                    print("Button clicked!")

            time_delta = clock.tick(60) / 1000.0
            manager.draw_ui(self.screen)
            manager.update(time_delta)

    def draw_game(self):
        # Create a 2 dimensional array using the column and row variables
        pygame.init()
        self.screen = pygame.display.set_mode(self.size)
        pygame.display.set_caption("Tic Tac Toe Random Grid")
        self.screen.fill(self.BLACK)
        # Draw the grid
        board_state = [
            [0, 0, 0],
            [0, 0, 0],
            [0, 0, 0]
        ]

        screen=pygame.display.set_mode((self.WIDTH,self.HEIGHT))
        screen.fill(self.WHITE)
        pygame.display.flip()


        """
        YOUR CODE HERE TO DRAW THE GRID OTHER CONTROLS AS PART OF THE GUI
        """   

        # -- RENDER MAIN MENU --

        # -- CREATE BOARD GRID --     
        grid_items = []
        row_offset = 100                             # init for default edge spacing

        for _ in range(self.GRID_SIZE):             # board cols
            rect = None
            prevRect = None
            for row in range(self.GRID_SIZE):       # board rows
                if (row == 0):
                    rect = pygame.draw.rect(
                        screen,
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
                grid_items.append(rect)

            row_offset = rect.bottomleft[1] + self.OFFSET

        pygame.display.update()

        self.draw_menu()

        game_status = GameStatus(board_state=board_state, turn_O=True) # player_one.get("symbol", "") == O
 
        # -- PASS PYGAME RECT ARRAY ALONG WITH GAME STATE TO KEEP TRACK OF CLICKED GRID ITEMS -- 
        self.play_game(mode="player_vs_ai", grid_items=grid_items, game_status=game_status)       # create players list [player_1_dict, player_2_dict]

    def change_turn(self):

        if(self.game_state.turn_O):
            pygame.display.set_caption("Tic Tac Toe - O's turn")
        else:
            pygame.display.set_caption("Tic Tac Toe - X's turn")


    def draw_circle(self, x, y):
        """
        YOUR CODE HERE TO DRAW THE CIRCLE FOR THE NOUGHTS PLAYER
        """
        

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
            grid_items: list[pygame.Rect], 
            game_status: GameStatus,
            mode = "player_vs_ai"
        ):

        done = False

        while not done:
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
                    # Get the position
                    xy_pos = event.dict['pos']
                    # pygame.button
                    
                    # Change the x/y screen coordinates to grid coordinates
                    for rect in grid_items:
                        if rect.collidepoint(xy_pos[0], xy_pos[1]):
                            self.draw_cross(rect.centerx, rect.centery)

                    # Check if the game is human vs human or human vs AI player from the GUI. 
                    # If it is human vs human then your opponent should have the value of the selected cell set to -1
                    # Then draw the symbol for your opponent in the selected cell
                    # Within this code portion, continue checking if the game has ended by using is_terminal function
                    
            # Update the screen with what was drawn.
            pygame.display.update()

        pygame.quit()

tictactoegame = RandomBoardTicTacToe()
"""
YOUR CODE HERE TO SELECT THE OPTIONS VIA THE GUI CALLED FROM THE ABOVE LINE
AFTER THE ABOVE LINE, THE USER SHOULD SELECT THE OPTIONS AND START THE GAME. 
YOUR FUNCTION PLAY_GAME SHOULD THEN BE CALLED WITH THE RIGHT OPTIONS AS SOON
AS THE USER STARTS THE GAME
"""

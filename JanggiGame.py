# Author: Michael Schwartz
# Date: 02MAR2021
# Description: A Janggi board game simulator.


import pygame


class JanggiGame:
    """Contains board dictionary initialized with pieces in their positions, game state, methods to make/validate moves.
    Determine if a player is in check, and other methods to facilitate those mentioned"""

    def __init__(self):
        """Initializes board, state to unfinished, and turn to blue"""
        self._board = {
            'a1': 'R_Ch', 'b1': 'R_El', 'c1': 'R_Ho', 'd1': 'R_Gu', 'e1': None, 'f1': 'R_Gu', 'g1': 'R_El', 'h1': 'R_Ho', 'i1': 'R_Ch',
            'a2': None, 'b2': None, 'c2': None, 'd2': None, 'e2': 'R_Ge', 'f2': None, 'g2': None, 'h2': None, 'i2': None,
            'a3': None, 'b3': 'R_Ca', 'c3': None, 'd3': None, 'e3': None, 'f3': None, 'g3': None, 'h3': 'R_Ca', 'i3': None,
            'a4': 'R_So', 'b4': None, 'c4': 'R_So', 'd4': None, 'e4': 'R_So', 'f4': None, 'g4': 'R_So', 'h4': None, 'i4': 'R_So',
            'a5': None, 'b5': None, 'c5': None, 'd5': None, 'e5': None, 'f5': None, 'g5': None, 'h5': None, 'i5': None,
            'a6': None, 'b6': None, 'c6': None, 'd6': None, 'e6': None, 'f6': None, 'g6': None, 'h6': None, 'i6': None,
            'a7': 'B_So', 'b7': None, 'c7': 'B_So', 'd7': None, 'e7': 'B_So', 'f7': None, 'g7': 'B_So', 'h7': None, 'i7': 'B_So',
            'a8': None, 'b8': 'B_Ca', 'c8': None, 'd8': None, 'e8': None, 'f8': None, 'g8': None, 'h8': 'B_Ca', 'i8': None,
            'a9': None, 'b9': None, 'c9': None, 'd9': None, 'e9': 'B_Ge', 'f9': None, 'g9': None, 'h9': None, 'i9': None,
            'a10': 'B_Ch', 'b10': 'B_El', 'c10': 'B_Ho', 'd10': 'B_Gu', 'e10': None, 'f10': 'B_Gu', 'g10': 'B_El', 'h10': 'B_Ho', 'i10': 'B_Ch'}
        self._game_state = 'UNFINISHED'
        self._turn = 'B'

    def get_board(self):
        return self._board
    def print_board(self):
        print('   a    ', 'b   ', 'c   ', 'd   ', 'e   ', 'f   ', 'g   ', 'h   ', 'i   ')
        print('1 ', self._board['a1'], self._board['b1'], self._board['c1'], self._board['d1'], self._board['e1'], self._board['f1'],
              self._board['g1'], self._board['h1'], self._board['i1'])
        print('2 ', self._board['a2'], self._board['b2'], self._board['c2'], self._board['d2'], self._board['e2'], self._board['f2'],
              self._board['g2'], self._board['h2'], self._board['i2'])
        print('3 ', self._board['a3'], self._board['b3'], self._board['c3'], self._board['d3'], self._board['e3'], self._board['f3'],
              self._board['g3'], self._board['h3'], self._board['i3'])
        print('4 ', self._board['a4'], self._board['b4'], self._board['c4'], self._board['d4'], self._board['e4'], self._board['f4'],
              self._board['g4'], self._board['h4'], self._board['i4'])
        print('5 ', self._board['a5'], self._board['b5'], self._board['c5'], self._board['d5'], self._board['e5'], self._board['f5'],
              self._board['g5'], self._board['h5'], self._board['i5'])
        print('6 ', self._board['a6'], self._board['b6'], self._board['c6'], self._board['d6'], self._board['e6'], self._board['f6'],
              self._board['g6'], self._board['h6'], self._board['i6'])
        print('7 ', self._board['a7'], self._board['b7'], self._board['c7'], self._board['d7'], self._board['e7'], self._board['f7'],
              self._board['g7'], self._board['h7'], self._board['i7'])
        print('8 ', self._board['a8'], self._board['b8'], self._board['c8'], self._board['d8'], self._board['e8'], self._board['f8'],
              self._board['g8'], self._board['h8'], self._board['i8'])
        print('9 ', self._board['a9'], self._board['b9'], self._board['c9'], self._board['d9'], self._board['e9'], self._board['f9'],
              self._board['g9'], self._board['h9'], self._board['i9'])
        print('10', self._board['a10'], self._board['b10'], self._board['c10'], self._board['d10'], self._board['e10'], self._board['f10'],
              self._board['g10'], self._board['h10'], self._board['i10'])

    def declare_winner(self):
        """If player is in check, tests for checkmate by seeing if the checked player can move a piece to
        get out of check. if impossible, updates the game state to declare the other player a winner"""
        fake_board = dict(self._board)

        if self.is_in_check('B'):  # if blue is in check
            for x in self._board:
                if self._board[x] is not None:
                    if self._board[x][0] == 'B':  # iterate though board stopping at blue pieces
                        for y in self._board:
                            self.fake_move(x, y)  # try all moves for each blue piece
                            if not self.is_in_check('B'):  # if a move causes blue to not be in check, reset board and continue game
                                self._board = dict(fake_board)
                                return
                            self._board = dict(fake_board)
            self._board = dict(fake_board)
            self._game_state = 'RED_WON'  # If a move cant be made to get blue out of check, declare red winner
            return

        if self.is_in_check('R'):  # if red is in check
            for x in self._board:
                if self._board[x] is not None:
                    if self._board[x][0] == 'R':  # iterate through board stopping at red pieces
                        for y in self._board:
                            self.fake_move(x, y)  # try all moves for each red piece
                            if not self.is_in_check('R'):  # if a move causes red to not be in check, resume game
                                self._board = dict(fake_board)
                                print(x, y)
                                return
                            self._board = dict(fake_board)
            self._board = dict(fake_board)
            self._game_state = 'BLUE_WON'  # if a move cant be made to get red out of check, declare blue winner
            return

    def get_game_state(self):
        """Returns game state, whether red or blue has won, or if the game is unfinished"""
        return self._game_state

    def check(self, team, board):
        """Takes 'red' or 'blue' as a parameter, returns True if that player is in check, false otherwise.
        checks by iterating through each enemy piece and checking if capturing the general is a valid move"""
        B_Ge_pos = list(board.keys())[list(board.values()).index('B_Ge')]
        R_Ge_pos = list(board.keys())[list(board.values()).index('R_Ge')]
        if team == 'blue':
            team = 'B'
        if team == 'red':
            team = 'R'
        if team == 'R':
            for x in board:
                if x != R_Ge_pos:
                    if self.validate_move(x, R_Ge_pos):  # if a piece can capture red's general
                        return True

            # for piece on blue team, check if make_move(piece, general) is valid
        if team == 'B':
            for x in board:
                if x != B_Ge_pos:
                    if self.validate_move(x, B_Ge_pos):  # if a piece can capture blue's general
                        return True
        return False

    def is_in_check(self, team):
        """Helper method for check, takes team string, returns call of check method passing team and board"""
        return self.check(team, self._board)

    def make_move(self, source, destination):
        """
        Takes source and destination square and moves the piece as long as it is a valid move (using validate_move)
        and the game is in progress
        :param source: square a piece is being moved from
        :param destination: square a piece is being moved to
        :return: True if a valid move. False if move_from doesn't have the player's piece, or if move is illegal,
        or if game is over.
        """
        source_piece = self._board[source]
        if self._game_state != 'UNFINISHED':  # if game is not in progress (a player has won)
            return False

        if not self.is_in_check(self._turn):  # if player to move is not in check
            if source == destination:
                self.switch_turn()  # player passes turn without moving piece
                return True

        if self._board[source] is None:
            return False

        if self._turn != self._board[source][0]:  # if piece being moved does not belong to player who's turn it is
            return False

        if not self.validate_move(source, destination):  # if move is not valid, return false
            return False
        temp = self._board[destination]
        self._board[destination] = self._board[source]
        self._board[source] = None
        if self.is_in_check(source_piece[0]):  # if moving into check, undo move
            self._board[source] = self._board[destination]
            self._board[destination] = temp
            return False  # Test if a player is in checkmate, declare winner if so
        self.declare_winner()
        self.switch_turn()
        return True

    def fake_move(self, source, destination):
        """
        Takes source and destination square and moves the piece as long as it is a valid move (using validate_move)
        only validates move and makes move, doesnt call other methods
        :param source: square a piece is being moved from
        :param destination: square a piece is being moved to
        :return: True if a valid move. False if source doesn't have a piece, or if move is illegal
        """

        if self._board[source] is None:
            return False

        if not self.validate_move(source, destination):
            return False
        self._board[destination] = self._board[source]
        self._board[source] = None
        return True

    def validate_move(self, source, destination):
        """takes source and destination positions, gets piece from source position,
        checks if that movement would be valid for that type of piece, and if the movement is not blocked
        Returns True if it is a valid move, False if not"""
        source_piece = self._board[source]
        destination_piece = self._board[destination]
        if source_piece is None:
            return False

        if destination_piece is not None:  # if player is attempting to capture
            if self._board[destination][0] == self._board[source][0]:  # if source and destination piece are on same team
                return False

        if 'Ch' in source_piece:  # if piece is a Chariot
            if source[0] != destination[0] and source[1:] != destination[1:]:  # if piece isn't being moved vertically or horizontally
                return False
            if (source[0] == destination[0]) and int(destination[1:]) > int(source[1:]):  # if moving down
                for x in range(int(source[1:]) + 1, int(destination[1:])):  # iterate through spots between source/destination
                    if self._board[source[0] + str(x)] is not None:  # if there is a piece in the spot
                        return False
            if (source[0] == destination[0]) and int(destination[1:]) < int(source[1:]):  # if moving up
                for x in range(int(destination[1:]) + 1, int(source[1:])):  # iterate through spots between source/destination
                    if self._board[source[0] + str(x)] is not None:  # if there is a piece in the spot
                        return False
            if (source[1:] == destination[1:]) and ord(destination[0]) > ord(source[0]):  # if moving right
                for x in range(ord(source[0]) + 1, ord(destination[0])):  # iterate through spots between source/destination
                    if self._board[chr(x) + source[1:]] is not None:  # if there is a piece in the spot
                        return False
            if (source[1:] == destination[1:]) and ord(destination[0]) < ord(source[0]):  # if moving left
                for x in range(ord(source[0]) - 1, ord(destination[0]), -1):  # iterate through spots between source/destination
                    if self._board[chr(x) + source[1:]] is not None:  # if there is a piece in the spot
                        return False

        if 'So' in source_piece:  # if piece to be moved is a soldier
            if source[0] != destination[0] and source[1:] != destination[1:]:  # if piece isn't being moved vertically or horizontally
                return False
            if source_piece[0] == 'B':  # if piece is Blue
                if int(destination[1:]) - int(source[1:]) not in [0, -1]:  # if trying to move more than 1 space vertically, or backwards
                    return False
            if source_piece[0] == 'R':  # if piece is Red
                if int(destination[1:]) - int(source[1:]) not in [0, 1]:  # if trying to move more than 1 space vertically, or backwards
                    return False
            if source[1:] == destination[1:]:  # if moving horizontally
                if abs(ord(destination[0]) - ord(source[0])) != 1:  # if trying to move more than 1 space horizontally
                    return False

        if 'Ho' in source_piece:  # if piece to be moved is a horse
            if (abs(int(destination[1:]) - int(source[1:])) == 1) and (abs(ord(destination[0]) - ord(source[0])) == 1):  # if move is 1 spot diagonally
                return False
            if (source[0] == destination[0]) or (source[1:] == destination[1:]):  # if whole move is vertical or horizontal
                return False
            if abs(ord(destination[0]) - ord(source[0])) == 1:  # if first move is vertical
                if int(destination[1:]) - int(source[1:]) == -2:  # if piece is moving up board
                    if self._board[source[0] + str(int(source[1:]) - 1)] is not None:  # if spot up from source is occupied
                        return False
                    if abs(ord(destination[0]) - ord(source[0])) != 1:  # if not moving diagonally 1 spot
                        return False
                    return True
                if int(destination[1:]) - int(source[1:]) == 2:  # if piece is moving down board
                    if self._board[source[0] + str(int(source[1:]) + 1)] is not None:  # if spot down from source is occupied
                        return False
                    if abs(ord(destination[0]) - ord(source[0])) != 1:  # if not moving diagonally 1 spot
                        return False
                    return True
                return False
            if abs(int(destination[1:]) - int(source[1:])) == 1:  # if first move is horizontal
                if abs(ord(destination[0]) - ord(source[0])) == -2:  # if piece is moving left
                    if self._board[chr(ord(source[0]) + 1) + str(int(source[1:]))] is not None:  # if spot left of source is occupied
                        return False
                    if abs(int(destination[1:]) - int(source[1:])) != 1:  # if not moving diagonally 1 spot
                        return False
                if abs(ord(destination[0]) - ord(source[0])) == 2:  # if piece is moving right
                    if self._board[chr(ord(source[0]) - 1) + str(int(source[1:]))] is not None:  # if spot right of source is occupied
                        return False
                    if abs(int(destination[1:]) - int(source[1:])) != 1:  # if not moving diagonally 1 spot
                        return False
                return True
            return False

        if 'El' in source_piece:
            if (abs(int(destination[1:]) - int(source[1:])) == 1) and (abs(ord(destination[0]) - ord(source[0])) == 1):  # if move is 1 spot diagonally
                return False
            if (source[0] == destination[0]) or (source[1:] == destination[1:]):  # if whole move is vertical or horizontal
                return False
            if abs(ord(destination[0]) - ord(source[0])) == 2:  # if first move is vertical
                if int(destination[1:]) - int(source[1:]) == -3:  # if piece is moving up board
                    if self._board[source[0] + str(int(source[1:]) - 1)] is not None:  # if spot up from source is occupied
                        return False
                    if abs(ord(destination[0]) - ord(source[0])) != 2:  # if not moving diagonally 2 spots
                        return False
                    return True
                if int(destination[1:]) - int(source[1:]) == 3:  # if piece is moving down board
                    if self._board[source[0] + str(int(source[1:]) + 1)] is not None:  # if spot down from source is occupied
                        return False
                    if abs(ord(destination[0]) - ord(source[0])) != 2:  # if not moving diagonally 2 spots
                        return False
                    return True
                return False
            if abs(int(destination[1:]) - int(source[1:])) == 2:  # if first move is horizontal
                if abs(ord(destination[0]) - ord(source[0])) == -3:  # if piece is moving left
                    if self._board[chr(ord(source[0]) + 1) + str(int(source[1:]))] is not None:  # if spot left of source is occupied
                        return False
                    if abs(int(destination[1:]) - int(source[1:])) != 2:  # if not moving diagonally 2 spots
                        return False
                if abs(ord(destination[0]) - ord(source[0])) == 3:  # if piece is moving right
                    if self._board[chr(ord(source[0]) - 1) + str(int(source[1:]))] is not None:  # if spot right of source is occupied
                        return False
                    if abs(int(destination[1:]) - int(source[1:])) != 2:  # if not moving diagonally 2 spots
                        return False
                    return True
            return False

        if 'Ca' in source_piece:
            count = 0
            if source[0] != destination[0] and source[1:] != destination[1:]:  # if piece isn't being moved vertically or horizontally
                return False
            if destination_piece is not None:
                if 'Ca' in destination_piece:
                    return False
            if (source[0] == destination[0]) and int(destination[1:]) > int(source[1:]):  # if moving down board
                for x in range(int(source[1:]) + 1, int(destination[1:])):  # iterate through spots between source/destination
                    if self._board[source[0] + str(x)] is not None:  # if there is a piece in the spot
                        count += 1
                        if 'Ca' in self._board[source[0] + str(x)]:  # if trying to jump over Cannon
                            return False
            if (source[0] == destination[0]) and int(destination[1:]) < int(source[1:]):  # if moving up board
                for x in range(int(source[1:]) - 1, int(destination[1:]), -1):  # iterate through spots between source/destination
                    if self._board[source[0] + str(x)] is not None:  # if there is a piece in the spot
                        count += 1
                        if 'Ca' in self._board[source[0] + str(x)]:  # if trying to jump of Cannon
                            return False
            if (source[1:] == destination[1:]) and ord(destination[0]) > ord(source[0]):  # if moving right
                for x in range(ord(source[0]) + 1, ord(destination[0])):  # iterate through spots between source/destination
                    if self._board[chr(x) + source[1:]] is not None:  # if there is a piece in the spot
                        count += 1
                        if 'Ca' in self._board[chr(x) + source[1:]]:
                            return False
            if (source[1:] == destination[1:]) and ord(destination[0]) < ord(source[0]):  # if moving left
                for x in range(ord(source[0]) - 1, ord(destination[0]), -1):  # iterate through spots between source/destination
                    if self._board[chr(x) + source[1:]] is not None:  # if there is a piece in the spot
                        count += 1
                        if 'Ca' in self._board[chr(x) + source[1:]]:
                            return False
            if count != 1:
                return False

        if 'Gu' in source_piece:
            if destination[0] not in ['d', 'e', 'f']:  # if trying to move out of fortress
                return False
            if (abs(ord(destination[0]) - ord(source[0])) > 1) or (abs(int(destination[1:]) - int(source[1:])) > 1):  # if trying to move > 1 space
                return False
            if source_piece[0] == 'B':  # if piece to be moved is blue
                if destination[1:] not in ['8', '9', '10']:  # if trying to move out of blue fortress
                    return False
                if source in ['d9', 'e8', 'f9', 'e10']:  # if piece to move shouldn't move diagonally
                    if source[0] != destination[0] and source[1:] != destination[1:]:  # if piece isn't being moved vertically or horizontally
                        return False
            if source_piece[0] == 'R':  # if piece to be moved is red
                if destination[1:] not in ['1', '2', '3']:  # if trying to move out of red fortress
                    return False

        if 'Ge' in source_piece:
            if destination[0] not in ['d', 'e', 'f']:  # if trying to move out of fortress
                return False
            if (abs(ord(destination[0]) - ord(source[0])) > 1) or (abs(int(destination[1:]) - int(source[1:])) > 1):  # if trying to move > 1 space
                return False
            if source_piece[0] == 'B':  # if piece to be moved is blue
                if destination[1:] not in ['8', '9', '10']:  # if trying to move out of blue fortress
                    return False
                if source in ['d9', 'e8', 'f9', 'e10']:  # if piece to move shouldn't move diagonally
                    if source[0] != destination[0] and source[1:] != destination[1:]:  # if piece isn't being moved vertically or horizontally
                        return False
            if source_piece[0] == 'R':  # if piece to be moved is red
                if destination[1:] not in ['1', '2', '3']:  # if trying to move out of red fortress
                    return False

        return True

    def switch_turn(self):
        """No input. If turn is currently BLUE, change to RED. If it is RED, change to BLUE"""
        if self._turn == 'B':
            self._turn = 'R'
        elif self._turn == 'R':
            self._turn = 'B'

    def get_turn(self):
        return self._turn

    def get_piece_from_position(self, position):
        """Takes board position, eg. 'b4', and returns the piece at that position"""
        return self._board[position]


boardWidth = 9
boardHeight = 10


def main():
    # initialize the pygame module
    pygame.init()

    game = JanggiGame()
    board = game.get_board()

    # load and set the lojgo
    logo = pygame.image.load("images/JanggiLogo.jpeg")
    pygame.display.set_icon(logo)
    pygame.display.set_caption("Janggi Game")
    bgd_image = pygame.image.load("images/JanggiBoard.jpeg")
    # create a surface on screen that has the size of 240 x 180
    windowHeight, windowWidth = 1024, 1006
    spaceHeight, spaceWidth = 101, 115

    screen = pygame.display.set_mode((windowHeight, windowWidth))

    screen.fill((56, 0, 0))

    #Horse
    horse = pygame.image.load("images/horse.png")
    horse.set_alpha(None)
    horse.set_colorkey((247, 247, 247))
    horse = pygame.transform.scale(horse, (50, 50))
    screen.blit(bgd_image,(0,0))
    screen.blit(horse, (30 + spaceWidth * 2, 20)) #45, 56 115 102

    #Cannon
    cannon = pygame.transform.scale(pygame.image.load("images/cannon.png"), (55, 55))

    elephant = pygame.transform.scale(pygame.image.load("images/elephant.png"), (50, 50))

    chariot = pygame.transform.scale(pygame.image.load("images/chariot.png"), (50, 50))

    guard = pygame.transform.scale(pygame.image.load("images/guard.png"), (50, 50))

    general = pygame.transform.scale(pygame.image.load("images/general.png"), (50, 50))

    general.set_colorkey((255,255,255))

    soldier = pygame.transform.scale(pygame.image.load("images/soldier.png"), (25, 50))

    red = pygame.transform.scale(pygame.image.load("images/red.png"), (50, 50))

    blue = pygame.transform.scale(pygame.image.load("images/blue.png"), (50, 50))

    game.make_move('c10', 'd8')


    for x in board:
        if board[x] is not None and board[x][0] == "R":
            screen.blit(red, (30 + spaceWidth*(ord(x[0])-97), 20 + spaceHeight*(int(x[1])-1)))
        if board[x] is not None and board[x][0] == "B":
            if len(x) == 2:
                screen.blit(blue, (30 + spaceWidth * (ord(x[0]) - 97), 20 + spaceHeight * (int(x[1]) - 1)))
            else:
                screen.blit(blue, (30 + spaceWidth * (ord(x[0]) - 97), 20 + spaceHeight * 9))
        if board[x] == "R_Ca" or board[x] == "B_Ca":
            screen.blit(cannon, (30 + spaceWidth*(ord(x[0])-97), 20 + spaceHeight*(int(x[1])-1)))
        if board[x] == "R_Ho" or board[x] == "B_Ho":
            if len(x) == 2:
                screen.blit(horse, (30 + spaceWidth*(ord(x[0])-97), 20 + spaceHeight*(int(x[1])-1)))
            else:
                screen.blit(horse, (30 + spaceWidth * (ord(x[0]) - 97), 20 + spaceHeight * 9))
        if board[x] == "R_El" or board[x] == "B_El":
            if len(x) == 2:
                screen.blit(elephant, (30 + spaceWidth*(ord(x[0])-97), 20 + spaceHeight*(int(x[1])-1)))
            else:
                screen.blit(elephant, (30 + spaceWidth * (ord(x[0]) - 97), 20 + spaceHeight * 9))

        if board[x] == "R_Ch" or board[x] == "B_Ch":
            if len(x) == 2:
                screen.blit(chariot, (30 + spaceWidth*(ord(x[0])-97), 20 + spaceHeight*(int(x[1])-1)))
            else:
                screen.blit(chariot, (30 + spaceWidth * (ord(x[0]) - 97), 20 + spaceHeight * 9))

        if board[x] == "R_Gu" or board[x] == "B_Gu":
            if len(x) == 2:
                screen.blit(guard, (30 + spaceWidth*(ord(x[0])-97), 20 + spaceHeight*(int(x[1])-1)))
            else:
                screen.blit(guard, (30 + spaceWidth * (ord(x[0]) - 97), 20 + spaceHeight * 9))

        if board[x] == "R_Ge" or board[x] == "B_Ge":
            if len(x) == 2:
                screen.blit(general, (30 + spaceWidth*(ord(x[0])-97), 20 + spaceHeight*(int(x[1])-1)))
            else:
                screen.blit(general, (30 + spaceWidth * (ord(x[0]) - 97), 20 + spaceHeight * 9))

        if board[x] == "R_So" or board[x] == "B_So":
            if len(x) == 2:
                screen.blit(soldier, (45 + spaceWidth*(ord(x[0])-97), 20 + spaceHeight*(int(x[1])-1)))
            else:
                screen.blit(soldier, (30 + spaceWidth * (ord(x[0]) - 97), 20 + spaceHeight * 9))

    # screen.blit(cannon, (30 + spaceWidth*1, 20 + spaceHeight*2))

    # define the position of the smiley
    xpos = 50
    ypos = 50
    # how many pixels we move our smiley each frame
    step_x = 10
    step_y = 10
    screen_width = 240
    screen_height = 180

    pygame.display.flip()

    # define a variable to control the main loop
    running = True

    # main loop
    while running:

        # event handling, gets all event from the event queue
        for event in pygame.event.get():
            # only do something if the event is of type QUIT
            if event.type == pygame.QUIT:
                # change the value to False, to exit the main loop
                running = False


# run the main function only if this module is executed as the main script
# (if you import this as a module then nothing is executed)
if __name__ == "__main__":
    # call the main function
    main()

JanggiGame().print_board()

game = JanggiGame()
game.print_board()
print(game.get_turn())
print(game.make_move('c10', 'd8'))
print(game.make_move('h1', 'e3'))
print(game.get_game_state())

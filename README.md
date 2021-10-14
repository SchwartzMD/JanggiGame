A general is in check if it could be captured on the opposing player's next move. A player cannot make a move that puts or leaves their general in check. The game ends when one player **checkmates** the other's general.  You don't actually capture a general, instead you have to put it in such a position that it cannot escape being in check, meaning that no matter what, it could be captured on the next move.  This works the same as in chess, if you're familiar with that game.

Unlike chess, Janggi allows you to pass a turn and thus there is no stalemate (a scenario when no legal moves can be made).

Locations on the board are specified using "algebraic notation", with columns labeled a-i and rows labeled 1-10, with row 1 being the Red side and row 10 the Blue side.

This program includes
* A method called `get_game_state` that just returns one of these values, depending on the game state: 'UNFINISHED' or 'RED_WON' or 'BLUE_WON'.
* A method called `is_in_check` that takes as a parameter either 'red' or 'blue' and returns True if that player is in check, but returns False otherwise.
* A method called `make_move` that takes two parameters - strings that represent the square to move from and the square to move to.  For example, `make_move('b3', 'b10')`.  If the square being moved from does not contain a piece belonging to the player whose turn it is, or if the indicated move is not legal, or if the game has already been won, then it returns False.  Otherwise it makes the indicated move, remove any captured piece, update the game state if necessary, update whose turn it is, and return True.

If the `make_move` method is passed the same string for the square moved from and to, it is processed as the player passing their turn, and return True.

Here's a very simple example of how the class could be used:
```
game = JanggiGame()
move_result = game.make_move('c1', 'e3') #should be False because it's not Red's turn
move_result = game.make_move('a7,'b7') #should return True
blue_in_check = game.is_in_check('blue') #should return False
game.make_move('a4', 'a5') #should return True
state = game.get_game_state() #should return UNFINISHED
game.make_move('b7','b6') #should return True
game.make_move('b3','b6') #should return False because it's an invalid move
game.make_move('a1','a4') #should return True
game.make_move('c7','d7') #should return True
game.make_move('a4','a4') #this will pass the Red's turn and return True
```


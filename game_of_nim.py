from games import *

class GameOfNim(Game):
    """Play Game of Nim with first player 'MAX'.
    A state has the player to move, a cached utility, a list of moves in
    the form of a list of (x, y) positions, and a board, in the form of
    a list with number of objects in each row."""

    def __init__(self, board=[3,1]):
        #creates the initial game state
        #first player is MAX
        #create a list of possible moves

        self.board = board

        moves = []
        for r, row in enumerate(board):
            for n in range(1, row + 1):
                moves.append((r, n))
        
        #create initial state
        self.initial = GameState(to_move ='MAX', utility=1, board=board, moves=moves)        
    
    def actions(self, state):
        """Legal moves are at least one object, all from the same row."""
        return state.moves
    
    def result(self, state, move):
        if move not in state.moves:
            return state  # Illegal move has no effect
        
        #create a copy of the board
        board = state.board.copy()

        #parse move
        row, num_objects = move

        #update board by removing objects
        board[row] -= num_objects

        #creates a list of possible moves from the new board
        moves = []
        for r, row_objects in enumerate(board):
            for n in range(1, row_objects +1):
                moves.append((r,n))

        #switch player
        next_player = 'MIN' if state.to_move == 'MAX' else 'MAX'

        #Return new state
        return GameState(to_move=next_player, utility=0, board=board, moves=moves)
    
    def utility(self, state, player):
        """Return the value to player; 1 for win, -1 for loss, 0 otherwise."""
        # return state.utility if player == 'MAX' else -state.utility
        if not self.terminal_test(state):
            return 0
        elif player == 'MAX':
            return 1
        elif player == 'MIN':
            return -1
    
    def terminal_test(self, state):
        """A state is terminal if there are no objects left"""
        return sum(state.board) == 0
        # return state.utility != 0 or len(state.moves) == 0
    
    def display(self, state):
        board = state.board
        print("board: ", board)

if __name__ == "__main__":
    nim = GameOfNim(board=[0, 5, 3, 1]) # Creating the game instance
    #nim = GameOfNim(board=[7, 5, 3, 1]) # a much larger tree to search
    print(nim.initial.board) # must be [0, 5, 3, 1]
    print(nim.initial.moves) # must be [(1, 1), (1, 2), (1, 3), (1, 4), (1, 5), (2,1), (2, 2), (2, 3), (3, 1)]
    print(nim.result(nim.initial, (1,3) ))
    utility = nim.play_game(alpha_beta_player, query_player) # computer moves first

    if (utility < 0):
        print("MIN won the game")
    else:
        print("MAX won the game")

    print ("\n utility is ", utility)

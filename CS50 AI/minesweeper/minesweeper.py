import itertools
import random

# Minesweeper handles the gameplay
class Minesweeper():
    """
    Minesweeper game representation
    """

    def __init__(self, height=8, width=8, mines=8):

        # Set initial width, height, and number of mines
        self.height = height
        self.width = width
        self.mines = set()

        # Initialize an empty field with no mines
        """
        Each cell is a pair (i, j) where i is the row and j is the column
        """
        self.board = []
        for i in range(self.height):
            row = []
            for j in range(self.width):
                row.append(False)
            self.board.append(row)

        # Add mines randomly
        while len(self.mines) != mines:
            i = random.randrange(height)
            j = random.randrange(width)
            if not self.board[i][j]:
                self.mines.add((i, j))
                self.board[i][j] = True

        # At first, player has found no mines
        self.mines_found = set()

    def print(self):
        """
        Prints a text-based representation
        of where mines are located.
        """
        for i in range(self.height):
            print("--" * self.width + "-")
            for j in range(self.width):
                if self.board[i][j]:
                    print("|X", end="")
                else:
                    print("| ", end="")
            print("|")
        print("--" * self.width + "-")

    def is_mine(self, cell):
        i, j = cell
        return self.board[i][j]

    def nearby_mines(self, cell):
        """
        Returns the number of mines that are
        within one row and column of a given cell,
        not including the cell itself.
        """

        # Keep count of nearby mines
        count = 0

        # Loop over all cells within one row and column
        for i in range(cell[0] - 1, cell[0] + 2):
            for j in range(cell[1] - 1, cell[1] + 2):

                # Ignore the cell itself
                if (i, j) == cell:
                    continue

                # Update count if cell in bounds and is mine
                if 0 <= i < self.height and 0 <= j < self.width:
                    if self.board[i][j]:
                        count += 1

        return count

    def won(self):
        """
        Checks if all mines have been flagged.
        """
        return self.mines_found == self.mines

# Sentence represents a logical sentence that contains both a set of cells and a count
class Sentence():
    """
    Logical statement about a Minesweeper game
    A sentence consists of a set of board cells,
    and a count of the number of those cells which are mines.
    """
    """
    Each sentence has a set of cells within it and a count of how many of those cells are mines
    """

    def __init__(self, cells, count):
        self.cells = set(cells)
        self.count = count

    def __eq__(self, other):
        return self.cells == other.cells and self.count == other.count

    def __str__(self):
        return f"{self.cells} = {self.count}"

    def known_mines(self):
        """
        Returns the set of all cells in self.cells known to be mines.
        """
        # A set of cells on the board that are involved in the sentence and a
        # number count, representing the count of how many of those cells are mines
        if len(self.cells) == self.count and self.count != 0:
            return self.cells
        return set()

    def known_safes(self):
        """
        Returns the set of all cells in self.cells known to be safe.
        """
        # A set of cells on the board that are involved in the sentence and a
        # number count, representing the count of how many of those cells are mines
        # if count is 0, then no mine
        if self.count == 0:
            return self.cells
        return set()

    def mark_mine(self, cell):
        """
        Updates internal knowledge representation given the fact that
        a cell is known to be a mine.
        """
        #If cell is in the sentence, the function should update the sentence so that cell is
        # no longer in the sentence, but still represents a logically correct sentence given 
        # that cell is known to be a mine.
        """In this case I need to remove the cell and decrease the count"""
        if cell in self.cells:
            self.cells.remove(cell)
            self.count -= 1
        
        # If cell is not in the sentence, then no action is necessary

    def mark_safe(self, cell):
        """
        Updates internal knowledge representation given the fact that
        a cell is known to be safe.
        """
        # If cell is in the sentence, the function should update the sentence so that cell is
        # no longer in the sentence, but still represents a logically correct sentence given 
        # that cell is known to be safe.
        """In this case I need to remove the cell and change nothing in the count"""
        if cell in self.cells:
            self.cells.remove(cell)

        # If cell is not in the sentence, then no action is necessary
        

# MinesweeperAI handles inferring which moves to make based on knowledge
class MinesweeperAI():
    """
    Minesweeper game player
    """

    def __init__(self, height=8, width=8):

        # Set initial height and width
        self.height = height
        self.width = width

        # Keep track of which cells have been clicked on
        self.moves_made = set()

        # Keep track of cells known to be safe or mines
        """
        self.mines contains a set of all cells known to be mines
        """
        self.mines = set()
        """
        self.safes contains a set of all cells known to be safe
        """
        self.safes = set()

        # List of sentences about the game known to be true
        """
        self.knowledge contains a list of all of the Sentences that the AI knows to be true
        """
        self.knowledge = []

    def mark_mine(self, cell):
        """
        Marks a cell as a mine, and updates all knowledge
        to mark that cell as a mine as well.
        """
        self.mines.add(cell)
        for sentence in self.knowledge:
            sentence.mark_mine(cell)

    def mark_safe(self, cell):
        """
        Marks a cell as safe, and updates all knowledge
        to mark that cell as safe as well.
        """
        self.safes.add(cell)
        for sentence in self.knowledge:
            sentence.mark_safe(cell)

    def add_knowledge(self, cell, count):
        # accept a cell, represented as a tuple (i, j) and its corresponding count
        # update self.mines, self.safes, self.moves_made, and self.knowledge
        """
        Called when the Minesweeper board tells us, for a given
        safe cell, how many neighboring cells have mines in them.

        This function should:
            1) mark the cell as a move that has been made
            2) mark the cell as safe
            3) add a new sentence to the AI's knowledge base
               based on the value of `cell` and `count`
            4) mark any additional cells as safe or as mines
               if it can be concluded based on the AI's knowledge base
            5) add any new sentences to the AI's knowledge base
               if they can be inferred from existing knowledge
        """
        # 1) mark the cell as a move that has been made
        # self.moves_made: keep track of which cells have been clicked on 
        self.moves_made.add(cell)

        # 2) mark the cell as safe
        self.mark_safe(cell)

        # 3) add a new sentence to the AI's knowledge base based on the value of `cell` and `count`
        # I'm using a list because Sentence is expecting to receive a cell and a number for counts
        und_cells = []
        count_mines = 0
        # Loop around the mines and check if they are in self.mines = set() and self.safes = set()
        # If they are not the cell itself or mine or safe, 
        # Since the cells are tuples(i,j) is necessary to have one for row and other for column
        for i in range(cell[0] - 1, cell[0] + 2):
            for j in range(cell[1] - 1, cell[1] + 2):

                # Ignore the self.mines
                if (i,j) in self.mines:
                    # count of the cell’s neighbors are mines. 
                    count_mines += 1

                # Check if cell in bounds 
                # Ignore the cell itself and the self.safes
                if 0 <= i < self.height and 0 <= j < self.width and (i,j) not in self.safes and (i,j) not in self.mines:
                    # Be sure to only include cells whose state is still undetermined in the sentence.
                    und_cells.append((i,j))

        # Count is all the mines that exists in the game
        # Count_mines is all the mines that I already found out
        # Be sure to only include cells whose state is still undetermined in the sentence.
        # To get all the remaining mines: count - count_mines
        new_sentence = Sentence(und_cells, count - count_mines)

        # 5) add any new sentences to the AI's knowledge base if they can be inferred from existing knowledge
        self.knowledge.append(new_sentence)

        # 4) mark any additional cells as safe or as mines if it can be concluded based on the AI's knowledge base
        
        # I made a function to make the following work
        for sentence in self.knowledge:
            if sentence.known_mines():
                for cell in sentence.known_mines().copy():
                    self.mark_mine(cell)
            if sentence.known_safes():
                for cell in sentence.known_safes().copy():
                    self.mark_safe(cell)

        # Verify if new_sentence is a subset of another sentence that already exists in the self.knowledge
        # Use of issubset() -> after create a new Sentence and append
        # Checar se new_sentence e sentence tem minas
        
        for sentence in self.knowledge:
            if new_sentence.cells.issubset(sentence.cells) and sentence.count > 0 and new_sentence.count > 0 and new_sentence != sentence:
                new_subset = sentence.cells.difference(new_sentence.cells)
                new_sentence_subset = Sentence(list(new_subset), sentence.count - new_sentence.count)
                self.knowledge.append(new_sentence_subset)
        

    def make_safe_move(self):
        """
        Returns a safe cell to choose on the Minesweeper board.
        The move must be known to be safe, and not already a move
        that has been made.

        This function may use the knowledge in self.mines, self.safes
        and self.moves_made, but should not modify any of those values.
        """
        # The move must be known to be safe
        for cell in self.safes:
            # not already a move that has been made
            if cell not in self.moves_made:
                return cell
        # If no safe move can be guaranteed, the function should return None
        return None
        

    def make_random_move(self):
        """
        Returns a move to make on the Minesweeper board.
        Should choose randomly among cells that:
            1) have not already been chosen, and
            2) are not known to be mines
        """
        # Create a list with all info you already have
        cells_so_far = []
        #Random
        # Since the cells are tuples(i,j) is necessary to have one for row and other for column
        for i in range(self.height):
            for j in range(self.width):
                # Have not already been chosen, and are not known to be mines
                if (i, j) not in self.moves_made and (i, j) not in self.mines:
                    # Append this cell to the list of all available cells
                    cells_so_far.append((i,j))
        # Take a random cell from the available cells
        if len(cells_so_far) != 0:
            return random.choice(cells_so_far)
        # If no such moves are possible, the function should return None
        else:
            return None

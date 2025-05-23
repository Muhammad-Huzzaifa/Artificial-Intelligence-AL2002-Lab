class SudokuSolver:
    def __init__(self, board=None):
        """Initialize the Sudoku solver with an optional initial board"""
        self.prop_kb = PropKB()
        self.fol_kb = FolKB()
        self.board = board if board else [[0]*9 for _ in range(9)]

    def prop_sentence(self, r, c, n):
        """Create a propositional logic sentence for cell (r,c) containing number n"""
        return Expr(f'R{r}C{c}N{n}')

    def add_prop_constraints(self):
        """Add all Sudoku constraints using propositional logic"""
        # 1. Each cell contains at least one number
        for r in range(9):
            for c in range(9):
                self.prop_kb.tell(associate('|', [self.prop_sentence(r, c, n) for n in range(1, 10)]))

        # 2. Each cell contains at most one number
        for r in range(9):
            for c in range(9):
                for n1 in range(1, 10):
                    for n2 in range(n1 + 1, 10):
                        self.prop_kb.tell(~self.prop_sentence(r, c, n1) | ~self.prop_sentence(r, c, n2))

        # 3. Row constraints
        for r in range(9):
            for n in range(1, 10):
                for c1 in range(9):
                    for c2 in range(c1 + 1, 9):
                        self.prop_kb.tell(~self.prop_sentence(r, c1, n) | ~self.prop_sentence(r, c2, n))

        # 4. Column constraints
        for c in range(9):
            for n in range(1, 10):
                for r1 in range(9):
                    for r2 in range(r1 + 1, 9):
                        self.prop_kb.tell(~self.prop_sentence(r1, c, n) | ~self.prop_sentence(r2, c, n))

        # 5. 3x3 box constraints
        for box_r in range(3):
            for box_c in range(3):
                for n in range(1, 10):
                    cells = [(3*box_r + i, 3*box_c + j) 
                            for i in range(3) for j in range(3)]
                    for i, (r1, c1) in enumerate(cells):
                        for r2, c2 in cells[i+1:]:
                            self.prop_kb.tell(~self.prop_sentence(r1, c1, n) | ~self.prop_sentence(r2, c2, n))

    def fol_add_constraints(self):
        """Add all Sudoku constraints using first-order logic"""
        # 1. Each cell contains exactly one number
        for r in range(9):
            for c in range(9):
                # At least one number
                self.fol_kb.tell(expr(f'Filled({r},{c},1) | Filled({r},{c},2) | ... | Filled({r},{c},9)'))
                # At most one number
                for n1 in range(1, 10):
                    for n2 in range(n1 + 1, 10):
                        self.fol_kb.tell(expr(f'~Filled({r},{c},{n1}) | ~Filled({r},{c},{n2})'))

        # 2. Row constraints
        for r in range(9):
            for n in range(1, 10):
                for c1 in range(9):
                    for c2 in range(c1 + 1, 9):
                        self.fol_kb.tell(expr(f'~Filled({r},{c1},{n}) | ~Filled({r},{c2},{n})'))

        # 3. Column constraints
        for c in range(9):
            for n in range(1, 10):
                for r1 in range(9):
                    for r2 in range(r1 + 1, 9):
                        self.fol_kb.tell(expr(f'~Filled({r1},{c},{n}) | ~Filled({r2},{c},{n})'))

        # 4. Box constraints
        for box_r in range(3):
            for box_c in range(3):
                for n in range(1, 10):
                    cells = [(3*box_r + i, 3*box_c + j) 
                            for i in range(3) for j in range(3)]
                    for i, (r1, c1) in enumerate(cells):
                        for r2, c2 in cells[i+1:]:
                            self.fol_kb.tell(expr(f'~Filled({r1},{c1},{n}) | ~Filled({r2},{c2},{n})'))

    def add_initial_board(self, board):
        """Add the initial numbers from the board to both KBs"""
        for r in range(9):
            for c in range(9):
                if board[r][c] != 0:
                    n = board[r][c]
                    # Add to propositional KB
                    self.prop_kb.tell(self.prop_sentence(r, c, n))
                    # Add to first-order KB
                    self.fol_kb.tell(expr(f'Filled({r},{c},{n})'))

    def solve_prop(self):
        """Solve Sudoku using propositional logic"""
        self.add_prop_constraints()
        # Use DPLL to find a solution
        model = dpll_satisfiable(associate('&', self.prop_kb.clauses))
        if model:
            # Extract solution from model
            solution = [[0]*9 for _ in range(9)]
            for r in range(9):
                for c in range(9):
                    for n in range(1, 10):
                        if model.get(self.prop_sentence(r, c, n), False):
                            solution[r][c] = n
            return solution
        return None

    def solve_fol(self):
        """Solve Sudoku using first-order logic"""
        self.fol_add_constraints()
        # Use forward chaining to find a solution
        solution = [[0]*9 for _ in range(9)]
        for r in range(9):
            for c in range(9):
                for n in range(1, 10):
                    query = expr(f'Filled({r},{c},{n})')
                    if fol_fc_ask(self.fol_kb, query):
                        solution[r][c] = n
        return solution if all(all(cell != 0 for cell in row) for row in solution) else None

    def print_board(self, board):
        """Print the Sudoku board in a readable format"""
        for i, row in enumerate(board):
            if i % 3 == 0 and i != 0:
                print('-'*21)
            for j, num in enumerate(row):
                if j % 3 == 0 and j != 0:
                    print('|', end=' ')
                print(num if num != 0 else '.', end=' ')
            print()
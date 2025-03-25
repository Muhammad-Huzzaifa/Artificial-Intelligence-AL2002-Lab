class AC3:

    def __init__(self, domains : dict, constraints : list[list[str]]) -> None:
        ''' Constructor for AC3 class

        Args:
            domains: The domains of the variables
            constraints: The constraints between the variables
        '''
        self.domains = domains
        self.constraints = constraints
        
        n = len(self.constraints)
        for i in range(n):
            constraint = self.constraints[i][::-1]
            if constraint[1] == '>':
                constraint[1] = '<'
            elif constraint[1] =='>=':
                constraint[1] = '<='
            elif constraint[1] =='<':
                constraint[1] = '>'
            elif constraint[1] =='<=':
                constraint[1] = '>='
            self.constraints.append(constraint)


    def constraint_value_check(self, x, y, constraint : str) -> bool:
        ''' Check if the constraint is satisfied

        Args:
            x: The first variable
            y: The second variable
            constraint: The constraint between the variables

        Returns:
            True if the constraint is satisfied, False otherwise
        '''
        constraint = constraint[1]

        if constraint == '>':
            return x > y
        elif constraint == '>=':
            return x >= y
        elif constraint == '<':
            return x < y
        elif constraint == '<=':
            return x <= y
        elif constraint == '=':
            return x == y
        elif constraint == '!=':
            return x != y


    def ac3_algorithm(self) -> bool:
        ''' AC3 Algorithm

        Returns:
            True if the domain is arc consistent under current domains, False otherwise
        '''
        queue = self.constraints[::]

        while queue:
            Xi, Xj = queue[0][0], queue[0][-1]
            queue.pop(0)
            
            constraint = [constraint for constraint in self.constraints if constraint[0] == Xi and constraint[-1] == Xj][0]

            if self.revise(constraint, Xi, Xj):
                if not self.domains[Xi]:
                    return False
                
                for constraint in self.constraints:
                    if constraint[-1] == Xi:
                        queue.append(constraint)

        return True


    def revise(self, constraint : str, Xi : str, Xj : str) -> bool:
        ''' Revise the domain of Xi
        
        Args:
            constraint: The constraint between the variables
            Xi: The first variable
            Xj: The second variable

        Returns:
            True if the domain is revised, False otherwise
        '''
        rev = False

        for x in self.domains[Xi]:
            if not any(self.constraint_value_check(x, y, constraint) for y in self.domains[Xj]):
                self.domains[Xi].remove(x)
                rev = True
        
        return rev
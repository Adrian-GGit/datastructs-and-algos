import pprint

class NeedlemanWunsch:
    
    def __init__(self, x: str, y: str, verbose: bool = False) -> None:
        self.x = x
        self.y = y
        self.table = []
        self.verbose = verbose
        self.width = len(y)+1                    
        self.height = len(x)+1
        self.table.append(list(range(self.width)))
        self.deletes = []
        for h in range(1, self.height):
            row = [h] + [-1]*len(y)
            self.table.append(row)

    def print(self) -> None:
        if self.verbose:
            pprint.pprint(self.table)

    def print_alignment(self) -> None:
        print(f"X: {self.x}")
        print(f"y: {self.y}")
        print(f"A: {self.alignment}  (deleted {', '.join(self.deletes) or 'none'})")

    def process(self) -> None:
        for ix in range(1, self.height):
            for iy in range(1, self.width):
                a =self.table[ix-1][iy]+1
                b = self.table[ix][iy-1]+1
                c = self.table[ix-1][iy-1] + self.substitute(ix, iy)
                self.table[ix][iy] = min(a,b,c)
            
    def substitute(self, i, j) -> int:
        return 1 if self.y[j-1] != self.x[i-1] else 0

        
    def extract_alignment(self):
        def get_operation(a, b) -> int:
            substitution = self.table[a-1][b-1]
            deletion = self.table[a-1][b]
            insertion = self.table[a][b-1]
            m = min(substitution, deletion, insertion)
            if substitution == m:
                return 1
            if deletion == m:
                return 2
            return 3

        i = self.height-1
        j = self.width-1
        alignment = []
        while i > 0 and j > 0:
            op = get_operation(i, j)
            if op == 1:  # subst
                i -= 1
                j -= 1
                alignment.append(self.y[j])
            elif op == 2: # deletion
                alignment.append("")
                self.deletes.append(self.x[i-1])
                i -= 1
            else:  # insertion
                alignment.append("-")
                j -= 1
        alignment.reverse()
        self.alignment = ''.join(alignment)
        self.print_alignment()
        return self.alignment

N = NeedlemanWunsch("amoney", "mokknkkey")
N.process()
N.print()
print("x aligned to y:")
N.extract_alignment()
print("--")
N = NeedlemanWunsch("monkkafey", "money")
N.process()
N.print()
print("y aligned to x:")
N.extract_alignment()
'''
Created by Lorenzo Mambretti
Dec 11, 2017
A simple python script to fit propositions and theorems in a graph.
Each node is a proposition, and the edge is a theorem
Finding a proof of a theorem means finding an alternative path between two nodes.
'''

class Theorem():

    def __init__(self, start, ending = [], name = "", bijective = False):
        self.ending = ending
        self.start = start
        self.name = name
        for s in start:
            s.add_theorem(self)
        
        if bijective:
            for e in ending:
                Theorem(ending, start, name)

    def apply(self, value, referee):
        
        for n in self.ending:
            if n.visited:
                continue
            else:
                n.value = value
                n.referee = referee
                for s in self.start:
                    print("Given",referee, s.proposition)
                print("for",self.name,n.referee, n.proposition)
                n.propagate(n.value, referee)

class Statement():
    referee = ""
    
    def __init__(self, proposition = ""):
        self.proposition = proposition
        self.value = None
        self.visited = False
        self.thms = []

    def propagate (self, value, referee):
        if self.visited == False:
            self.visited = True
            self.value = value
            for t in self.thms:
                t.apply(self.value, referee)

    def add_theorem(self,theorem):
        self.thms.append(theorem)


compact_set = Statement("is compact")
closed_set = Statement("is closed")
open_set = Statement("is open")
bounded_set = Statement("is bounded")
has_supremum = Statement("has supremum")
is_CauchySeq = Statement("is a cauchy sequence")
converges = Statement("converges")
contain_lp = Statement("contains all its limit points")
is_lp = Statement("is a limit points")
Th334 = Theorem([compact_set], [closed_set, bounded_set], name = "Characterization of Compactness in R", bijective = True)
AoC = Theorem([bounded_set], [has_supremum], name = "Axiom of Completeness")
CauchyCr = Theorem([is_CauchySeq], [converges], name = "Cauchy Criterion")
Theorem([closed_set],[contain_lp], name = "definition of closed set", bijective = True)
Theorem([contain_lp],[is_lp])
Theorem([is_lp],[converges], name = "definition of limit point")

compact_set.propagate(True, "the set A")

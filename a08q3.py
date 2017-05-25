## Class definition of Budget and associated methods and properties of the class.

class Budget:
    '''Fields: month(Str), withdrawals (listof Nat), deposits (listof Nat),
          requires: month has format MONXX where:
          - MON is one of JAN,FEB,MAR,APR,MAY,JUN,JUL,AUG,SEP,OCT,NOV,DEC
          - XX is a 2-digit year starting from 00
          (e.g.MAR00 represents March 2000)'''  
    
    def __init__(self,mnth,low,lod):
        self.month = mnth
        self.withdrawals = low
        self.deposits = lod
        
    def __repr__(self):
        s = "Budget for the month of {0}:\nWithdrawals:{1}\nDeposits:{2}\nNet:{3}"
        return s.format(self.month,
                        self.withdrawals,
                        self.deposits,
                        sum(self.deposits) - sum(self.withdrawals))
    
    def __eq__(self, other):
        return type(other) == type(self) and self.month == other.month and \
               self.withdrawals == other.withdrawals and self.deposits == other.deposits  
        
## add_transactions(self,lot) is a method that consumes a list of transactions, lot and adds the
## withdrawals and deposits in the appropriate properties list (low,lod) and produces
## the net difference between the two properties.
## Effects: the object, self is mutated.
## add_transactions: object (listof Int) -> Int
## Examples:
## b1.add_transactions([9]) => 9
## b1.add_transaction([-9]) => -9

    
    def add_transactions(self,lot):
        for i in lot:
           if i<0:
                self.withdrawals.append(-i)
           else:
                self.deposits.append(i)
        self.net=(sum(self.deposits))-(sum(self.withdrawals))
        return self.net
    
# end of Budget class

## Examples of Budget:
b1=Budget("FEB00",[],[])
b2=Budget("JAN00",[2],[])
b3=Budget("MAR00",[],[5])
b4=Budget("JUN01",[4,2,3],[])
b5=Budget("APR00",[],[3,4,2])
b6=Budget("JUL01",[8,6,12,3],[100,12])






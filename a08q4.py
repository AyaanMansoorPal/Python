##
## *********************************
## Ayaan Mansoor Pal 
## *********************************
##

import check
## Budget Class:

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

## End of Budget Class        

## Useful Examples and Constants:
budgets1=[Budget("MAR17",[],[10,10]),
          Budget("FEB17",[5,22],[30,10]),
          Budget("JAN17",[2,7,3,8],[5,10,20]),
          Budget("DEC16",[25],[]),
          Budget("NOV16",[5,10,10,5],[30,5])]
budgets2=[Budget("MAR16",[],[])]
budgets3=[Budget("NOV17",[29],[30]),
          Budget("OCT16",[10],[20])]
budgets4=[Budget("FEB16",[],[]),
          Budget("DEC17",[90,20,10],[30,20,10]),
          Budget("MAR16",[20,90,10],[10,26,23,30])]
budgets5=[Budget("JUN10",[],[]),
          Budget("JUL12",[],[]),
          Budget("AUG13",[],[])]
budgets6=[Budget("JAN00",[30,20,12],[50]),
          Budget("JUL02",[],[]),
          Budget("DEC09",[30],[0])]
budgets7=[Budget("FEB20",[20,30,20,10],[30,90,100,30]),
          Budget("DEC10",[30,30,30],[30,90,100]),
          Budget("OCT04",[30],[1])]
budgets8=[Budget("JAN09",[20,10,30],[50,30]),
          Budget("FEB20",[],[10]),
          Budget("MAR30",[10],[50]),
          Budget("APR09",[30],[])]


## best_and_worst(lob) consumes a list of Budgets called lob and finds the months
## in which the best deposit took place and the worst withdrawals took place and
## produces a dictionary where these results are stored. The keys in the dictionary are
## are the labels for the values.
## best_and_worst: (listof Budget)-> (dictof Str (anyof (listof Str) Nat))
## requires: lob to be non-empty
## Examples:
         
def best_and_worst(lob):
   withdrawals=[]
   deposits=[]
   
   for m in range(len(lob)):
       for o in range(len(lob[m].withdrawals)):
         if lob[m].withdrawals!=[]:
            withdrawals.append(lob[m].withdrawals[o])
   
   if withdrawals==[]:
       maxW=0
   else:
       maxW=max(withdrawals)
   
   for i in range(len(lob)):
      for j in range(len(lob[i].deposits)): 
          if lob[i].deposits!=[]:
            deposits.append(lob[i].deposits[j])
   
   if deposits==[]:
        maxD=0
   else:
        maxD=max(deposits)
   
   W_months=[]
   D_months=[]
   for i in lob:
     if maxW in i.withdrawals:
            W_months.append(i.month)
     if maxD in i.deposits:
            D_months.append(i.month)
  
   budget_dict={'D_months': D_months,
                  'W_months':W_months,
                  'maxW':maxW,
                  'maxD':maxD}
   return budget_dict

## Tests:
## Test 1:
check.expect("Q4T1",best_and_worst(budgets1),{'D_months':["FEB17","NOV16"],
                                              'W_months':["DEC16"],
                                              'maxW':25,
                                              'maxD':30})
## Test 2:
check.expect("Q4T2",best_and_worst(budgets2),{'D_months':[],
                                              'W_months':[],
                                              'maxW':0,
                                              'maxD':0})
## Test 3:
check.expect("Q4T3",best_and_worst(budgets3),{'D_months':["NOV17"],
                                              'W_months':["NOV17"],
                                              'maxW':29,
                                              'maxD':30})
## Test 4:
check.expect("Q4T4",best_and_worst(budgets4),{'D_months':["DEC17","MAR16"],
                                              'W_months':["DEC17","MAR16"],
                                              'maxW':90,
                                              'maxD':30})
## Test 5:
check.expect("Q4T5",best_and_worst(budgets5),{'D_months':[],
                                              'W_months':[],
                                              'maxW':0,
                                              'maxD':0})
## Test 6:
check.expect("Q4T6",best_and_worst(budgets6),{'D_months':["JAN00"],
                                              'W_months':["JAN00","DEC09"],
                                              'maxW':30,
                                              'maxD':50})
## Test 7:
check.expect("Q4T7",best_and_worst(budgets7),{'D_months':["FEB20","DEC10"],
                                              'W_months':["FEB20","DEC10","OCT04"],
                                              'maxW':30,
                                              'maxD':100})
## Test 8:
check.expect("Q4T8",best_and_worst(budgets8),{'D_months':["JAN09","MAR30"],
                                              'W_months':["JAN09","APR09"],
                                              'maxW':30,
                                              'maxD':50})
                                                          



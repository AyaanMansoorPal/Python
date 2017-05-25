##
## *********************************
## Ayaan Mansoor Pal 
## *********************************
##

import check

## Important and useful constants:
invalid_msg = "Invalid update"


## a Team is a Str
## requires: the value is the name of a city

## a Scoresheet is a Str and represents a set of results over
## one or more games for a given team, e.g. "WLLTW"
## requires: non-empty and each character is (anyof "W" "L" "T")

## update_standings(curr_stats,weekly_result) consumes two dictionaries, curr_standings
## and weekly_result, and mutates the points of each entry in curr_stats according to the
## Scoresheet in weekly_result points. If the team does not exist in curr_standings
## then the invalid_msg is printed.
## Effects: the values in curr_stats are mutated according to the Scoresheet.
##          If an entry in weekly_result is not in curr_stats, "Invalid update" is printed.
## update_standings: (dictof Team Nat) (dictof Team Scoresheet) -> None
## Examples:

def update_standings(curr_stats, weekly_result):
    if curr_stats=={}:
        print(invalid_msg)
        return None
    else:
       for m in weekly_result:
            if m in curr_stats:
                score=0
                for o in weekly_result[m]:
                    if o=="W":
                        score=score+2
                    elif o=="L":
                        score=score+0
                    elif o=="T":
                        score=score+1
                curr_stats[m]=curr_stats[m]+score
            else:
                print(invalid_msg)
                return None

## Tests:
## Test 1:
curr={}
weekly={"Ottawa":"W"}
check.set_screen(invalid_msg)
check.expect("Q1T001",update_standings(curr,weekly),None)
check.expect("Q1T01",curr,curr)
## Test 2:
curr={"Montreal":23}
weekly={}
check.expect("Q1T002",update_standings(curr,weekly),None)
check.expect("Q1T02",curr,{"Montreal":23})
## Test 3:
curr={"Montreal":0}
weekly={"Edmonton":"W"}
check.set_screen(invalid_msg)
check.expect("Q1T003",update_standings(curr,weekly),None)
check.expect("Q1T03",curr,{"Montreal":0})
## Test 4:
curr={"Montreal":0}
weekly={"Montreal":"W"}
check.expect("Q1T004",update_standings(curr,weekly),None)
check.expect("Q1T04",curr,{"Montreal":2})
## Test 5:
curr={"Montreal":0}
weekly={"Montreal":"L"}
check.expect("Q1T005",update_standings(curr,weekly),None)
check.expect("Q1T05",curr,{"Montreal":0})
## Test 6:
curr={"Montreal":0}
weekly={"Montreal":"T"}
check.expect("Q1T006",update_standings(curr,weekly),None)
check.expect("Q1T06",curr,{"Montreal":1})
## Test 7:
curr={"Montreal":0}
weekly={"Montreal":"WTL"}
check.expect("Q1T007",update_standings(curr,weekly),None)
check.expect("Q1T07",curr,{"Montreal":3})
## Test 8:
curr={"Montreal":0}
weekly={"Montreal":"WTT"}
check.expect("Q1T008",update_standings(curr,weekly),None)
check.expect("Q1T08",curr,{"Montreal":4})
## Test 9:
curr={"Montreal":0}
weekly={"Montreal":"WWW"}
check.expect("Q1T009",update_standings(curr,weekly),None)
check.expect("Q1T09",curr,{"Montreal":6})
## Test 10:
curr={"Winnipeg":10,
      "Lahore":20,
      "Islamabad":100}
weekly={"Lahore":"LLL",
        "Winnipeg":"WWWW",
        "Islamabad":"TTTTT"}
check.expect("Q1T010",update_standings(curr,weekly),None)
check.expect("Q1T10",curr,{"Winnipeg":18,
                           "Lahore":20,
                           "Islamabad":105})
## Test 11:
curr={"Montreal":0,
      "Waterloo":50}
weekly={"Waterloo":"L",
       "Montreal":"TWLTWL"}
check.expect("Q1T011",update_standings(curr,weekly),None)
check.expect("Q1T11",curr,{"Montreal":6,
                           "Waterloo":50})
                
## Test 12:
curr={"Montreal":10,
      "Lahore":20,
      "Trinidad":30,
      "Waterloo":30}
weekly={"Waterloo":"WWW",
        "Trinidad":"L",
        "Lahore":"TWLW",
        "Montreal":"WWWW",
        "Tokyo":"WWWWWWW"}
check.set_screen(invalid_msg)
check.expect("Q1T012",update_standings(curr,weekly),None)
check.expect("Q1T12",curr,curr)

                
    

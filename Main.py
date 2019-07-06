from finite_automata import NFA, DFA
from Minimization import DFA_MIN


print("start:")
number_of_states = int(input())
alphabet = input().split(",")
alph = ""
for  i in alphabet:
    alph = alph + i
transitions_and_states = []
rules = int(input("Number of Rules:"))
while (rules > 0):
    rules -= 1
    transitions_and_states.append(input())

start_state = []
final_sates = []

for i in transitions_and_states:
    temp = i.split(",")
    if (temp[0].startswith("->")):
        start_state.append(int(temp[0][3:]))

    for j in temp:
        if (j.startswith("*") and (int(j[2:]) not in final_sates )):
            final_sates.append(int(j[2:]))

transition_functions = []
def make_tuple(list):
    res = (int(list[0]) , list[1] , int(list[2]))
    return res
transitions = []

for i in transitions_and_states:
    temp = i.split(",")
    start = temp[0]
    symbol = temp[1]
    end = temp[2]
    k = temp[0].index("q")
    start = int(start[(k + 1):])
    k = temp[2].index("q")
    end = int(end[(k + 1):])
    temp = (start,symbol,end)

    transitions.append(temp)



final = ""
for i in range(0,len(final_sates)):
    if (i == 0):
        final = final + str(final_sates[i])
    else:
        final = final + " " + str(final_sates[i])




Name = "test.txt"
MyFile = open(Name,'w')
MyFile.write(str(number_of_states) + "\n")
MyFile.write(alph + "\n")
MyFile.write(final + "\n")
MyFile.write(str(start_state[0]) + "\n")
for i in transitions:
    temp = str(i[0]) + " " + str(i[1]) + " " + str(i[2]) + "\n"
    MyFile.write(temp)
MyFile.close()



filename = "test.txt"
file = open(filename, 'r')
lines = file.readlines()
file.close()


nfa = NFA()
dfa = DFA()

nfa.construct_nfa_from_file(lines)
dfa.convert_from_nfa(nfa)
dfa.print_dfa()



dfa = DFA_MIN("DFA.txt",None,None,None,None)
dfa._remove_unreachable_states()
dfa.minimize()
print(dfa)





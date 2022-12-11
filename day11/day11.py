input_file = open("day11.txt")

class Monkey:
    def __init__(self, starting : list, operation : str, operator : str, divisor : int, true_decision : int, false_decision : int):
        self.items = starting
        self.op = operation
        self.operator = operator
        self.divisor = divisor
        self.t_decision = true_decision
        self.f_decision = false_decision
        
    def __str__(self) -> str:
        return f"Items: {self.items}\nOperation: new = old {self.op} {self.operator}\nTest: divisible by {self.divisor}\n  If true: throw to {self.t_decision}\n  If false: throw to {self.f_decision}"

monkeys = []
lines = []
for line in input_file:
    if line != "\n" and line != "":
        lines.append(line)
    else:
        starting = list(map(int, str(lines[1]).split(':')[1].strip().split(',')))
        op = str(lines[2]).split()[4]
        operator = str(lines[2]).split()[5]
        divisor = str(lines[3]).split()[3]
        true = str(lines[4]).split()[5]
        false = str(lines[5]).split()[5]
        monkeys.append(Monkey(starting, op, operator, int(divisor), int(true), int(false)))
        lines = []
        
for m in monkeys:
    print(m)
input_file = open("day11.txt")

class Monkey:
    def __init__(self, starting : list[int], operation : str, operator : str, divisor : int, true_decision : int, false_decision : int):
        self.items : list[int] = starting
        self.op = operation
        self.operator = operator
        self.divisor = divisor
        self.t_decision = true_decision
        self.f_decision = false_decision
        self.inspected_count = 0
        
    def __str__(self) -> str:
        return f"Items: {self.items}\nOperation: new = old {self.op} {self.operator}\nTest: divisible by {self.divisor}\n  If true: throw to {self.t_decision}\n  If false: throw to {self.f_decision}"

monkeys : list[Monkey] = []
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
    
current_round = 1
while current_round <= 20:
    current_monkey = 0
    for m in monkeys:
        print(f"Monkey {current_monkey}")
        while len(m.items) > 0:
            item = m.items[0]
            print(f"inspecting item with value {item}")
            #apply operation to worry
            if m.op == '+':
                if m.operator == 'old':
                    item += item
                else:
                    item += int(m.operator)  
                print(f"value is increased by {m.operator} to {item}")
            elif m.op == '*':
                if m.operator == 'old':
                    item = item ** 2
                else:
                    item = item * int(m.operator)
                print(f"value is multipled by {m.operator} to {item}")
            #divide worry
            item //= 3
            print(f"value is divided by 3 to {item}")
            #test item
            test = False
            if (item % m.divisor) == 0:
                test = True
                print(f"item is divisible by {m.divisor}")
            else:
                print(f"item is not divisible by {m.divisor}")
            #throw item
            throw_to = m.t_decision if test else m.f_decision
            monkeys[throw_to].items.append(item)
            print(f"item with value {item} thrown to monkey {throw_to}\n")
            m.inspected_count += 1
            m.items.pop(0)
        current_monkey += 1
    if current_round % 5 == 0:
        print(f"after {current_round} rounds:")
        i = 0
        for m in monkeys:
            print(f"Monkey {i}: {m.items}")
            i += 1
    
    current_round += 1

print("\n")
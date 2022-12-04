from utils import read_file

def compute_priority(item):
    if(item.isupper()):
         return 26 + ord(item) - 64
    else:
        return ord(item) - 96

def get_priority_sum(input):
    priority_sum = 0
    for rucksack in input:
        comp1 = rucksack[:len(rucksack)//2]
        comp2 = rucksack[len(rucksack)//2:]
        for item in comp1:
            if item in comp2:
                priority_sum += compute_priority(item)
                break
    return priority_sum

def get_common_items(input):
    priority_sum = 0
    group = []
    for rucksack in input:
        group.append(rucksack)
        if len(group) == 3:
            common = set(group[0]).intersection(set(group[1])).intersection(set(group[2]))
            priority_sum += compute_priority(list(common)[0])
            group = []

    return priority_sum

if __name__=="__main__":
    data = "data/day03.txt"
    input = read_file(data)

    priority_sum = get_priority_sum(input)
    print(f'Total priority: {priority_sum}')
    common_priority_sum = get_common_items(input)
    print(f'Commonon priority sum: {common_priority_sum}')

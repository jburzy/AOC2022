from utils import read_file

def count_overlapping_pairs(input):
    count = 0
    for pair in input:
        pair = pair.split(',')
        range1 = pair[0].split('-')
        range1 = range(int(range1[0]),int(range1[1])+1)
        range2 = pair[1].split('-')
        range2 = range(int(range2[0]),int(range2[1])+1)
        if len(list(set(range1).intersection(set(range2)))) != 0:
            count += 1
    return count

def count_fully_contained_pairs(input):
    count = 0
    for pair in input:
        pair = pair.split(',')
        range1 = pair[0].split('-')
        range2 = pair[1].split('-')
        if int(range1[0]) >= int(range2[0]) and int(range1[1]) <= int(range2[1]):
            count += 1
        elif int(range2[0]) >= int(range1[0]) and int(range2[1]) <= int(range1[1]):
            count += 1
    return count


if __name__=="__main__":
    data = "data/day04.txt"
    input = read_file(data)

    counts1 = count_fully_contained_pairs(input)
    print(f'Total number of fully overlapping pairs: {counts1}')
    counts2 = count_overlapping_pairs(input)
    print(f'Total number of overlapping pairs: {counts2}')


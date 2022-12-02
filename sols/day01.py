from utils import read_file

def get_max_cal(input):
    max_cal = 0
    tmp_cal = 0
    for val in input:
        # we have reached the end of one elf's inventory
        if val == '':
            if tmp_cal > max_cal:
                max_cal = tmp_cal
            tmp_cal = 0
        else:
            tmp_cal += int(val)
    return max_cal

def get_top_3_cal(input):
    cal_totals = []
    tmp_cal = 0
    for val in input:
        # we have reached the end of one elf's inventory
        if val == '':
            cal_totals.append(tmp_cal)
            tmp_cal = 0
        else:
            tmp_cal += int(val)
    return sum(sorted(cal_totals)[-3:])

if __name__=="__main__":
    data = "data/day01.txt"
    input = read_file(data)

    max_cal = get_max_cal(input)
    print(f'The elf carrying the most calories has: {max_cal} Cal')
    top_3_cal = get_top_3_cal(input)
    print(f'The elves carrying the top 3 most calories have: {top_3_cal} Cal')

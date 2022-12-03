from utils import read_file

scores = {'rock': 1,'paper': 2,'scissor': 3}
player1_code = {'A': 'rock', 'B': 'paper', 'C': 'scissor'}

choice_to_score = {
    'rock': {'rock': 3,'paper': 0,'scissor': 6},
    'paper': {'rock': 6,'paper': 3,'scissor': 0},
    'scissor': {'rock': 0,'paper': 6,'scissor': 3}
}
score_to_choice = {
    6: {'rock': 'paper',   'paper': 'scissor', 'scissor': 'rock'},
    3: {'rock': 'rock',    'paper': 'paper',   'scissor': 'scissor'},
    0: {'rock': 'scissor', 'paper': 'rock',    'scissor': 'paper'}
}

def get_score_1(input):
    player2_code = {'X': 'rock','Y': 'paper', 'Z': 'scissor'}
    total_score = 0
    for round in input:
        values = round.split(' ')
        player1 = player1_code[values[0]]
        player2 = player2_code[values[1]]

        choice_score = scores[player2]
        round_score = choice_to_score[player2][player1]
        
        total_score += choice_score + round_score
    return total_score

def get_score_2(input):
    result_code = {'X': 0,'Y': 3, 'Z': 6}
    total_score = 0
    for round in input:
        values = round.split(' ')
        # get player1's choice
        player1 = player1_code[values[0]]
        # get the final round score
        round_score = result_code[values[1]]
        # determine what player2 needs to play to 
        # achieve the round score
        player2 = score_to_choice[round_score][player1]
        # get the corresponding score for player2
        choice_score = scores[player2]
        
        total_score += choice_score + round_score
    return total_score

if __name__=="__main__":
    data = "data/day02.txt"
    input = read_file(data)

    score1 = get_score_1(input)
    print(f'Total score part1: {score1}')
    score2 = get_score_2(input)
    print(f'Total score part2: {score2}')

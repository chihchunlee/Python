import random,time

def roll_dice(n):
    dice = []
    for i in range(n):
        dice.append(random.randint(1,6))
    return dice

def find_winner(cdice_list,udice_list):
    computer_total = sum(cdice_list)
    user_total = sum(udice_list)
    print('電腦總分',computer_total)
    print('使用者總分',user_total)
    if user_total > computer_total:
        print('使用者贏')
    elif user_total < computer_total:
        print('電腦贏')
    else:
        print('平手')

def roll_again(choices,dice_list):
    print('重骰')
    time.sleep(3)
    for i in range(len(choices)):
        if choices[i] == 'r':
            dice_list[i] = random.randint(1,6)
    time.sleep(3)

def computer_strategy1(n):
    print('電腦在思考...')
    time.sleep(3)

    choices = ''
    for i in range(n):
        choices = choices + 'r'
    return choices

def computer_strategy2(n):
    print('電腦在思考...')
    time.sleep(3)

    choices = ''
    for i in range(n):
        if computer_rolls[i] < 5:
            choices = choices + 'r'
        else:
            choices = choices + '-'

    return choices

number_dice = input('輸入骰子數:')
number_dice = int(number_dice)
ready = input('準備好開始了嗎?按任意鍵繼續')
user_rolls = roll_dice(number_dice)
print('第一次骰的結果:',user_rolls)

user_choices = input('輸入-保留或輸入r重骰:')
while len(user_choices) != number_dice:
    print('您必須輸入=',number_dice,'長度')
    user_choices = input('輸入-保留或輸入r重骰:')
roll_again(user_choices,user_rolls)
print('玩家重骰',user_rolls)


print('輪到電腦')
computer_rolls = roll_dice(number_dice)
print('電腦第一次骰的結果:',computer_rolls)

cprandom = [computer_strategy1(number_dice),computer_strategy2(number_dice)]

computer_choices = random.choices(cprandom)
print('電腦選擇',computer_choices)

roll_again(computer_choices,computer_rolls)
print('電腦重骰',computer_rolls)

find_winner(computer_rolls,user_rolls)




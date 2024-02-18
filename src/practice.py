import random
import data

def generate_data(index_data = {}) -> {}:

    status_min = index_data.get("status_min")
    if status_min == None:
        status_min = 0
    points_min = index_data.get("points_min")
    if points_min == None:
        points_min = 0
    double_min = index_data.get("double_min")
    if double_min == None:
        double_min = 0
    type_min = index_data.get("type_min")
    if type_min == None:
        type_min = 0

    status_max = index_data.get("status_max")
    if status_max == None:
        status_max = len(data.PLAYER_STATUS)-1
    points_max = index_data.get("points_max")
    if points_max == None:
        points_max = len(data.SCORE_POINTS)-1
    double_max = index_data.get("double_max")
    if double_max == None:
        double_max = len(data.SCORE_DOUBLE)-1
    type_max = index_data.get("type_max")
    if type_max == None:
        type_max = len(data.ATTACK_TYPE)-1

    # ランダムで出題するため、それぞれのdataのindexをランダムで取得
    status_index = random.randint(status_min, status_max)
    points_index = random.randint(points_min, points_max)
    double_index = random.randint(double_min, double_max)
    type_index = random.randint(type_min, type_max)

    # ランダムで取得したindexに該当する値を取得
    q_status = data.PLAYER_STATUS[status_index]
    q_points = data.SCORE_POINTS[points_index]
    q_double = data.SCORE_DOUBLE[double_index]
    q_type = data.ATTACK_TYPE[type_index]

    # 正解の値
    correct_answer = data.DATA[q_status][q_points][q_double][q_type]

    return {
        "question": f'{q_status}の{q_points}{q_double}{q_type}',
        "correct_answer": correct_answer
    }

def question(index_data = {}) -> str:
    # 問題文の生成
    generated_question = generate_data(index_data)

    # 出題
    print(generated_question["question"])

    # プレイヤーの回答を標準入力で取得
    player_answer = input()

    # 正誤判定
    # 等しい場合は「正解」と出力
    correct_answer = generated_question["correct_answer"]
    if correct_answer == player_answer:
        return "success"
    else:
        # 正解がno-dataの場合、それっぽいある程度の文言を許容する
        if correct_answer == "no-data" and player_answer in data.NO_DATA:
            return "success"
        else: 
            return correct_answer

def practice():

    result = question()

    if result == "success":
        print("SUCCESS")
    else:
        print(f"FAILURE, {result} IS CORRECT")

def game():
    count = 0
    willStartNextGame = True
    while willStartNextGame:
        result = question()
        if result == "success":
            count+=1
        else:
            print(f"{result} IS CORRECT, FINISH {count} GAMES")
            willStartNextGame = False

def gameEasy():
    count = 0
    willStartNextGame = True
    while willStartNextGame:
        result = question({"points_min":2})
        if result == "success":
            count+=1
        else:
            print(f"{result} IS CORRECT, FINISH {count} GAMES")
            willStartNextGame = False
from collections import defaultdict

def solution(genres, plays):
    answer = []
    top_gen = []
    total_dict = defaultdict(list); count_dict = defaultdict(list)

    for i, (g, p) in enumerate(zip(genres, plays)):
        total_dict[g].append((p, i))

    for k, v in total_dict.items():
        sum = 0
        for v in total_dict[k]: sum += int(v[0])
        count_dict[k] = sum

    sort_dict = sorted(count_dict.items(), key = lambda x:x[1], reverse = True)
    for i, v in enumerate(sort_dict):
        if  i < 2: top_gen.append(v[0])

    for v in top_gen:
        song = total_dict[v]
        song.sort()

        if len(song) < 2:
            answer.append(song[-1][1])
            continue

        if(song[-1][0] == song[-2][0] and song[-1][1] > song[-2][1]):
            answer.append(song[-2][1])
            answer.append(song[-1][1])
        else:
            answer.append(song[-1][1])
            answer.append(song[-2][1])

    return answer
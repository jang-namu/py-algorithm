def solution(genres, plays):
    best_album = dict()

    length = len(genres)
    for number, genre, play in zip(range(length), genres, plays):
        if genre not in best_album:
            best_album[genre] = []
        best_album[genre].append((play, number))

    sorted_genres = sorted(list(best_album.keys()),
                           key=lambda x: sum(t[0] for t in best_album[x]),
                           reverse=True)

    for key in best_album:
        best_album[key] = sorted(best_album[key],
                                 key=lambda x: [x[0], -x[1]], reverse=True)

    answer = []
    for key in sorted_genres:
        genres_counts = min(2, len(best_album[key]))
        for idx in range(genres_counts):
            answer.append(best_album[key][idx][1])

    return answer
competitions = [
    ["HTML", "C#"],
    ["C#", "Python"],
    ["Python", "HTML"],
]
results = [0, 0, 1]


def tournament_winner(competitions, results):
    curBestTeam = ""
    scores = {curBestTeam: 0}

    for idx, competition in enumerate(competitions):
        result = results[idx]
        homeTeam, awayTeam = competition

        winTeam = homeTeam if result == 1 else awayTeam

        update_score(winTeam, 3, scores)

        if scores[winTeam] > scores[curBestTeam]:
            curBestTeam = winTeam

    return curBestTeam


def update_score(team, points, scores):
    if team not in scores:
        scores[team] = 0

    scores[team] += points


print(tournament_winner(competitions, results))

def solution(points, routes):
    answer = 0
    coord = dict()
    for i in range(len(routes)):
        t = 0
        for j in range(len(routes[i]) - 1):
            start = points[routes[i][j] - 1]
            end = points[routes[i][j + 1] - 1]
            x = start[0]
            y = start[1]
            if start[0] < end[0]:
                dx = 1
            else:
                dx = -1
            if start[1] < end[1]:
                dy = 1
            else:
                dy = -1
            while True:
                if (x == end[0] and y == end[1]):
                    break
                if (t, x, y) not in coord:
                    coord[(t, x, y)] = 0
                elif coord[(t, x, y)] == 0:
                    coord[(t, x, y)] += 1
                    answer += 1
                t += 1
                if x != end[0]:
                    x += dx
                    continue
                if y!= end[1]:
                    y += dy
        if (t, x, y) not in coord:
            coord[(t, x, y)] = 0
        elif coord[(t, x, y)] == 0:
            coord[(t, x, y)] += 1
            answer += 1
    return answer
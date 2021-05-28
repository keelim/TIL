def solution(n, t, m, timetable):

    timetable: list = [
        int(time[:2])*60 + int(time[3:])
        for time in timetable
    ]
    timetable.sort()

    current = 540

    for ele1 in range(n):
        for ele2 in range(m):
            if timetable and timetable[0] <= current:
                candidate = timetable.pop(0)-1
            else:
                candidate = current
        current += t

    h, m = divmod(candidate, 60)
    return str(h).zfill(2)+':'+str(m).zfill(2)


def calcTime(froms, to):
    fh, fm = froms.split(':')
    th, tm = to.split(':')
    hour = int(th)-int(fh)
    minute = int(tm)-int(fm)
    return hour*60 + minute


def changeSheet(sheet):
    sheet = sheet.replace('A#', 'a')
    sheet = sheet.replace('C#', 'c')
    sheet = sheet.replace('D#', 'd')
    sheet = sheet.replace('F#', 'f')
    sheet = sheet.replace('G#', 'g')
    sheet = sheet.replace('E#', 'e')
    return sheet


def solution(m, musicinfos):
    answer = '(None)'
    m = changeSheet(m)
    dic = {}
    for music in musicinfos:
        f, to, title, sheet = music.split(',')
        playingTime = calcTime(f, to)
        sheet = changeSheet(sheet)
        dic[title] = playingTime
        if playingTime > len(sheet):
            sheet = sheet*((playingTime//len(sheet))+1)
            sheet = sheet[:playingTime]
        elif playingTime < len(sheet):
            sheet = sheet[:playingTime]

        if m in sheet:
            if answer == '(None)':
                answer = title
            elif answer != '(None)':
                if dic[title] > dic[answer]:
                    answer = title

    return answer

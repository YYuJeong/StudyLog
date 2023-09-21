def solution(files):
    decomp = []

    for idx, file in enumerate(files):
        file = file.lower()
        num = False
        decomp.append([idx, '', ''])
        for i, c in enumerate(file):
            if c.isdigit():
                num = True
                decomp[-1][2] += c
            else:
                if num:
                    break
                decomp[-1][1] += c
        decomp[-1][2] = int(decomp[-1][2])
    decomp = sorted(decomp, key=lambda x: (x[1], x[2], x[0]))

    return [files[v[0]] for v in decomp]

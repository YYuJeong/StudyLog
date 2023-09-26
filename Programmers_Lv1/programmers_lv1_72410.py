def solution(new_id):
    answer = ''
    
    new_id = new_id.lower()
    possible_str = "._-abcdefghijklmnopqrstuvwxyz0123456789"
    
    dot_cnt = 0
    for idx, c in enumerate(new_id):

        if c not in possible_str:
            new_id = new_id.replace(c, '')
        
        if c == '.':
            dot_cnt += 1
            if dot_cnt >= 2:
                new_id = new_id.replace('.'*dot_cnt, '.')
                dot_cnt = 0          

    while new_id.startswith('.') or new_id.endswith('.'):
        if new_id.startswith('.'):
            new_id = new_id[1:]
        if new_id.endswith('.'):
            new_id = new_id[:-1]
    
    if new_id == '':
        new_id += 'a'
    
    if len(new_id) >= 16:
        new_id = new_id[:15]
        if new_id.endswith('.'):
            new_id = new_id[:-1]
            
    if len(new_id) <= 2:
        while len(new_id) < 3:
            new_id += new_id[-1]
            
    return new_id
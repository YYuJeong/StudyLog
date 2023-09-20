def solution(board, moves):
    answer = 0
    basket = []
    
    for move in moves:
        for idx in range(len(board)):
            if board[idx][move-1] != 0:
                basket.append(board[idx][move-1])
                board[idx][move-1] = 0
                if len(basket) > 1 and basket[-1] == basket[-2]:
                    answer += 2
                    basket = basket[:-2]
def knight_tour(N, startX, startY):
    # 騎士的八個可能移動方向
    moves = [
        (-2, 1), (-2, -1), (2, 1), (2, -1),
        (1, 2), (1, -2), (-1, 2), (-1, -2)
    ]
    
    # 初始化棋盤，False 表示尚未訪問
    board = [[False for _ in range(N)] for _ in range(N)]
    
    # 堆疊，儲存目前的位置和步驟
    stack = [(startX, startY)]
    board[startX][startY] = True  # 起點已訪問
    visited_count = 1  # 已訪問格數
    
    while stack:
        x, y = stack[-1]  # 取堆疊頂部的當前位置
        found_next_move = False
        
        for dx, dy in moves:
            nx, ny = x + dx, y + dy
            # 如果新位置在棋盤範圍內且未被訪問
            if 0 <= nx < N and 0 <= ny < N and not board[nx][ny]:
                stack.append((nx, ny))  # 將新位置加入堆疊
                board[nx][ny] = True  # 標記為已訪問
                visited_count += 1
                found_next_move = True
                break  # 跳出迴圈，繼續探索新位置
        
        if not found_next_move:
            # 如果無法繼續移動，則回溯
            stack.pop()
    
    # 判斷是否訪問了棋盤上的所有格子
    return visited_count == N * N


# 主程式：接受輸入並輸出結果
if __name__ == "__main__":
    # 輸入三個數字：N, startX, startY
    N = int(input("請輸入棋盤大小 N (4 ≤ N ≤ 10): "))
    startX = int(input("請輸入騎士的起始位置 X (0 ≤ X < N): "))
    startY = int(input("請輸入騎士的起始位置 Y (0 ≤ Y < N): "))
    
    # 確保輸入範圍合法
    if 4 <= N <= 10 and 0 <= startX < N and 0 <= startY < N:
        # 執行騎士遍歷棋盤的函式
        result = knight_tour(N, startX, startY)
        print(result)  # 輸出 True 或 False
    else:
        print("輸入數據不合法，請重新確認。")

def josephus_problem(n, k):
    # 建立一個初始隊列，從 1 到 n
    people = list(range(1, n + 1))
    
    # 初始化索引指向第一個人
    index = 0

    # 不斷移除直到只剩下一個人
    while len(people) > 1:
        # 計算要移除的人的索引
        index = (index + k - 1) % len(people)
        # 移除該人
        people.pop(index)
    
    # 剩下的最後一個人即為勝利者
    return people[0]

# 主程式：接受輸入並輸出結果
if __name__ == "__main__":
    n = int(input("請輸入參與遊戲的人數 n: "))
    k = int(input("請輸入每次數到第 k 個人的值 k: "))
    
    # 確保輸入值是正整數
    if n > 0 and k > 0:
        winner = josephus_problem(n, k)
        print(f"最後剩下的人的編號是: {winner}")
    else:
        print("輸入的 n 和 k 必須是正整數，請重新確認。")

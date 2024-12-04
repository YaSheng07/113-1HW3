def top_item(stack, top):
    if top == -1:  # 如果top指標為-1，代表堆疊為空
        return "Stack is empty"  # 堆疊為空
    else:
        return stack[top]  # 否則，返回堆疊頂端的元素
19

21 
def is_full(stack, top, N):
    if top == N - 1:  # 如果top指標指向堆疊的頂端，即堆疊已滿
        return True  # 傳回True，表示堆疊已滿
    else:
        return False  # 否則傳回False，表示堆疊未滿
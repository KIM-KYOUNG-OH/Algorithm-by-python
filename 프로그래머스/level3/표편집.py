def solution(n, k, cmds):
    linked_list = {i: [i - 1, i + 1] for i in range(n)}
    linked_list[0][0] = None
    linked_list[n - 1][1] = None
    stack = []
    answer = ['O' for _ in range(n)]
    for cmd in cmds:
        print('cmd = ', cmd)
        if cmd == 'C':
            prev, next = linked_list[k]
            stack.append([prev, k, next])
            answer[k] = 'X'

            if next is None:
                k = linked_list[k][0]
            else:
                k = linked_list[k][1]

            if prev is None:
                linked_list[next][0] = prev
            elif next is None:
                linked_list[prev][1] = next
            else:
                linked_list[prev][1] = next
                linked_list[next][0] = prev
        elif cmd == 'Z':
            prev, cur, next = stack.pop()
            answer[cur] = 'O'

            if prev is None:
                linked_list[next][0] = cur
            elif next is None:
                linked_list[prev][1] = cur
            else:
                linked_list[prev][1] = cur
                linked_list[next][0] = cur

        else:
            oper, distance = cmd.split(' ')
            if oper == 'D':
                for _ in range(int(distance)):
                    k = linked_list[k][1]
            else:
                for _ in range(int(distance)):
                    k = linked_list[k][0]
        print('k = ', k)
        print('stack = ', stack)
    return ''.join(answer)


print(solution(8, 2, ["D 2","C","U 3","C","D 4","C","U 2","Z","Z","U 1","C"]))
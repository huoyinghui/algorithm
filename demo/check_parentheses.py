from stack.sstack import SStack


open_parentheses = {
    '{': True,
    '[': True,
    '(': True,
}
close_parentheses = {
    '}': True,
    ']': True,
    ')': True,
}
table = {
    '{': '}',
    '(': ')',
    '[': ']',
}


def check_parentheses(text=None):
    if not text:
        return
    s = SStack()
    cnt = 0
    for c in text:
        if open_parentheses.get(c, False):
            s.push(c)
        elif close_parentheses.get(c, False):
            if table.get(s.pop(), None) == c:
                cnt += 1
            else:
                print('匹配失败:', c)
                return

    print('匹配成功:', cnt)


def main():
    check_parentheses('123{adjk}')
    check_parentheses('123{a(dj)k}')
    check_parentheses('123{ad(j)k}')

if __name__ == '__main__':
    main()
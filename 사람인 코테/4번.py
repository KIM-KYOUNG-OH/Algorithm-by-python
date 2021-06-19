text = input().strip()
length = len(text)
is_open = False  # 괄호 안이면 True, 괄호 밖이면 False
bracket_content = ''  # 괄호 안의 내용
references = dict()  # 참조 문헌
index = 1  # 참조 문헌 번호
fixed_text = ''  # 수정된 논문
for i in range(length):
    if not is_open and text[i] == '[':
        is_open = True
    elif is_open and text[i] == ']':
        is_open = False
        bracket_content = bracket_content.strip().split(', ')
        for reference in bracket_content:
            if reference not in references:
                references[reference] = index
                index += 1
        fixed_bracket_content = []
        for reference in bracket_content:
            fixed_bracket_content.append(references[reference])
        fixed_bracket_content.sort()
        fixed_text += ' ' + ', '.join(map(str, fixed_bracket_content)) + ' '
        bracket_content = ''
    elif is_open:
        bracket_content += text[i]
        continue
    fixed_text += text[i]

print(fixed_text)
answer = sorted(references.items(), key=lambda x: x[1])  # 참조 문헌 index 오름차순 정렬
for ref in answer:
    print('[%d] %s' % (ref[1], ref[0]))

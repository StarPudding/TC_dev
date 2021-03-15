import sys

if __name__ == '__main__':
    sentinel = ''  # 遇到这个就结束
    lines = []
    for line in iter(input, sentinel):
        lines.append(line)

    for i in range(0, len(lines)):
        if i != len(lines)-1:
            a = lines[i]
            temp = a.split(': ')
            front = '"'+temp[0]+'": '
            after = '"'+temp[1]+'",'
            print(front+after)
        else:
            a = lines[i]
            temp = a.split(': ')
            front = '"'+temp[0]+'": '
            if len(temp) == 1:
                print(front+'""')
            else:
                after = '"' + temp[1] + '"'
                print(front + after)

# -*- coding:utf-8 -*-

if __name__ == '__main__':
    rest = 1
    for i in range(9):
        rest = (rest + 1) * 2
        print('猴子第%s天有%s个桃子' % (10 - i - 1, rest))

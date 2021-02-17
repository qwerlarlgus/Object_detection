import sys

if __name__ == '__main__':
    argument = sys.argv
    del argument[0]			# 첫번째 인자는 script.py 즉 실행시킨 파일명이 되기 때문에 지운다
#    print('Argument : {}'.format(argument))

print('Occupied   : {}'.format(argument[0]))
print('Free Space : {}'.format(argument[1]))
print('# of Entry : {}'.format(argument[2]))
print('# of Exit  : {}'.format(argument[3]))


# import sys
# import re
# input = sys.stdin.readline

# string = input().strip()
# pat_word = re.compile('[a-zA-Z0-9 ]')
# pat_word1 = re.compile('<.+?>')
# string = pat_word1.sub(lambda m:m.group(0)[::-1], string)
# string = pat_word.sub(lambda m:m.group(0)[::-1], string)
# print(string)
# print(string.replace('<','#').replace('>','<').replace('#','>'))
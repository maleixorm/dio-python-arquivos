arquivo = open('lorem.txt', 'r')
# print(arquivo.read())
# print(arquivo.readline())
# print(arquivo.readlines())
while len(linha := arquivo.readline()):
    print(linha)
arquivo.close()
import displayio as dio

class btm:
    def update(self, file):
        with open(file) as f:
            for i in range(self.alto):
                st = f.readline()
                for j in range(self.largo):
#                     print((i,j),st[j])
                    self.mapa[j,i] = 1 if st[j] == '1' else 0 #aquí se hace la conversión

    def __init__(self, file):
        self.largo = len(open(file).readline()) - 2
        self.alto = len(open(file).readlines())
        self.mapa = dio.Bitmap(self.largo, self.alto, 2)
        self.update(file) #???
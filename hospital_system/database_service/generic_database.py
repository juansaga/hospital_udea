from os import remove
class basic_database:
    def __init__(self,database_name) -> None:
        self.database_name = database_name


    def create(self, data: list):
        text_plain = open( self.database_name , 'a')
        info = data[0]
        for i in range(1, len(data)):
            info += ',' + data[i]
        info += '\n'
        text_plain.write(info)
        print('Dato inserted with exito')
        text_plain.close()


    def read(self, id):
        with open(self.database_name, "r") as datos:
            valores = []
            count = 0
            for linea in datos:
                valores.append([x for x in linea.strip().split(",")])
                if id == valores[count][0]:
                    print(valores[count])
                    break
                count += 1
            
        datos.close()
        

    def update(self, old_id : str, data: list):
        with open(self.database_name, "r") as datos:
            valores = []
            k = False
            count = 0
            for linea in datos:
                valores.append([x for x in linea.strip().split(",")])
                if old_id == valores[count][0]:
                    k = True
                    valores[count] = data
                count += 1
            datos.close()
            remove(self.database_name)
            text_plain = open( self.database_name , 'a')
            for linea in valores:
                info = linea[0]
                for i in range(1,len(linea)):
                    info += ','+linea[i]
                info += '\n'
                text_plain.write(info)

        text_plain.close()
        if k:
            print('dato actualizado con exito')  
        else:
            print('dato doesnt exists')
        

    def delete(self , id):
        with open(self.database_name, "r") as datos:
            valores = []
            posicion=0
            k = False
            count = 0
            for linea in datos:
                valores.append([x for x in linea.strip().split(",")])
                if id == valores[count][0]:
                    k = True
                    posicion = count
                count += 1
            datos.close()
            if k :
                remove(self.database_name)
                text_plain = open( self.database_name , 'a')
                for i in range(len(valores)):
                    if i != posicion:
                        info = valores[i][0]
                        for j in range(1, len(valores[i])):
                            info += ',' + valores[i][j]
                        info += '\n'
                        text_plain.write( info )
                print('The user has been deleted')
                text_plain.close()

            else:
                print('Dato no valido ')
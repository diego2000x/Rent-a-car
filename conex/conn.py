import pymysql
import traceback

class Conex:
    def __init__(self, host, user, passwd, database):
        try:
            self.__myconn = pymysql.connect(host=host, user=user, passwd=passwd, database=database)
        except Exception as ex:
            print(traceback.print_exc())
            self.__myconn = None

    def closeConex(self):
        if self.__myconn:
            self.__myconn.close()

    def getConex(self):
        return self.__myconn
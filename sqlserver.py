import pyodbc
import pandas as pd
from dotenv import dotenv_values

class SqlServer():

    # Atributos Privados
    __cfg_conexao = None
    __cursor = None
    __query = None
    __metodo = None

    # Atributos publicos
    conexao = None
    


    def __init__(self):
        self.__cfg_conexao = self.__configura_conexao()
        self.conexao = pyodbc.connect(self.__cfg_conexao)
        self.__cursor = self.conexao.cursor()


    
    def __configura_conexao(self):
        # Dados para a conexão
        dados_conexao = dotenv_values('.env')
        driver = dados_conexao['DRIVER']
        dbname = dados_conexao['DBNAME']
        dbhost = dados_conexao['DBHOST']
        dbport = dados_conexao['DBPORT']
        dbuser = dados_conexao['DBUSER']
        dbpass = dados_conexao['DBPASS']

        cfg_conexao = f'''Driver={driver}; Server={dbhost},{dbport}; Database={dbname}; UID={dbuser}; PWD={dbpass};''' 
        return cfg_conexao


    def get_cfg_conexao(self):
        return {self.__cfg_conexao}
    

    def ler(self, consulta):
        self.__metodo = 'ler'
        self.__query = str(consulta)
        return self.__executa_query()


    def gravar(self, query:str):
        self.__metodo = 'gravar'
        self.__query = query
        return self.__executa_query()
        

    def __executa_query(self):
        resultado = None
        try:
            #self.__cursor.execute(self.__query)
            if self.__metodo == 'ler':
                resultado = pd.read_sql_query(self.__query, self.conexao)
            elif self.__metodo == 'gravar':
                self.__cursor.execute(self.__query)
            else:
                return '''{ 'status' : 99, 'message' : 'metodo não implementado'}'''
            self.conexao.commit()
            return resultado

        except Exception as e:
            print(f'''Erro ao executar a consulta: {e} 
                    {self.__query}''', flush=True)
            self.conexao.close()
        finally:
            # Fechar a conexão com o banco de dados
            self.conexao.close()




#res = SqlServer().ler('select top 100 * from gtcconhe where dtemissao >= {}'.format('2023-01-01'))
#res = SqlServer().ler('''select getdate() data''')
# query = '''INSERT INTO PNXImpEtq (impressora, usuario) VALUES ('Datamax-Dev','userTest')'''
# res = SqlServer().gravar(query)
# print(res)




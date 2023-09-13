# python-classes
    Here I am making my first Python classes available.

sqlserver
---------
The idea is to have a facilitator to read and record, without having to worry about other details, such as connection, for example.

    Configure:
    
    file .env
    
        DRIVER='ODBC Driver 17 for SQL Server'
        
        DBHOST=
        
        DBPORT=
        
        DBNAME=
        
        DBUSER=
        
        DBPASS=

 

How to use
----------

    #### Read

        res = SqlServer().ler('select top 100 * from gtcconhe where dtemissao >= {}'.format('2023-01-01'))
        
        res = SqlServer().ler('''select getdate() data''')
    
    
    #### Write
        query = '''INSERT INTO PNXImpEtq (impressora, usuario) VALUES ('Datamax-Dev','userTest')'''
        
        res = SqlServer().gravar(query)

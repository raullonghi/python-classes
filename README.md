# python-classes
Here I am making my first Python classes available.

### sqlserver
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

res = SqlServer().ler('select top 100 * from gtcconhe where dtemissao >= {}'.format('2023-01-01')) \r\n
res = SqlServer().ler('''select getdate() data''') \r\n
\r\n
query = '''INSERT INTO PNXImpEtq (impressora, usuario) VALUES ('Datamax-Dev','userTest')''' \r\n
res = SqlServer().gravar(query) \r\n

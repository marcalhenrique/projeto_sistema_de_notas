import psycopg2 as pg

# Classe responsável por conectar ao banco de dados
class ConnectPostgresql:

    def __init__(self):
        # Setando as variáveis de conexão
        self.conn = None
        self.curs = None

    def connect(self):
        # Conectando ao banco de dados
        self.conn = pg.connect(
                                host="sistema_de_notas_db",
                                user = "postgres",
                                password = "postgres",
                                database = "db_sistema",
                                port = "5441",
            )

        self.curs = self.conn.cursor()
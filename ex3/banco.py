import sqlite3
from datetime import date

import arquivos

NOME_ARQUIVO = "arena.db"


def conectar(nome_arquivo=NOME_ARQUIVO):
 
    conn = sqlite3.connect(nome_arquivo)
    conn.execute("""
        CREATE TABLE IF NOT EXISTS partidas (
            id             INTEGER PRIMARY KEY AUTOINCREMENT,
            jogador        TEXT NOT NULL,
            inimigo        TEXT NOT NULL,
            resultado      TEXT NOT NULL,
            turnos         INTEGER NOT NULL,
            vida_restante  INTEGER NOT NULL,
            data           TEXT NOT NULL
        )
    """)
    conn.commit()
    return conn


def registrar_partida(conn, jogador, inimigo, resultado, turnos, vida_restante, data=None):

    raise NotImplementedError


def historico(conn, jogador):

    raise NotImplementedError


def contar_resultados(conn, jogador):

    raise NotImplementedError


def ranking(conn, limite=5):


    raise NotImplementedError


def exportar_ranking(conn, caminho, limite=5):

    raise NotImplementedError

import sqlite3
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import os 
from matplotlib.ticker import MaxNLocator

DB_NAME = 'biblioteca.db'
DB_PATH = DB_NAME

def get_db_connection():
    """Establece y retorna la conexión a la base de datos."""
    try:
        conn = sqlite3.connect(DB_PATH)
        return conn
    except sqlite3.Error as e:
        print(f"Error al conectar con la base de datos: {e}")
        return None

ALL_IMPORTS = {
    'pd': pd,
    'plt': plt,
    'sns': sns
}
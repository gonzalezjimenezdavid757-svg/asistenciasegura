
import os
from dotenv import load_dotenv

load_dotenv()


class Config:
    SECRET_KEY = os.getenv("SECRET_KEY", "solo-para-desarrollo")

    # Modo desarrollo
    MODO_DESARROLLO = os.getenv("MODO_DESARROLLO", "0") == "1"

    # Base de datos
    DB_HOST = os.getenv("DB_HOST", "localhost")
    DB_PORT = int(os.getenv("DB_PORT", "3306"))
    DB_USER = os.getenv("DB_USER", "root")
    DB_PASSWORD = os.getenv("DB_PASSWORD", "")
    DB_NAME = os.getenv("DB_NAME", "asist_e4")
    DB_SSL_CA = os.getenv("DB_SSL_CA", "")

    # Dispositivo ESP32
    CLAVE_DISPOSITIVO = os.getenv("CLAVE_DISPOSITIVO", "")

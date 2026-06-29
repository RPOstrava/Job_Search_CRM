import os

BASE_DIR = os.path.abspath(os.path.dirname(__file__))
# Cesta k souboru applications.db uvnitř složky database
DATABASE_PATH = os.path.join(BASE_DIR, 'database', 'applications.db')

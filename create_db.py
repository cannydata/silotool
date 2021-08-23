import sqlite3, config

connection = sqlite3.connect(config.DB_FILE)
cursor = connection.cursor()

cursor.execute("""
    CREATE TABLE IF NOT EXISTS external_domains(
        id INTEGER PRIMARY KEY,
        site_id INTEGER,
        domain TEXT NOT NULL UNIQUE,
        checked INTEGER NOT NULL,
        status_code INTEGER,
        last_date DATE NOT NULL
    )
""")

connection.commit()

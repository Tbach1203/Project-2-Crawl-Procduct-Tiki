import psycopg2
from config.config import load_config
from psycopg2.extras import execute_batch
import os
import json

def connect(config):
    try:
        with psycopg2.connect(**config) as conn:
            print('Connected to the PostgreSQL server.')
            return conn
    except (psycopg2.DatabaseError, Exception) as error:
        print(error)
 
def create_table(conn):
    sql = """
    CREATE TABLE IF NOT EXISTS product (
        id BIGINT PRIMARY KEY,
        name TEXT,
        url_key TEXT,
        price DOUBLE PRECISION,
        description TEXT,
        images TEXT
    );
    """
    with conn.cursor() as cur:
        cur.execute(sql)
    conn.commit()

def load_json_chunks(folder_path):
    products = []

    for file_name in sorted(os.listdir(folder_path)):
        if not file_name.endswith(".json"):
            continue

        file_path = os.path.join(folder_path, file_name)
        print(f"Loading {file_path}")

        with open(file_path, "r", encoding="utf-8") as f:
            data = json.load(f)
            products.extend(data)

    return products

def insert_products(conn, products):
    sql = """
    INSERT INTO product (id, name, url_key, price, description, images)
    VALUES (%s, %s, %s, %s, %s, %s)
    ON CONFLICT (id) DO NOTHING
    """

    values = [
        (
            p.get("id"),
            p.get("name"),
            p.get("url_key"),
            p.get("price"),
            p.get("description"),
            p.get("images")
        )
        for p in products
    ]
    with conn.cursor() as cur:
        execute_batch(cur, sql, values, page_size=500)
    conn.commit()
    print(f"Inserted {len(values)} records")

if __name__ == '__main__':
    config = load_config()
    conn = connect(config)
    create_table(conn)
    products = load_json_chunks("product")
    insert_products(conn, products)
    conn.close()

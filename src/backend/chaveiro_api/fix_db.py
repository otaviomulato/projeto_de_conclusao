import sqlite3
import os

db_path = 'db.sqlite3'

if os.path.exists(db_path):
    try:
        conn = sqlite3.connect(db_path)
        cursor = conn.cursor()
        
        print("Checking for conflicting orders...")
        # Check if there are orders
        cursor.execute("SELECT count(*) FROM dados_pedido")
        count = cursor.fetchone()[0]
        print(f"Found {count} orders.")
        
        if count > 0:
            print("Deleting existing orders to resolve migration conflict...")
            cursor.execute("DELETE FROM dados_pedido")
            conn.commit()
            print("Orders deleted successfully.")
        else:
            print("No orders found. The issue might be elsewhere or already resolved.")
            
        conn.close()
    except Exception as e:
        print(f"An error occurred: {e}")
else:
    print(f"Database file not found at {db_path}")

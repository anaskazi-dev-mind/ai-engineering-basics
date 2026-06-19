class DatabaseConnection:

    def __enter__(self):
        print("[Log] Connection is make with the database.")

        return "Database_object_123"
    
    def __exit__(self, exc_type, exc_value, traceback):
        print("[Log] Connection is Close with the Database.")


print("Server Start")

with DatabaseConnection() as db:
    print("Data is Saved.")

print("Server End")
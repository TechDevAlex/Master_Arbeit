from database.db_connection import create_connection
from search.search_logic import search

def main():
    create_connection()

if __name__ == "__main__":
    main()

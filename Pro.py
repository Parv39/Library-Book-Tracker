import mysql.connector
import matplotlib.pyplot as plt

# --- Connect to MySQL Database ---
conn = mysql.connector.connect(
    host="localhost",
    user="root",
    password="PARV@SHARMA19",
    database="library"
)
cursor = conn.cursor()

# --- Fetch All Books ---
cursor.execute("SELECT * FROM books")
books = cursor.fetchall()

# --- Sort Books by ID (for Binary Search) ---
books.sort(key=lambda x: x[0])  # x[0] = book id

# --- Binary Search Function (DAA Concept) ---
def binary_search(books, book_id):
    low, high = 0, len(books) - 1
    while low <= high:
        mid = (low + high) // 2
        if books[mid][0] == book_id:
            return books[mid]
        elif books[mid][0] < book_id:
            low = mid + 1
        else:
            high = mid - 1
    return None

# --- User Input for Search ---
search_id = int(input("Enter Book ID to Search: "))
result = binary_search(books, search_id)

if result:
    print(f"✅ Book Found: ID={result[0]}, Title={result[1]}, Author={result[2]}, Price={result[3]}")
else:
    print("❌ Book not found")

# --- Visualization (Python + Matplotlib) ---
author_count = {}
for _, _, author, _ in books:
    author_count[author] = author_count.get(author, 0) + 1

plt.bar(author_count.keys(), author_count.values(), color='skyblue')
plt.title("Number of Books by Each Author")
plt.xlabel("Author")
plt.ylabel("Number of Books")
plt.show()

# --- Close Connection ---
conn.close()
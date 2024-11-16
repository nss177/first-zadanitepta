import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
from ttkthemes import ThemedTk  # Для улучшения интерфейса

#  базы данных книг
books = [
    {"title": "Гарри Поттер и философский камень", "author": "Дж.К. Роулинг", "genre": "Фэнтези", "pages": 320, "year": 1997},
    {"title": "1984", "author": "Джордж Оруэлл", "genre": "Дистопия", "pages": 328, "year": 1949},
    {"title": "Властелин колец", "author": "Дж. Р. Р. Толкин", "genre": "Фэнтези", "pages": 1200, "year": 1954},
    {"title": "Мастер и Маргарита", "author": "Михаил Булгаков", "genre": "Роман", "pages": 450, "year": 1967},
    {"title": "Убить пересмешника", "author": "Харпер Ли", "genre": "Драма", "pages": 281, "year": 1960},
    {"title": "Джейн Эйр", "author": "Шарлотта Бронте", "genre": "Роман", "pages": 500, "year": 1847},
    {"title": "Анна Каренина", "author": "Лев Толстой", "genre": "Роман", "pages": 850, "year": 1878},
    {"title": "Грозовой перевал", "author": "Эмили Бронте", "genre": "Роман", "pages": 500, "year": 1847},
    {"title": "Шерлок Холмс", "author": "Артур Конан Дойл", "genre": "Детектив", "pages": 350, "year": 1892}
]


def show_book_info(event):
    selected_book_title = book_combobox.get()
    book = next((b for b in books if b["title"] == selected_book_title), None)

    if book:

        title_label.config(text=book["title"])
        genre_label.config(text=f"Жанр: {book['genre']}")
        pages_label.config(text=f"Количество страниц: {book['pages']}")
        author_label.config(text=f"Автор: {book['author']}")
        year_label.config(text=f"Год издания: {book['year']}")

       
        canvas.delete("all")  
        canvas.create_rectangle(10, 10, 180, 250, fill="#d9d9d9", outline="#000000", width=2)  # Рисуем прямоугольник как обложку
        canvas.create_text(95, 130, text=book["title"], width=160, anchor="center", font=("Arial", 10, "bold"))
    else:
        messagebox.showerror("Ошибка", "Выбранная книга не найдена.")


def create_app():
    global book_combobox, title_label, genre_label, pages_label, author_label, year_label, canvas

    root = ThemedTk(theme="arc")  # Использование красивой темы
    root.title("Экспертная система: Рекомендации книг")
    root.geometry("800x600")
    root.config(bg="#f4f4f9")


    header = tk.Label(root, text="Выберите книгу для получения информации", font=("Arial", 18, "bold"), bg="#f4f4f9", fg="#333")
    header.pack(pady=20)

 
    select_book_frame = tk.Frame(root, bg="#f4f4f9")
    select_book_frame.pack(pady=10, fill="x", padx=20)

    tk.Label(select_book_frame, text="Выберите книгу:", font=("Arial", 12), bg="#f4f4f9", fg="#333").pack(pady=5)
    book_titles = [book["title"] for book in books]  # Список всех названий книг
    book_combobox = ttk.Combobox(select_book_frame, values=book_titles, state="readonly", width=40)
    book_combobox.set("Выберите книгу")
    book_combobox.pack(pady=5)
    book_combobox.bind("<<ComboboxSelected>>", show_book_info)

 
    info_frame = tk.Frame(root, bg="#f4f4f9", bd=2, relief="solid")
    info_frame.pack(pady=20, fill="x", padx=40)

   
    title_label = tk.Label(info_frame, text="Название книги:", font=("Arial", 14, "bold"), bg="#f4f4f9", anchor="w", fg="#333")
    title_label.pack(fill="x", padx=10, pady=5)

    genre_label = tk.Label(info_frame, text="Жанр:", font=("Arial", 12), bg="#f4f4f9", anchor="w", fg="#333")
    genre_label.pack(fill="x", padx=10, pady=5)

    pages_label = tk.Label(info_frame, text="Количество страниц:", font=("Arial", 12), bg="#f4f4f9", anchor="w", fg="#333")
    pages_label.pack(fill="x", padx=10, pady=5)

    author_label = tk.Label(info_frame, text="Автор:", font=("Arial", 12), bg="#f4f4f9", anchor="w", fg="#333")
    author_label.pack(fill="x", padx=10, pady=5)

    year_label = tk.Label(info_frame, text="Год издания:", font=("Arial", 12), bg="#f4f4f9", anchor="w", fg="#333")
    year_label.pack(fill="x", padx=10, pady=5)

   
    canvas_frame = tk.Frame(root, bg="#f4f4f9")
    canvas_frame.pack(pady=10)

    canvas = tk.Canvas(canvas_frame, width=200, height=250, bg="#f4f4f9", bd=0, highlightthickness=0)
    canvas.pack()

   
    root.mainloop()

# Запуск приложения
if __name__ == "__main__":
    create_app()

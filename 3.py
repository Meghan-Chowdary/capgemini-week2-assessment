# 3. You are building a Library Management System. Create a `Book` class with properties like `title`, `author`, and `isbn`. Write a method to display book details.
lis1={}
lis2={}
class Book:
    def __init__(self,title,author,isbn) :
        self.title=title
        self.author=author
        self.isbn=isbn
        lis1[f'title={title}']=title
        lis1[f'author={author}']=author
        lis2[f"isbn={isbn}"]=lis1
    def display(self):
        print(f"{lis2}")

book1=Book("sdgbvg","dtbh gsf",8520)
book2=Book("sdyukmhgbvg","dtbhdgbsdgsf",7410)
book3=Book("sgfb xfb","gbs",9630)
book1.display()
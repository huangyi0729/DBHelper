class Book:
    def __init__(self, title, author, price):
        self.title = title
        self.author = author
        self.price = price
    def show_info(self):
        print(f"《{self.title}》 作者：{self.author}，价格：{self.price:.2f}元")


if __name__ == "__main__":
    print("=== 图书信息 ===")
    title = input("请输入书名：")
    author = input("请输入作者：")
    price = float(input("请输入价格："))
    book = Book(title, author, price)
    book.show_info()

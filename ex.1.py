class publication:
    def __init__(self, name):
        self.name = name
class Books(publication):
    def __init__(self,name,author, page_count):
        self.name = name
        self.author = author
        self.page_count = page_count

    def print_information(self):
        print(f"Book name: {self.name}")
        print(f"Author Name: {self.author}")
        print(f"Page Count: {self.page_count}")

class Magazine(publication):
    def __init__(self, editor, publication_name):
        self.editor = editor
        self.publication_name = publication_name

    def print_information(self):
        print(f"{self.editor}: {self.publication_name}")
# Main program
if __name__ == "__main__":
    magazine = Magazine("Donald Duck", "Aki Hyyppa")
    book = Books("Compartment No. 6", "Rosa Likson", 192)


    print("Publication Information")
    magazine.print_information()
    book.print_information()






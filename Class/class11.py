
class Publication:
    def __init__(self, name):
        self.name = name

class Book(Publication):
    def __init__(self,name, author, page_count):
        Publication.__init__(self, name)
        self.author = author
        self.page_count = page_count

    def print_information(self):
        print(f"Book Publication: {self.name}")
        print(f"Book Author: {self.author}")
        print(f"Book Page Count: {self.page_count}")
        

class Magazine(Publication):
    def __init__(self, name, chief_editor):
        Publication.__init__(self, name)
        self.chief_editor = chief_editor

    def print_information(self):
        print(f"Magazine Publication: {self.name}")
        print(f"Magazine Chief Editior: {self.chief_editor}")

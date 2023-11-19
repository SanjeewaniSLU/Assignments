#1
class Publication:
    def __init__(self, name):
        self.name = name


class Book(Publication):
    def __init__(self,name, author, page_count):
        super().__init__(name)
        self.author = author
        self.page_count = page_count

    def print_information(self):
        print(f"Name of Book: {self.name}")
        print(f"Author of Book: {self.author}")
        print(f"Page_count of Book: {self.page_count}")


class Magazine(Publication):
    def __init__(self, name, chief_editor):
        super().__init__(name)
        self.chief_editor = chief_editor

    def print_information(self):
        print(f"Name of Magazine: {self.name}")
        print(f"Chief Editor of magazine: {self.chief_editor}")


Donald_Duck = Magazine(name="Donald Duck", chief_editor="Aki Hyyppä")
Compartment_no_6 = Book(name="Compartment No. 6", author="Rosa Liksom", page_count=192)
print("-.-" * 12)
Donald_Duck.print_information()
print("-.-" * 12)
Compartment_no_6.print_information()
print("-.-" * 12)
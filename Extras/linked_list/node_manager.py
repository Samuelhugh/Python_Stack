class SList:
    def __init__(self):
        self.head = None



my_list = SList()


if __name__ == "__main__":
    print("the file is being executed directly")
else:
    print("The file is being executed because it is imported by another file. The file is called: ", __name__)
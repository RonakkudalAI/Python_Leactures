class Laptop:
    storage_type ="ssd"
    
    def __init__(self ,Ram, Storage):
         self.Ram = Ram
         self.Storage = Storage

    def get_info(self):
        print(f"laptop has {self.Ram} Ram & {self.Storage} {self.storage_type}")

l1 = Laptop("16gb","512gb")
    
l2 = Laptop("8gb","256gb")

l1.get_info()
l2.get_info()
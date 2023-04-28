from ctypes import set_errno


class Students:
    def __init__(self, name, email):
        self.name = name
        self.email = email

    def get_std(self):
        return self.__class__
    
std = Students('john', 'email.com')
print(std.get_std())


#print(dir(std))























# class boys(Students):
#     def __init__(self, name, email, school):
#         super().__init__(self, name, email)
#         self.school_name = school



# class Animal:
#     def __init__(self, name):
#         self._name = name
        
#     def make_sound(self):
#         print("Some generic animal sound")
        
# class Cat(Animal):
#     def __init__(self, name, breed):
#         super().__init__(name)
#         self._breed = breed
        
#     def make_sound(self):
#         super().make_sound()
#         print("Meow")

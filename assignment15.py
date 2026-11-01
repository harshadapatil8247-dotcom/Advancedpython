import gc

print("Garbage collection enabled:",
      gc.isenabled())


print("Initial GC count:", gc.get_count())

class Student:
    def __init__(self, name):
        self.name = name
        self.ref = None

s1 = Student("Rahul")
s2 = Student("Amit")

s1.ref = s2
s2.ref = s1

print("\nCircular references created.")

del s1
del s2

print("Objects are now unreachable.")

gc.disable()
print("\nAutomatic GC disabled:",
      gc.isenabled())

collected = gc.collect()

print("Objects collected manually:", collected)

print("GC count after collection:", gc.get_count())
print("GC statistics:", gc.get_stats())

gc.enable()

print("\nAutomatic GC enabled:",
      gc.isenabled())
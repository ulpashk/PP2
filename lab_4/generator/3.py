#Define a function with a generator which can iterate the numbers, which are divisible by 3 and 4, between a given range 0 and n.

print("the number N: ")
N = int(input())
class numbers:
  def __iter__(self):
    self.a = 0
    return self

  def __next__(self):
    if self.a <= N:
        x = self.a
        self.a += 1
        return x
    else:
      raise StopIteration

divisi = numbers()
it = iter(divisi)
print(' ')
print("Numbers, which are divisible by 3 and 4 between 0 and {}:" .format(N))

for x in it:
    if(x % 3 == 0):
        if(x % 4 == 0):
            print(x)
        
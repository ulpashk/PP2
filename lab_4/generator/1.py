#Create a generator that generates the squares of numbers up to some number N
print("the number N: ")
N = int(input())
class numbers:
  def __iter__(self):
    self.a = 1
    return self

  def __next__(self):
    if self.a <= N:
      x = self.a
      self.a += 1
      return x*x
    else:
      raise StopIteration

squares = numbers()
it = iter(squares)
print(' ')
print("Squares of numbers up to {}:" .format(N))

for x in it:
  print(x)
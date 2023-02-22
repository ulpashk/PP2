#Implement a generator called squares to yield the square of all numbers from (a) to (b). Test it with a "for" loop and print each of the yielded values.

print("the number a: ")
a = int(input())
print("the number b: ")
b = int(input())

class numbers:
  def __iter__(self):
    self.e = a
    return self

  def __next__(self):
    if self.e <= b:
      x = self.e
      self.e += 1
      return x*x
    else:
      raise StopIteration

squares = numbers()
it = iter(squares)
print(' ')
print("Squares of numbers from {} up to {}:" .format(a, b) )
print(' ')
for x in it:
  print(x)
#Write a program using generator to print the even numbers between 0 and n in comma separated form where n is input from console.
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

evenns = numbers()
it = iter(evenns)
print(' ')
print("Even numbers between 0 and {}:" .format(N))

for x in it:
    if(x % 2 == 0):
        if(x != N and x != N-1):
            print(x, end=', ')
        else:
            print(x)
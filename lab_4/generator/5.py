#Implement a generator that returns all numbers from (n) down to 0
print('print the number n:')
n = int(input())
class MyNumbers:
  def __iter__(self):
    self.a = n
    return self

  def __next__(self):
    if self.a >= 0:
        x = self.a
        self.a -= 1
        return x
    else:
        raise StopIteration

myclass = MyNumbers()
myiter = iter(myclass)

print('All numbers from {} down to 0:' .format(n))
print(' ')
for x in myiter:
    print(x)
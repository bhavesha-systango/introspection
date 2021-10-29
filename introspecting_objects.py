a = 42
print(dir(a))
print(getattr(a, 'denominator'))
print(a.denominator)
print(getattr(a, 'conjugate'))
print(callable(getattr(a,'conjugate')))
hasattr(a,'denominator')
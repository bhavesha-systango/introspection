from itertools import chain
import inspect
class Batch:
    def __init__(self, iterables=()):
        self._iterables = list(iterables)

    def append(self, iterable):
        self.iterables.append(iterable)

    def __iter__(self):
        return chain(*self._iterables)

print(inspect.isclass(Batch))
print(inspect.getmembers(Batch))
print("-------")
print(list(chain([1,2,3],[4,5,6])))
print(inspect.getmembers(Batch, inspect.isfunction))
init_sig = inspect.signature(Batch.__init__)
print(init_sig)
print(init_sig.parameters)
print(init_sig.parameters['iterables'].default)
def report_scope(arg):
    from pprint import pprint as pp
    x = 496
    pp(locals(), width = 10)

print(report_scope(42))

name = "bhavesh"
age =23
country = 'india'
print(f"{name} is{23} years old")
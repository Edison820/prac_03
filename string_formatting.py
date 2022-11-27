"""
CP1404 - Practical
String_formatting
1922 Gibson L-5 CES for about $16,035!

"""

name = "Gibson L-5 CES"
year = 1922
cost = 16035.4

print(f"{year} {name} for about ${cost:,.2f}!")



for i in range(0,151,50):
    print('{0:>6}'.format(i, end='\n'))
print()
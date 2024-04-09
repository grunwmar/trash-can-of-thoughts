from rational import Rational

p = Rational(7, 4)

strings = [
    "{num}/{div}",
    "{quot} ⌐ {rem}",
    "{quot}[{rem}/{div}]"
]



for s in strings:
    print(p, "->", p.strf(s))
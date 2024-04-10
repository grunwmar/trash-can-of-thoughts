from rational_numbers import Rational
import sys

f = float(sys.argv[1])

r = Rational.from_float(f)

print("\n", f, "=", r)
print("\n", f, "=", r.strf("{quot} r {rem}"))
print("\n", f, "=", r.strf("{quot} [{rem}/{div}]"), "\n")

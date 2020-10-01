string = input('input comma separated string')
x = [x for x in string.split(",")]
print(",".join(sorted(set(x)))

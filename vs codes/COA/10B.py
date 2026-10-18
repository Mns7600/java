s1 = input("I1 source(s): ").split()
d1 = input("I1 destination: ").strip()
s2 = input("I2 source(s): ").split()
d2 = input("I2 destination: ").strip()
if d1 in s2:
    print("RAW hazard (Read After Write)")
elif d2 in s1:
    print("WAR hazard (Write After Read)")
elif d1 == d2:
    print("WAW hazard (Write After Write)")
else:
    print("No hazard")
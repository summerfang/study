import winsound

for i in range(21000, 32767):
    print("\rThe current frequency is ", i, "Hz", end="")
    winsound.Beep(i, 10000)

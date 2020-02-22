import winsound

for i in range(1500, 32767, 100):
    print("\rThe current frequency is ", i, "Hz", end="")
    winsound.Beep(i, 3000)

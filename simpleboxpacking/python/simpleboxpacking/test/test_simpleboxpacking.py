from simpleboxpacking import SimpleBoxPacking 

def test_w():
    GW = 64
    GH = 48
    n = 10
    ratio = 16/9

    box_packing = SimpleBoxPacking(GW, GH, n, ratio)
    assert box_packing.w == 1 
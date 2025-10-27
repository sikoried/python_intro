def multiply(x, y):
    return x * y

def test_multiply():
    a = 3
    b = 5
    assert multiply(a, b) == a * b, "Fehler beim Multiplizieren, 3 * 5 = 15"
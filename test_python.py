from math import pi, sqrt, pow, hypot

def legal_age(age):
    if age < 18:
        return False
    else:
        return True


def age_pow(n):
  return n * n


ages = [5, 12, 17, 18, 24, 32]
def test_filter(legal_age, ages):
    ages_filter = filter(legal_age, ages)
    for age in ages_filter:
        assert age >= 18
    print('filter test OK')

def test_map(age_pow, ages):
    ages_map = map(age_pow, ages)
    for a, m in zip(ages, ages_map):
        assert a*a == m
    print('map test OK')


def test_math():
    # print(pi)
    # print(sqrt(25))
    # print(pow(2, 3))
    # print(hypot(3, 4))
    assert pi == 3.141592653589793
    assert sqrt(25) == 5
    assert sqrt(81) == 9
    assert pow(2, 3) == 8
    assert pow(25, 2) == 625
    assert hypot(3, 4) == 5
    print('math test OK')


if __name__ == '__main__':

    test_filter(legal_age, ages)
    test_map(age_pow, ages)
    test_math()


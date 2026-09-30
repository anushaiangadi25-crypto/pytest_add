from SI import calculate_SI


def test_pos_SI():
    assert calculate_SI(2000,8,12)==1920
def test_zero():
    assert calculate_SI(1000,0,12)== 0
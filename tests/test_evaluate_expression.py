from opendssdirect.utils import _evaluate_expression as ee



def test_ee():

    assert ee('1') == '1'
    assert ee('1.0') == '1.0'
    assert ee('a') == 'a'
    assert ee('[a]') == ['a']
    assert ee('(a)') == ('a', )
    assert ee('(a, , )') == ('a', )
    assert ee('[a, , ]') == ['a', ]
    assert ee('true') == True
    assert ee('[true]') == [True]
    assert ee('[true, false]') == [True, False]
    assert ee('(true, false)') == (True, False)

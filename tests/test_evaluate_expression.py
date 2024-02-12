def test_ee():
    import sys
    if sys.platform == 'win32':
        # When running pytest, the faulthandler seems too eager
        # to grab FPC's exceptions, even when handled
        import faulthandler
        faulthandler.disable()
        from opendssdirect.utils import _evaluate_expression as ee
        faulthandler.enable()
    else:
        from opendssdirect.utils import _evaluate_expression as ee

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

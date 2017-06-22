import os

def test_import():

    import opendssdirect


def test_ActiveClass():

    import opendssdirect as dss

    assert dss.dss_lib.DSSPut_Command('Redirect {}'.format(os.path.abspath(os.path.join('.', './data/13Bus/IEEE13Nodeckt.dss')))) == "", "Unable to find test data"

    assert dss.ActiveClass.ActiveClassName() == 'Line'

    assert dss.ActiveClass.AllNames() == [u'650632',
     u'632670',
     u'670671',
     u'671680',
     u'632633',
     u'632645',
     u'645646',
     u'692675',
     u'671684',
     u'684611',
     u'684652',
     u'671692']

    assert dss.ActiveClass.Count() == 12

    assert dss.ActiveClass.First() == 1

    assert dss.ActiveClass.Name() == '650632'

    assert dss.ActiveClass.Next() == 2
    assert dss.ActiveClass.Next() == 3

    assert dss.ActiveClass.Name('650632') == '0'

    assert dss.ActiveClass.Name() == '650632'

    assert dss.ActiveClass.NumElements() == 12


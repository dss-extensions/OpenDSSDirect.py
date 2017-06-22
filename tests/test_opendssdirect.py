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

    assert dss.Basic.Classes() == [u'Solution',
     u'LineCode',
     u'LoadShape',
     u'TShape',
     u'PriceShape',
     u'XYcurve',
     u'GrowthShape',
     u'TCC_Curve',
     u'Spectrum',
     u'WireData',
     u'CNData',
     u'TSData',
     u'LineGeometry',
     u'LineSpacing',
     u'XfmrCode',
     u'Line',
     u'Vsource',
     u'Isource',
     u'VCCS',
     u'Load',
     u'Transformer',
     u'RegControl',
     u'Capacitor',
     u'Reactor',
     u'CapControl',
     u'Fault',
     u'Generator',
     u'GenDispatcher',
     u'Storage',
     u'StorageController',
     u'Relay',
     u'Recloser',
     u'Fuse',
     u'SwtControl',
     u'PVSystem',
     u'UPFC',
     u'UPFCControl',
     u'InvControl',
     u'ExpControl',
     u'GICLine',
     u'GICTransformer',
     u'VSConverter',
     u'Monitor',
     u'EnergyMeter',
     u'Sensor']
    assert os.path.abspath(dss.Basic.DataPath()) == os.path.abspath('.')
    assert dss.Basic.AllowForms() == 1
    assert dss.Basic.NumCircuits() == 1
    assert dss.Basic.NumClasses() == 45
    assert dss.Basic.NumUserClasses() == 0
    assert dss.Basic.ShowPanel() == -1
    assert dss.Basic.Start() == 1
    assert dss.Basic.UserClasses() == []
    assert dss.Basic.Version()

    # assert dss.Bus.Coorddefined() == 1
    # assert dss.Bus.CplxSeqVoltages() == [0.0, 0.078125, 0.0, 0.4103854298591614, -1687792.875, 7.377432823181152]


def test_configuration():

    import opendssdirect as dss

    assert dss.Basic.AllowForms() == 1, "Allow forms should be disabled"

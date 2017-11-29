import pytest as pt
import os
import sys
import pandas as pd
from pandas.util.testing import assert_dict_equal
import numpy as np
import six

current_directory = os.path.dirname(os.path.realpath(__file__))
PATH_TO_DSS = os.path.abspath(os.path.join(
    current_directory, './data/13Bus/IEEE13Nodeckt.dss'))


def is_windows():
    return sys.platform.lower().startswith('win')


@pt.fixture()
def dss():
    import opendssdirect as dss
    assert dss.utils.run_command(
        'Redirect {}'.format(
            PATH_TO_DSS
        )
    ) == "", "Unable to find test data"
    return dss


def test_package_import():

    import opendssdirect


def test_module_import():

    import inspect

    from opendssdirect import ActiveClass as m
    inspect.ismodule(m)

    from opendssdirect import Basic as m
    inspect.ismodule(m)

    from opendssdirect import Bus as m
    inspect.ismodule(m)

    from opendssdirect import Capacitors as m
    inspect.ismodule(m)

    from opendssdirect import CapControls as m
    inspect.ismodule(m)

    from opendssdirect import Circuit as m
    inspect.ismodule(m)

    from opendssdirect import CktElement as m
    inspect.ismodule(m)

    from opendssdirect import Element as m
    inspect.ismodule(m)

    from opendssdirect import Executive as m
    inspect.ismodule(m)

    from opendssdirect import Fuses as m
    inspect.ismodule(m)

    from opendssdirect import Generators as m
    inspect.ismodule(m)

    from opendssdirect import Isource as m
    inspect.ismodule(m)

    from opendssdirect import Lines as m
    inspect.ismodule(m)

    from opendssdirect import Loads as m
    inspect.ismodule(m)

    from opendssdirect import LoadShape as m
    inspect.ismodule(m)

    from opendssdirect import Meters as m
    inspect.ismodule(m)

    from opendssdirect import Monitors as m
    inspect.ismodule(m)

    from opendssdirect import Parser as m
    inspect.ismodule(m)

    from opendssdirect import PDElements as m
    inspect.ismodule(m)

    from opendssdirect import Properties as m
    inspect.ismodule(m)

    from opendssdirect import PVsystems as m
    inspect.ismodule(m)

    from opendssdirect import Reclosers as m
    inspect.ismodule(m)

    from opendssdirect import RegControls as m
    inspect.ismodule(m)

    from opendssdirect import Relays as m
    inspect.ismodule(m)

    from opendssdirect import Sensors as m
    inspect.ismodule(m)

    from opendssdirect import Settings as m
    inspect.ismodule(m)

    from opendssdirect import Solution as m
    inspect.ismodule(m)

    from opendssdirect import SwtControls as m
    inspect.ismodule(m)

    from opendssdirect import Topology as m
    inspect.ismodule(m)
    from opendssdirect import Transformers as m
    inspect.ismodule(m)

    from opendssdirect import Vsources as m
    inspect.ismodule(m)

    from opendssdirect import XYCurves as m
    inspect.ismodule(m)

    from opendssdirect import dss_lib as m
    inspect.ismodule(m)


def test_ActiveClass(dss):

    assert dss.ActiveClass.ActiveClassName() == u'Line'
    assert dss.ActiveClass.AllNames() == [
        u'650632',
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
        u'671692'
    ]
    assert dss.ActiveClass.Count() == 12
    assert dss.ActiveClass.First() == 1
    assert dss.ActiveClass.Name() == u'650632'
    assert dss.ActiveClass.Next() == 2
    assert dss.ActiveClass.Next() == 3
    assert dss.ActiveClass.Name(u'650632') == u'0'
    assert dss.ActiveClass.Name() == u'650632'
    assert dss.ActiveClass.NumElements() == 12


def test_configuration():

    import opendssdirect as dss

    assert dss.Basic.AllowForms() == 1, "Allow forms should be disabled"


def test_13Node(dss):

    assert dss.ActiveClass.ActiveClassName() == u'Line'
    assert dss.ActiveClass.AllNames() == [
        u'650632',
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
        u'671692'
    ]
    assert dss.ActiveClass.Count() == 12
    assert dss.ActiveClass.First() == 1
    assert dss.ActiveClass.Name() == u'650632'
    assert dss.ActiveClass.Next() == 2
    assert dss.ActiveClass.NumElements() == 12


def test_13Node_Basic(dss):

    assert dss.Basic.AllowForms() == 1
    assert dss.Basic.Classes() == [u'Solution', u'LineCode', u'LoadShape', u'TShape', u'PriceShape', u'XYcurve', u'GrowthShape', u'TCC_Curve', u'Spectrum', u'WireData', u'CNData', u'TSData', u'LineGeometry', u'LineSpacing', u'XfmrCode', u'Line', u'Vsource', u'Isource', u'VCCS', u'Load', u'Transformer', u'RegControl', u'Capacitor', u'Reactor',
                                   u'CapControl', u'Fault', u'Generator', u'GenDispatcher', u'Storage', u'StorageController', u'Relay', u'Recloser', u'Fuse', u'SwtControl', u'PVSystem', u'UPFC', u'UPFCControl', u'ESPVLControl', u'IndMach012', u'InvControl', u'ExpControl', u'GICLine', u'GICTransformer', u'VSConverter', u'Monitor', u'EnergyMeter', u'Sensor']
    assert dss.Basic.NumClasses() == 47
    assert dss.Basic.ShowPanel() == 0
    assert dss.Basic.ClearAll() == 0
    assert os.path.abspath(dss.Basic.DataPath()) == os.path.abspath('.')
    # assert dss.Basic.DefaultEditor() == u'open -t'
    assert dss.Basic.NewCircuit('Circuit') == u'New Circuit'
    assert dss.Basic.NumCircuits() == 1
    assert dss.Basic.NumUserClasses() == 0
    assert dss.Basic.Reset() == 0
    assert dss.Basic.Start() == 1
    assert dss.Basic.UserClasses() == []
    from six import string_types
    # u'Version xxxx (64-bit build); License Status: Open '
    assert isinstance(dss.Basic.Version(), string_types)


def test_13Node_Bus(dss):

    assert dss.Bus.Coorddefined() == 1
    np.testing.assert_array_almost_equal(dss.Bus.CplxSeqVoltages(), [
                                         7.275957614183426e-12, 4.31951048085466e-06, 57503.46213437529, 33187.98898326319, -0.7758574371237046, 1.4866859858011594], decimal=4)
    assert dss.Bus.Cust_Duration() == 0.0
    assert dss.Bus.Cust_Interrupts() == 0.0
    assert dss.Bus.Distance() == 0.0
    assert dss.Bus.GetUniqueNodeNumber() == 0
    assert dss.Bus.Int_Duration() == 0.0
    assert dss.Bus.Isc() == [0.0, 0.0, 0.0, 0.0, 0.0, 0.0]
    assert dss.Bus.Lambda() == 0.0
    assert dss.Bus.N_Customers() == 0
    assert dss.Bus.N_interrupts() == 0.0
    assert dss.Bus.Name() == u'sourcebus'
    assert dss.Bus.Nodes() == [1, 2, 3]
    assert dss.Bus.NumNodes() == 3
    np.testing.assert_array_almost_equal(dss.Bus.PuVoltage(), [
                                         0.866065862637831, 0.4998770273321037, -0.0001655104421677343, -0.9999937910431469, -0.8659003521956633, 0.5001167639062155], decimal=4)
    assert dss.Bus.SectionID() == 0
    np.testing.assert_array_almost_equal(dss.Bus.SeqVoltages(
    ), [4.3195104808607886e-06, 66393.45427218509, 1.6769585514012348], decimal=4)
    assert dss.Bus.TotalMiles() == 0.0
    np.testing.assert_array_almost_equal(dss.Bus.VLL(), [
                                         57513.67538924719, 99584.34438494075, 57480.70805232015, -99600.26176213453, -114994.38344156733, 15.917377193771244], decimal=4)
    np.testing.assert_array_almost_equal(dss.Bus.VMagAngle(), [
                                         66393.52547161786, 29.992738890948125, 66394.86962078432, -90.00948310376482, 66391.9676657127, 149.99062328146098], decimal=4)
    assert dss.Bus.Voc() == [0.0, 0.0, 0.0, 0.0, 0.0, 0.0]
    np.testing.assert_array_almost_equal(dss.Bus.Voltages(), [
                                         57502.68627693818, 33189.4756735685, -10.98911230901207, -66394.86871137226, -57491.697164629164, 33205.39305076227], decimal=4)
    assert dss.Bus.X() == 200.0
    assert dss.Bus.Y() == 400.0
    assert dss.Bus.YscMatrix() == [0.0]
    assert dss.Bus.Zsc0() == [0.0, 0.0]
    assert dss.Bus.Zsc1() == [0.0, 0.0]
    assert dss.Bus.ZscMatrix() == [0.0]
    assert dss.Bus.ZscRefresh() == 1
    assert dss.Bus.kVBase() == 66.39528095680697
    np.testing.assert_array_almost_equal(dss.Bus.puVLL(), [1.693378168100472e-11, -4.667955969702419e-11, -
                                                           1.395316990173399e-06, -5.577283842337346e-06, 1.3953000563917182e-06, 5.577330521897042e-06], decimal=4)
    np.testing.assert_array_almost_equal(dss.Bus.puVmagAngle(), [
                                         5.239275814449394e-07, -79.42845561076332, 5.238427215809797e-07, -79.4299867740603, 9.484135993651139e-06, 74.63582918382964], decimal=4)


def test_13Node_Circuit(dss):

    np.testing.assert_array_almost_equal(dss.Circuit.AllBusDistances(), [
                                         0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], decimal=4)
    np.testing.assert_array_almost_equal(dss.Circuit.AllBusMagPu(), [0.9999735600909612, 0.9999938047400851, 0.9999500974911693, 0.9999107734075059, 0.9999708382014062, 0.9999310912254219, 1.0560331208541838, 1.0373856699381676, 1.0560496734277571, 1.011300431272264, 1.0270174666164649, 1.0015359172418576, 0.9871584562161683, 1.0084198145936507, 0.9824418963411172, 0.9827959271001375, 1.0402765227909403, 0.964869605360475, 1.019729240260045,
                                                                     1.0022697678941448, 1.0180132408663718, 1.0002355078501333, 0.9648695979124887, 0.9827959177333715, 1.040276521652259, 0.9762713001854915, 1.0426333240830927, 0.9629347471054315, 0.9608229488014672, 0.9753328230988354, 1.004024331469046, 1.0318708269152446, 0.9897380852516064, 1.0143428459400463, 1.0289449404033275, 1.0041840427671582, 0.9827959396392048, 1.0402765376331038, 0.9648696191496499, 0.9808725592235161, 0.9628392247223574], decimal=4)
    assert dss.Circuit.AllBusNames() == [u'sourcebus', u'650', u'rg60', u'633', u'634',
                                         u'671', u'645', u'646', u'692', u'675', u'611', u'652', u'670', u'632', u'680', u'684']
    np.testing.assert_array_almost_equal(dss.Circuit.AllBusVMag(), [0.9999735600909612, 0.9999938047400851, 0.9999500974911693, 0.9999107734075059, 0.9999708382014062, 0.9999310912254219, 1.0560331208541838, 1.0373856699381676, 1.0560496734277571, 1.011300431272264, 1.0270174666164649, 1.0015359172418576, 0.9871584562161683, 1.0084198145936507, 0.9824418963411172, 0.9827959271001375, 1.0402765227909403, 0.964869605360475, 1.019729240260045,
                                                                    1.0022697678941448, 1.0180132408663718, 1.0002355078501333, 0.9648695979124887, 0.9827959177333715, 1.040276521652259, 0.9762713001854915, 1.0426333240830927, 0.9629347471054315, 0.9608229488014672, 0.9753328230988354, 1.004024331469046, 1.0318708269152446, 0.9897380852516064, 1.0143428459400463, 1.0289449404033275, 1.0041840427671582, 0.9827959396392048, 1.0402765376331038, 0.9648696191496499, 0.9808725592235161, 0.9628392247223574], decimal=4)
    np.testing.assert_array_almost_equal(dss.Circuit.AllBusVolts(), [57502.68627693818, 33189.4756735685, -10.98911230901207, -66394.86871137226, -57491.697164629164, 33205.39305076227, 2401.562772055762, -0.4668925451039482, -1201.2376854909323, -2079.7175095625, -1200.3115874754303, 2080.141929910249, 2536.3561212894438, -0.5793172973319122, -1246.2598833517864, -2157.4877090219084, -1267.587749407154, 2196.935519634186, 2426.4276379311646, -109.96690599537264, -1300.0162579690939, -2096.283396703043, -1120.4139031363902, 2128.6003868309604, 273.12117506928445, -15.653348732054143, -149.22067946929405, -236.2877841616899, -124.73744800718065, 242.00686102787685, 2350.0805301839578, -221.08294871607683, -1338.4006550620513, -2109.7980124414166, -1015.3876288957937, 2083.1079654828877, -1295.6831435171484, -2078.3650896480167, -1122.3784857728665, 2129.5577123236694, -
                                                                     1296.2402814635552, -2073.1585039035635, -1121.7801053097155, 2124.3493400045577, -1015.3876231065364, 2083.107948404428, 2350.080508274622, -221.08294141465848, -1338.400658901049, -2109.798006767321, 2333.5022250500942, -229.75875811896063, -1347.9783594336611, -2110.41134996152, -1013.9483472387761, 2078.6396489285494, -1002.1065310288469, 2078.745142088486, 2332.4304274000037, -217.31255727308186, 2407.056725017637, -145.37420380313188, -1312.2984849124346, -2102.3703908080543, -1082.9865109797865, 2116.1022239294853, 2433.8514624314753, -107.52417704907307, -1300.7601876895642, -2101.268404324189, -1123.5546141566904, 2134.134702369962, 2350.0805587856653, -221.08296622672697, -1338.4006783138987, -2109.7980399064168, -1015.3876332233444, 2083.108000216942, 2345.391500510206, -221.60314314042807, -1009.5495489075352, 2080.524597665617], decimal=4)
    np.testing.assert_array_almost_equal(dss.Circuit.AllElementLosses(), [-3567.2317221830845, -1736.6105734708244, 0.03228838509740308, 0.26247332685953007, 0.12209068980929441, 0.12385511858400423, 0.0, 0.0, 0.06534666416840627, 0.06707862443476915, 0.0, 0.0, 0.13509748949622735, 0.13686198239726946, 0.0, 0.0, 5.5526721532734085, 10.096270647399884, 1155.0168946622257, 660.0436384952801, 159.99892650617605, 110.00542923577791, 120.00015747507646, 89.99764493365784, 120.00492260783774, 90.00952390501756, 170.00027419023695, 124.99693537687827, 234.56562985851542, 134.6270475273679, 166.6736550753605, 148.05222349379017, 484.99675064222447, 190.0228608055384, 68.00032507676042, 59.997846126968334, 290.01666583912, 212.03346194114658, 163.45696048067904,
                                                                          76.93101512773492, 121.93923493761854, 81.93523562163435, 16.999798182421245, 10.000536316150352, 66.00002389593134, 37.998647503238885, 117.00497287474145, 68.00811702391309, -1.4551915228366852e-14, -593.4866454474861, 0.0, -92.45484141123522, 60.738506098096956, 196.01888910912663, 12.990842590497573, 41.49525104173738, 22.7289781935591, 72.33498233978072, 7.693588522863128e-12, -0.004169224402815679, 0.8244852537013503, 1.0561387185878994, 2.7673862000581577, 2.4007964145294536, 0.5274843376703211, 0.4197453440363606, 4.162853304240387, 2.4192732671323176, 0.5795023244819895, 0.470693780053145, 0.3824189497624757, 0.38736389633078216, 0.7998310440541245, 0.23088042051736557, 9.05452249571681e-06, -1.4551915228366852e-14], decimal=4)
    assert dss.Circuit.AllElementNames() == [u'Vsource.source', u'Transformer.sub', u'Transformer.reg1', u'RegControl.reg1', u'Transformer.reg2', u'RegControl.reg2', u'Transformer.reg3', u'RegControl.reg3', u'Transformer.xfm1', u'Load.671', u'Load.634a', u'Load.634b', u'Load.634c', u'Load.645', u'Load.646', u'Load.692', u'Load.675a',
                                             u'Load.675b', u'Load.675c', u'Load.611', u'Load.652', u'Load.670a', u'Load.670b', u'Load.670c', u'Capacitor.cap1', u'Capacitor.cap2', u'Line.650632', u'Line.632670', u'Line.670671', u'Line.671680', u'Line.632633', u'Line.632645', u'Line.645646', u'Line.692675', u'Line.671684', u'Line.684611', u'Line.684652', u'Line.671692']
    assert dss.Circuit.AllNodeDistances() == [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0,
                                              0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0]
    assert dss.Circuit.AllNodeNames() == [u'sourcebus.1', u'sourcebus.2', u'sourcebus.3', u'650.1', u'650.2', u'650.3', u'rg60.1', u'rg60.2', u'rg60.3', u'633.1', u'633.2', u'633.3', u'634.1', u'634.2', u'634.3', u'671.1', u'671.2', u'671.3',
                                          u'645.2', u'645.3', u'646.2', u'646.3', u'692.3', u'692.1', u'692.2', u'675.1', u'675.2', u'675.3', u'611.3', u'652.1', u'670.1', u'670.2', u'670.3', u'632.1', u'632.2', u'632.3', u'680.1', u'680.2', u'680.3', u'684.1', u'684.3']
    assert dss.Circuit.Capacity() == 0.0
    assert dss.Circuit.Disable('632') == u''
    assert dss.Circuit.Enable('632') == u''
    assert dss.Circuit.EndOfTimeStepUpdate() == 0
    assert dss.Circuit.FirstElement() == 1
    assert dss.Circuit.FirstPCElement() == 1
    assert dss.Circuit.FirstPDElement() == 1
    np.testing.assert_array_almost_equal(dss.Circuit.LineLosses(
    ), [106.50229735065263, 317.2298451074293], decimal=4)
    np.testing.assert_array_almost_equal(
        dss.Circuit.Losses(), [112409.79273249737, 327916.3848071047], decimal=4)
    assert dss.Circuit.Name() == u'ieee13nodeckt'
    assert dss.Circuit.NextElement() == 2
    assert dss.Circuit.NextPCElement() == 2
    assert dss.Circuit.NextPDElement() == 0
    assert dss.Circuit.NumBuses() == 16
    assert dss.Circuit.NumCktElements() == 38
    assert dss.Circuit.NumNodes() == 41
    assert dss.Circuit.ParentPDElement() == 0
    assert dss.Circuit.Sample() == 0
    assert dss.Circuit.SaveSample() == 0
    assert dss.Circuit.SetActiveBus() == u'-1'
    assert dss.Circuit.SetActiveBusi() == 0
    assert dss.Circuit.SetActiveClass() == u'0'
    assert dss.Circuit.SetActiveElement() == u'-1'
    assert dss.Circuit.SubstationLosses() == [0.0, 0.0]
    np.testing.assert_array_almost_equal(dss.Circuit.TotalPower(
    ), [-3567.2317221830845, -1736.6105734708244], decimal=4)
    assert dss.Circuit.UpdateStorage() == 0
    np.testing.assert_array_almost_equal(dss.Circuit.YCurrents(), [69802.42815021457, -72191.08720767738, -97420.52952591189, -24355.132407117453, 27618.101397342507, 96546.21962200984, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, -13.819481227119581, 10.715709888633683, -8.9625106416662, -3.414850873765033, -3.1289140707121987, -18.49184953395263, -2.667902859232754, 3.8347722723473936, -0.4672472800431251, -1.9471898670746128, 3.135150139275879, -1.8875824052727808, -3.3135886635147926, -1.3209068014917555, 7.105427357601002e-15,
                                                                   1.4210854715202004e-14, -7.105427357601002e-15, -1.4210854715202004e-14, 0.2588941552615527, -1.0392702554685158, -0.2588941552615527, 1.0392702554685158, -9.005000094089581, 4.591965873291912, -3.088362344352049, -0.8861563878518304, -1.9622176477142474, -10.940625499462755, 0.028098534526863506, -3.017966109087453, 0.0, 0.0, 0.06480217600793559, -0.0435836257331399, -1.7986925506572469, -0.9602909725739117, -0.05809415121825623, -1.0852001390951926, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], decimal=4)
    assert dss.Circuit.YNodeOrder() == [u'SOURCEBUS.1', u'SOURCEBUS.2', u'SOURCEBUS.3', u'650.1', u'650.2', u'650.3', u'RG60.1', u'RG60.2', u'RG60.3', u'633.1', u'633.2', u'633.3', u'634.1', u'634.2', u'634.3', u'671.1', u'671.2', u'671.3',
                                        u'645.2', u'646.2', u'646.3', u'692.3', u'692.1', u'675.1', u'675.2', u'675.3', u'611.3', u'652.1', u'670.1', u'670.2', u'670.3', u'632.1', u'632.2', u'632.3', u'680.1', u'680.2', u'680.3', u'645.3', u'692.2', u'684.1', u'684.3']
    np.testing.assert_array_almost_equal(dss.Circuit.YNodeVArray(), [57502.68627693818, 33189.4756735685, -10.98911230901207, -66394.86871137226, -57491.697164629164, 33205.39305076227, 2401.562772055762, -0.4668925451039482, -1201.2376854909323, -2079.7175095625, -1200.3115874754303, 2080.141929910249, 2536.3561212894438, -0.5793172973319122, -1246.2598833517864, -2157.4877090219084, -1267.587749407154, 2196.935519634186, 2426.4276379311646, -109.96690599537264, -1300.0162579690939, -2096.283396703043, -1120.4139031363902, 2128.6003868309604, 273.12117506928445, -15.653348732054143, -149.22067946929405, -236.2877841616899, -124.73744800718065, 242.00686102787685, 2350.0805301839578, -221.08294871607683, -1338.4006550620513, -2109.7980124414166, -1015.3876288957937, 2083.1079654828877, -1295.6831435171484, -2078.3650896480167, -1296.2402814635552, -2073.1585039035635, -
                                                                     1121.7801053097155, 2124.3493400045577, -1015.3876231065364, 2083.107948404428, 2350.080508274622, -221.08294141465848, 2333.5022250500942, -229.75875811896063, -1347.9783594336611, -2110.41134996152, -1013.9483472387761, 2078.6396489285494, -1002.1065310288469, 2078.745142088486, 2332.4304274000037, -217.31255727308186, 2407.056725017637, -145.37420380313188, -1312.2984849124346, -2102.3703908080543, -1082.9865109797865, 2116.1022239294853, 2433.8514624314753, -107.52417704907307, -1300.7601876895642, -2101.268404324189, -1123.5546141566904, 2134.134702369962, 2350.0805587856653, -221.08296622672697, -1338.4006783138987, -2109.7980399064168, -1015.3876332233444, 2083.108000216942, -1122.3784857728665, 2129.5577123236694, -1338.400658901049, -2109.798006767321, 2345.391500510206, -221.60314314042807, -1009.5495489075352, 2080.524597665617], decimal=4)


def test_13Node_CktElement(dss):

    assert dss.CktElement.AllPropertyNames() == [u'bus1', u'bus2', u'linecode', u'length', u'phases', u'r1', u'x1', u'r0', u'x0', u'C1', u'C0', u'rmatrix', u'xmatrix', u'cmatrix', u'Switch', u'Rg', u'Xg', u'rho',
                                                 u'geometry', u'units', u'spacing', u'wires', u'EarthModel', u'cncables', u'tscables', u'B1', u'B0', u'normamps', u'emergamps', u'faultrate', u'pctperm', u'repair', u'basefreq', u'enabled', u'like']
    assert dss.CktElement.AllVariableNames() == []
    assert dss.CktElement.AllVariableValues() == [0.0]
    assert dss.CktElement.BusNames() == [u'671', u'692']
    assert dss.CktElement.Close() == 0
    np.testing.assert_array_almost_equal(dss.CktElement.CplxSeqCurrents(), [66.53025245666505, 13.676485538482666, 141.9625213874072, -15.550956740585985, 10.600583242109401, -
                                                                            71.13971231916744, -66.53025245666505, -13.676485538482666, -141.9625213874072, 15.550956740585985, -10.600583242109401, 71.13971231916744], decimal=4)
    np.testing.assert_array_almost_equal(dss.CktElement.CplxSeqVoltages(), [-1.2359179246288363, -82.59099855820193, 2386.0459226713465, -162.491803967821, -34.72947456275983,
                                                                            23.999853809946103, -1.2359245776542025, -82.5909999258505, 2386.045908475094, -162.49180241272535, -34.7294756228182, 23.999860923917254], decimal=4)
    np.testing.assert_array_almost_equal(dss.CktElement.Currents(), [219.09335708618164, -73.01418352127075, 38.38997459411621, -56.7409553527832, -57.892574310302734,
                                                                     170.78459548950195, -219.09335708618164, 73.01418352127075, -38.38997459411621, 56.7409553527832, 57.892574310302734, -170.78459548950195], decimal=4)
    np.testing.assert_array_almost_equal(dss.CktElement.CurrentsMagAng(), [230.9393212828229, -18.430962758395474, 68.50785475902325, -55.918380174918454, 180.33005355954046,
                                                                           108.72563470506053, 230.9393212828229, 161.56903723193298, 68.50785475902325, 124.08161981541, 180.33005355954046, -71.27436528526792], decimal=4)
    assert dss.CktElement.DisplayName() == u'Line_671692'
    assert dss.CktElement.EmergAmps() == 600.0
    assert dss.CktElement.Enabled() == 1
    assert dss.CktElement.EnergyMeter() == u''
    from six import string_types
    assert isinstance(dss.CktElement.GUID(), string_types)
    assert dss.CktElement.HasSwitchControl() == 0
    assert dss.CktElement.HasVoltControl() == 0
    assert dss.CktElement.IsOpen() == 0
    np.testing.assert_almost_equal(dss.CktElement.Losses(), [
                                   0.00905452249571681, -1.4551915228366852e-11], decimal=4)
    assert dss.CktElement.Name() == u'Line.671692'
    assert dss.CktElement.NodeOrder() == [1, 2, 3, 1, 2, 3]
    assert dss.CktElement.NormalAmps() == 400.0
    assert dss.CktElement.NumConductors() == 3
    assert dss.CktElement.NumControls() == 0
    assert dss.CktElement.NumPhases() == 3
    assert dss.CktElement.NumProperties() == 35
    assert dss.CktElement.NumTerminals() == 2
    assert dss.CktElement.OCPDevIndex() == 0
    assert dss.CktElement.OCPDevType() == 0
    assert dss.CktElement.Open() == 0
    np.testing.assert_array_almost_equal(dss.CktElement.PhaseLosses(), [
                                         5.3332970710471275e-06, 1.4551915228366852e-14, 4.693326191045344e-07, 0.0, 3.2518928055651486e-06, -2.9103830456733704e-14], decimal=4)
    np.testing.assert_array_almost_equal(dss.CktElement.Powers(), [531.0292237718563, 123.15140569189936, 68.33078768274852, -156.93722390935451, 414.5461550055662,
                                                                   52.81608277791104, -531.0292184385592, -123.15140569189934, -68.3307872134159, 156.93722390935451, -414.54615175367337, -52.81608277791107], decimal=4)
    np.testing.assert_array_almost_equal(dss.CktElement.Residuals(), [
                                         203.7642921065592, 11.61634976990784, 203.7642921065592, -168.3836502204206], decimal=4)
    np.testing.assert_array_almost_equal(dss.CktElement.SeqCurrents(), [
                                         67.92143070218641, 142.81172827963962, 71.92517663465829, 67.92143070218641, 142.81172827963962, 71.92517663465829], decimal=4)
    np.testing.assert_array_almost_equal(dss.CktElement.SeqPowers(), [-3.635341586794097, -16.43369091330689, 1023.7679950283105, 42.112652185360545, -6.2264861453966915, -
                                                                      6.648697143839365, 3.635342970790345, 16.433690913306886, -1023.7679889097534, -42.112652185360524, 6.226487697365985, 6.648697143839375], decimal=4)
    np.testing.assert_array_almost_equal(dss.CktElement.SeqVoltages(), [
                                         82.60024537467991, 2391.5724390980245, 42.215274324634755, 82.6002468417225, 2391.5724248289184, 42.21527924109106], decimal=4)
    assert dss.CktElement.Variablei() == 0.0
    np.testing.assert_array_almost_equal(dss.CktElement.Voltages(), [2350.0805301839578, -221.08294871607683, -1338.4006550620513, -2109.7980124414166, -1015.3876288957937,
                                                                     2083.1079654828877, 2350.080508274622, -221.08294141465848, -1338.400658901049, -2109.798006767321, -1015.3876231065364, 2083.107948404428], decimal=4)
    np.testing.assert_array_almost_equal(dss.CktElement.VoltagesMagAng(), [2360.456771170086, -5.374262178524929, 2498.5123507343887, -122.3899728004033, 2317.4017417730743,
                                                                           115.98639992871324, 2360.4567486732017, -5.3742620518852195, 2498.5123479995295, -122.3899729444441, 2317.4017238846714, 115.98639998506223], decimal=4)
    np.testing.assert_array_almost_equal(dss.CktElement.YPrim(), [10000000.0, 0.0, 0.0, 0.0, 0.0, 0.0, -10000000.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 10000000.0, 0.0, 0.0, 0.0, 0.0, 0.0, -10000000.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 10000000.0, 0.0, 0.0, 0.0, 0.0,
                                                                  0.0, -10000000.0, 0.0, -10000000.0, 0.0, 0.0, 0.0, 0.0, 0.0, 10000000.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, -10000000.0, 0.0, 0.0, 0.0, 0.0, 0.0, 10000000.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, -10000000.0, 0.0, 0.0, 0.0, 0.0, 0.0, 10000000.0, 0.0], decimal=4)


def test_13Node_Capacitors(dss):

    assert dss.Capacitors.AddStep() == 0
    assert dss.Capacitors.AllNames() == [u'cap1', u'cap2']
    assert dss.Capacitors.AvailableSteps() == 0
    assert dss.Capacitors.Close() == 0
    assert dss.Capacitors.Count() == 2
    assert dss.Capacitors.First() == 1
    assert dss.Capacitors.IsDelta() == 0
    assert dss.Capacitors.Name() == u'cap1'
    assert dss.Capacitors.Next() == 2
    assert dss.Capacitors.NumSteps() == 1
    assert dss.Capacitors.Open() == 0
    assert dss.Capacitors.States() == [0]
    assert dss.Capacitors.SubtractStep() == 0
    assert dss.Capacitors.kV() == 2.4
    assert dss.Capacitors.kvar() == 100.0


def test_13Node_CapControls(dss):

    assert dss.CapControls.AllNames() == []
    assert dss.CapControls.CTRatio() == 0.0
    assert dss.CapControls.Capacitor() == u''
    assert dss.CapControls.Count() == 0
    assert dss.CapControls.Delay() == 0.0
    assert dss.CapControls.DelayOff() == 0.0
    assert dss.CapControls.First() == 0
    assert dss.CapControls.Mode() == 1
    assert dss.CapControls.MonitoredObj() == u''
    assert dss.CapControls.MonitoredTerm() == 0
    assert dss.CapControls.Name() == u''
    assert dss.CapControls.Next() == 0
    assert dss.CapControls.OFFSetting() == 0.0
    assert dss.CapControls.ONSetting() == 0.0
    assert dss.CapControls.PTRatio() == 0.0
    assert dss.CapControls.UseVoltOverride() == 0
    assert dss.CapControls.Vmax() == 0.0
    assert dss.CapControls.Vmin() == 0.0


def test_13Node_Element(dss):

    assert dss.Element.AllPropertyNames() == [u'bus1', u'bus2', u'linecode', u'length', u'phases', u'r1', u'x1', u'r0', u'x0', u'C1', u'C0', u'rmatrix', u'xmatrix', u'cmatrix', u'Switch', u'Rg', u'Xg', u'rho',
                                              u'geometry', u'units', u'spacing', u'wires', u'EarthModel', u'cncables', u'tscables', u'B1', u'B0', u'normamps', u'emergamps', u'faultrate', u'pctperm', u'repair', u'basefreq', u'enabled', u'like']
    assert dss.Element.Name() == u'Line.671692'
    assert dss.Element.NumProperties() == 35


def test_13Node_Executive(dss):

    assert dss.Executive.Command() == u'New'
    assert dss.Executive.CommandHelp(
    ) == u'Create a new object within the DSS. Object becomes the active object\r\nExample: New Line.line1 ...'
    assert dss.Executive.NumCommands() == 104
    assert dss.Executive.NumOptions() == 110
    assert dss.Executive.Option() == u'type'
    assert dss.Executive.OptionHelp() == u'Sets the active DSS class type.  Same as Class=...'
    assert dss.Executive.OptionValue() == u'Line'


def test_13Node_Fuses(dss):

    assert dss.Fuses.AllNames() == []
    assert dss.Fuses.Close() == 0
    assert dss.Fuses.Count() == 0
    assert dss.Fuses.First() == 0
    assert dss.Fuses.Idx() == 0
    assert dss.Fuses.IsBlown() == 0
    assert dss.Fuses.MonitoredObj() == u''
    assert dss.Fuses.MonitoredTerm() == 0
    assert dss.Fuses.Name() == u''
    assert dss.Fuses.Next() == 0
    assert dss.Fuses.NumPhases() == 0
    assert dss.Fuses.Open() == 0
    assert dss.Fuses.RatedCurrent() == -1.0
    assert dss.Fuses.SwitchedObj() == u''
    assert dss.Fuses.TCCCurve() == u'No Fuse Active!'


def test_13Node_Generators(dss):

    assert dss.Generators.AllNames() == []
    assert dss.Generators.Count() == 0
    assert dss.Generators.First() == 0
    assert dss.Generators.ForcedON() == 0
    assert dss.Generators.Idx() == 0
    assert dss.Generators.Model() == -1
    assert dss.Generators.Name() == u''
    assert dss.Generators.Next() == 0
    assert dss.Generators.PF() == 0.0
    assert dss.Generators.Phases() == 0
    assert dss.Generators.RegisterNames(
    ) == [u'kWh', u'kvarh', u'Max kW', u'Max kVA', u'Hours', u'$']
    assert dss.Generators.RegisterValues() == [0.0]
    assert dss.Generators.Vmaxpu() == -1.0
    assert dss.Generators.Vminpu() == -1.0
    assert dss.Generators.kV() == -1.0
    assert dss.Generators.kVARated() == -1.0
    assert dss.Generators.kW() == 0.0
    assert dss.Generators.kvar() == 0.0


def test_13Node_Isource(dss):

    assert dss.Isource.AllNames() == []
    assert dss.Isource.Amps() == 0.0
    assert dss.Isource.AngleDeg() == 0.0
    assert dss.Isource.Count() == 0
    assert dss.Isource.First() == 0
    assert dss.Isource.Frequency() == 0.0
    assert dss.Isource.Name() == u'671692'
    assert dss.Isource.Next() == 0


def test_13Node_Lines(dss):

    assert dss.Lines.AllNames() == [u'650632', u'632670', u'670671', u'671680', u'632633',
                                    u'632645', u'645646', u'692675', u'671684', u'684611', u'684652', u'671692']
    assert dss.Lines.Bus1() == u'671'
    assert dss.Lines.Bus2() == u'692'
    assert dss.Lines.C0() == 0.0
    assert dss.Lines.C1() == 0.0
    assert dss.Lines.CMatrix() == [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0]
    assert dss.Lines.Count() == 12
    assert dss.Lines.EmergAmps() == 600.0
    assert dss.Lines.First() == 1
    assert dss.Lines.Geometry() == u''
    assert dss.Lines.Length() == 2000.0
    assert dss.Lines.LineCode() == u'mtx601'
    assert dss.Lines.Name() == u'650632'
    assert dss.Lines.Next() == 2
    assert dss.Lines.NormAmps() == 400.0
    assert dss.Lines.NumCust() == 0
    assert dss.Lines.Parent() == 0
    assert dss.Lines.Phases() == 3
    assert dss.Lines.R0() == 0.1784
    assert dss.Lines.R1() == 0.058
    assert dss.Lines.RMatrix() == [
        0.3465, 0.156, 0.158, 0.156, 0.3375, 0.1535, 0.158, 0.1535, 0.3414]
    assert dss.Lines.Rg() == 0.01805
    assert dss.Lines.Rho() == 100.0
    assert dss.Lines.Spacing() == u''
    assert dss.Lines.Units() == 5
    assert dss.Lines.X0() == 0.4047
    assert dss.Lines.X1() == 0.1206
    assert dss.Lines.XMatrix() == [
        1.0179, 0.5017, 0.4236, 0.5017, 1.0478, 0.3849, 0.4236, 0.3849, 1.0348]
    assert dss.Lines.Xg() == 0.155081
    assert dss.Lines.Yprim() == [3.4335554553543783, -9.8965831153747, -1.4568043853617796, 3.658944244501999, -0.7977560291105917, 2.7352081140105042, -3.4335554553543783, 9.896583182049687, 1.4568043853617796, -3.6589442587894965, 0.7977560291105917, -2.7352081282980016, -1.4568043853617796, 3.658944244501999, 3.006548025596122, -9.377989931528099, -0.3787147764220645, 2.0889991803940724, 1.4568043853617796, -3.6589442587894965, -3.006548025596122, 9.377989998203086, 0.3787147764220645, -2.08899919468157, -0.7977560291105917, 2.7352081140105042, -0.3787147764220645, 2.0889991803940724, 2.658753201413196, -8.847115639537611, 0.7977560291105917, -2.7352081282980016, 0.3787147764220645, -2.08899919468157, -2.658753201413196,
                                 8.847115706212598, -3.4335554553543783, 9.896583182049687, 1.4568043853617796, -3.6589442587894965, 0.7977560291105917, -2.7352081282980016, 3.4335554553543783, -9.8965831153747, -1.4568043853617796, 3.658944244501999, -0.7977560291105917, 2.7352081140105042, 1.4568043853617796, -3.6589442587894965, -3.006548025596122, 9.377989998203086, 0.3787147764220645, -2.08899919468157, -1.4568043853617796, 3.658944244501999, 3.006548025596122, -9.377989931528099, -0.3787147764220645, 2.0889991803940724, 0.7977560291105917, -2.7352081282980016, 0.3787147764220645, -2.08899919468157, -2.658753201413196, 8.847115706212598, -0.7977560291105917, 2.7352081140105042, -0.3787147764220645, 2.0889991803940724, 2.658753201413196, -8.847115639537611]


def test_13Node_Loads(dss):

    assert dss.Loads.AllNames() == [u'671', u'634a', u'634b', u'634c', u'645', u'646',
                                    u'692', u'675a', u'675b', u'675c', u'611', u'652', u'670a', u'670b', u'670c']
    assert dss.Loads.AllocationFactor() == 0.5
    assert dss.Loads.CFactor() == 4.0
    assert dss.Loads.CVRCurve() == u''
    assert dss.Loads.CVRvars() == 2.0
    assert dss.Loads.CVRwatts() == 1.0
    assert dss.Loads.Class() == 1
    assert dss.Loads.Count() == 15
    assert dss.Loads.Daily() == u''
    assert dss.Loads.Duty() == u''
    assert dss.Loads.First() == 1
    assert dss.Loads.Growth() == u''
    assert dss.Loads.Idx() == 1
    assert dss.Loads.IsDelta() == 1
    assert dss.Loads.Model() == 1
    assert dss.Loads.Name() == u'671'
    assert dss.Loads.Next() == 2
    assert dss.Loads.NumCust() == 1
    assert dss.Loads.PF() == 0.8240419241993675
    assert dss.Loads.PctMean() == 50.0
    assert dss.Loads.PctStdDev() == 10.0
    assert dss.Loads.RelWeighting() == 1.0
    assert dss.Loads.Rneut() == -1.0
    assert dss.Loads.Spectrum() == u'defaultload'
    assert dss.Loads.Status() == 0
    assert dss.Loads.Vmaxpu() == 1.05
    assert dss.Loads.VminEmerg() == 0.0
    assert dss.Loads.VminNorm() == 0.0
    assert dss.Loads.Vminpu() == 0.95
    assert dss.Loads.XfkVA() == 0.0
    assert dss.Loads.Xneut() == 0.0
    assert dss.Loads.Yearly() == u''
    assert dss.Loads.ZipV() == []
    assert dss.Loads.kV() == 0.277
    assert dss.Loads.kVABase() == 194.164878389476
    assert dss.Loads.kW() == 160.0
    assert dss.Loads.kWh() == 0.0
    assert dss.Loads.kWhDays() == 30.0
    assert dss.Loads.kvar() == 110.0
    assert dss.Loads.puSeriesRL() == 50.0


def test_13Node_LoadShape(dss):

    assert dss.LoadShape.AllNames() == [u'default']
    assert dss.LoadShape.Count() == 1
    assert dss.LoadShape.First() == 1
    assert dss.LoadShape.HrInterval() == 1.0
    assert dss.LoadShape.MinInterval() == 60.0
    assert dss.LoadShape.Name() == u'default'
    assert dss.LoadShape.Next() == 0
    assert dss.LoadShape.Normalize() == 0
    assert dss.LoadShape.Npts() == 24
    assert dss.LoadShape.PBase() == 0.0
    assert dss.LoadShape.PMult() == [0.677, 0.6256, 0.6087, 0.5833, 0.58028, 0.6025, 0.657, 0.7477, 0.832,
                                     0.88, 0.94, 0.989, 0.985, 0.98, 0.9898, 0.999, 1.0, 0.958, 0.936, 0.913, 0.876, 0.876, 0.828, 0.756]
    assert dss.LoadShape.QBase() == 0.0
    assert dss.LoadShape.QMult() == [0.0]
    assert dss.LoadShape.SInterval() == 3600.0
    assert dss.LoadShape.TimeArray() == [0.0]
    assert dss.LoadShape.UseActual() == 0


def test_13Node_Meters(dss):

    assert dss.Meters.AllBranchesInZone() == []
    assert dss.Meters.AllEndElements() == []
    assert dss.Meters.AllNames() == []
    assert dss.Meters.AllocFactors() == [0.0]
    assert dss.Meters.AvgRepairTime() == 0.0
    assert dss.Meters.CalcCurrent() == [0.0]
    assert dss.Meters.CloseAllDIFiles() == 0
    assert dss.Meters.Count() == 0
    assert dss.Meters.CountBranches() == 0
    assert dss.Meters.CountEndElements() == 0
    assert dss.Meters.CustInterrupts() == 0.0
    assert dss.Meters.DIFilesAreOpen() == 0
    assert dss.Meters.DoReliabilityCalc() == 0
    assert dss.Meters.FaultRateXRepairHrs() == 0.0
    assert dss.Meters.First() == 0
    assert dss.Meters.MeteredElement() == u''
    assert dss.Meters.MeteredTerminal() == 0
    assert dss.Meters.Name() == u'0'
    assert dss.Meters.Next() == 0
    assert dss.Meters.NumSectionBranches() == 0
    assert dss.Meters.NumSectionCustomers() == 0
    assert dss.Meters.NumSections() == 0
    assert dss.Meters.OCPDeviceType() == 0
    assert dss.Meters.OpenAllDIFiles() == 0
    assert dss.Meters.PeakCurrent() == [0.0]
    assert dss.Meters.RegisterNames() == []
    assert dss.Meters.RegisterValues() == [0.0]
    assert dss.Meters.Reset() == 0
    assert dss.Meters.ResetAll() == 0
    assert dss.Meters.SAIDI() == 0.0
    assert dss.Meters.SAIFI() == 0.0
    assert dss.Meters.SAIFIkW() == 0.0
    assert dss.Meters.Sample() == 0
    assert dss.Meters.SampleAll() == 0
    assert dss.Meters.Save() == 0
    assert dss.Meters.SaveAll() == 0
    assert dss.Meters.SectSeqidx() == 0
    assert dss.Meters.SectTotalCust() == 0
    assert dss.Meters.SeqListSize() == 0
    assert dss.Meters.SequenceList() == 0
    assert dss.Meters.SetActiveSection() == 0
    assert dss.Meters.SumBranchFltRates() == 0.0
    assert dss.Meters.TotalCustomers() == 0
    assert dss.Meters.Totals() == [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0,
                                   0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0]


def test_13Node_Monitors(dss):

    assert dss.Monitors.AllNames() == []
    assert dss.Monitors.ByteStream() == []
    assert dss.Monitors.Count() == 0
    assert dss.Monitors.Element() == u'0'
    assert dss.Monitors.FileName() == u''
    # assert isinstance(dss.Monitors.FileVersion(), int)
    assert dss.Monitors.First() == 0
    assert dss.Monitors.Mode() == 0
    assert dss.Monitors.Name() == u''
    assert dss.Monitors.Next() == 0
    assert dss.Monitors.Process() == 0
    assert dss.Monitors.ProcessAll() == 0
    assert dss.Monitors.Reset() == 0
    assert dss.Monitors.ResetAll() == 0
    assert dss.Monitors.Sample() == 0
    assert dss.Monitors.SampleAll() == 0
    assert dss.Monitors.Save() == 0
    assert dss.Monitors.SaveAll() == 0
    assert dss.Monitors.Show() == 0
    assert dss.Monitors.Terminal() == 0


def test_13Node_PDElements(dss):

    assert dss.PDElements.AccumulatedL() == 0.0
    assert dss.PDElements.Count() == 19
    assert dss.PDElements.FaultRate() == 0.1
    assert dss.PDElements.First() == 1
    assert dss.PDElements.FromTerminal() == 1
    assert dss.PDElements.IsShunt() == 0
    assert dss.PDElements.Lambda() == 0.0
    assert dss.PDElements.Name() == u'Transformer.sub'
    assert dss.PDElements.Next() == 1
    assert dss.PDElements.NumCustomers() == 0
    assert dss.PDElements.ParentPDElement() == 0
    assert dss.PDElements.PctPermanent() == 0.0
    assert dss.PDElements.RepairTime() == 0.0
    assert dss.PDElements.SectionID() == 0
    assert dss.PDElements.TotalCustomers() == 0
    assert dss.PDElements.TotalMiles() == 0.0


def test_13Node_Properties(dss):

    if is_windows():
        print("Properties interface currently not supported")
    else:
        assert dss.Properties.Description() == u'Name of bus to which first terminal is connected.\r\nExample:\r\nbus1=busname   (assumes all terminals connected in normal phase order)\r\nbus1=busname.3.1.2.0 (specify terminal to node connections explicitly)'
        assert dss.Properties.Name() == u'bus1'

        assert dss.Properties.Name('1') == u'bus1'
        assert dss.Properties.Value('1') == u'671'


def test_13Node_PVsystems(dss):

    assert dss.PVsystems.Count() == 0
    assert dss.PVsystems.First() == 0
    assert dss.PVsystems.Idx() == 0
    assert dss.PVsystems.Irradiance() == -1.0
    assert dss.PVsystems.Next() == 0
    assert dss.PVsystems.kVARated() == -1.0
    assert dss.PVsystems.kW() == 0.0
    assert dss.PVsystems.kvar() == 0.0
    assert dss.PVsystems.pf() == 0.0


def test_13Node_Reclosers(dss):

    assert dss.Reclosers.AllNames() == []
    assert dss.Reclosers.Close() == 0
    assert dss.Reclosers.Count() == 0
    assert dss.Reclosers.First() == 0
    assert dss.Reclosers.GroundInst() == 0.0
    assert dss.Reclosers.GroundTrip() == 0.0
    assert dss.Reclosers.Idx() == 0
    assert dss.Reclosers.MonitoredObj() == u''
    assert dss.Reclosers.MonitoredTerm() == 0
    assert dss.Reclosers.Name() == u''
    assert dss.Reclosers.Next() == 0
    assert dss.Reclosers.NumFast() == 0
    assert dss.Reclosers.Open() == 0
    assert dss.Reclosers.PhaseInst() == 0.0
    assert dss.Reclosers.PhaseTrip() == 0.0
    assert dss.Reclosers.RecloseIntervals() == [-1.0]
    assert dss.Reclosers.Shots() == 0
    assert dss.Reclosers.SwitchedObj() == u''
    assert dss.Reclosers.SwitchedTerm() == 0


def test_13Node_RegControls(dss):

    assert dss.RegControls.AllNames() == [u'reg1', u'reg2', u'reg3']
    assert dss.RegControls.CTPrimary() == 700.0
    assert dss.RegControls.Count() == 3
    assert dss.RegControls.Delay() == 15.0
    assert dss.RegControls.First() == 1
    assert dss.RegControls.ForwardBand() == 2.0
    assert dss.RegControls.ForwardR() == 3.0
    assert dss.RegControls.ForwardVreg() == 122.0
    assert dss.RegControls.ForwardX() == 9.0
    assert dss.RegControls.IsInverseTime() == 0
    assert dss.RegControls.IsReversible() == 0
    assert dss.RegControls.MaxTapChange() == 16
    assert dss.RegControls.MonitoredBus() == u''
    assert dss.RegControls.Name() == u'reg1'
    assert dss.RegControls.Next() == 2
    assert dss.RegControls.PTRatio() == 20.0
    assert dss.RegControls.ReverseBand() == 3.0
    assert dss.RegControls.ReverseR() == 0.0
    assert dss.RegControls.ReverseVreg() == 120.0
    assert dss.RegControls.ReverseX() == 0.0
    assert dss.RegControls.TapDelay() == 2.0
    assert dss.RegControls.TapNumber() == 6
    assert dss.RegControls.TapWinding() == 2
    assert dss.RegControls.Transformer() == u'reg2'
    assert dss.RegControls.VoltageLimit() == 0.0
    assert dss.RegControls.Winding() == 2


def test_13Node_Relays(dss):

    assert dss.Relays.AllNames() == []
    assert dss.Relays.Count() == 0
    assert dss.Relays.First() == 0
    assert dss.Relays.Idx() == 0
    assert dss.Relays.MonitoredObj() == u''
    assert dss.Relays.MonitoredTerm() == 0
    assert dss.Relays.Name() == u''
    assert dss.Relays.Next() == 0
    assert dss.Relays.SwitchedObj() == u''
    assert dss.Relays.SwitchedTerm() == 0


def test_13Node_Sensors(dss):

    assert dss.Sensors.AllNames() == []
    assert dss.Sensors.Count() == 0
    assert dss.Sensors.Currents() == [0.0]
    assert dss.Sensors.First() == 0
    assert dss.Sensors.IsDelta() == 0
    assert dss.Sensors.MeteredElement() == u''
    assert dss.Sensors.MeteredTerminal() == 0
    assert dss.Sensors.Name() == u''
    assert dss.Sensors.Next() == 0
    assert dss.Sensors.PctError() == 0.0
    assert dss.Sensors.Reset() == 0
    assert dss.Sensors.ResetAll() == 0
    assert dss.Sensors.ReverseDelta() == 0
    assert dss.Sensors.Weight() == 0.0
    assert dss.Sensors.kVBase() == 0.0
    assert dss.Sensors.kW() == [0.0]
    assert dss.Sensors.kvar() == [0.0]


def test_13Node_Settings(dss):

    assert dss.Settings.AllocationFactors() == 0.0
    assert dss.Settings.AllowDuplicates() == 0
    assert dss.Settings.AutoBusList() == u'Allocation Factor must be greater than zero.'
    assert dss.Settings.CktModel() == 1
    assert dss.Settings.EmergVmaxpu() == 1.08
    assert dss.Settings.EmergVminpu() == 0.9
    assert dss.Settings.LossRegs() == [13]
    assert dss.Settings.LossWeight() == 1.0
    assert dss.Settings.NormVmaxpu() == 1.05
    assert dss.Settings.NormVminpu() == 0.95
    assert dss.Settings.PriceCurve() == u''
    assert dss.Settings.PriceSignal() == 25.0
    assert dss.Settings.Trapezoidal() == 0
    assert dss.Settings.UERegs() == [10]
    assert dss.Settings.UEWeight() == 1.0
    assert dss.Settings.VoltageBases() == [115.0, 4.16, 0.48]
    assert dss.Settings.ZoneLock() == 0


def test_13Node_Solution(dss):

    assert dss.Solution.AddType() == 1
    assert dss.Solution.Algorithm() == 0
    assert dss.Solution.BuildYMatrix() == 0
    assert dss.Solution.Capkvar() == 600.0
    assert dss.Solution.CheckControls() == 0
    assert dss.Solution.CheckFaultStatus() == 0
    assert dss.Solution.Cleanup() == 0
    assert dss.Solution.ControlActionsDone() == 1
    assert dss.Solution.ControlIterations() == 3
    assert dss.Solution.ControlMode() == 0
    assert dss.Solution.Converged() == 1
    assert dss.Solution.Convergence() == 0.0001
    assert dss.Solution.DblHour() == 0.0
    assert dss.Solution.DefaultDaily() == u'default'
    assert dss.Solution.DefaultYearly() == u'default'
    assert dss.Solution.DoControlActions() == 0
    assert dss.Solution.EventLog() == [u'Hour=0, Sec=0, ControlIter=1, Element=Regulator.reg3, Action= CHANGED 7 TAPS TO 1.04375.', u'Hour=0, Sec=0, ControlIter=1, Element=Regulator.reg2, Action= CHANGED 5 TAPS TO 1.03125.', u'Hour=0, Sec=0, ControlIter=1, Element=Regulator.reg1, Action= CHANGED 7 TAPS TO 1.04375.',
                                       u'Hour=0, Sec=0, ControlIter=2, Element=Regulator.reg3, Action= CHANGED 2 TAPS TO 1.05625.', u'Hour=0, Sec=0, ControlIter=2, Element=Regulator.reg2, Action= CHANGED 1 TAPS TO 1.0375.', u'Hour=0, Sec=0, ControlIter=2, Element=Regulator.reg1, Action= CHANGED 2 TAPS TO 1.05625.']
    assert dss.Solution.FinishTimeStep() == 0
    assert dss.Solution.Frequency() == 60.0
    assert dss.Solution.GenMult() == 1.0
    assert dss.Solution.GenPF() == 1.0
    assert dss.Solution.GenkW() == 1000.0
    assert dss.Solution.Hour() == 0
    assert dss.Solution.InitSnap() == 0
    assert dss.Solution.Iterations() == 11
    assert dss.Solution.LDCurve() == u''
    assert dss.Solution.LoadModel() == 1
    assert dss.Solution.LoadMult() == 1.0
    assert dss.Solution.MaxControlIterations() == 10
    assert dss.Solution.MaxIterations() == 15
    assert dss.Solution.Mode() == 0
    assert dss.Solution.ModeID() == u'Snap'
    assert dss.Solution.MostIterationsDone() == 0
    assert dss.Solution.Number() == 100
    assert dss.Solution.PctGrowth() == 2.499999999999991
    assert isinstance(dss.Solution.ProcessTime(), float)
    assert dss.Solution.Random() == 1
    assert dss.Solution.SampleControlDevices() == 0
    assert dss.Solution.SampleDoControlActions() == 0
    assert dss.Solution.Seconds() == 0.001
    assert dss.Solution.Solve() == 0
    assert dss.Solution.SolveDirect() == 0
    assert dss.Solution.SolveNoControl() == 0
    assert dss.Solution.SolvePFlow() == 0
    assert dss.Solution.SolvePlusControl() == 0
    assert dss.Solution.StepSize() == 0.001
    assert dss.Solution.StepSizeHr() == 0.0
    assert dss.Solution.StepSizeMin() == 0.0
    assert dss.Solution.SystemYChanged() == 0
    assert isinstance(dss.Solution.TimeTimeStep(), float)
    assert dss.Solution.TotalIterations() == 2
    assert isinstance(dss.Solution.TotalTime(), float)
    assert dss.Solution.Year() == 0


def test_13Node_SwtControls(dss):

    assert dss.SwtControls.Action() == 0
    assert dss.SwtControls.AllNames() == []
    assert dss.SwtControls.Count() == 0
    assert dss.SwtControls.Delay() == 0.0
    assert dss.SwtControls.First() == 0
    assert dss.SwtControls.IsLocked() == 0
    assert dss.SwtControls.Name() == u''
    assert dss.SwtControls.Next() == 0
    assert dss.SwtControls.SwitchedObj() == u''
    assert dss.SwtControls.SwitchedTerm() == 0


def test_13Node_Topology(dss):

    assert dss.Topology.ActiveBranch() == 0
    assert dss.Topology.ActiveLevel() == 0
    assert dss.Topology.AllIsolatedBranches() == []
    assert dss.Topology.AllIsolatedLoads() == []
    assert dss.Topology.AllLoopedPairs() == [u'Transformer.reg3', u'Transformer.reg2',
                                             u'Transformer.reg2', u'Line.650632', u'Transformer.reg1', u'Line.650632']
    assert dss.Topology.BranchName() == u''
    assert dss.Topology.BusName() == u''
    assert dss.Topology.First() == 1
    assert dss.Topology.FirstLoad() == 0
    assert dss.Topology.ForwardBranch() == 1
    assert dss.Topology.LoopedBranch() == 0
    assert dss.Topology.Next() == 1
    assert dss.Topology.NextLoad() == 0
    assert dss.Topology.NumIsolatedBranches() == 0
    assert dss.Topology.NumIsolatedLoads() == 0
    assert dss.Topology.NumLoops() == 1
    assert dss.Topology.ParallelBranch() == 0


def test_13Node_Transformers(dss):

    assert dss.Transformers.AllNames() == [
        u'sub', u'reg1', u'reg2', u'reg3', u'xfm1']
    assert dss.Transformers.Count() == 5
    assert dss.Transformers.First() == 1
    assert dss.Transformers.IsDelta() == 0
    assert dss.Transformers.MaxTap() == 1.1
    assert dss.Transformers.MinTap() == 0.9
    assert dss.Transformers.Name() == u'sub'
    assert dss.Transformers.Next() == 2
    assert dss.Transformers.NumTaps() == 32
    assert dss.Transformers.NumWindings() == 2
    assert dss.Transformers.R() == 5e-05
    assert dss.Transformers.Rneut() == -1.0
    assert dss.Transformers.Tap() == 1.05625
    assert dss.Transformers.Wdg() == 2
    assert dss.Transformers.XfmrCode() == u''
    assert dss.Transformers.Xhl() == 0.0001
    assert dss.Transformers.Xht() == 0.35
    assert dss.Transformers.Xlt() == 0.3
    assert dss.Transformers.Xneut() == 0.0
    assert dss.Transformers.kV() == 2.4
    assert dss.Transformers.kVA() == 1666.0


def test_13Node_Vsources(dss):

    assert dss.Vsources.AllNames() == [u'source']
    assert dss.Vsources.AngleDeg() == 30.0
    assert dss.Vsources.BasekV() == 115.0
    assert dss.Vsources.Count() == 1
    assert dss.Vsources.First() == 1
    assert dss.Vsources.Frequency() == 60.0
    assert dss.Vsources.Name() == u'source'
    assert dss.Vsources.Next() == 0
    assert dss.Vsources.PU() == 1.0001
    assert dss.Vsources.Phases() == 3


def test_13Node_XYCurves(dss):

    assert dss.XYCurves.Count() == 0
    assert dss.XYCurves.First() == 0
    assert dss.XYCurves.Name() == u''
    assert dss.XYCurves.Next() == 0
    assert dss.XYCurves.Npts() == 0
    assert dss.XYCurves.X() == 0.0
    assert dss.XYCurves.XArray() == [0.0]
    assert dss.XYCurves.XScale() == 0.0
    assert dss.XYCurves.XShift() == 0.0
    assert dss.XYCurves.Y() == 0.0
    assert dss.XYCurves.YArray() == [0.0]
    assert dss.XYCurves.YScale() == 0.0
    assert dss.XYCurves.YShift() == 0.0


def test_capacitors_to_dataframe(dss):

    expected_dict = pd.DataFrame(
        {
            'AddStep': {
                'cap1': 0,
                'cap2': 0,
            },
            'AvailableSteps': {
                'cap1': 0,
                'cap2': 0,
            },
            'Close': {
                'cap1': 0,
                'cap2': 0,
            },
            'Count': {
                'cap1': 2,
                'cap2': 2
            },
            'IsDelta': {
                'cap1': 0,
                'cap2': 0
            },
            'Name': {
                'cap1': 'cap1',
                'cap2': 'cap2'
            },
            'NumSteps': {
                'cap1': 1,
                'cap2': 1
            },
            'Open': {
                'cap1': 0,
                'cap2': 0
            },
            'States': {
                'cap1': [0],
                'cap2': [0]
            },
            'SubtractStep': {
                'cap1': 0,
                'cap2': 0
            },
            'kV': {
                'cap1': 4.16,
                'cap2': 2.4
            },
            'kvar': {
                'cap1': 600.0,
                'cap2': 100.0
            }
        }
    ).to_dict()

    actual_dict = dss.utils.capacitors_to_dataframe().to_dict()

    assert_dict_equal(actual_dict, expected_dict)


def test_fuses_to_dataframe(dss):

    expected_dict = pd.DataFrame(
        {'Close': {'': 0},
         'Count': {'': 0},
         'Idx': {'': 0},
         'IsBlown': {'': 0},
         'MonitoredObj': {'': ''},
         'MonitoredTerm': {'': 0},
         'Name': {'': ''},
         'NumPhases': {'': 0},
         'Open': {'': 0},
         'RatedCurrent': {'': -1.0},
         'SwitchedObj': {'': ''},
         'TCCCurve': {'': 'No Fuse Active!'}}
    ).to_dict()

    actual_dict = dss.utils.fuses_to_dataframe().to_dict()

    assert_dict_equal(actual_dict, expected_dict)


def test_generators_to_dataframe(dss):

    expected_dict = pd.DataFrame(
        {'Count': {'': 0},
         'ForcedON': {'': 0},
         'Idx': {'': 0},
         'Model': {'': -1},
         'Name': {'': ''},
         'PF': {'': 0.0},
         'Phases': {'': 0},
         'RegisterNames': {'': ['kWh', 'kvarh', 'Max kW', 'Max kVA', 'Hours', '$']},
         'RegisterValues': {'': [0.0]},
         'Vmaxpu': {'': -1.0},
         'Vminpu': {'': -1.0},
         'kV': {'': -1.0},
         'kVARated': {'': -1.0},
         'kW': {'': 0.0},
         'kvar': {'': 0.0}}
    ).to_dict()

    actual_dict = dss.utils.generators_to_dataframe().to_dict()

    assert_dict_equal(actual_dict, expected_dict)



def test_isource_to_dataframe(dss):

    expected_dict = pd.DataFrame(
        {'Amps': {'671692': 0.0},
         'AngleDeg': {'671692': 0.0},
         'Count': {'671692': 0},
         'Frequency': {'671692': 0.0},
         'Name': {'671692': '671692'}}
    ).to_dict()

    actual_dict = dss.utils.isource_to_dataframe().to_dict()

    assert_dict_equal(actual_dict, expected_dict)



def test_lines_to_dataframe(dss):

    expected_dict = pd.DataFrame(
        {'Bus1': {'632633': '632.1.2.3', '632645': '632.3.2', '632670': '632.1.2.3', '645646': '645.3.2', '650632': 'rg60.1.2.3', '670671': '670.1.2.3', '671680': '671.1.2.3', '671684': '671.1.3', '671692': '671', '684611': '684.3', '684652': '684.1', '692675': '692.1.2.3'}, 'Bus2': {'632633': '633.1.2.3', '632645': '645.3.2', '632670': '670.1.2.3', '645646': '646.3.2', '650632': '632.1.2.3', '670671': '671.1.2.3', '671680': '680.1.2.3', '671684': '684.1.3', '671692': '692', '684611': '611.3', '684652': '652.1', '692675': '675.1.2.3'}, 'C0': {'632633': 1.6, '632645': 1.6, '632670': 1.6, '645646': 1.6, '650632': 1.6, '670671': 1.6, '671680': 1.6, '671684': 1.6, '671692': 0.0, '684611': 3.4, '684652': 3.4, '692675': 1.6}, 'C1': {'632633': 3.4, '632645': 3.4, '632670': 3.4, '645646': 3.4, '650632': 3.4, '670671': 3.4, '671680': 3.4, '671684': 3.4, '671692': 0.0, '684611': 3.4, '684652': 3.4, '692675': 3.4}, 'CMatrix': {'632633': [2.7999999999999994, -0.6, -0.6, -0.6, 2.7999999999999994, -0.6, -0.6, -0.6, 2.7999999999999994], '632645': [2.7999999999999994, -0.6, -0.6, 2.7999999999999994], '632670': [2.7999999999999994, -0.6, -0.6, -0.6, 2.7999999999999994, -0.6, -0.6, -0.6, 2.7999999999999994], '645646': [2.7999999999999994, -0.6, -0.6, 2.7999999999999994], '650632': [2.7999999999999994, -0.6, -0.6, -0.6, 2.7999999999999994, -0.6, -0.6, -0.6, 2.7999999999999994], '670671': [2.7999999999999994, -0.6, -0.6, -0.6, 2.7999999999999994, -0.6, -0.6, -0.6, 2.7999999999999994], '671680': [2.7999999999999994, -0.6, -0.6, -0.6, 2.7999999999999994, -0.6, -0.6, -0.6, 2.7999999999999994], '671684': [2.7999999999999994, -0.6, -0.6, 2.7999999999999994], '671692': [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], '684611': [2.7999999999999994], '684652': [236.0], '692675': [383.948, 0.0, 0.0, 0.0, 383.948, 0.0, 0.0, 0.0, 383.948]}, 'Count': {'632633': 12, '632645': 12, '632670': 12, '645646': 12, '650632': 12, '670671': 12, '671680': 12, '671684': 12, '671692': 12, '684611': 12, '684652': 12, '692675': 12}, 'EmergAmps': {'632633': 600.0, '632645': 600.0, '632670': 600.0, '645646': 600.0, '650632': 600.0, '670671': 600.0, '671680': 600.0, '671684': 600.0, '671692': 600.0, '684611': 600.0, '684652': 600.0, '692675': 600.0}, 'Geometry': {'632633': '', '632645': '', '632670': '', '645646': '', '650632': '', '670671': '', '671680': '', '671684': '', '671692': '', '684611': '', '684652': '', '692675': ''}, 'Length': {'632633': 500.0, '632645': 500.0, '632670': 667.0, '645646': 300.0, '650632': 2000.0, '670671': 1333.0, '671680': 1000.0, '671684': 300.0, '671692': 0.001, '684611': 300.0, '684652': 800.0, '692675': 500.0}, 'LineCode': {'632633': 'mtx602', '632645': 'mtx603', '632670': 'mtx601', '645646': 'mtx603', '650632': 'mtx601', '670671': 'mtx601', '671680': 'mtx601', '671684': 'mtx604', '671692': '', '684611': 'mtx605', '684652': 'mtx607', '692675': 'mtx606'}, 'Name': {'632633': '632633', '632645': '632645', '632670': '632670', '645646': '645646', '650632': '650632', '670671': '670671', '671680': '671680', '671684': '671684', '671692': '671692', '684611': '684611', '684652': '684652', '692675': '692675'}, 'NormAmps': {'632633': 400.0, '632645': 400.0, '632670': 400.0, '645646': 400.0, '650632': 400.0, '670671': 400.0, '671680': 400.0, '671684': 400.0, '671692': 400.0, '684611': 400.0, '684652': 400.0, '692675': 400.0}, 'NumCust': {'632633': 0, '632645': 0, '632670': 0, '645646': 0, '650632': 0, '670671': 0, '671680': 0, '671684': 0, '671692': 0, '684611': 0, '684652': 0, '692675': 0}, 'Parent': {'632633': 0, '632645': 0, '632670': 0, '645646': 0, '650632': 0, '670671': 0, '671680': 0, '671684': 0, '671692': 0, '684611': 0, '684652': 0, '692675': 0}, 'Phases': {'632633': 3, '632645': 2, '632670': 3, '645646': 2, '650632': 3, '670671': 3, '671680': 3, '671684': 2, '671692': 3, '684611': 1, '684652': 1, '692675': 3}, 'R0': {'632633': 0.1784, '632645': 0.1784, '632670': 0.1784, '645646': 0.1784, '650632': 0.1784, '670671': 0.1784, '671680': 0.1784, '671684': 0.1784, '671692': 0.0001, '684611': 0.058, '684652': 0.058, '692675': 0.1784}, 'R1': {'632633': 0.058, '632645': 0.058, '632670': 0.058, '645646': 0.058, '650632': 0.058, '670671': 0.058, '671680': 0.058, '671684': 0.058, '671692': 0.0001, '684611': 0.058, '684652': 0.058, '692675': 0.058}, 'RMatrix': {'632633': [0.7526, 0.158, 0.156, 0.158, 0.7475, 0.1535, 0.156, 0.1535, 0.7436], '632645': [1.3238, 0.2066, 0.2066, 1.3294], '632670': [0.3465, 0.156, 0.158, 0.156, 0.3375, 0.1535, 0.158, 0.1535, 0.3414], '645646': [1.3238, 0.2066, 0.2066, 1.3294], '650632': [0.3465, 0.156, 0.158, 0.156, 0.3375, 0.1535, 0.158, 0.1535, 0.3414], '670671': [0.3465, 0.156, 0.158, 0.156, 0.3375, 0.1535, 0.158, 0.1535, 0.3414], '671680': [0.3465, 0.156, 0.158, 0.156, 0.3375, 0.1535, 0.158, 0.1535, 0.3414], '671684': [1.3238, 0.2066, 0.2066, 1.3294], '671692': [0.0001, 0.0, 0.0, 0.0, 0.0001, 0.0, 0.0, 0.0, 0.0001], '684611': [1.3292], '684652': [1.3425], '692675': [0.791721, 0.318476, 0.28345, 0.318476, 0.781649, 0.318476, 0.28345, 0.318476, 0.791721]}, 'Rg': {'632633': 0.01805, '632645': 0.01805, '632670': 0.01805, '645646': 0.01805, '650632': 0.01805, '670671': 0.01805, '671680': 0.01805, '671684': 0.01805, '671692': 0.01805, '684611': 0.01805, '684652': 0.01805, '692675': 0.01805}, 'Rho': {'632633': 100.0, '632645': 100.0, '632670': 100.0, '645646': 100.0, '650632': 100.0, '670671': 100.0, '671680': 100.0, '671684': 100.0, '671692': 100.0, '684611': 100.0, '684652': 100.0, '692675': 100.0}, 'Spacing': {'632633': '', '632645': '', '632670': '', '645646': '', '650632': '', '670671': '', '671680': '', '671684': '', '671692': '', '684611': '', '684652': '', '692675': ''}, 'Units': {'632633': 5, '632645': 5, '632670': 5, '645646': 5, '650632': 5, '670671': 5, '671680': 5, '671684': 5, '671692': 0, '684611': 5, '684652': 5, '692675': 5}, 'X0': {'632633': 0.4047, '632645': 0.4047, '632670': 0.4047, '645646': 0.4047, '650632': 0.4047, '670671': 0.4047, '671680': 0.4047, '671684': 0.4047, '671692': 0.0, '684611': 0.1206, '684652': 0.1206, '692675': 0.4047}, 'X1': {'632633': 0.1206, '632645': 0.1206, '632670': 0.1206, '645646': 0.1206, '650632': 0.1206, '670671': 0.1206, '671680': 0.1206, '671684': 0.1206, '671692': 0.0, '684611': 0.1206, '684652': 0.1206, '692675': 0.1206}, 'XMatrix': {'632633': [1.1814, 0.4236, 0.5017, 0.4236, 1.1983, 0.3849, 0.5017, 0.3849, 1.2112], '632645': [1.3569, 0.4591, 0.4591, 1.3471], '632670': [1.0179, 0.5017, 0.4236, 0.5017, 1.0478, 0.3849, 0.4236, 0.3849, 1.0348], '645646': [1.3569, 0.4591, 0.4591, 1.3471], '650632': [1.0179, 0.5017, 0.4236, 0.5017, 1.0478, 0.3849, 0.4236, 0.3849, 1.0348], '670671': [1.0179, 0.5017, 0.4236, 0.5017, 1.0478, 0.3849, 0.4236, 0.3849, 1.0348], '671680': [1.0179, 0.5017, 0.4236, 0.5017, 1.0478, 0.3849, 0.4236, 0.3849, 1.0348], '671684': [1.3569, 0.4591, 0.4591, 1.3471], '671692': [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], '684611': [1.3475], '684652': [0.5124], '692675': [0.438352, 0.0276838, -0.0184204, 0.0276838, 0.396697, 0.0276838, -0.0184204, 0.0276838, 0.438352]}, 'Xg': {'632633': 0.155081, '632645': 0.155081, '632670': 0.155081, '645646': 0.155081, '650632': 0.155081, '670671': 0.155081, '671680': 0.155081, '671684': 0.155081, '671692': 0.155081, '684611': 0.155081, '684652': 0.155081, '692675': 0.155081}, 'Yprim': {'632633': [5.564470386941076, -7.133623601000619, -1.495114717049371, 1.5058679382212923, -2.1394214811205607, 1.6900708859940965, -5.564470386941076, 7.1336236509818685, 1.495114717049371, -1.50586794893156, 2.1394214811205607, -1.6900708967043643, -1.495114717049371, 1.5058679382212923, 4.9084071780443566, -7.063229336176304, -1.0879942589622877, 1.3823589025648546, 1.495114717049371, -1.50586794893156, -4.9084071780443566, 7.063229386157554, 1.0879942589622877, -1.3823589132751224, -2.1394214811205607, 1.6900708859940965, -1.0879942589622877, 1.3823589025648546, 5.189061809545032, -7.0854196238242695, 2.1394214811205607, -1.6900708967043643, 1.0879942589622877, -1.3823589132751224, -5.189061809545032, 7.085419673805519, -5.564470386941076, 7.1336236509818685, 1.495114717049371, -1.50586794893156, 2.1394214811205607, -1.6900708967043643, 5.564470386941076, -7.133623601000619, -1.495114717049371, 1.5058679382212923, -2.1394214811205607, 1.6900708859940965, 1.495114717049371, -1.50586794893156, -4.9084071780443566, 7.063229386157554, 1.0879942589622877, -1.3823589132751224, -1.495114717049371, 1.5058679382212923, 4.9084071780443566, -7.063229336176304, -1.0879942589622877, 1.3823589025648546, 2.1394214811205607, -1.6900708967043643, 1.0879942589622877, -1.3823589132751224, -5.189061809545032, 7.085419673805519, -2.1394214811205607, 1.6900708859940965, -1.0879942589622877, 1.3823589025648546, 5.189061809545032, -7.0854196238242695], '632645': [4.3049233159489235, -4.005143807731639, -1.4446006150659336, 0.5995892139073424, -4.3049233159489235, 4.005143857712889, 1.4446006150659336, -0.5995892246176102, -1.4446006150659336, 0.5995892139073424, 4.334844320861555, -3.9868570103932255, 1.4446006150659336, -0.5995892246176102, -4.334844320861555, 3.9868570603744753, -4.3049233159489235, 4.005143857712889, 1.4446006150659336, -0.5995892246176102, 4.3049233159489235, -4.005143807731639, -1.4446006150659336, 0.5995892139073424, 1.4446006150659336, -0.5995892246176102, -4.334844320861555, 3.9868570603744753, -1.4446006150659336, 0.5995892139073424, 4.334844320861555, -3.9868570103932255], '632670': [3.4335554553543783, -9.8965831153747, -1.4568043853617796, 3.658944244501999, -0.7977560291105917, 2.7352081140105042, -3.4335554553543783, 9.896583182049687, 1.4568043853617796, -3.6589442587894965, 0.7977560291105917, -2.7352081282980016, -1.4568043853617796, 3.658944244501999, 3.006548025596122, -9.377989931528099, -0.3787147764220645, 2.0889991803940724, 1.4568043853617796, -3.6589442587894965, -3.006548025596122, 9.377989998203086, 0.3787147764220645, -2.08899919468157, -0.7977560291105917, 2.7352081140105042, -0.3787147764220645, 2.0889991803940724, 2.658753201413196, -8.847115639537611, 0.7977560291105917, -2.7352081282980016, 0.3787147764220645, -2.08899919468157, -2.658753201413196, 8.847115706212598, -3.4335554553543783, 9.896583182049687, 1.4568043853617796, -3.6589442587894965, 0.7977560291105917, -2.7352081282980016, 3.4335554553543783, -9.8965831153747, -1.4568043853617796, 3.658944244501999, -0.7977560291105917, 2.7352081140105042, 1.4568043853617796, -3.6589442587894965, -3.006548025596122, 9.377989998203086, 0.3787147764220645, -2.08899919468157, -1.4568043853617796, 3.658944244501999, 3.006548025596122, -9.377989931528099, -0.3787147764220645, 2.0889991803940724, 0.7977560291105917, -2.7352081282980016, 0.3787147764220645, -2.08899919468157, -2.658753201413196, 8.847115706212598, -0.7977560291105917, 2.7352081140105042, -0.3787147764220645, 2.0889991803940724, 2.658753201413196, -8.847115639537611], '645646': [7.174872193248206, -6.675239732866065, -2.407667691776556, 0.9993153679365236, -7.174872193248206, 6.675239762854815, 2.407667691776556, -0.9993153743626844, -2.407667691776556, 0.9993153679365236, 7.224740534769255, -6.6447617373020424, 2.407667691776556, -0.9993153743626844, -7.224740534769255, 6.644761767290793, -7.174872193248206, 6.675239762854815, 2.407667691776556, -0.9993153743626844, 7.174872193248206, -6.675239732866065, -2.407667691776556, 0.9993153679365236, 2.407667691776556, -0.9993153743626844, -7.224740534769255, 6.644761767290793, -2.407667691776556, 0.9993153679365236, 7.224740534769255, -6.6447617373020424], '650632': [1.145090744360685, -3.300510291288572, -0.48584426251815294, 1.2202578674652254, -0.2660516357083827, 0.9121918679463129, -1.145090744360685, 3.3005104912135703, 0.48584426251815294, -1.2202579103062965, 0.2660516357083827, -0.912191910787384, -0.48584426251815294, 1.2202578674652254, 1.0026837665363062, -3.1275594644757296, -0.12630137793675839, 0.6966811885852322, 0.48584426251815294, -1.2202579103062965, -1.0026837665363062, 3.127559664400728, 0.12630137793675839, -0.6966812314263033, -0.2660516357083827, 0.9121918679463129, -0.12630137793675839, 0.6966811885852322, 0.886694192671301, -2.950512888096904, 0.2660516357083827, -0.912191910787384, 0.12630137793675839, -0.6966812314263033, -0.886694192671301, 2.950513088021902, -1.145090744360685, 3.3005104912135703, 0.48584426251815294, -1.2202579103062965, 0.2660516357083827, -0.912191910787384, 1.145090744360685, -3.300510291288572, -0.48584426251815294, 1.2202578674652254, -0.2660516357083827, 0.9121918679463129, 0.48584426251815294, -1.2202579103062965, -1.0026837665363062, 3.127559664400728, 0.12630137793675839, -0.6966812314263033, -0.48584426251815294, 1.2202578674652254, 1.0026837665363062, -3.1275594644757296, -0.12630137793675839, 0.6966811885852322, 0.2660516357083827, -0.912191910787384, 0.12630137793675839, -0.6966812314263033, -0.886694192671301, 2.950513088021902, -0.2660516357083827, 0.9121918679463129, -0.12630137793675839, 0.6966811885852322, 0.886694192671301, -2.950512888096904], '670671': [1.7180656329492654, -4.952003604504783, -0.7289486309349635, 1.8308445480500222, -0.3991772478745428, 1.3686299951334238, -1.7180656329492654, 4.9520037377547945, 0.7289486309349635, -1.8308445766035961, 0.3991772478745428, -1.3686300236869977, -0.7289486309349635, 1.8308445480500222, 1.5044017502420202, -4.69251249150727, -0.18949944176557929, 1.045283139377864, 0.7289486309349635, -1.8308445766035961, -1.5044017502420202, 4.692512624757282, 0.18949944176557929, -1.045283167931438, -0.3991772478745428, 1.3686299951334238, -0.18949944176557929, 1.045283139377864, 1.3303738824775715, -4.426876217870621, 0.3991772478745428, -1.3686300236869977, 0.18949944176557929, -1.045283167931438, -1.3303738824775715, 4.426876351120633, -1.7180656329492654, 4.9520037377547945, 0.7289486309349635, -1.8308445766035961, 0.3991772478745428, -1.3686300236869977, 1.7180656329492654, -4.952003604504783, -0.7289486309349635, 1.8308445480500222, -0.3991772478745428, 1.3686299951334238, 0.7289486309349635, -1.8308445766035961, -1.5044017502420202, 4.692512624757282, 0.18949944176557929, -1.045283167931438, -0.7289486309349635, 1.8308445480500222, 1.5044017502420202, -4.69251249150727, -0.18949944176557929, 1.045283139377864, 0.3991772478745428, -1.3686300236869977, 0.18949944176557929, -1.045283167931438, -1.3303738824775715, 4.426876351120633, -0.3991772478745428, 1.3686299951334238, -0.18949944176557929, 1.045283139377864, 1.3303738824775715, -4.426876217870621], '671680': [2.29018148872137, -6.601020882464641, -0.9716885250363059, 2.4405157991920574, -0.5321032714167654, 1.8243838001542325, -2.29018148872137, 6.601020982427141, 0.9716885250363059, -2.440515820612593, 0.5321032714167654, -1.824383821574768, -0.9716885250363059, 2.4405157991920574, 2.0053675330726124, -6.255119228838956, -0.25260275587351677, 1.393362441432071, 0.9716885250363059, -2.440515820612593, -2.0053675330726124, 6.255119328801456, 0.25260275587351677, -1.3933624628526067, -0.5321032714167654, 1.8243838001542325, -0.25260275587351677, 1.393362441432071, 1.773388385342602, -5.901026076081305, 0.5321032714167654, -1.824383821574768, 0.25260275587351677, -1.3933624628526067, -1.773388385342602, 5.901026176043804, -2.29018148872137, 6.601020982427141, 0.9716885250363059, -2.440515820612593, 0.5321032714167654, -1.824383821574768, 2.29018148872137, -6.601020882464641, -0.9716885250363059, 2.4405157991920574, -0.5321032714167654, 1.8243838001542325, 0.9716885250363059, -2.440515820612593, -2.0053675330726124, 6.255119328801456, 0.25260275587351677, -1.3933624628526067, -0.9716885250363059, 2.4405157991920574, 2.0053675330726124, -6.255119228838956, -0.25260275587351677, 1.393362441432071, 0.5321032714167654, -1.824383821574768, 0.25260275587351677, -1.3933624628526067, -1.773388385342602, 5.901026176043804, -0.5321032714167654, 1.8243838001542325, -0.25260275587351677, 1.393362441432071, 1.773388385342602, -5.901026076081305], '671684': [7.174872193248206, -6.675239732866065, -2.407667691776556, 0.9993153679365236, -7.174872193248206, 6.675239762854815, 2.407667691776556, -0.9993153743626844, -2.407667691776556, 0.9993153679365236, 7.224740534769255, -6.6447617373020424, 2.407667691776556, -0.9993153743626844, -7.224740534769255, 6.644761767290793, -7.174872193248206, 6.675239762854815, 2.407667691776556, -0.9993153743626844, 7.174872193248206, -6.675239732866065, -2.407667691776556, 0.9993153679365236, 2.407667691776556, -0.9993153743626844, -7.224740534769255, 6.644761767290793, -2.407667691776556, 0.9993153679365236, 7.224740534769255, -6.6447617373020424], '671692': [10000000.0, 0.0, 0.0, 0.0, 0.0, 0.0, -10000000.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 10000000.0, 0.0, 0.0, 0.0, 0.0, 0.0, -10000000.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 10000000.0, 0.0, 0.0, 0.0, 0.0, 0.0, -10000000.0, 0.0, -10000000.0, 0.0, 0.0, 0.0, 0.0, 0.0, 10000000.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, -10000000.0, 0.0, 0.0, 0.0, 0.0, 0.0, 10000000.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, -10000000.0, 0.0, 0.0, 0.0, 0.0, 0.0, 10000000.0, 0.0], '684611': [6.529823239597013, -6.6197237251699725, -6.529823239597013, 6.619723755158723, -6.529823239597013, 6.619723755158723, 6.529823239597013, -6.6197237251699725], '684652': [4.290972612222875, -1.6377544265266006, -4.290972612222875, 1.637761166855122, -4.290972612222875, 1.637761166855122, 4.290972612222875, -1.6377544265266006], '692675': [10.412482684253026, -7.836346738670522, -2.4285352771370636, 3.079311097832397, -1.080921781180488, 2.49252596573072, -10.412482684253026, 7.836353592313676, 2.4285352771370636, -3.079311097832397, 1.080921781180488, -2.49252596573072, -2.4285352771370636, 3.079311097832397, 11.54642946546697, -8.19720842103701, -2.428535277137064, 3.079311097832396, 2.4285352771370636, -3.079311097832397, -11.54642946546697, 8.197215274680165, 2.428535277137064, -3.079311097832396, -1.080921781180488, 2.49252596573072, -2.428535277137064, 3.079311097832396, 10.412482684253028, -7.83634673867052, 1.080921781180488, -2.49252596573072, 2.428535277137064, -3.079311097832396, -10.412482684253028, 7.8363535923136745, -10.412482684253026, 7.836353592313676, 2.4285352771370636, -3.079311097832397, 1.080921781180488, -2.49252596573072, 10.412482684253026, -7.836346738670522, -2.4285352771370636, 3.079311097832397, -1.080921781180488, 2.49252596573072, 2.4285352771370636, -3.079311097832397, -11.54642946546697, 8.197215274680165, 2.428535277137064, -3.079311097832396, -2.4285352771370636, 3.079311097832397, 11.54642946546697, -8.19720842103701, -2.428535277137064, 3.079311097832396, 1.080921781180488, -2.49252596573072, 2.428535277137064, -3.079311097832396, -10.412482684253028, 7.8363535923136745, -1.080921781180488, 2.49252596573072, -2.428535277137064, 3.079311097832396, 10.412482684253028, -7.83634673867052]}}
    ).to_dict()

    actual_dict = dss.utils.lines_to_dataframe().to_dict()

    assert_dict_equal(actual_dict, expected_dict)



def test_loads_to_dataframe(dss):

    expected_dict = pd.DataFrame(
        {'AllocationFactor': {'611': 0.5, '634a': 0.5, '634b': 0.5, '634c': 0.5, '645': 0.5, '646': 0.5, '652': 0.5, '670a': 0.5, '670b': 0.5, '670c': 0.5, '671': 0.5, '675a': 0.5, '675b': 0.5, '675c': 0.5, '692': 0.5}, 'CFactor': {'611': 4.0, '634a': 4.0, '634b': 4.0, '634c': 4.0, '645': 4.0, '646': 4.0, '652': 4.0, '670a': 4.0, '670b': 4.0, '670c': 4.0, '671': 4.0, '675a': 4.0, '675b': 4.0, '675c': 4.0, '692': 4.0}, 'CVRCurve': {'611': '', '634a': '', '634b': '', '634c': '', '645': '', '646': '', '652': '', '670a': '', '670b': '', '670c': '', '671': '', '675a': '', '675b': '', '675c': '', '692': ''}, 'CVRvars': {'611': 2.0, '634a': 2.0, '634b': 2.0, '634c': 2.0, '645': 2.0, '646': 2.0, '652': 2.0, '670a': 2.0, '670b': 2.0, '670c': 2.0, '671': 2.0, '675a': 2.0, '675b': 2.0, '675c': 2.0, '692': 2.0}, 'CVRwatts': {'611': 1.0, '634a': 1.0, '634b': 1.0, '634c': 1.0, '645': 1.0, '646': 1.0, '652': 1.0, '670a': 1.0, '670b': 1.0, '670c': 1.0, '671': 1.0, '675a': 1.0, '675b': 1.0, '675c': 1.0, '692': 1.0}, 'Class': {'611': 1, '634a': 1, '634b': 1, '634c': 1, '645': 1, '646': 1, '652': 1, '670a': 1, '670b': 1, '670c': 1, '671': 1, '675a': 1, '675b': 1, '675c': 1, '692': 1}, 'Count': {'611': 15, '634a': 15, '634b': 15, '634c': 15, '645': 15, '646': 15, '652': 15, '670a': 15, '670b': 15, '670c': 15, '671': 15, '675a': 15, '675b': 15, '675c': 15, '692': 15}, 'Daily': {'611': '', '634a': '', '634b': '', '634c': '', '645': '', '646': '', '652': '', '670a': '', '670b': '', '670c': '', '671': '', '675a': '', '675b': '', '675c': '', '692': ''}, 'Duty': {'611': '', '634a': '', '634b': '', '634c': '', '645': '', '646': '', '652': '', '670a': '', '670b': '', '670c': '', '671': '', '675a': '', '675b': '', '675c': '', '692': ''}, 'Growth': {'611': '', '634a': '', '634b': '', '634c': '', '645': '', '646': '', '652': '', '670a': '', '670b': '', '670c': '', '671': '', '675a': '', '675b': '', '675c': '', '692': ''}, 'Idx': {'611': 11, '634a': 2, '634b': 3, '634c': 4, '645': 5, '646': 6, '652': 12, '670a': 13, '670b': 14, '670c': 15, '671': 1, '675a': 8, '675b': 9, '675c': 10, '692': 7}, 'IsDelta': {'611': 0, '634a': 0, '634b': 0, '634c': 0, '645': 0, '646': 1, '652': 0, '670a': 0, '670b': 0, '670c': 0, '671': 1, '675a': 0, '675b': 0, '675c': 0, '692': 1}, 'Model': {'611': 5, '634a': 1, '634b': 1, '634c': 1, '645': 1, '646': 2, '652': 2, '670a': 1, '670b': 1, '670c': 1, '671': 1, '675a': 1, '675b': 1, '675c': 1, '692': 5}, 'Name': {'611': '611', '634a': '634a', '634b': '634b', '634c': '634c', '645': '645', '646': '646', '652': '652', '670a': '670a', '670b': '670b', '670c': '670c', '671': '671', '675a': '675a', '675b': '675b', '675c': '675c', '692': '692'}, 'NumCust': {'611': 1, '634a': 1, '634b': 1, '634c': 1, '645': 1, '646': 1, '652': 1, '670a': 1, '670b': 1, '670c': 1, '671': 1, '675a': 1, '675b': 1, '675c': 1, '692': 1}, 'PF': {'611': 0.9048187022009941, '634a': 0.8240419241993675, '634b': 0.8, '634c': 0.8, '645': 0.8056510126494245, '646': 0.8673133941933718, '652': 0.8300495997825932, '670a': 0.8619342151577695, '670b': 0.8666224568741688, '670c': 0.8645818496218686, '671': 0.8682431421244591, '675a': 0.9311010850748034, '675b': 0.7498378553650925, '675c': 0.8072891017918288, '692': 0.7476519144858309}, 'PctMean': {'611': 50.0, '634a': 50.0, '634b': 50.0, '634c': 50.0, '645': 50.0, '646': 50.0, '652': 50.0, '670a': 50.0, '670b': 50.0, '670c': 50.0, '671': 50.0, '675a': 50.0, '675b': 50.0, '675c': 50.0, '692': 50.0}, 'PctStdDev': {'611': 10.0, '634a': 10.0, '634b': 10.0, '634c': 10.0, '645': 10.0, '646': 10.0, '652': 10.0, '670a': 10.0, '670b': 10.0, '670c': 10.0, '671': 10.0, '675a': 10.0, '675b': 10.0, '675c': 10.0, '692': 10.0}, 'RelWeighting': {'611': 1.0, '634a': 1.0, '634b': 1.0, '634c': 1.0, '645': 1.0, '646': 1.0, '652': 1.0, '670a': 1.0, '670b': 1.0, '670c': 1.0, '671': 1.0, '675a': 1.0, '675b': 1.0, '675c': 1.0, '692': 1.0}, 'Rneut': {'611': -1.0, '634a': -1.0, '634b': -1.0, '634c': -1.0, '645': -1.0, '646': -1.0, '652': -1.0, '670a': -1.0, '670b': -1.0, '670c': -1.0, '671': -1.0, '675a': -1.0, '675b': -1.0, '675c': -1.0, '692': -1.0}, 'Spectrum': {'611': 'defaultload', '634a': 'defaultload', '634b': 'defaultload', '634c': 'defaultload', '645': 'defaultload', '646': 'defaultload', '652': 'defaultload', '670a': 'defaultload', '670b': 'defaultload', '670c': 'defaultload', '671': 'defaultload', '675a': 'defaultload', '675b': 'defaultload', '675c': 'defaultload', '692': 'defaultload'}, 'Status': {'611': 0, '634a': 0, '634b': 0, '634c': 0, '645': 0, '646': 0, '652': 0, '670a': 0, '670b': 0, '670c': 0, '671': 0, '675a': 0, '675b': 0, '675c': 0, '692': 0}, 'Vmaxpu': {'611': 1.05, '634a': 1.05, '634b': 1.05, '634c': 1.05, '645': 1.05, '646': 1.05, '652': 1.05, '670a': 1.05, '670b': 1.05, '670c': 1.05, '671': 1.05, '675a': 1.05, '675b': 1.05, '675c': 1.05, '692': 1.05}, 'VminEmerg': {'611': 0.0, '634a': 0.0, '634b': 0.0, '634c': 0.0, '645': 0.0, '646': 0.0, '652': 0.0, '670a': 0.0, '670b': 0.0, '670c': 0.0, '671': 0.0, '675a': 0.0, '675b': 0.0, '675c': 0.0, '692': 0.0}, 'VminNorm': {'611': 0.0, '634a': 0.0, '634b': 0.0, '634c': 0.0, '645': 0.0, '646': 0.0, '652': 0.0, '670a': 0.0, '670b': 0.0, '670c': 0.0, '671': 0.0, '675a': 0.0, '675b': 0.0, '675c': 0.0, '692': 0.0}, 'Vminpu': {'611': 0.95, '634a': 0.95, '634b': 0.95, '634c': 0.95, '645': 0.95, '646': 0.95, '652': 0.95, '670a': 0.95, '670b': 0.95, '670c': 0.95, '671': 0.95, '675a': 0.95, '675b': 0.95, '675c': 0.95, '692': 0.95}, 'XfkVA': {'611': 0.0, '634a': 0.0, '634b': 0.0, '634c': 0.0, '645': 0.0, '646': 0.0, '652': 0.0, '670a': 0.0, '670b': 0.0, '670c': 0.0, '671': 0.0, '675a': 0.0, '675b': 0.0, '675c': 0.0, '692': 0.0}, 'Xneut': {'611': 0.0, '634a': 0.0, '634b': 0.0, '634c': 0.0, '645': 0.0, '646': 0.0, '652': 0.0, '670a': 0.0, '670b': 0.0, '670c': 0.0, '671': 0.0, '675a': 0.0, '675b': 0.0, '675c': 0.0, '692': 0.0}, 'Yearly': {'611': '', '634a': '', '634b': '', '634c': '', '645': '', '646': '', '652': '', '670a': '', '670b': '', '670c': '', '671': '', '675a': '', '675b': '', '675c': '', '692': ''}, 'ZipV': {'611': [], '634a': [], '634b': [], '634c': [], '645': [], '646': [], '652': [], '670a': [], '670b': [], '670c': [], '671': [], '675a': [], '675b': [], '675c': [], '692': []}, 'kV': {'611': 2.4, '634a': 0.277, '634b': 0.277, '634c': 0.277, '645': 2.4, '646': 4.16, '652': 2.4, '670a': 2.4, '670b': 2.4, '670c': 2.4, '671': 4.16, '675a': 2.4, '675b': 2.4, '675c': 2.4, '692': 4.16}, 'kVABase': {'611': 187.88294228055935, '634a': 194.164878389476, '634b': 150.0, '634c': 150.0, '645': 211.00947846009194, '646': 265.18672666632466, '652': 154.20765220960988, '670a': 19.72308292331602, '670b': 76.15773105863909, '670c': 135.32553343696821, '671': 1330.2725284692608, '675a': 520.8886637276722, '675b': 90.68627239003708, '675c': 359.22694776422327, '692': 227.37853900489378}, 'kW': {'611': 170.0, '634a': 160.0, '634b': 120.0, '634c': 120.0, '645': 170.0, '646': 230.0, '652': 128.0, '670a': 17.0, '670b': 66.0, '670c': 117.0, '671': 1155.0, '675a': 485.0, '675b': 68.0, '675c': 290.0, '692': 170.0}, 'kWh': {'611': 0.0, '634a': 0.0, '634b': 0.0, '634c': 0.0, '645': 0.0, '646': 0.0, '652': 0.0, '670a': 0.0, '670b': 0.0, '670c': 0.0, '671': 0.0, '675a': 0.0, '675b': 0.0, '675c': 0.0, '692': 0.0}, 'kWhDays': {'611': 30.0, '634a': 30.0, '634b': 30.0, '634c': 30.0, '645': 30.0, '646': 30.0, '652': 30.0, '670a': 30.0, '670b': 30.0, '670c': 30.0, '671': 30.0, '675a': 30.0, '675b': 30.0, '675c': 30.0, '692': 30.0}, 'kvar': {'611': 80.0, '634a': 110.0, '634b': 90.0, '634c': 90.0, '645': 125.0, '646': 132.0, '652': 86.0, '670a': 10.0, '670b': 38.0, '670c': 68.0, '671': 660.0, '675a': 190.0, '675b': 60.0, '675c': 212.0, '692': 151.0}, 'puSeriesRL': {'611': 50.0, '634a': 50.0, '634b': 50.0, '634c': 50.0, '645': 50.0, '646': 50.0, '652': 50.0, '670a': 50.0, '670b': 50.0, '670c': 50.0, '671': 50.0, '675a': 50.0, '675b': 50.0, '675c': 50.0, '692': 50.0}}
    ).to_dict()

    actual_dict = dss.utils.loads_to_dataframe().to_dict()

    assert_dict_equal(actual_dict, expected_dict)



def test_loadshape_to_dataframe(dss):

    expected_dict = pd.DataFrame(
        {'Count': {'default': 1}, 'HrInterval': {'default': 1.0}, 'MinInterval': {'default': 60.0}, 'Name': {'default': 'default'}, 'Normalize': {'default': 0}, 'Npts': {'default': 24}, 'PBase': {'default': 0.0}, 'PMult': {'default': [0.677, 0.6256, 0.6087, 0.5833, 0.58028, 0.6025, 0.657, 0.7477, 0.832, 0.88, 0.94, 0.989, 0.985, 0.98, 0.9898, 0.999, 1.0, 0.958, 0.936, 0.913, 0.876, 0.876, 0.828, 0.756]}, 'QBase': {'default': 0.0}, 'QMult': {'default': [0.0]}, 'SInterval': {'default': 3600.0}, 'TimeArray': {'default': [0.0]}, 'UseActual': {'default': 0}}
    ).to_dict()

    actual_dict = dss.utils.loadshape_to_dataframe().to_dict()

    assert_dict_equal(actual_dict, expected_dict)


def test_meters_to_dataframe(dss):

    expected_dict = pd.DataFrame(
        {'AllBranchesInZone': {'0': []},
         'AllEndElements': {'0': []},
         'AllocFactors': {'0': [0.0]},
         'AvgRepairTime': {'0': 0.0},
         'CalcCurrent': {'0': [0.0]},
         'CloseAllDIFiles': {'0': 0},
         'Count': {'0': 0},
         'CountBranches': {'0': 0},
         'CountEndElements': {'0': 0},
         'CustInterrupts': {'0': 0.0},
         'DIFilesAreOpen': {'0': 0},
         'DoReliabilityCalc': {'0': 0},
         'FaultRateXRepairHrs': {'0': 0.0},
         'MeteredElement': {'0': ''},
         'MeteredTerminal': {'0': 0},
         'Name': {'0': '0'},
         'NumSectionBranches': {'0': 0},
         'NumSectionCustomers': {'0': 0},
         'NumSections': {'0': 0},
         'OCPDeviceType': {'0': 0},
         'OpenAllDIFiles': {'0': 0},
         'PeakCurrent': {'0': [0.0]},
         'RegisterNames': {'0': []},
         'RegisterValues': {'0': [0.0]},
         'Reset': {'0': 0},
         'ResetAll': {'0': 0},
         'SAIDI': {'0': 0.0},
         'SAIFI': {'0': 0.0},
         'SAIFIkW': {'0': 0.0},
         'Sample': {'0': 0},
         'SampleAll': {'0': 0},
         'Save': {'0': 0},
         'SaveAll': {'0': 0},
         'SectSeqidx': {'0': 0},
         'SectTotalCust': {'0': 0},
         'SeqListSize': {'0': 0},
         'SequenceList': {'0': 0},
         'SetActiveSection': {'0': 0},
         'SumBranchFltRates': {'0': 0.0},
         'TotalCustomers': {'0': 0},
         'Totals': {'0': [0.0,
           0.0,
           0.0,
           0.0,
           0.0,
           0.0,
           0.0,
           0.0,
           0.0,
           0.0,
           0.0,
           0.0,
           0.0,
           0.0,
           0.0,
           0.0,
           0.0,
           0.0,
           0.0,
           0.0,
           0.0,
           0.0,
           0.0,
           0.0,
           0.0,
           0.0,
           0.0,
           0.0,
           0.0,
           0.0,
           0.0,
           0.0,
           0.0,
           0.0,
           0.0,
           0.0,
           0.0,
           0.0,
           0.0,
           0.0,
           0.0,
           0.0,
           0.0,
           0.0,
           0.0,
           0.0,
           0.0,
           0.0,
           0.0,
           0.0,
           0.0,
           0.0,
           0.0,
           0.0,
           0.0,
           0.0,
           0.0,
           0.0,
           0.0,
           0.0,
           0.0,
           0.0,
           0.0,
           0.0,
           0.0,
           0.0,
           0.0]}}
    ).to_dict()

    actual_dict = dss.utils.meters_to_dataframe().to_dict()

    assert_dict_equal(actual_dict, expected_dict)


def test_pvsystems_to_dataframe(dss):

    dss.run_command('New PVSystem.631')

    expected_dict = pd.DataFrame(
        {'Count': {'631': 1},
         'Idx': {'631': 1},
         'Irradiance': {'631': 1.0},
         'Name': {'631': '631'},
         'kVARated': {'631': 500.0},
         'kW': {'631': 499.99999999999994},
         'kvar': {'631': 0.0},
         'pf': {'631': 1.0}}
    ).to_dict()

    actual_dict = dss.utils.pvsystems_to_dataframe().to_dict()

    assert_dict_equal(actual_dict, expected_dict)


def test_reclosers_to_dataframe(dss):

    expected_dict = pd.DataFrame(
        {'Close': {'': 0},
         'Count': {'': 0},
         'GroundInst': {'': 0.0},
         'GroundTrip': {'': 0.0},
         'Idx': {'': 0},
         'MonitoredObj': {'': ''},
         'MonitoredTerm': {'': 0},
         'Name': {'': ''},
         'NumFast': {'': 0},
         'Open': {'': 0},
         'PhaseInst': {'': 0.0},
         'PhaseTrip': {'': 0.0},
         'RecloseIntervals': {'': [-1.0]},
         'Shots': {'': 0},
         'SwitchedObj': {'': ''},
         'SwitchedTerm': {'': 0}}
    ).to_dict()

    actual_dict = dss.utils.reclosers_to_dataframe().to_dict()

    assert_dict_equal(actual_dict, expected_dict)



def test_regcontrols_to_dataframe(dss):

    expected_dict = pd.DataFrame(
        {'CTPrimary': {'reg1': 700.0, 'reg2': 700.0, 'reg3': 700.0}, 'Count': {'reg1': 3, 'reg2': 3, 'reg3': 3}, 'Delay': {'reg1': 15.0, 'reg2': 15.0, 'reg3': 15.0}, 'ForwardBand': {'reg1': 2.0, 'reg2': 2.0, 'reg3': 2.0}, 'ForwardR': {'reg1': 3.0, 'reg2': 3.0, 'reg3': 3.0}, 'ForwardVreg': {'reg1': 122.0, 'reg2': 122.0, 'reg3': 122.0}, 'ForwardX': {'reg1': 9.0, 'reg2': 9.0, 'reg3': 9.0}, 'IsInverseTime': {'reg1': 0, 'reg2': 0, 'reg3': 0}, 'IsReversible': {'reg1': 0, 'reg2': 0, 'reg3': 0}, 'MaxTapChange': {'reg1': 16, 'reg2': 16, 'reg3': 16}, 'MonitoredBus': {'reg1': '', 'reg2': '', 'reg3': ''}, 'Name': {'reg1': 'reg1', 'reg2': 'reg2', 'reg3': 'reg3'}, 'PTRatio': {'reg1': 20.0, 'reg2': 20.0, 'reg3': 20.0}, 'ReverseBand': {'reg1': 3.0, 'reg2': 3.0, 'reg3': 3.0}, 'ReverseR': {'reg1': 0.0, 'reg2': 0.0, 'reg3': 0.0}, 'ReverseVreg': {'reg1': 120.0, 'reg2': 120.0, 'reg3': 120.0}, 'ReverseX': {'reg1': 0.0, 'reg2': 0.0, 'reg3': 0.0}, 'TapDelay': {'reg1': 2.0, 'reg2': 2.0, 'reg3': 2.0}, 'TapNumber': {'reg1': 9, 'reg2': 6, 'reg3': 9}, 'TapWinding': {'reg1': 2, 'reg2': 2, 'reg3': 2}, 'Transformer': {'reg1': 'reg1', 'reg2': 'reg2', 'reg3': 'reg3'}, 'VoltageLimit': {'reg1': 0.0, 'reg2': 0.0, 'reg3': 0.0}, 'Winding': {'reg1': 2, 'reg2': 2, 'reg3': 2}}
    ).to_dict()

    actual_dict = dss.utils.regcontrols_to_dataframe().to_dict()

    assert_dict_equal(actual_dict, expected_dict)



def test_relays_to_dataframe(dss):

    expected_dict = pd.DataFrame(
        {'Count': {'': 0},
         'Idx': {'': 0},
         'MonitoredObj': {'': ''},
         'MonitoredTerm': {'': 0},
         'Name': {'': ''},
         'SwitchedObj': {'': ''},
         'SwitchedTerm': {'': 0}}
    ).to_dict()

    actual_dict = dss.utils.relays_to_dataframe().to_dict()

    assert_dict_equal(actual_dict, expected_dict)



def test_sensors_to_dataframe(dss):

    expected_dict = pd.DataFrame(
        {'Count': {'': 0},
         'Currents': {'': [0.0]},
         'IsDelta': {'': 0},
         'MeteredElement': {'': ''},
         'MeteredTerminal': {'': 0},
         'Name': {'': ''},
         'PctError': {'': 0.0},
         'Reset': {'': 0},
         'ResetAll': {'': 0},
         'ReverseDelta': {'': 0},
         'Weight': {'': 0.0},
         'kVBase': {'': 0.0},
         'kW': {'': [0.0]},
         'kvar': {'': [0.0]}}
    ).to_dict()

    actual_dict = dss.utils.sensors_to_dataframe().to_dict()

    assert_dict_equal(actual_dict, expected_dict)



def test_transformers_to_dataframe(dss):

    expected_dict = pd.DataFrame(
        {'Count': {'reg1': 5, 'reg2': 5, 'reg3': 5, 'sub': 5, 'xfm1': 5}, 'IsDelta': {'reg1': 0, 'reg2': 0, 'reg3': 0, 'sub': 0, 'xfm1': 0}, 'MaxTap': {'reg1': 1.1, 'reg2': 1.1, 'reg3': 1.1, 'sub': 1.1, 'xfm1': 1.1}, 'MinTap': {'reg1': 0.9, 'reg2': 0.9, 'reg3': 0.9, 'sub': 0.9, 'xfm1': 0.9}, 'Name': {'reg1': 'reg1', 'reg2': 'reg2', 'reg3': 'reg3', 'sub': 'sub', 'xfm1': 'xfm1'}, 'NumTaps': {'reg1': 32, 'reg2': 32, 'reg3': 32, 'sub': 32, 'xfm1': 32}, 'NumWindings': {'reg1': 2, 'reg2': 2, 'reg3': 2, 'sub': 2, 'xfm1': 2}, 'R': {'reg1': 5e-05, 'reg2': 5e-05, 'reg3': 5e-05, 'sub': 5e-06, 'xfm1': 0.0055000000000000005}, 'Rneut': {'reg1': -1.0, 'reg2': -1.0, 'reg3': -1.0, 'sub': -1.0, 'xfm1': -1.0}, 'Tap': {'reg1': 1.05625, 'reg2': 1.0375, 'reg3': 1.05625, 'sub': 1.0, 'xfm1': 1.0}, 'Wdg': {'reg1': 2, 'reg2': 2, 'reg3': 2, 'sub': 2, 'xfm1': 2}, 'XfmrCode': {'reg1': '', 'reg2': '', 'reg3': '', 'sub': '', 'xfm1': ''}, 'Xhl': {'reg1': 0.0001, 'reg2': 0.0001, 'reg3': 0.0001, 'sub': 8e-05, 'xfm1': 0.02}, 'Xht': {'reg1': 0.35, 'reg2': 0.35, 'reg3': 0.35, 'sub': 0.04, 'xfm1': 0.01}, 'Xlt': {'reg1': 0.3, 'reg2': 0.3, 'reg3': 0.3, 'sub': 0.04, 'xfm1': 0.01}, 'Xneut': {'reg1': 0.0, 'reg2': 0.0, 'reg3': 0.0, 'sub': 0.0, 'xfm1': 0.0}, 'kV': {'reg1': 2.4, 'reg2': 2.4, 'reg3': 2.4, 'sub': 4.16, 'xfm1': 0.48}, 'kVA': {'reg1': 1666.0, 'reg2': 1666.0, 'reg3': 1666.0, 'sub': 5000.0, 'xfm1': 500.0}}
    ).to_dict()

    actual_dict = dss.utils.transformers_to_dataframe().to_dict()

    assert_dict_equal(actual_dict, expected_dict)



def test_vsources_to_dataframe(dss):

    expected_dict = pd.DataFrame(
        {'AngleDeg': {'source': 30.0}, 'BasekV': {'source': 115.0}, 'Count': {'source': 1}, 'Frequency': {'source': 60.0}, 'Name': {'source': 'source'}, 'PU': {'source': 1.0001}, 'Phases': {'source': 3}}
    ).to_dict()

    actual_dict = dss.utils.vsources_to_dataframe().to_dict()

    assert_dict_equal(actual_dict, expected_dict)


def test_xycurves_to_dataframe(dss):

    expected_dict = pd.DataFrame(
        {'Count': {'': 0}, 'Name': {'': ''}, 'Npts': {'': 0}, 'X': {'': 0.0}, 'XArray': {'': [0.0]}, 'XScale': {'': 0.0}, 'XShift': {'': 0.0}, 'Y': {'': 0.0}, 'YArray': {'': [0.0]}, 'YScale': {'': 0.0}, 'YShift': {'': 0.0}}
    ).to_dict()

    actual_dict = dss.utils.xycurves_to_dataframe().to_dict()

    assert_dict_equal(actual_dict, expected_dict)


def test_storage_to_dataframe(dss):

    dss.run_command('New Storage.631')

    expected_dict = pd.DataFrame({'%Charge': {'Storage.631': '100'},
     '%Discharge': {'Storage.631': '100'},
     '%EffCharge': {'Storage.631': '90'},
     '%EffDischarge': {'Storage.631': '90'},
     '%IdlingkW': {'Storage.631': '1'},
     '%Idlingkvar': {'Storage.631': '0'},
     '%R': {'Storage.631': '0'},
     '%X': {'Storage.631': '50'},
     '%reserve': {'Storage.631': '20'},
     '%stored': {'Storage.631': '100'},
     'Balanced': {'Storage.631': 'No'},
     'ChargeTrigger': {'Storage.631': '0'},
     'DischargeTrigger': {'Storage.631': '0'},
     'DispMode': {'Storage.631': 'default'},
     'DynaDLL': {'Storage.631': ''},
     'DynaData': {'Storage.631': ()},
     'LimitCurrent': {'Storage.631': 'No'},
     'State': {'Storage.631': 'IDLING'},
     'TimeChargeTrig': {'Storage.631': '2'},
     'UserData': {'Storage.631': ()},
     'UserModel': {'Storage.631': ''},
     'Vmaxpu': {'Storage.631': '1.1'},
     'Vminpu': {'Storage.631': '0.9'},
     'basefreq': {'Storage.631': '60'},
     'bus1': {'Storage.631': '631_1'},
     'class': {'Storage.631': '1'},
     'conn': {'Storage.631': 'wye'},
     'daily': {'Storage.631': ''},
     'debugtrace': {'Storage.631': 'NO'},
     'duty': {'Storage.631': ''},
     'enabled': {'Storage.631': True},
     'kVA': {'Storage.631': '25'},
     'kW': {'Storage.631': '0'},
     'kWhrated': {'Storage.631': '50'},
     'kWhstored': {'Storage.631': '50'},
     'kWrated': {'Storage.631': '25'},
     'kv': {'Storage.631': '12.47'},
     'kvar': {'Storage.631': '0'},
     'like': {'Storage.631': ''},
     'model': {'Storage.631': '1'},
     'pf': {'Storage.631': '1'},
     'phases': {'Storage.631': '3'},
     'spectrum': {'Storage.631': ''},
     'yearly': {'Storage.631': ''}}
    ).to_dict()


    actual_dict = dss.utils.class_to_dataframe('Storage').to_dict()

    assert_dict_equal(actual_dict, expected_dict)

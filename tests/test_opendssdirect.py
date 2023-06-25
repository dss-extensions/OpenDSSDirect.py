# -*- coding: utf-8 -*-
import pytest as pt
import os
import pandas as pd
try:
    from pandas._testing import assert_dict_equal #TODO: migrate to something else, this is bad
except:
    from pandas.util.testing import assert_dict_equal

import numpy as np

current_directory = os.path.dirname(os.path.realpath(__file__))
PATH_TO_DSS = os.path.abspath(
    os.path.join(current_directory, "./data/13Bus/IEEE13Nodeckt.dss")
)


@pt.fixture()
def dss():
    import opendssdirect as dss

    dss.Error.ExtendedErrors(True)
    dss.Text.Command("set eventlogdefault=yes")
    assert (
        dss.utils.run_command("Redirect {}".format(PATH_TO_DSS)) == ""
    ), "Unable to find test data"
    return dss


def test_extended_errors(dss):
    assert dss.Error.ExtendedErrors()


def test_package_import():

    import opendssdirect

    assert getattr(opendssdirect, "__version__") is not None


def test_module_import():

    import inspect

    from opendssdirect import ActiveClass as m

    assert inspect.ismodule(m)

    from opendssdirect import Basic as m

    assert inspect.ismodule(m)

    from opendssdirect import Bus as m

    assert inspect.ismodule(m)

    from opendssdirect import Capacitors as m

    assert inspect.ismodule(m)

    from opendssdirect import CapControls as m

    assert inspect.ismodule(m)

    from opendssdirect import Circuit as m

    assert inspect.ismodule(m)

    from opendssdirect import CktElement as m

    assert inspect.ismodule(m)

    from opendssdirect import Element as m

    assert inspect.ismodule(m)

    from opendssdirect import Executive as m

    assert inspect.ismodule(m)

    from opendssdirect import Fuses as m

    assert inspect.ismodule(m)

    from opendssdirect import Generators as m

    assert inspect.ismodule(m)

    from opendssdirect import Isource as m

    assert inspect.ismodule(m)

    from opendssdirect import Lines as m

    assert inspect.ismodule(m)

    from opendssdirect import Loads as m

    assert inspect.ismodule(m)

    from opendssdirect import LoadShape as m

    assert inspect.ismodule(m)

    from opendssdirect import Meters as m

    assert inspect.ismodule(m)

    from opendssdirect import Monitors as m

    assert inspect.ismodule(m)

    from opendssdirect import Parser as m

    assert inspect.ismodule(m)

    from opendssdirect import PDElements as m

    assert inspect.ismodule(m)

    from opendssdirect import Properties as m

    assert inspect.ismodule(m)

    from opendssdirect import PVsystems as m

    assert inspect.ismodule(m)

    from opendssdirect import Reclosers as m

    assert inspect.ismodule(m)

    from opendssdirect import RegControls as m

    assert inspect.ismodule(m)

    from opendssdirect import Relays as m

    assert inspect.ismodule(m)

    from opendssdirect import Sensors as m

    assert inspect.ismodule(m)

    from opendssdirect import Settings as m

    assert inspect.ismodule(m)

    from opendssdirect import Solution as m

    assert inspect.ismodule(m)

    from opendssdirect import SwtControls as m

    assert inspect.ismodule(m)

    from opendssdirect import Topology as m

    assert inspect.ismodule(m)

    from opendssdirect import Transformers as m

    assert inspect.ismodule(m)

    from opendssdirect import Vsources as m

    assert inspect.ismodule(m)

    from opendssdirect import XYCurves as m

    assert inspect.ismodule(m)


def test_ActiveClass(dss):

    assert dss.ActiveClass.ActiveClassName() == u"Line"
    assert dss.ActiveClass.AllNames() == [
        u"650632",
        u"632670",
        u"670671",
        u"671680",
        u"632633",
        u"632645",
        u"645646",
        u"692675",
        u"671684",
        u"684611",
        u"684652",
        u"671692",
    ]
    assert dss.ActiveClass.Count() == 12
    assert dss.ActiveClass.First() == 1
    assert dss.ActiveClass.Name() == u"650632"
    assert dss.ActiveClass.Next() == 2
    assert dss.ActiveClass.Next() == 3
    assert dss.ActiveClass.Name(u"650632") is None
    assert dss.ActiveClass.Name() == u"650632"
    assert dss.ActiveClass.NumElements() == 12


def test_configuration():

    import opendssdirect as dss

    # Test toggling the console output using AllowForms.
    # Note COM's AllowForms can only be disabled and it ignores
    # the user's command to reallow forms if they were previously
    # disabled.
    assert not dss.Basic.AllowForms(), "Allow forms should be disabled by default"

    check_if_true = True
    try:
        dss.Basic.AllowForms(True)
    except:
        # On Windows, without a console, we cannot activate this.
        # Users can use the callback mechanism to integrate to GUIs though.
        check_if_true = False

    if check_if_true:
        assert dss.Basic.AllowForms()

    dss.Basic.AllowForms(False)
    assert not dss.Basic.AllowForms()


def test_13Node(dss):

    assert dss.ActiveClass.ActiveClassName() == u"Line"
    assert dss.ActiveClass.AllNames() == [
        u"650632",
        u"632670",
        u"670671",
        u"671680",
        u"632633",
        u"632645",
        u"645646",
        u"692675",
        u"671684",
        u"684611",
        u"684652",
        u"671692",
    ]
    assert dss.ActiveClass.Count() == 12
    assert dss.ActiveClass.First() == 1
    assert dss.ActiveClass.Name() == u"650632"
    assert dss.ActiveClass.Next() == 2
    assert dss.ActiveClass.NumElements() == 12


def test_13Node_Basic(dss):

    assert dss.Basic.AllowForms() is False
    dss_classes = [
        u"LineCode",
        u"LoadShape",
        u"TShape",
        u"PriceShape",
        u"XYcurve",
        u"GrowthShape",
        u"TCC_Curve",
        u"Spectrum",
        u"WireData",
        u"CNData",
        u"TSData",
        u"LineSpacing",
        u"LineGeometry",
        u"XfmrCode",
        u"Line",
        u"Vsource",
        u"Isource",
        u"VCCS",
        u"Load",
        u"Transformer",
        u"RegControl",
        u"Capacitor",
        u"Reactor",
        u"CapControl",
        u"Fault",
        "DynamicExp",
        u"Generator",
        u"GenDispatcher",
        u"Storage",
        u"StorageController",
        u"Relay",
        u"Recloser",
        u"Fuse",
        u"SwtControl",
        u"PVSystem",
        u"UPFC",
        u"UPFCControl",
        u"ESPVLControl",
        u"IndMach012",
        u"GICsource",
        u"AutoTrans",
        u"InvControl",
        u"ExpControl",
        u"GICLine",
        u"GICTransformer",
        u"VSConverter",
        u"Monitor",
        u"EnergyMeter",
        u"Sensor",
    ]
    assert dss.Basic.Classes() == dss_classes
    assert dss.Basic.NumClasses() == len(dss_classes)
    assert dss.Basic.ShowPanel() == 0
    assert dss.Basic.ClearAll() is None
    assert os.path.abspath(dss.Basic.DataPath()) == os.path.abspath("." + os.sep)
    # assert dss.Basic.DefaultEditor() == u'open -t'
    assert dss.Basic.NewCircuit("Circuit") == u"New Circuit"
    assert dss.Basic.NumCircuits() == 1
    assert dss.Basic.NumUserClasses() == 0
    assert dss.Basic.Reset() is None
    assert dss.Basic.Start(1) == 1
    assert dss.Basic.UserClasses() == []

    # u'Version xxxx (64-bit build); License Status: Open '
    assert isinstance(dss.Basic.Version(), str)


def test_13Node_Bus(dss):

    assert dss.Bus.Coorddefined() == 1
    np.testing.assert_array_almost_equal(
        dss.Bus.CplxSeqVoltages(),
        [
            7.275957614183426e-12,
            4.31951048085466e-06,
            57503.46213437529,
            33187.98898326319,
            -0.7758574371237046,
            1.4866859858011594,
        ],
        decimal=4,
    )
    assert dss.Bus.Cust_Duration() == 0.0
    assert dss.Bus.Cust_Interrupts() == 0.0
    assert dss.Bus.Distance() == 0.0
    assert dss.Bus.Int_Duration() == 0.0
    assert dss.Bus.Isc() == [0.0, 0.0, 0.0, 0.0, 0.0, 0.0]
    assert dss.Bus.Lambda() == 0.0
    assert dss.Bus.N_Customers() == 0
    assert dss.Bus.N_interrupts() == 0.0
    assert dss.Bus.Name() == u"sourcebus"
    assert dss.Bus.Nodes() == [1, 2, 3]
    assert dss.Bus.NumNodes() == 3
    np.testing.assert_array_almost_equal(
        dss.Bus.PuVoltage(),
        [
            0.866065862637831,
            0.4998770273321037,
            -0.0001655104421677343,
            -0.9999937910431469,
            -0.8659003521956633,
            0.5001167639062155,
        ],
        decimal=4,
    )
    assert dss.Bus.SectionID() == 0
    np.testing.assert_array_almost_equal(
        dss.Bus.SeqVoltages(),
        [4.3195104808607886e-06, 66393.45427218509, 1.6769585514012348],
        decimal=4,
    )
    assert dss.Bus.TotalMiles() == 0.0
    np.testing.assert_array_almost_equal(
        dss.Bus.VLL(),
        [
            57513.675065203715,
            99584.34445786041,
            57480.70844478478,
            -99600.26210451458,
            -114994.38350998849,
            15.917646654175769,
        ],
        decimal=4,
    )
    np.testing.assert_array_almost_equal(
        dss.Bus.VMagAngle(),
        [
            66393.52536507105,
            29.99273887874033,
            66394.86975917802,
            -90.00948289764032,
            66391.9679007487,
            149.99062319535992,
        ],
        decimal=4,
    )
    assert dss.Bus.Voc() == [0.0, 0.0, 0.0, 0.0, 0.0, 0.0]
    np.testing.assert_array_almost_equal(
        dss.Bus.Voltages(),
        [
            57502.68619173074,
            33189.47560805491,
            -10.988873472977797,
            -66394.8688498055,
            -57491.69731825776,
            33205.39325470909,
        ],
        decimal=4,
    )
    assert dss.Bus.X() == 200.0
    assert dss.Bus.Y() == 400.0
    assert dss.Bus.YscMatrix() == [0.0]
    assert dss.Bus.Zsc0() == [0.0, 0.0]
    assert dss.Bus.Zsc1() == [0.0, 0.0]
    assert dss.Bus.ZscMatrix() == [0.0]
    assert dss.Bus.ZscRefresh() == 1
    assert dss.Bus.kVBase() == 66.39528095680697
    np.testing.assert_array_almost_equal(
        dss.Bus.puVLL(),
        [
            1.693378168100472e-11,
            -4.667955969702419e-11,
            -1.395316990173399e-06,
            -5.577283842337346e-06,
            1.3953000563917182e-06,
            5.577330521897042e-06,
        ],
        decimal=4,
    )
    np.testing.assert_array_almost_equal(
        dss.Bus.puVmagAngle(),
        [
            5.239275814449394e-07,
            -79.42845561076332,
            5.238427215809797e-07,
            -79.4299867740603,
            9.484135993651139e-06,
            74.63582918382964,
        ],
        decimal=4,
    )

    assert dss.Bus.GetUniqueNodeNumber(6) == 6

    # TODO: this should not be sorted, we should define the order of the results
    assert sorted(dss.YMatrix.getV()[2:]) == sorted(dss.Circuit.AllBusVolts())
    
    assert dss.Bus.AllPDEatBus() == ["Transformer.sub"]
    assert dss.Bus.AllPCEatBus() == ["Vsource.source"]
    
    dss.Circuit.SetActiveBus("684")
    assert dss.Bus.AllPDEatBus() == ['Line.671684', 'Line.684611', 'Line.684652']
    assert dss.Bus.AllPCEatBus() == []


def test_13Node_Circuit(dss):

    np.testing.assert_array_almost_equal(
        dss.Circuit.AllBusDistances(),
        [
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
        ],
        decimal=4,
    )
    np.testing.assert_array_almost_equal(
        dss.Circuit.AllBusMagPu(),
        [
            0.9999735600909612,
            0.9999938047400851,
            0.9999500974911693,
            0.9999107734075059,
            0.9999708382014062,
            0.9999310912254219,
            1.0560331208541838,
            1.0373856699381676,
            1.0560496734277571,
            1.011300431272264,
            1.0270174666164649,
            1.0015359172418576,
            0.9871584562161683,
            1.0084198145936507,
            0.9824418963411172,
            0.9827959271001375,
            1.0402765227909403,
            0.964869605360475,
            1.019729240260045,
            1.0022697678941448,
            1.0180132408663718,
            1.0002355078501333,
            0.9648695979124887,
            0.9827959177333715,
            1.040276521652259,
            0.9762713001854915,
            1.0426333240830927,
            0.9629347471054315,
            0.9608229488014672,
            0.9753328230988354,
            1.004024331469046,
            1.0318708269152446,
            0.9897380852516064,
            1.0143428459400463,
            1.0289449404033275,
            1.0041840427671582,
            0.9827959396392048,
            1.0402765376331038,
            0.9648696191496499,
            0.9808725592235161,
            0.9628392247223574,
        ],
        decimal=4,
    )
    assert dss.Circuit.AllBusNames() == [
        u"sourcebus",
        u"650",
        u"rg60",
        u"633",
        u"634",
        u"671",
        u"645",
        u"646",
        u"692",
        u"675",
        u"611",
        u"652",
        u"670",
        u"632",
        u"680",
        u"684",
    ]
    np.testing.assert_array_almost_equal(
        dss.Circuit.AllBusVMag(),
        [
            66393.52539552496,
            66394.86979179642,
            66391.96794809647,
            2401.562819706807,
            2401.7070791741353,
            2401.611632421512,
            2536.356186390269,
            2491.569167533136,
            2536.3959701204935,
            2428.916823657129,
            2466.6701721813,
            2405.475341545256,
            273.56904917876017,
            279.46191055063275,
            272.26354300042595,
            2360.4547243616744,
            2498.5158328915445,
            2317.417277288994,
            2449.1659503353567,
            2407.237532618285,
            2445.0446146882787,
            2402.351820088669,
            2317.4172594012716,
            2360.4547018641397,
            2498.51583015672,
            2344.783889705437,
            2504.1760259677267,
            2312.771190032886,
            2307.6987616644665,
            2342.53046877393,
            2411.4410522318617,
            2478.3268829140106,
            2377.1416224123977,
            2436.2241662817532,
            2471.299259609313,
            2411.835119182976,
            2360.454754475996,
            2498.5158685371925,
            2317.4173104059755,
            2355.8353074279407,
            2312.5410863842267,
        ],
        decimal=4,
    )
    np.testing.assert_array_almost_equal(
        dss.Circuit.AllBusVolts(),
        [
            57502.68622482564,
            33189.47561163729,
            -10.988868660972098,
            -66394.86888242468,
            -57491.697356164674,
            33205.39328374589,
            2401.562774320432,
            -0.46690091155609226,
            -1201.2376790663666,
            -2079.7175126796437,
            -1200.3116016198273,
            2080.1419403490627,
            2536.356120228099,
            -0.5793286234950956,
            -1246.2598772664523,
            -2157.4877137350218,
            -1267.5877694598496,
            2196.935539327288,
            2426.426283208282,
            -109.96557825373475,
            -1300.0178453618112,
            -2096.2860825922016,
            -1120.4252829545615,
            2128.6048961933866,
            273.1208520924334,
            -15.653268696155022,
            -149.22087189563985,
            -236.28815213487727,
            -124.73890495654813,
            242.00752558006548,
            2350.0787848280174,
            -221.0796482325268,
            -1338.403130602016,
            -2109.8005657418075,
            -1015.4071554561624,
            2083.115730276635,
            -1295.6847720988385,
            -2078.36830798424,
            -1122.389508981748,
            2129.5620039280097,
            -1296.2419078314422,
            -2073.161856729391,
            -1121.791131783235,
            2124.3537662394715,
            -1015.4071496666254,
            2083.115713199053,
            2350.078762918045,
            -221.07964093085445,
            -1338.4031344410685,
            -2109.8005600677157,
            2333.5003985622425,
            -229.7550420165232,
            -1347.980749354996,
            -2110.413577571908,
            -1013.968224484203,
            2078.6483630432745,
            -1002.1266180672616,
            2078.753428367296,
            2332.4291296649067,
            -217.30934684181196,
            2407.055227539434,
            -145.37221180195166,
            -1312.3003350597062,
            -2102.372937700745,
            -1083.0006449663492,
            2116.1077231577597,
            2433.850246648693,
            -107.5228592594183,
            -1300.761594930117,
            -2101.270878230695,
            -1123.5656240409862,
            2134.1389201731336,
            2350.078813428112,
            -221.07966574213293,
            -1338.4031538526608,
            -2109.8005932052947,
            -1015.4071597837608,
            2083.1157650090267,
            2345.3898452775716,
            -221.5997955616163,
            -1009.5693326805173,
            2080.5326334201427
        ],
        decimal=4,
    )
    np.testing.assert_array_almost_equal(
        dss.Circuit.AllElementLosses(),
        [
            -3567.2118131482466,
            -1736.5765097263468,
            0.032287805258994925,
            0.26246873644273727,
            0.12209388323919848,
            0.12385831108468119,
            0.0,
            0.0,
            0.06534575459547341,
            0.06707771651400253,
            0.0,
            0.0,
            0.13508947523473763,
            0.13685396666557062,
            0.0,
            0.0,
            5.552658784485829,
            10.096246342088037,
            1155.0138982861056,
            660.0382376763037,
            160.00037738764146,
            110.00734172751001,
            119.9992158606513,
            89.99779381448772,
            120.00422631732324,
            90.00659913976898,
            169.99904086275643,
            124.99723393693857,
            234.5678795827955,
            134.62671049947627,
            166.67403146247804,
            148.05321488529017,
            485.00362356791345,
            190.0283200695573,
            67.99940602340334,
            59.998096141950576,
            290.01455466662827,
            212.02260131243509,
            163.45974879842822,
            76.92806636588504,
            121.93682536877428,
            81.93452983101116,
            16.999947095957083,
            10.000698861826827,
            65.99949909005798,
            37.99886582656774,
            117.00423402328065,
            68.00542694061349,
            3.637978807091713e-15,
            -593.4894936633161,
            -7.275957614183426e-15,
            -92.45613844770335,
            60.73577186508966,
            196.0096471850517,
            12.99022667714674,
            41.493211844628966,
            22.728048743806546,
            72.33188446746446,
            5.234676238908984e-12,
            -0.004169129951053901,
            0.8244626383214345,
            1.0561103481200407,
            2.767287477929902,
            2.4007086567327933,
            0.5274717697917658,
            0.4197353422563319,
            4.162818220041052,
            2.419260565770499,
            0.5794728640665707,
            0.4706685197881088,
            0.3823941052403825,
            0.3873387140735213,
            0.7998080968317226,
            0.23087380865922022,
            9.054574940819293e-06,
            0.0
        ],
        decimal=4,
    )
    assert dss.Circuit.AllElementNames() == [
        u"Vsource.source",
        u"Transformer.sub",
        u"Transformer.reg1",
        u"RegControl.reg1",
        u"Transformer.reg2",
        u"RegControl.reg2",
        u"Transformer.reg3",
        u"RegControl.reg3",
        u"Transformer.xfm1",
        u"Load.671",
        u"Load.634a",
        u"Load.634b",
        u"Load.634c",
        u"Load.645",
        u"Load.646",
        u"Load.692",
        u"Load.675a",
        u"Load.675b",
        u"Load.675c",
        u"Load.611",
        u"Load.652",
        u"Load.670a",
        u"Load.670b",
        u"Load.670c",
        u"Capacitor.cap1",
        u"Capacitor.cap2",
        u"Line.650632",
        u"Line.632670",
        u"Line.670671",
        u"Line.671680",
        u"Line.632633",
        u"Line.632645",
        u"Line.645646",
        u"Line.692675",
        u"Line.671684",
        u"Line.684611",
        u"Line.684652",
        u"Line.671692",
    ]
    assert dss.Circuit.AllNodeDistances() == [
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
    ]
    assert dss.Circuit.AllNodeNames() == [
        u"sourcebus.1",
        u"sourcebus.2",
        u"sourcebus.3",
        u"650.1",
        u"650.2",
        u"650.3",
        u"rg60.1",
        u"rg60.2",
        u"rg60.3",
        u"633.1",
        u"633.2",
        u"633.3",
        u"634.1",
        u"634.2",
        u"634.3",
        u"671.1",
        u"671.2",
        u"671.3",
        u"645.2",
        u"645.3",
        u"646.2",
        u"646.3",
        u"692.3",
        u"692.1",
        u"692.2",
        u"675.1",
        u"675.2",
        u"675.3",
        u"611.3",
        u"652.1",
        u"670.1",
        u"670.2",
        u"670.3",
        u"632.1",
        u"632.2",
        u"632.3",
        u"680.1",
        u"680.2",
        u"680.3",
        u"684.1",
        u"684.3",
    ]
    #    assert dss.Circuit.Capacity() == 0.0 ---- NEEDS PARAMS
    assert dss.Circuit.Disable("632") is None
    assert dss.Circuit.Enable("632") is None
    assert dss.Circuit.EndOfTimeStepUpdate() is None
    assert dss.Circuit.FirstElement() == 1
    assert dss.Circuit.FirstPCElement() == 1
    assert dss.Circuit.FirstPDElement() == 1

    np.testing.assert_array_almost_equal(
        dss.Circuit.LineLosses(), [106.49777151284596, 317.2152703225946], decimal=4
    )
    np.testing.assert_array_almost_equal(
        dss.Circuit.Losses(), [112405.24721566019, 327901.77539538965], decimal=4
    )
    assert dss.Circuit.Name() == u"ieee13nodeckt"
    assert dss.Circuit.NextElement() == 2
    assert dss.Circuit.NextPCElement() == 2
    assert dss.Circuit.NextPDElement() == 0
    assert dss.Circuit.NumBuses() == 16
    assert dss.Circuit.NumCktElements() == 38
    assert dss.Circuit.NumNodes() == 41
    assert dss.Circuit.ParentPDElement() == 0
    assert dss.Circuit.Sample() is None
    assert dss.Circuit.SaveSample() is None
    assert dss.Circuit.SetActiveBus("") == -1  # returns integer

    assert dss.Circuit.SetActiveBus("650") == 1
    assert dss.Bus.Name() == "650"

    assert dss.Circuit.SetActiveBusi(0) == 0
    assert dss.Bus.Name() == "sourcebus"

    with pt.raises(dss.DSSException):
        dss.Circuit.SetActiveClass("")

    assert dss.Circuit.SetActiveClass("Load") == 19

    assert dss.Circuit.SetActiveElement("") == -1
    assert dss.Circuit.SubstationLosses() == [0.0, 0.0]

    np.testing.assert_array_almost_equal(
        dss.Circuit.TotalPower(), [-3567.2118131482466, -1736.5765097263468], decimal=4
    )
    assert dss.Circuit.UpdateStorage() is None
    np.testing.assert_array_almost_equal(
        dss.Circuit.YCurrents(),
        [
            69802.42815021734,
            -72191.08720768025,
            -97420.52952591579,
            -24355.13240711842,
            27618.10139734361,
            96546.21962201368,
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
            -13.833771377298945,
            10.726871597152865,
            -8.968504770843197,
            -3.417089130031627,
            -3.12498992294411,
            -18.470505046170956,
            -2.667048628795584,
            3.832056283537952,
            -0.46758569533298555,
            -1.9484679417918613,
            3.1346343241285695,
            -1.8835883417461048,
            -3.31446662403701,
            -1.321239610087268,
            -7.105427357601002e-15,
            0.0,
            7.105427357601002e-15,
            0.0,
            0.25870863043271797,
            -1.0385283598223651,
            -0.25870863043271797,
            1.0385283598223651,
            -9.011574972517224,
            4.59535774077078,
            -3.0888821721242508,
            -0.8862751281506647,
            -1.9603496363737634,
            -10.9319093354963,
            0.028161796268869943,
            -3.0158125881806797,
            0.0,
            0.0,
            0.06464719014600195,
            -0.04347962137929162,
            -1.7990236975013012,
            -0.9604538679363639,
            -0.05795649932674607,
            -1.0830078082714039,
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
        ],
        decimal=4,
    )
    assert dss.Circuit.YNodeOrder() == [
        u"SOURCEBUS.1",
        u"SOURCEBUS.2",
        u"SOURCEBUS.3",
        u"650.1",
        u"650.2",
        u"650.3",
        u"RG60.1",
        u"RG60.2",
        u"RG60.3",
        u"633.1",
        u"633.2",
        u"633.3",
        u"634.1",
        u"634.2",
        u"634.3",
        u"671.1",
        u"671.2",
        u"671.3",
        u"645.2",
        u"646.2",
        u"646.3",
        u"692.3",
        u"692.1",
        u"675.1",
        u"675.2",
        u"675.3",
        u"611.3",
        u"652.1",
        u"670.1",
        u"670.2",
        u"670.3",
        u"632.1",
        u"632.2",
        u"632.3",
        u"680.1",
        u"680.2",
        u"680.3",
        u"645.3",
        u"692.2",
        u"684.1",
        u"684.3",
    ]

    np.testing.assert_array_almost_equal(
        dss.Circuit.YNodeVArray(),
        [
            57502.68622482564,
            33189.47561163729,
            -10.988868660972098,
            -66394.86888242468,
            -57491.697356164674,
            33205.39328374589,
            2401.562774320432,
            -0.46690091155609226,
            -1201.2376790663666,
            -2079.7175126796437,
            -1200.3116016198273,
            2080.1419403490627,
            2536.356120228099,
            -0.5793286234950956,
            -1246.2598772664523,
            -2157.4877137350218,
            -1267.5877694598496,
            2196.935539327288,
            2426.426283208282,
            -109.96557825373475,
            -1300.0178453618112,
            -2096.2860825922016,
            -1120.4252829545615,
            2128.6048961933866,
            273.1208520924334,
            -15.653268696155022,
            -149.22087189563985,
            -236.28815213487727,
            -124.73890495654813,
            242.00752558006548,
            2350.0787848280174,
            -221.0796482325268,
            -1338.403130602016,
            -2109.8005657418075,
            -1015.4071554561624,
            2083.115730276635,
            -1295.6847720988385,
            -2078.36830798424,
            -1296.2419078314422,
            -2073.161856729391,
            -1121.791131783235,
            2124.3537662394715,
            -1015.4071496666254,
            2083.115713199053,
            2350.078762918045,
            -221.07964093085445,
            2333.5003985622425,
            -229.7550420165232,
            -1347.980749354996,
            -2110.413577571908,
            -1013.968224484203,
            2078.6483630432745,
            -1002.1266180672616,
            2078.753428367296,
            2332.4291296649067,
            -217.30934684181196,
            2407.055227539434,
            -145.37221180195166,
            -1312.3003350597062,
            -2102.372937700745,
            -1083.0006449663492,
            2116.1077231577597,
            2433.850246648693,
            -107.5228592594183,
            -1300.761594930117,
            -2101.270878230695,
            -1123.5656240409862,
            2134.1389201731336,
            2350.078813428112,
            -221.07966574213293,
            -1338.4031538526608,
            -2109.8005932052947,
            -1015.4071597837608,
            2083.1157650090267,
            -1122.389508981748,
            2129.5620039280097,
            -1338.4031344410685,
            -2109.8005600677157,
            2345.3898452775716,
            -221.5997955616163,
            -1009.5693326805173,
            2080.5326334201427,
        ],
        decimal=4,
    )


def test_13Node_CktElement(dss):

    assert dss.CktElement.AllPropertyNames() == [
        u"bus1",
        u"bus2",
        u"linecode",
        u"length",
        u"phases",
        u"r1",
        u"x1",
        u"r0",
        u"x0",
        u"C1",
        u"C0",
        u"rmatrix",
        u"xmatrix",
        u"cmatrix",
        u"Switch",
        u"Rg",
        u"Xg",
        u"rho",
        u"geometry",
        u"units",
        u"spacing",
        u"wires",
        u"EarthModel",
        u"cncables",
        u"tscables",
        u"B1",
        u"B0",
        u"Seasons",
        u"Ratings",
        u"LineType",
        u"normamps",
        u"emergamps",
        u"faultrate",
        u"pctperm",
        u"repair",
        u"basefreq",
        u"enabled",
        u"like",
    ]
    with pt.raises(dss.DSSException):
        dss.CktElement.AllVariableNames()
    
    with pt.raises(dss.DSSException):
        dss.CktElement.AllVariableValues()
        
    assert dss.CktElement.BusNames() == [u"671", u"692"]
    assert dss.CktElement.Open(1, 0) is None
    assert dss.CktElement.IsOpen(1, 0)
    assert dss.CktElement.Close(1, 0) is None
    assert not dss.CktElement.IsOpen(1, 0)

    np.testing.assert_array_almost_equal(
        dss.CktElement.CplxSeqCurrents(),
        [
            66.53162574768066,
            13.672725677490234,
            141.9624731550164,
            -15.549381131404303,
            10.605624913220915,
            -71.14006817889842,
            -66.53162574768066,
            -13.672725677490234,
            -141.9624731550164,
            15.549381131404303,
            -10.605624913220915,
            71.14006817889842,
        ],
        decimal=4,
    )
    np.testing.assert_array_almost_equal(
        dss.CktElement.CplxSeqVoltages(),
        [
            -1.2438337433870856,
            -82.58816123256645,
            2386.0519853836104,
            -162.48665009879235,
            -34.729366812206194,
            23.99516309883188,
            -1.243840396549615,
            -82.58816259983894,
            2386.051971187363,
            -162.4866485438543,
            -34.72936787276865,
            23.99517021283873,
        ],
        decimal=4,
    )

    np.testing.assert_array_almost_equal(
        dss.CktElement.Currents(),
        [
            219.09972381591797,
            -73.0167236328125,
            38.39052391052246,
            -56.74091720581055,
            -57.89537048339844,
            170.77581787109375,
            -219.09972381591797,
            73.0167236328125,
            -38.39052391052246,
            56.74091720581055,
            57.89537048339844,
            -170.77581787109375,
        ],
        decimal=4,
    )
    np.testing.assert_array_almost_equal(
        dss.CktElement.CurrentsMagAng(),
        [
            230.9461645195305,
            -18.431061226098382,
            68.50813098808815,
            -55.91798179283929,
            180.32263832628155,
            108.72737150582326,
            230.9461645195305,
            161.56893876423007,
            68.50813098808815,
            124.08201819748916,
            180.32263832628155,
            -71.2726284845052,
        ],
        decimal=4,
    )
    assert dss.CktElement.DisplayName() == u"Line_671692"
    assert dss.CktElement.EmergAmps() == 600.0
    assert dss.CktElement.Enabled() == 1
    assert dss.CktElement.EnergyMeter() == u""

    assert isinstance(dss.CktElement.GUID(), str)
    assert dss.CktElement.HasSwitchControl() == 0
    assert dss.CktElement.HasVoltControl() == 0
    np.testing.assert_almost_equal(
        dss.CktElement.Losses(),
        [0.009054574940819293, 0.0],
        decimal=4,
    )
    assert dss.CktElement.Name() == u"Line.671692"
    assert dss.CktElement.NodeOrder() == [1, 2, 3, 1, 2, 3]
    np.testing.assert_almost_equal(
        dss.CktElement.TotalPowers(),
        [1013.9073121262952, 19.02222347205106, -1013.9073030717203, -19.02222347205106],
        decimal=5,
    )
    assert dss.CktElement.NormalAmps() == 400.0
    assert dss.CktElement.NumConductors() == 3
    assert dss.CktElement.NumControls() == 0
    assert dss.CktElement.NumPhases() == 3
    assert dss.CktElement.NumProperties() == 38
    assert dss.CktElement.NumTerminals() == 2
    assert dss.CktElement.OCPDevIndex() == 0
    assert dss.CktElement.OCPDevType() == 0
    np.testing.assert_array_almost_equal(
        dss.CktElement.PhaseLosses(),
        [
            5.333613138645887e-06,
            2.9103830456733704e-14,
            4.6933640260249376e-07,
            0.0,
            3.251625457778573e-06,
            -2.9103830456733704e-14,
        ],
        decimal=4,
    )
    np.testing.assert_array_almost_equal(
        dss.CktElement.Powers(),
        [
            531.0441242773005,
            123.15656327805627,
            68.33002183423334,
            -156.9385702870313,
            414.5331660147614,
            52.80423048102608,
            -531.0441189436874,
            -123.15656327805624,
            -68.33002136489694,
            156.9385702870313,
            -414.5331627631359,
            -52.80423048102611,            
        ],
        decimal=4,
    )
    np.testing.assert_array_almost_equal(
        dss.CktElement.Residuals(),
        [203.7660567138995, 11.613009831248048, 203.7660567138995, -168.3869901590804],
        decimal=4,
    )
    np.testing.assert_array_almost_equal(
        dss.CktElement.SeqCurrents(),
        [
            67.92201890463316,
            142.811508772432,
            71.92627183650107,
            67.92201890463316,
            142.811508772432,
            71.92627183650107,            
        ],
        decimal=4,
    )
    np.testing.assert_array_almost_equal(
        dss.CktElement.SeqPowers(),
        [
            -3.6358786615457435,
            -16.433154110257448,
            1023.7692233179367,
            42.10387505212601,
            -6.226032530095827,
            -6.6484974698176496,
            3.635880045565927,
            16.433154110257433,
            -1023.7692171993988,
            -42.10387505212598,
            6.226034082112406,
            6.648497469817642,
        ],
        decimal=4,
    )
    np.testing.assert_array_almost_equal(
        dss.CktElement.SeqVoltages(),
        [
            82.59752719154237,
            2391.5781376349373,
            42.212519130185925,
            82.59752865884985,
            2391.5781233658486,
            42.21252404660491,            
        ],
        decimal=4,
    )

    with pt.raises(dss.DSSException):
        dss.CktElement.Variablei(1)

    with pt.raises(dss.DSSException):
        dss.CktElement.Variablei(1, 10)

    with pt.raises(dss.DSSException):
        dss.CktElement.Variable("some invalid name")

    with pt.raises(dss.DSSException):
        dss.CktElement.Variable("some invalid name", 10)

    np.testing.assert_array_almost_equal(
        dss.CktElement.Voltages(),
        [
            2350.0787848280174,
            -221.0796482325268,
            -1338.403130602016,
            -2109.8005657418075,
            -1015.4071554561624,
            2083.115730276635,
            2350.078762918045,
            -221.07964093085445,
            -1338.4031344410685,
            -2109.8005600677157,
            -1015.4071496666254,
            2083.115713199053,            
        ],
        decimal=4,
    )
    np.testing.assert_array_almost_equal(
        dss.CktElement.VoltagesMagAng(),
        [
            2360.4547243616744,
            -5.374186385394941,
            2498.5158328915445,
            -122.38998937216338,
            2317.417277288994,
            115.98674977755289,
            2360.4547018641397,
            -5.374186258749708,
            2498.51583015672,
            -122.38998951620502,
            2317.4172594012716,
            115.98674983388848,
        ],
        decimal=4,
    )

    np.testing.assert_array_almost_equal(
        dss.CktElement.YPrim(),
        [
            10000000.0,
            0.0,
            0.0,
            0.0,
            0.0,
            0.0,
            -10000000.0,
            0.0,
            0.0,
            0.0,
            0.0,
            0.0,
            0.0,
            0.0,
            10000000.0,
            0.0,
            0.0,
            0.0,
            0.0,
            0.0,
            -10000000.0,
            0.0,
            0.0,
            0.0,
            0.0,
            0.0,
            0.0,
            0.0,
            10000000.0,
            0.0,
            0.0,
            0.0,
            0.0,
            0.0,
            -10000000.0,
            0.0,
            -10000000.0,
            0.0,
            0.0,
            0.0,
            0.0,
            0.0,
            10000000.0,
            0.0,
            0.0,
            0.0,
            0.0,
            0.0,
            0.0,
            0.0,
            -10000000.0,
            0.0,
            0.0,
            0.0,
            0.0,
            0.0,
            10000000.0,
            0.0,
            0.0,
            0.0,
            0.0,
            0.0,
            0.0,
            0.0,
            -10000000.0,
            0.0,
            0.0,
            0.0,
            0.0,
            0.0,
            10000000.0,
            0.0,
        ],
        decimal=4,
    )

    # Create an element with "variables" available to test
    dss.run_command("New PVSystem.631")
    dss.Circuit.SetActiveElement("PVSystem.631")
    assert dss.CktElement.AllVariableNames() == [
        u"Irradiance",
        u"PanelkW",
        u"P_TFactor",
        u"Efficiency",
        u"Vreg",
        u"Vavg (DRC)",
        u"volt-var",
        u"volt-watt",
        u"DRC",
        u"VV_DRC",
        u"watt-pf",
        u"watt-var",
        u"kW_out_desired",
        "Grid voltage",
        "di/dt",
        "it",
        "it History",
        "Rated VDC",
        "Avg duty cycle",
        "Target (Amps)",
        "Series L",
        "Max. Amps (phase)",
    ]
    assert dss.CktElement.AllVariableValues() == [
        1.0,
        500.0,
        1.0,
        1.0,
        9999.0,
        9999.0,
        9999.0,
        9999.0,
        9999.0,
        9999.0,
        9999.0,
        9999.0,
        500.0,
        0.0,
        0.0,
        0.0,
        0.0,
        8000.0,
        0.0,
        0.0,
        0.0,
        0.0,
    ]
    assert dss.CktElement.Variablei(2) == 500.0
    assert dss.CktElement.Variable(u"PanelkW") == 500.0


def test_13Node_Capacitors(dss):
    assert dss.Capacitors.AddStep() == 0
    assert dss.Capacitors.AllNames() == [u"cap1", u"cap2"]
    assert dss.Capacitors.AvailableSteps() == 0
    assert dss.Capacitors.Close() is None
    assert dss.Capacitors.Count() == 2
    assert dss.Capacitors.First() == 1
    assert dss.Capacitors.IsDelta() == 0
    assert dss.Capacitors.Name() == u"cap1"
    assert dss.Capacitors.Next() == 2
    assert dss.Capacitors.NumSteps() == 1
    assert dss.Capacitors.Open() is None
    assert dss.Capacitors.States() == [0]
    assert dss.Capacitors.SubtractStep() == 0
    assert dss.Capacitors.kV() == 2.4
    assert dss.Capacitors.kvar() == 100.0


def test_13Node_CapControls(dss):
    assert dss.CapControls.AllNames() == []
    # assert dss.CapControls.CTRatio() == 0.0
    # assert dss.CapControls.Capacitor() == u""
    assert dss.CapControls.Count() == 0
    assert dss.CapControls.First() == 0
    assert dss.CapControls.Next() == 0
    # assert dss.CapControls.Delay() == 0.0
    # assert dss.CapControls.DelayOff() == 0.0
    # assert dss.CapControls.Mode() == 1
    # assert dss.CapControls.MonitoredObj() == u""
    # assert dss.CapControls.MonitoredTerm() == 0
    # assert dss.CapControls.Name() == u""
    # assert dss.CapControls.OFFSetting() == 0.0
    # assert dss.CapControls.ONSetting() == 0.0
    # assert dss.CapControls.PTRatio() == 0.0
    # assert dss.CapControls.UseVoltOverride() == 0
    # assert dss.CapControls.Vmax() == 0.0
    # assert dss.CapControls.Vmin() == 0.0


def test_13Node_Element(dss):
    assert dss.Element.AllPropertyNames() == [
        u"bus1",
        u"bus2",
        u"linecode",
        u"length",
        u"phases",
        u"r1",
        u"x1",
        u"r0",
        u"x0",
        u"C1",
        u"C0",
        u"rmatrix",
        u"xmatrix",
        u"cmatrix",
        u"Switch",
        u"Rg",
        u"Xg",
        u"rho",
        u"geometry",
        u"units",
        u"spacing",
        u"wires",
        u"EarthModel",
        u"cncables",
        u"tscables",
        u"B1",
        u"B0",
        u"Seasons",
        u"Ratings",
        u"LineType",
        u"normamps",
        u"emergamps",
        u"faultrate",
        u"pctperm",
        u"repair",
        u"basefreq",
        u"enabled",
        u"like",
    ]
    assert dss.Element.Name() == u"Line.671692"
    assert dss.Element.NumProperties() == 38


def test_13Node_Executive(dss):
    assert dss.Executive.Command(1) == u"New"
    assert (
        dss.Executive.CommandHelp(1).replace(os.linesep, "\n")
        == u"Create a new object within the DSS. Object becomes the active object\nExample: New Line.line1 ..."
    )
    assert (
        dss.Executive.NumCommands() == 125
    )  # adjusted to the latest version on 2022-03-22
    assert (
        dss.Executive.NumOptions() == 128
    )  # adjusted to the latest version on 2023-03-15
    assert dss.Executive.Option(1) == u"type"
    assert (
        dss.Executive.OptionHelp(1)
        == u"Sets the active DSS class type.  Same as Class=..."
    )
    assert dss.Executive.OptionValue(1) == u"Line"


def test_13Node_Fuses(dss):
    assert dss.Fuses.AllNames() == []
    assert dss.Fuses.Count() == 0
    assert dss.Fuses.First() == 0
    assert dss.Fuses.Idx() == 0
    assert dss.Fuses.Next() == 0
    # assert dss.Fuses.Close() is None
    # assert dss.Fuses.IsBlown() == 0
    # assert dss.Fuses.MonitoredObj() == u""
    # assert dss.Fuses.MonitoredTerm() == 0
    # assert dss.Fuses.Name() == u""
    # assert dss.Fuses.NumPhases() == 0
    # assert dss.Fuses.Open() is None
    # assert dss.Fuses.RatedCurrent() == -1.0
    # assert dss.Fuses.SwitchedObj() == u""
    # assert dss.Fuses.TCCCurve() == u"No Fuse Active!"


def test_13Node_Generators(dss):

    assert dss.Generators.AllNames() == []
    assert dss.Generators.Count() == 0
    assert dss.Generators.First() == 0
    assert dss.Generators.Next() == 0
    assert dss.Generators.Idx() == 0
    # assert dss.Generators.ForcedON() == 0
    # assert dss.Generators.Model() == -1
    # assert dss.Generators.Name() == u""
    # assert dss.Generators.PF() == 0.0
    # assert dss.Generators.Phases() == 0
    assert dss.Generators.RegisterNames() == [
        u"kWh",
        u"kvarh",
        u"Max kW",
        u"Max kVA",
        u"Hours",
        u"$",
    ]
    # assert dss.Generators.RegisterValues() == [0.0]
    # assert dss.Generators.Vmaxpu() == -1.0
    # assert dss.Generators.Vminpu() == -1.0
    # assert dss.Generators.kV() == -1.0
    # assert dss.Generators.kVARated() == -1.0
    # assert dss.Generators.kW() == 0.0
    # assert dss.Generators.kvar() == 0.0


def test_13Node_Isource(dss):

    assert dss.Isource.AllNames() == []
    assert dss.Isource.Count() == 0
    assert dss.Isource.First() == 0
    assert dss.Isource.Next() == 0
    # assert dss.Isource.Amps() == 0.0
    # assert dss.Isource.AngleDeg() == 0.0
    # assert dss.Isource.Frequency() == 0.0
    # assert dss.Isource.Name() == u""


def test_13Node_Lines(dss):

    assert dss.Lines.AllNames() == [
        u"650632",
        u"632670",
        u"670671",
        u"671680",
        u"632633",
        u"632645",
        u"645646",
        u"692675",
        u"671684",
        u"684611",
        u"684652",
        u"671692",
    ]
    assert dss.Lines.Bus1() == u"671"
    assert dss.Lines.Bus2() == u"692"
    assert dss.Lines.C0() == 0.0
    assert dss.Lines.C1() == 0.0
    assert dss.Lines.CMatrix() == [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0]
    assert dss.Lines.Count() == 12
    assert dss.Lines.EmergAmps() == 600.0
    assert dss.Lines.First() == 1
    assert dss.Lines.Geometry() == u""
    assert dss.Lines.Length() == 2000.0
    assert dss.Lines.LineCode() == u"mtx601"
    assert dss.Lines.Name() == u"650632"
    assert dss.Lines.Next() == 2
    assert dss.Lines.NormAmps() == 400.0
    assert dss.Lines.NumCust() == 0
    assert dss.Lines.Parent() == 0
    assert dss.Lines.Phases() == 3
    assert dss.Lines.Rg() == 0.01805
    assert dss.Lines.Rho() == 100.0
    assert dss.Lines.Spacing() == u""
    assert dss.Lines.Units() == 5
    assert dss.Lines.Xg() == 0.155081

    np.testing.assert_array_almost_equal(dss.Lines.Yprim(), [
        3.4336493324686748,
        -9.89685369864876,
        -1.4568442159669834,
        3.659044283989984,
        -0.7977778406219831,
        2.7352828975550736,
        -3.4336493324686748,
        9.896853765321925,
        1.4568442159669834,
        -3.6590442982770908,
        0.7977778406219831,
        -2.73528291184218,
        -1.4568442159669834,
        3.659044283989984,
        3.0066302278661308,
        -9.378246335904445,
        -0.3787251308930535,
        2.089056295888508,
        1.4568442159669834,
        -3.6590442982770908,
        -3.0066302278661308,
        9.37824640257761,
        0.3787251308930535,
        -2.0890563101756148,
        -0.7977778406219831,
        2.7352828975550736,
        -0.3787251308930535,
        2.089056295888508,
        2.6588258945971046,
        -8.847357529237488,
        0.7977778406219831,
        -2.73528291184218,
        0.3787251308930535,
        -2.0890563101756148,
        -2.6588258945971046,
        8.847357595910653,
        -3.4336493324686748,
        9.896853765321925,
        1.4568442159669834,
        -3.6590442982770908,
        0.7977778406219831,
        -2.73528291184218,
        3.4336493324686748,
        -9.89685369864876,
        -1.4568442159669834,
        3.659044283989984,
        -0.7977778406219831,
        2.7352828975550736,
        1.4568442159669834,
        -3.6590442982770908,
        -3.0066302278661308,
        9.37824640257761,
        0.3787251308930535,
        -2.0890563101756148,
        -1.4568442159669834,
        3.659044283989984,
        3.0066302278661308,
        -9.378246335904445,
        -0.3787251308930535,
        2.089056295888508,
        0.7977778406219831,
        -2.73528291184218,
        0.3787251308930535,
        -2.0890563101756148,
        -2.6588258945971046,
        8.847357595910653,
        -0.7977778406219831,
        2.7352828975550736,
        -0.3787251308930535,
        2.089056295888508,
        2.6588258945971046,
        -8.847357529237488
    ])
    with pt.raises(dss.DSSException):
        # This is not allowed at the moment (the value is/was ignored before)
        # so an exception was added in case someone was trying to use it
        dss.Lines.Yprim(dss.Lines.Yprim())

    assert dss.Lines.R0() == 3.378787878787879e-05
    assert dss.Lines.X0() == 7.664772727272727e-05
    assert dss.Lines.RMatrix() == [
        6.5625e-05,
        2.9545454545454545e-05,
        2.9924242424242424e-05,
        2.9545454545454545e-05,
        6.392045454545455e-05,
        2.9071969696969698e-05,
        2.9924242424242424e-05,
        2.9071969696969698e-05,
        6.46590909090909e-05,
    ]
    assert dss.Lines.XMatrix() == [
        0.00019278409090909093,
        9.50189393939394e-05,
        8.022727272727272e-05,
        9.50189393939394e-05,
        0.0001984469696969697,
        7.289772727272727e-05,
        8.022727272727272e-05,
        7.289772727272727e-05,
        0.00019598484848484847,
    ]

    assert dss.Lines.R1() == 1.0984848484848486e-05
    assert dss.Lines.X1() == 2.284090909090909e-05


def test_13Node_Loads(dss):

    assert dss.Loads.AllNames() == [
        u"671",
        u"634a",
        u"634b",
        u"634c",
        u"645",
        u"646",
        u"692",
        u"675a",
        u"675b",
        u"675c",
        u"611",
        u"652",
        u"670a",
        u"670b",
        u"670c",
    ]
    assert dss.Loads.AllocationFactor() == 0.5
    assert dss.Loads.CFactor() == 4.0
    assert dss.Loads.CVRCurve() == u""
    assert dss.Loads.CVRvars() == 2.0
    assert dss.Loads.CVRwatts() == 1.0
    assert dss.Loads.Class() == 1
    assert dss.Loads.Count() == 15
    assert dss.Loads.Daily() == u""
    assert dss.Loads.Duty() == u""
    assert dss.Loads.First() == 1
    assert dss.Loads.Growth() == u""
    assert dss.Loads.Idx() == 1
    assert dss.Loads.IsDelta() == 1
    assert dss.Loads.Model() == 1
    assert dss.Loads.Name() == u"671"
    assert dss.Loads.Next() == 2
    assert dss.Loads.NumCust() == 1
    assert dss.Loads.PF() == 0.8240419241993675
    assert dss.Loads.PctMean() == 50.0
    assert dss.Loads.PctStdDev() == 10.0
    assert dss.Loads.RelWeighting() == 1.0
    assert dss.Loads.Rneut() == -1.0
    assert dss.Loads.Spectrum() == u"defaultload"
    assert dss.Loads.Status() == 0
    assert dss.Loads.Vmaxpu() == 1.05
    assert dss.Loads.VminEmerg() == 0.0
    assert dss.Loads.VminNorm() == 0.0
    assert dss.Loads.Vminpu() == 0.95
    assert dss.Loads.XfkVA() == 0.0
    assert dss.Loads.Xneut() == 0.0
    assert dss.Loads.Yearly() == u""
    assert dss.Loads.ZipV() == [0, 0, 0, 0, 0, 0, 0]
    assert dss.Loads.kV() == 0.277
    assert dss.Loads.kVABase() == 194.164878389476
    assert dss.Loads.kW() == 160.0
    assert dss.Loads.kWh() == 0.0
    assert dss.Loads.kWhDays() == 30.0
    assert dss.Loads.kvar() == 110.0
    assert dss.Loads.puSeriesRL() == 50.0


def test_13Node_LoadShape(dss):
    assert dss.LoadShape.AllNames() == [u"default"]
    assert dss.LoadShape.Count() == 1
    assert dss.LoadShape.First() == 1
    assert dss.LoadShape.HrInterval() == 1.0
    assert dss.LoadShape.MinInterval() == 60.0
    assert dss.LoadShape.Name() == u"default"
    assert dss.LoadShape.Next() == 0
    assert dss.LoadShape.Normalize() is None
    assert dss.LoadShape.Npts() == 24
    assert dss.LoadShape.PBase() == 0.0
    assert dss.LoadShape.PMult() == [
        0.677,
        0.6256,
        0.6087,
        0.5833,
        0.58028,
        0.6025,
        0.657,
        0.7477,
        0.832,
        0.88,
        0.94,
        0.989,
        0.985,
        0.98,
        0.9898,
        0.999,
        1.0,
        0.958,
        0.936,
        0.913,
        0.876,
        0.876,
        0.828,
        0.756,
    ]
    assert dss.LoadShape.QBase() == 0.0
    assert dss.LoadShape.QMult() == [0.0]
    assert dss.LoadShape.SInterval() == 3600.0
    assert dss.LoadShape.TimeArray() == [0.0]
    assert dss.LoadShape.UseActual() == 0


def test_13Node_Meters(dss):
    with pt.raises(dss.DSSException):
        assert dss.Meters.AllEndElements()

    assert dss.Meters.Count() == 0
    assert dss.Meters.Next() == 0
    assert dss.Meters.First() == 0
    assert dss.Meters.ResetAll() is None
    assert dss.Meters.AllNames() == []
    assert dss.Meters.SampleAll() is None
    assert dss.Meters.SaveAll() is None
    assert dss.Meters.ZonePCE() == []


def test_13Node_Monitors(dss):
    assert dss.Monitors.AllNames() == []
    assert dss.Monitors.Count() == 0
    assert dss.Monitors.First() == 0
    assert dss.Monitors.Next() == 0
    assert dss.Monitors.ProcessAll() is None
    assert dss.Monitors.ResetAll() is None
    assert dss.Monitors.SaveAll() is None
    assert dss.Monitors.SampleAll() is None
    
    dss.Text.Command("new monitor.test_monitor element=Transformer.Reg3 terminal=2 mode=2")
    dss.Text.Command("solve mode=daily step=15m number=10")
    
    assert dss.Monitors.Count() == 1
    assert dss.Monitors.First() == 1
    
    expected_dict = pd.DataFrame(
        {
            "Tap (pu)": {
                0: 1.056249976158142,
                1: 1.056249976158142,
                2: 1.056249976158142,
                3: 1.056249976158142,
                4: 1.056249976158142,
                5: 1.056249976158142,
                6: 1.056249976158142,
                7: 1.056249976158142,
                8: 1.056249976158142,
                9: 1.056249976158142
            },
            "hour": {
                0: 0.0,
                1: 0.0,
                2: 0.0,
                3: 1.0,
                4: 1.0,
                5: 1.0,
                6: 1.0,
                7: 2.0,
                8: 2.0,
                9: 2.0
            },
            "second": {
                0: 900.0,
                1: 1800.0,
                2: 2700.0,
                3: 0.0,
                4: 900.0,
                5: 1800.0,
                6: 2700.0,
                7: 0.0,
                8: 900.0,
                9: 1800.0
            }
        }
    ).to_dict()

    actual_dict = dss.utils.monitor_to_dataframe().to_dict()
    assert_dict_equal(actual_dict, expected_dict)


def test_13Node_PDElements(dss):

    assert dss.PDElements.AccumulatedL() == 0.0
    assert dss.PDElements.Count() == 19
    assert dss.PDElements.FaultRate() == 0.1
    assert dss.PDElements.First() == 1
    assert dss.PDElements.FromTerminal() == 1
    assert dss.PDElements.IsShunt() == 0
    assert dss.PDElements.Lambda() == 0.0
    assert dss.PDElements.Name() == u"Transformer.sub"
    assert dss.PDElements.Next() == 1
    assert dss.PDElements.NumCustomers() == 0
    assert dss.PDElements.ParentPDElement() == 0
    assert dss.PDElements.PctPermanent() == 0.0
    assert dss.PDElements.RepairTime() == 0.0
    assert dss.PDElements.SectionID() == 0
    assert dss.PDElements.TotalCustomers() == 0
    assert dss.PDElements.TotalMiles() == 0.0

    all_names = dss.PDElements.AllNames()
    all_max_currents = dss.PDElements.AllMaxCurrents()
    all_max_currents_all_terms = dss.PDElements.AllMaxCurrents(AllNodes=True)
    all_pct_norm = dss.PDElements.AllPctNorm()
    all_pct_emerg = dss.PDElements.AllPctEmerg()
    all_currents = dss.PDElements.AllCurrents()
    all_currents_polar = dss.PDElements.AllCurrentsMagAng()
    all_cplx_seq_currents = dss.PDElements.AllCplxSeqCurrents()
    all_seq_currents = dss.PDElements.AllSeqCurrents()
    all_powers = dss.PDElements.AllPowers()
    all_seq_powers = dss.PDElements.AllSeqPowers()
    all_num_phases = dss.PDElements.AllNumPhases()
    all_num_conductors = dss.PDElements.AllNumConductors()
    all_num_terminals = dss.PDElements.AllNumTerminals()

    ang = np.deg2rad(np.asarray(all_currents_polar[1::2]))
    np.testing.assert_array_almost_equal(
        np.asarray(all_currents).view(dtype=complex),
        np.asarray(all_currents_polar[::2]) * (np.cos(ang) + 1j * np.sin(ang)),
        decimal=4,
    )

    np.testing.assert_array_almost_equal(
        np.abs(np.asarray(all_cplx_seq_currents).view(dtype=complex)),
        all_seq_currents,
        decimal=4,
    )

    all_max_currents2 = []
    all_max_currents_all_terms_2 = []
    all_norm_amp2 = []
    all_emerg_amp2 = []
    all_currents2 = []
    all_cplx_seq_currents2 = []
    all_powers2 = []
    all_seq_powers2 = []
    all_num_phases2 = []
    all_num_conductors2 = []
    all_num_terminals2 = []

    for name in all_names:
        # We have to iterate by name to include disabled elements
        dss.PDElements.Name(name)
        
        currents = np.asarray(dss.CktElement.Currents()).view(dtype=complex)
        
        all_max_currents2.append(np.max(np.abs(currents[:dss.CktElement.NumPhases()])))
        all_max_currents_all_terms_2.append(np.max(np.abs(currents)))
        
        all_currents2.append(currents)
        all_norm_amp2.append(dss.CktElement.NormalAmps())
        all_emerg_amp2.append(dss.CktElement.EmergAmps())
        all_cplx_seq_currents2.append(dss.CktElement.CplxSeqCurrents())
        all_powers2.append(dss.CktElement.Powers())
        all_seq_powers2.append(dss.CktElement.SeqPowers())

        all_num_phases2.append(dss.CktElement.NumPhases())
        all_num_conductors2.append(dss.CktElement.NumConductors())
        all_num_terminals2.append(dss.CktElement.NumTerminals())

    np.testing.assert_array_almost_equal(all_max_currents, all_max_currents2, decimal=4)
    np.testing.assert_array_almost_equal(
        all_max_currents_all_terms, 
        all_max_currents_all_terms_2, 
        decimal=4
    )

    np.testing.assert_array_almost_equal(
        all_pct_norm,
        100 * np.asarray(all_max_currents) / np.asarray(all_norm_amp2),
        decimal=4,
    )

    np.testing.assert_array_almost_equal(
        all_pct_emerg,
        100 * np.asarray(all_max_currents) / np.asarray(all_emerg_amp2),
        decimal=4,
    )

    np.testing.assert_array_almost_equal(
        np.asarray(all_currents).view(dtype=complex), 
        np.concatenate(all_currents2), 
        decimal=4
    )

    np.testing.assert_array_almost_equal(
        all_powers, np.concatenate(all_powers2), decimal=4
    )

    np.testing.assert_array_almost_equal(
        all_seq_powers, np.concatenate(all_seq_powers2), decimal=4
    )


def test_13Node_Properties(dss):  # TODO!! rework DSSProperty
    dss.dss_lib.DSSProperty_Set_Index(0)  # TODO?
    assert (
        dss.Properties.Description().replace(os.linesep, "\n")
        == u"Name of bus to which first terminal is connected.\nExample:\nbus1=busname   (assumes all terminals connected in normal phase order)\nbus1=busname.3.1.2.0 (specify terminal to node connections explicitly)"
    )
    assert dss.Properties.Name() == u"bus1"

    dss.dss_lib.DSSProperty_Set_Index(0)  # TODO?
    assert dss.Properties.Name() == u"bus1"
    assert dss.Properties.Value() == u"671"


def test_13Node_PVsystems(dss):
    assert dss.PVsystems.Count() == 0
    assert dss.PVsystems.First() == 0
    assert dss.PVsystems.Idx() == 0
    assert dss.PVsystems.Next() == 0


def test_13Node_Reclosers(dss):
    assert dss.Reclosers.AllNames() == []
    assert dss.Reclosers.Count() == 0
    assert dss.Reclosers.First() == 0
    assert dss.Reclosers.Idx() == 0
    assert dss.Reclosers.Next() == 0


def test_13Node_RegControls(dss):

    assert dss.RegControls.AllNames() == [u"reg1", u"reg2", u"reg3"]
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
    assert dss.RegControls.MonitoredBus() == u""
    assert dss.RegControls.Name() == u"reg1"
    assert dss.RegControls.Next() == 2
    assert dss.RegControls.PTRatio() == 20.0
    assert dss.RegControls.ReverseBand() == 3.0
    assert dss.RegControls.ReverseR() == 0.0
    assert dss.RegControls.ReverseVreg() == 120.0
    assert dss.RegControls.ReverseX() == 0.0
    assert dss.RegControls.TapDelay() == 2.0
    assert dss.RegControls.TapNumber() == 6
    assert dss.RegControls.TapWinding() == 2
    assert dss.RegControls.Transformer() == u"reg2"
    assert dss.RegControls.VoltageLimit() == 0.0
    assert dss.RegControls.Winding() == 2


def test_13Node_Relays(dss):

    assert dss.Relays.AllNames() == []
    assert dss.Relays.Count() == 0
    assert dss.Relays.First() == 0
    assert dss.Relays.Idx() == 0
    assert dss.Relays.Next() == 0


def test_13Node_Sensors(dss):
    assert dss.Sensors.AllNames() == []
    assert dss.Sensors.Count() == 0
    assert dss.Sensors.First() == 0
    assert dss.Sensors.Next() == 0
    assert dss.Sensors.ResetAll() is None

    assert dss.Sensors.Currents() == [0.0]


def test_13Node_Settings(dss):
    with pt.raises(dss.DSSException):
        dss.Settings.AllocationFactors(0)

    assert dss.Settings.AllocationFactors(1) is None
    assert dss.Settings.AllowDuplicates() == 0
    assert dss.Settings.CktModel() == 0

    # Fixed in DSS C-API 0.10.4, previously it was an uninitialized value
    # (COM still had the bug when this comment was written)
    assert dss.Settings.AutoBusList() == u""

    assert dss.Settings.EmergVmaxpu() == 1.08
    assert dss.Settings.EmergVminpu() == 0.9
    assert dss.Settings.LossRegs() == [13]
    assert dss.Settings.LossWeight() == 1.0
    assert dss.Settings.NormVmaxpu() == 1.05
    assert dss.Settings.NormVminpu() == 0.95
    assert dss.Settings.PriceCurve() == u""
    assert dss.Settings.PriceSignal() == 25.0
    assert dss.Settings.Trapezoidal() == 0
    assert dss.Settings.UERegs() == [10]
    assert dss.Settings.UEWeight() == 1.0
    assert dss.Settings.VoltageBases() == [115.0, 4.16, 0.48]
    assert dss.Settings.ZoneLock() == 0


def test_13Node_Solution(dss):
    assert dss.Solution.AddType() == 1
    assert dss.Solution.Algorithm() == 0
    assert dss.Solution.Capkvar() == 600.0
    assert dss.Solution.CheckControls() is None
    assert dss.Solution.CheckFaultStatus() is None
    assert dss.Solution.Cleanup() is None
    assert dss.Solution.ControlActionsDone() == 1
    assert dss.Solution.ControlIterations() == 3
    assert dss.Solution.ControlMode() == 0
    assert dss.Solution.Converged() == 1
    assert dss.Solution.Convergence() == 0.0001
    assert dss.Solution.DblHour() == 0.0
    assert dss.Solution.DefaultDaily() == u"default"
    assert dss.Solution.DefaultYearly() == u"default"
    assert dss.Solution.DoControlActions() is None
    assert dss.Solution.EventLog() == [
        u"Hour=0, Sec=0, ControlIter=1, Element=Regulator.reg3, Action= CHANGED 7 TAPS TO 1.04375.",
        u"Hour=0, Sec=0, ControlIter=1, Element=Regulator.reg2, Action= CHANGED 5 TAPS TO 1.03125.",
        u"Hour=0, Sec=0, ControlIter=1, Element=Regulator.reg1, Action= CHANGED 7 TAPS TO 1.04375.",
        u"Hour=0, Sec=0, ControlIter=2, Element=Regulator.reg3, Action= CHANGED 2 TAPS TO 1.05625.",
        u"Hour=0, Sec=0, ControlIter=2, Element=Regulator.reg2, Action= CHANGED 1 TAPS TO 1.0375.",
        u"Hour=0, Sec=0, ControlIter=2, Element=Regulator.reg1, Action= CHANGED 2 TAPS TO 1.05625.",
    ]
    assert dss.Solution.FinishTimeStep() is None
    assert dss.Solution.Frequency() == 60.0
    assert dss.Solution.GenMult() == 1.0
    assert dss.Solution.GenPF() == 1.0
    assert dss.Solution.GenkW() == 1000.0
    assert dss.Solution.Hour() == 0
    assert dss.Solution.InitSnap() is None
    assert dss.Solution.Iterations() == 11
    assert dss.Solution.LDCurve() == u""
    assert dss.Solution.LoadModel() == 1
    assert dss.Solution.LoadMult() == 1.0
    assert dss.Solution.MaxControlIterations() == 10
    assert dss.Solution.MaxIterations() == 15
    assert dss.Solution.Mode() == 0
    assert dss.Solution.ModeID() == u"Snap"
    assert dss.Solution.MostIterationsDone() == 0
    assert dss.Solution.Number() == 100
    assert dss.Solution.PctGrowth() == 2.499999999999991
    assert isinstance(dss.Solution.ProcessTime(), float)
    assert dss.Solution.Random() == 1
    assert dss.Solution.SampleControlDevices() is None
    assert dss.Solution.SampleDoControlActions() is None
    assert dss.Solution.Seconds() == 0.001
    assert dss.Solution.Solve() is None
    assert dss.Solution.SolveDirect() is None
    assert dss.Solution.SolveNoControl() is None
    assert dss.Solution.SolvePFlow() is None
    assert dss.Solution.SolvePlusControl() is None
    assert dss.Solution.StepSize() == 0.001
    assert dss.Solution.SystemYChanged() == 0
    assert isinstance(dss.Solution.TimeTimeStep(), float)
    assert dss.Solution.TotalIterations() == 2
    assert isinstance(dss.Solution.TotalTime(), float)
    assert dss.Solution.Year() == 0


def test_13Node_SwtControls(dss):
    assert dss.SwtControls.AllNames() == []
    assert dss.SwtControls.Count() == 0
    assert dss.SwtControls.First() == 0
    assert dss.SwtControls.Next() == 0


def test_13Node_Topology(dss):
    assert dss.Topology.ActiveBranch() == 0
    assert dss.Topology.ActiveLevel() == 0
    assert dss.Topology.AllIsolatedBranches() == []
    assert dss.Topology.AllIsolatedLoads() == []
    assert dss.Topology.AllLoopedPairs() == [
        u"Transformer.reg3",
        u"Transformer.reg2",
        u"Transformer.reg2",
        u"Line.650632",
        u"Transformer.reg1",
        u"Line.650632",
    ]
    assert dss.Topology.BranchName() == u""
    assert dss.Topology.BusName() == u""
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
    assert dss.Transformers.AllNames() == [u"sub", u"reg1", u"reg2", u"reg3", u"xfm1"]
    assert dss.Transformers.Count() == 5
    assert dss.Transformers.First() == 1
    assert dss.Transformers.IsDelta() == 0
    assert dss.Transformers.MaxTap() == 1.1
    assert dss.Transformers.MinTap() == 0.9
    assert dss.Transformers.Name() == u"sub"
    assert dss.Transformers.Next() == 2
    assert dss.Transformers.NumTaps() == 32
    assert dss.Transformers.NumWindings() == 2
    assert dss.Transformers.R() == 5e-03
    assert dss.Transformers.Rneut() == -1.0
    assert dss.Transformers.Tap() == 1.05625
    assert dss.Transformers.Wdg() == 2
    assert dss.Transformers.XfmrCode() == u""
    assert dss.Transformers.Xhl() == 0.01
    assert dss.Transformers.Xht() == 35
    assert dss.Transformers.Xlt() == 30
    assert dss.Transformers.Xneut() == 0.0
    assert dss.Transformers.kV() == 2.4
    assert dss.Transformers.kVA() == 1666.0


def test_13Node_Vsources(dss):
    assert dss.Vsources.AllNames() == [u"source"]
    assert dss.Vsources.AngleDeg() == 30.0
    assert dss.Vsources.BasekV() == 115.0
    assert dss.Vsources.Count() == 1
    assert dss.Vsources.First() == 1
    assert dss.Vsources.Frequency() == 60.0
    assert dss.Vsources.Name() == u"source"
    assert dss.Vsources.Next() == 0
    assert dss.Vsources.PU() == 1.0001
    assert dss.Vsources.Phases() == 3


def test_13Node_XYCurves(dss):
    assert dss.XYCurves.Count() == 0
    assert dss.XYCurves.First() == 0
    assert dss.XYCurves.Next() == 0


def test_capacitors_to_dataframe(dss):
    expected_dict = pd.DataFrame(
        {
            "AvailableSteps": {"cap1": 0, "cap2": 0},
            "IsDelta": {"cap1": 0, "cap2": 0},
            "Name": {"cap1": "cap1", "cap2": "cap2"},
            "NumSteps": {"cap1": 1, "cap2": 1},
            "States": {"cap1": [1], "cap2": [1]},
            "kV": {"cap1": 4.16, "cap2": 2.4},
            "kvar": {"cap1": 600.0, "cap2": 100.0},
            "Idx": {"cap1": 1, "cap2": 2},
        }
    ).to_dict()

    actual_dict = dss.utils.capacitors_to_dataframe().to_dict()
    assert_dict_equal(actual_dict, expected_dict)


def test_fuses_to_dataframe(dss):
    expected_dict = {}
    actual_dict = dss.utils.fuses_to_dataframe().to_dict()
    assert_dict_equal(actual_dict, expected_dict)


def test_generators_to_dataframe(dss):
    expected_dict = {}
    actual_dict = dss.utils.generators_to_dataframe().to_dict()
    assert_dict_equal(actual_dict, expected_dict)


def test_isource_to_dataframe(dss):
    expected_dict = {}
    actual_dict = dss.utils.isource_to_dataframe().to_dict()
    assert_dict_equal(actual_dict, expected_dict)

    dss.Text.Command("New Isource.sampleIsource Bus1=611.3 Phases=1 Amps=0.1 Angle=30")

    expected_dict = pd.DataFrame(
        {
            "Amps": {"sampleisource": 0.1},
            "AngleDeg": {"sampleisource": 30.0},
            "Frequency": {"sampleisource": 60.0},
            "Idx": {"sampleisource": 1},
            "Name": {"sampleisource": "sampleisource"},
        }
    ).to_dict()

    actual_dict = dss.utils.isource_to_dataframe().to_dict()
    assert_dict_equal(actual_dict, expected_dict)


def test_lines_to_dataframe(dss):
    expected_dict = pd.DataFrame(
        {
            "TotalCust": {
                "650632": 0,
                "632670": 0,
                "670671": 0,
                "671680": 0,
                "632633": 0,
                "632645": 0,
                "645646": 0,
                "692675": 0,
                "671684": 0,
                "684611": 0,
                "684652": 0,
                "671692": 0,
            },
            "Bus1": {
                "632633": "632.1.2.3",
                "632645": "632.3.2",
                "632670": "632.1.2.3",
                "645646": "645.3.2",
                "650632": "rg60.1.2.3",
                "670671": "670.1.2.3",
                "671680": "671.1.2.3",
                "671684": "671.1.3",
                "671692": "671",
                "684611": "684.3",
                "684652": "684.1",
                "692675": "692.1.2.3",
            },
            "Bus2": {
                "632633": "633.1.2.3",
                "632645": "645.3.2",
                "632670": "670.1.2.3",
                "645646": "646.3.2",
                "650632": "632.1.2.3",
                "670671": "671.1.2.3",
                "671680": "680.1.2.3",
                "671684": "684.1.3",
                "671692": "692",
                "684611": "611.3",
                "684652": "652.1",
                "692675": "675.1.2.3",
            },
            "C0": {
                "632633": 0.0003030303030303031,
                "632645": 0.0003030303030303031,
                "632670": 0.0003030303030303031,
                "645646": 0.0003030303030303031,
                "650632": 0.0003030303030303031,
                "670671": 0.0003030303030303031,
                "671680": 0.0003030303030303031,
                "671684": 0.0003030303030303031,
                "671692": 0.0,
                "684611": 0.0006439393939393939,
                "684652": 0.0006439393939393939,
                "692675": 0.0003030303030303031,
            },
            "C1": {
                "632633": 0.0006439393939393939,
                "632645": 0.0006439393939393939,
                "632670": 0.0006439393939393939,
                "645646": 0.0006439393939393939,
                "650632": 0.0006439393939393939,
                "670671": 0.0006439393939393939,
                "671680": 0.0006439393939393939,
                "671684": 0.0006439393939393939,
                "671692": 0.0,
                "684611": 0.0006439393939393939,
                "684652": 0.0006439393939393939,
                "692675": 0.0006439393939393939,
            },
            "CMatrix": {
                "632633": [
                    0.0005303030303030302,
                    -0.00011363636363636361,
                    -0.00011363636363636361,
                    -0.00011363636363636361,
                    0.0005303030303030302,
                    -0.00011363636363636361,
                    -0.00011363636363636361,
                    -0.00011363636363636361,
                    0.0005303030303030302,
                ],
                "632645": [
                    0.0005303030303030302,
                    -0.00011363636363636361,
                    -0.00011363636363636361,
                    0.0005303030303030302,
                ],
                "632670": [
                    0.0005303030303030302,
                    -0.00011363636363636361,
                    -0.00011363636363636361,
                    -0.00011363636363636361,
                    0.0005303030303030302,
                    -0.00011363636363636361,
                    -0.00011363636363636361,
                    -0.00011363636363636361,
                    0.0005303030303030302,
                ],
                "645646": [
                    0.0005303030303030302,
                    -0.00011363636363636361,
                    -0.00011363636363636361,
                    0.0005303030303030302,
                ],
                "650632": [
                    0.0005303030303030302,
                    -0.00011363636363636361,
                    -0.00011363636363636361,
                    -0.00011363636363636361,
                    0.0005303030303030302,
                    -0.00011363636363636361,
                    -0.00011363636363636361,
                    -0.00011363636363636361,
                    0.0005303030303030302,
                ],
                "670671": [
                    0.0005303030303030302,
                    -0.00011363636363636361,
                    -0.00011363636363636361,
                    -0.00011363636363636361,
                    0.0005303030303030302,
                    -0.00011363636363636361,
                    -0.00011363636363636361,
                    -0.00011363636363636361,
                    0.0005303030303030302,
                ],
                "671680": [
                    0.0005303030303030302,
                    -0.00011363636363636361,
                    -0.00011363636363636361,
                    -0.00011363636363636361,
                    0.0005303030303030302,
                    -0.00011363636363636361,
                    -0.00011363636363636361,
                    -0.00011363636363636361,
                    0.0005303030303030302,
                ],
                "671684": [
                    0.0005303030303030302,
                    -0.00011363636363636361,
                    -0.00011363636363636361,
                    0.0005303030303030302,
                ],
                "671692": [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0],
                "684611": [0.0005303030303030302],
                "684652": [0.0446969696969697],
                "692675": [
                    0.07271742424242425,
                    0.0,
                    0.0,
                    0.0,
                    0.07271742424242425,
                    0.0,
                    0.0,
                    0.0,
                    0.07271742424242425,
                ],
            },
            "EmergAmps": {
                "632633": 600.0,
                "632645": 600.0,
                "632670": 600.0,
                "645646": 600.0,
                "650632": 600.0,
                "670671": 600.0,
                "671680": 600.0,
                "671684": 600.0,
                "671692": 600.0,
                "684611": 600.0,
                "684652": 600.0,
                "692675": 600.0,
            },
            "Geometry": {
                "632633": "",
                "632645": "",
                "632670": "",
                "645646": "",
                "650632": "",
                "670671": "",
                "671680": "",
                "671684": "",
                "671692": "",
                "684611": "",
                "684652": "",
                "692675": "",
            },
            "Length": {
                "632633": 500.0,
                "632645": 500.0,
                "632670": 667.0,
                "645646": 300.0,
                "650632": 2000.0,
                "670671": 1333.0,
                "671680": 1000.0,
                "671684": 300.0,
                "671692": 0.001,
                "684611": 300.0,
                "684652": 800.0,
                "692675": 500.0,
            },
            "LineCode": {
                "632633": "mtx602",
                "632645": "mtx603",
                "632670": "mtx601",
                "645646": "mtx603",
                "650632": "mtx601",
                "670671": "mtx601",
                "671680": "mtx601",
                "671684": "mtx604",
                "671692": "",
                "684611": "mtx605",
                "684652": "mtx607",
                "692675": "mtx606",
            },
            "Name": {
                "632633": "632633",
                "632645": "632645",
                "632670": "632670",
                "645646": "645646",
                "650632": "650632",
                "670671": "670671",
                "671680": "671680",
                "671684": "671684",
                "671692": "671692",
                "684611": "684611",
                "684652": "684652",
                "692675": "692675",
            },
            "NormAmps": {
                "632633": 400.0,
                "632645": 400.0,
                "632670": 400.0,
                "645646": 400.0,
                "650632": 400.0,
                "670671": 400.0,
                "671680": 400.0,
                "671684": 400.0,
                "671692": 400.0,
                "684611": 400.0,
                "684652": 400.0,
                "692675": 400.0,
            },
            "NumCust": {
                "632633": 0,
                "632645": 0,
                "632670": 0,
                "645646": 0,
                "650632": 0,
                "670671": 0,
                "671680": 0,
                "671684": 0,
                "671692": 0,
                "684611": 0,
                "684652": 0,
                "692675": 0,
            },
            "Phases": {
                "632633": 3,
                "632645": 2,
                "632670": 3,
                "645646": 2,
                "650632": 3,
                "670671": 3,
                "671680": 3,
                "671684": 2,
                "671692": 3,
                "684611": 1,
                "684652": 1,
                "692675": 3,
            },
            "R0": {
                "632633": 3.378787878787879e-05,
                "632645": 3.378787878787879e-05,
                "632670": 3.378787878787879e-05,
                "645646": 3.378787878787879e-05,
                "650632": 3.378787878787879e-05,
                "670671": 3.378787878787879e-05,
                "671680": 3.378787878787879e-05,
                "671684": 3.378787878787879e-05,
                "671692": 0.0001,
                "684611": 1.0984848484848486e-05,
                "684652": 1.0984848484848486e-05,
                "692675": 3.378787878787879e-05,
            },
            "R1": {
                "632633": 1.0984848484848486e-05,
                "632645": 1.0984848484848486e-05,
                "632670": 1.0984848484848486e-05,
                "645646": 1.0984848484848486e-05,
                "650632": 1.0984848484848486e-05,
                "670671": 1.0984848484848486e-05,
                "671680": 1.0984848484848486e-05,
                "671684": 1.0984848484848486e-05,
                "671692": 0.0001,
                "684611": 1.0984848484848486e-05,
                "684652": 1.0984848484848486e-05,
                "692675": 1.0984848484848486e-05,
            },
            "RMatrix": {
                "632633": [
                    0.0001425378787878788,
                    2.9924242424242424e-05,
                    2.9545454545454545e-05,
                    2.9924242424242424e-05,
                    0.0001415719696969697,
                    2.9071969696969698e-05,
                    2.9545454545454545e-05,
                    2.9071969696969698e-05,
                    0.00014083333333333333,
                ],
                "632645": [
                    0.000250719696969697,
                    3.912878787878788e-05,
                    3.912878787878788e-05,
                    0.000251780303030303,
                ],
                "632670": [
                    6.5625e-05,
                    2.9545454545454545e-05,
                    2.9924242424242424e-05,
                    2.9545454545454545e-05,
                    6.392045454545455e-05,
                    2.9071969696969698e-05,
                    2.9924242424242424e-05,
                    2.9071969696969698e-05,
                    6.46590909090909e-05,
                ],
                "645646": [
                    0.000250719696969697,
                    3.912878787878788e-05,
                    3.912878787878788e-05,
                    0.000251780303030303,
                ],
                "650632": [
                    6.5625e-05,
                    2.9545454545454545e-05,
                    2.9924242424242424e-05,
                    2.9545454545454545e-05,
                    6.392045454545455e-05,
                    2.9071969696969698e-05,
                    2.9924242424242424e-05,
                    2.9071969696969698e-05,
                    6.46590909090909e-05,
                ],
                "670671": [
                    6.5625e-05,
                    2.9545454545454545e-05,
                    2.9924242424242424e-05,
                    2.9545454545454545e-05,
                    6.392045454545455e-05,
                    2.9071969696969698e-05,
                    2.9924242424242424e-05,
                    2.9071969696969698e-05,
                    6.46590909090909e-05,
                ],
                "671680": [
                    6.5625e-05,
                    2.9545454545454545e-05,
                    2.9924242424242424e-05,
                    2.9545454545454545e-05,
                    6.392045454545455e-05,
                    2.9071969696969698e-05,
                    2.9924242424242424e-05,
                    2.9071969696969698e-05,
                    6.46590909090909e-05,
                ],
                "671684": [
                    0.000250719696969697,
                    3.912878787878788e-05,
                    3.912878787878788e-05,
                    0.000251780303030303,
                ],
                "671692": [0.0001, 0.0, 0.0, 0.0, 0.0001, 0.0, 0.0, 0.0, 0.0001],
                "684611": [0.00025174242424242423],
                "684652": [0.0002542613636363636],
                "692675": [
                    0.00014994715909090909,
                    6.0317424242424236e-05,
                    5.368371212121212e-05,
                    6.0317424242424236e-05,
                    0.00014803958333333333,
                    6.0317424242424236e-05,
                    5.368371212121212e-05,
                    6.0317424242424236e-05,
                    0.00014994715909090909,
                ],
            },
            "Rg": {
                "632633": 0.01805,
                "632645": 0.01805,
                "632670": 0.01805,
                "645646": 0.01805,
                "650632": 0.01805,
                "670671": 0.01805,
                "671680": 0.01805,
                "671684": 0.01805,
                "671692": 0.01805,
                "684611": 0.01805,
                "684652": 0.01805,
                "692675": 0.01805,
            },
            "Rho": {
                "632633": 100.0,
                "632645": 100.0,
                "632670": 100.0,
                "645646": 100.0,
                "650632": 100.0,
                "670671": 100.0,
                "671680": 100.0,
                "671684": 100.0,
                "671692": 100.0,
                "684611": 100.0,
                "684652": 100.0,
                "692675": 100.0,
            },
            "Spacing": {
                "632633": "",
                "632645": "",
                "632670": "",
                "645646": "",
                "650632": "",
                "670671": "",
                "671680": "",
                "671684": "",
                "671692": "",
                "684611": "",
                "684652": "",
                "692675": "",
            },
            "Units": {
                "632633": 5,
                "632645": 5,
                "632670": 5,
                "645646": 5,
                "650632": 5,
                "670671": 5,
                "671680": 5,
                "671684": 5,
                "671692": 0,
                "684611": 5,
                "684652": 5,
                "692675": 5,
            },
            "X0": {
                "632633": 7.664772727272727e-05,
                "632645": 7.664772727272727e-05,
                "632670": 7.664772727272727e-05,
                "645646": 7.664772727272727e-05,
                "650632": 7.664772727272727e-05,
                "670671": 7.664772727272727e-05,
                "671680": 7.664772727272727e-05,
                "671684": 7.664772727272727e-05,
                "671692": 0.0,
                "684611": 2.284090909090909e-05,
                "684652": 2.284090909090909e-05,
                "692675": 7.664772727272727e-05,
            },
            "X1": {
                "632633": 2.284090909090909e-05,
                "632645": 2.284090909090909e-05,
                "632670": 2.284090909090909e-05,
                "645646": 2.284090909090909e-05,
                "650632": 2.284090909090909e-05,
                "670671": 2.284090909090909e-05,
                "671680": 2.284090909090909e-05,
                "671684": 2.284090909090909e-05,
                "671692": 0.0,
                "684611": 2.284090909090909e-05,
                "684652": 2.284090909090909e-05,
                "692675": 2.284090909090909e-05,
            },
            "XMatrix": {
                "632633": [
                    0.00022375,
                    8.022727272727272e-05,
                    9.50189393939394e-05,
                    8.022727272727272e-05,
                    0.00022695075757575757,
                    7.289772727272727e-05,
                    9.50189393939394e-05,
                    7.289772727272727e-05,
                    0.00022939393939393942,
                ],
                "632645": [
                    0.00025698863636363636,
                    8.695075757575758e-05,
                    8.695075757575758e-05,
                    0.00025513257575757577,
                ],
                "632670": [
                    0.00019278409090909093,
                    9.50189393939394e-05,
                    8.022727272727272e-05,
                    9.50189393939394e-05,
                    0.0001984469696969697,
                    7.289772727272727e-05,
                    8.022727272727272e-05,
                    7.289772727272727e-05,
                    0.00019598484848484847,
                ],
                "645646": [
                    0.00025698863636363636,
                    8.695075757575758e-05,
                    8.695075757575758e-05,
                    0.00025513257575757577,
                ],
                "650632": [
                    0.00019278409090909093,
                    9.50189393939394e-05,
                    8.022727272727272e-05,
                    9.50189393939394e-05,
                    0.0001984469696969697,
                    7.289772727272727e-05,
                    8.022727272727272e-05,
                    7.289772727272727e-05,
                    0.00019598484848484847,
                ],
                "670671": [
                    0.00019278409090909093,
                    9.50189393939394e-05,
                    8.022727272727272e-05,
                    9.50189393939394e-05,
                    0.0001984469696969697,
                    7.289772727272727e-05,
                    8.022727272727272e-05,
                    7.289772727272727e-05,
                    0.00019598484848484847,
                ],
                "671680": [
                    0.00019278409090909093,
                    9.50189393939394e-05,
                    8.022727272727272e-05,
                    9.50189393939394e-05,
                    0.0001984469696969697,
                    7.289772727272727e-05,
                    8.022727272727272e-05,
                    7.289772727272727e-05,
                    0.00019598484848484847,
                ],
                "671684": [
                    0.00025698863636363636,
                    8.695075757575758e-05,
                    8.695075757575758e-05,
                    0.00025513257575757577,
                ],
                "671692": [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0],
                "684611": [0.0002552083333333333],
                "684652": [9.704545454545454e-05],
                "692675": [
                    8.302121212121212e-05,
                    5.24314393939394e-06,
                    -3.488712121212121e-06,
                    5.24314393939394e-06,
                    7.513200757575758e-05,
                    5.24314393939394e-06,
                    -3.488712121212121e-06,
                    5.24314393939394e-06,
                    8.302121212121212e-05,
                ],
            },
            "Xg": {
                "632633": 0.155081,
                "632645": 0.155081,
                "632670": 0.155081,
                "645646": 0.155081,
                "650632": 0.155081,
                "670671": 0.155081,
                "671680": 0.155081,
                "671684": 0.155081,
                "671692": 0.155081,
                "684611": 0.155081,
                "684652": 0.155081,
                "692675": 0.155081,
            },
            "Yprim": {
                "632633": [
                    5.564622525570931,
                    -7.133818641976722,
                    -1.495155595100418,
                    1.5059091102776052,
                    -2.1394799752143716,
                    1.6901170943579362,
                    -5.564622525570931,
                    7.133818691956606,
                    1.495155595100418,
                    -1.5059091209875801,
                    2.1394799752143716,
                    -1.6901171050679111,
                    -1.495155595100418,
                    1.5059091102776052,
                    4.908541379197551,
                    -7.063422452497184,
                    -1.0880240059003325,
                    1.3823966977507467,
                    1.495155595100418,
                    -1.5059091209875801,
                    -4.908541379197551,
                    7.063422502477067,
                    1.0880240059003325,
                    -1.3823967084607216,
                    -2.1394799752143716,
                    1.6901170943579362,
                    -1.0880240059003325,
                    1.3823966977507467,
                    5.189203684098949,
                    -7.085613346851578,
                    2.1394799752143716,
                    -1.6901171050679111,
                    1.0880240059003325,
                    -1.3823967084607216,
                    -5.189203684098949,
                    7.085613396831461,
                    -5.564622525570931,
                    7.133818691956606,
                    1.495155595100418,
                    -1.5059091209875801,
                    2.1394799752143716,
                    -1.6901171050679111,
                    5.564622525570931,
                    -7.133818641976722,
                    -1.495155595100418,
                    1.5059091102776052,
                    -2.1394799752143716,
                    1.6901170943579362,
                    1.495155595100418,
                    -1.5059091209875801,
                    -4.908541379197551,
                    7.063422502477067,
                    1.0880240059003325,
                    -1.3823967084607216,
                    -1.495155595100418,
                    1.5059091102776052,
                    4.908541379197551,
                    -7.063422452497184,
                    -1.0880240059003325,
                    1.3823966977507467,
                    2.1394799752143716,
                    -1.6901171050679111,
                    1.0880240059003325,
                    -1.3823967084607216,
                    -5.189203684098949,
                    7.085613396831461,
                    -2.1394799752143716,
                    1.6901170943579362,
                    -1.0880240059003325,
                    1.3823966977507467,
                    5.189203684098949,
                    -7.085613346851578,
                ],
                "632645": [
                    4.3050410172015825,
                    -4.005253312691522,
                    -1.4446401120068793,
                    0.5996056073245764,
                    -4.3050410172015825,
                    4.0052533626714055,
                    1.4446401120068793,
                    -0.5996056180345513,
                    -1.4446401120068793,
                    0.5996056073245764,
                    4.3349628401868,
                    -3.986966015372319,
                    1.4446401120068793,
                    -0.5996056180345513,
                    -4.3349628401868,
                    3.9869660653522025,
                    -4.3050410172015825,
                    4.0052533626714055,
                    1.4446401120068793,
                    -0.5996056180345513,
                    4.3050410172015825,
                    -4.005253312691522,
                    -1.4446401120068793,
                    0.5996056073245764,
                    1.4446401120068793,
                    -0.5996056180345513,
                    -4.3349628401868,
                    3.9869660653522025,
                    -1.4446401120068793,
                    0.5996056073245764,
                    4.3349628401868,
                    -3.986966015372319,
                ],
                "632670": [
                    3.4336493324686748,
                    -9.89685369864876,
                    -1.4568442159669834,
                    3.659044283989984,
                    -0.7977778406219831,
                    2.7352828975550736,
                    -3.4336493324686748,
                    9.896853765321925,
                    1.4568442159669834,
                    -3.6590442982770908,
                    0.7977778406219831,
                    -2.73528291184218,
                    -1.4568442159669834,
                    3.659044283989984,
                    3.0066302278661308,
                    -9.378246335904445,
                    -0.3787251308930535,
                    2.089056295888508,
                    1.4568442159669834,
                    -3.6590442982770908,
                    -3.0066302278661308,
                    9.37824640257761,
                    0.3787251308930535,
                    -2.0890563101756148,
                    -0.7977778406219831,
                    2.7352828975550736,
                    -0.3787251308930535,
                    2.089056295888508,
                    2.6588258945971046,
                    -8.847357529237488,
                    0.7977778406219831,
                    -2.73528291184218,
                    0.3787251308930535,
                    -2.0890563101756148,
                    -2.6588258945971046,
                    8.847357595910653,
                    -3.4336493324686748,
                    9.896853765321925,
                    1.4568442159669834,
                    -3.6590442982770908,
                    0.7977778406219831,
                    -2.73528291184218,
                    3.4336493324686748,
                    -9.89685369864876,
                    -1.4568442159669834,
                    3.659044283989984,
                    -0.7977778406219831,
                    2.7352828975550736,
                    1.4568442159669834,
                    -3.6590442982770908,
                    -3.0066302278661308,
                    9.37824640257761,
                    0.3787251308930535,
                    -2.0890563101756148,
                    -1.4568442159669834,
                    3.659044283989984,
                    3.0066302278661308,
                    -9.378246335904445,
                    -0.3787251308930535,
                    2.089056295888508,
                    0.7977778406219831,
                    -2.73528291184218,
                    0.3787251308930535,
                    -2.0890563101756148,
                    -2.6588258945971046,
                    8.847357595910653,
                    -0.7977778406219831,
                    2.7352828975550736,
                    -0.3787251308930535,
                    2.089056295888508,
                    2.6588258945971046,
                    -8.847357529237488,
                ],
                "645646": [
                    7.175068362002635,
                    -6.675422241131079,
                    -2.407733520011465,
                    0.9993426902982676,
                    -7.175068362002635,
                    6.675422271119008,
                    2.407733520011465,
                    -0.9993426967242526,
                    -2.407733520011465,
                    0.9993426902982676,
                    7.224938066978001,
                    -6.644943412265743,
                    2.407733520011465,
                    -0.9993426967242526,
                    -7.224938066978001,
                    6.644943442253672,
                    -7.175068362002635,
                    6.675422271119008,
                    2.407733520011465,
                    -0.9993426967242526,
                    7.175068362002635,
                    -6.675422241131079,
                    -2.407733520011465,
                    0.9993426902982676,
                    2.407733520011465,
                    -0.9993426967242526,
                    -7.224938066978001,
                    6.644943442253672,
                    -2.407733520011465,
                    0.9993426902982676,
                    7.224938066978001,
                    -6.644943412265743,
                ],
                "650632": [
                    1.1451220523783028,
                    -3.3006005308153292,
                    -0.485857546024989,
                    1.22029123063551,
                    -0.26605890984743125,
                    0.9122168082594669,
                    -1.1451220523783028,
                    3.3006007307348617,
                    0.485857546024989,
                    -1.2202912734754099,
                    0.26605890984743125,
                    -0.9122168510993668,
                    -0.485857546024989,
                    1.22029123063551,
                    1.0027111809933547,
                    -3.1276449753401,
                    -0.12630483115283336,
                    0.6967002366036674,
                    0.485857546024989,
                    -1.2202912734754099,
                    -1.0027111809933547,
                    3.1276451752596324,
                    0.12630483115283336,
                    -0.6967002794435673,
                    -0.26605890984743125,
                    0.9122168082594669,
                    -0.12630483115283336,
                    0.6967002366036674,
                    0.8867184358481343,
                    -2.95059355831667,
                    0.26605890984743125,
                    -0.9122168510993668,
                    0.12630483115283336,
                    -0.6967002794435673,
                    -0.8867184358481343,
                    2.9505937582362023,
                    -1.1451220523783028,
                    3.3006007307348617,
                    0.485857546024989,
                    -1.2202912734754099,
                    0.26605890984743125,
                    -0.9122168510993668,
                    1.1451220523783028,
                    -3.3006005308153292,
                    -0.485857546024989,
                    1.22029123063551,
                    -0.26605890984743125,
                    0.9122168082594669,
                    0.485857546024989,
                    -1.2202912734754099,
                    -1.0027111809933547,
                    3.1276451752596324,
                    0.12630483115283336,
                    -0.6967002794435673,
                    -0.485857546024989,
                    1.22029123063551,
                    1.0027111809933547,
                    -3.1276449753401,
                    -0.12630483115283336,
                    0.6967002366036674,
                    0.26605890984743125,
                    -0.9122168510993668,
                    0.12630483115283336,
                    -0.6967002794435673,
                    -0.8867184358481343,
                    2.9505937582362023,
                    -0.26605890984743125,
                    0.9122168082594669,
                    -0.12630483115283336,
                    0.6967002366036674,
                    0.8867184358481343,
                    -2.95059355831667,
                ],
                "670671": [
                    1.718112606719134,
                    -4.952138997638645,
                    -0.7289685611777779,
                    1.8308946053187896,
                    -0.39918816181159994,
                    1.368667414957135,
                    -1.718112606719134,
                    4.952139130885014,
                    0.7289685611777779,
                    -1.8308946338715828,
                    0.39918816181159994,
                    -1.3686674435099282,
                    -0.7289685611777779,
                    1.8308946053187896,
                    1.5044428822105846,
                    -4.6926407898738605,
                    -0.1895046228849712,
                    1.045311718549333,
                    0.7289685611777779,
                    -1.8308946338715828,
                    -1.5044428822105846,
                    4.692640923120229,
                    0.1895046228849712,
                    -1.0453117471021263,
                    -0.39918816181159994,
                    1.368667414957135,
                    -0.1895046228849712,
                    1.045311718549333,
                    1.3304102563362856,
                    -4.42699725345461,
                    0.39918816181159994,
                    -1.3686674435099282,
                    0.1895046228849712,
                    -1.0453117471021263,
                    -1.3304102563362856,
                    4.426997386700979,
                    -1.718112606719134,
                    4.952139130885014,
                    0.7289685611777779,
                    -1.8308946338715828,
                    0.39918816181159994,
                    -1.3686674435099282,
                    1.718112606719134,
                    -4.952138997638645,
                    -0.7289685611777779,
                    1.8308946053187896,
                    -0.39918816181159994,
                    1.368667414957135,
                    0.7289685611777779,
                    -1.8308946338715828,
                    -1.5044428822105846,
                    4.692640923120229,
                    0.1895046228849712,
                    -1.0453117471021263,
                    -0.7289685611777779,
                    1.8308946053187896,
                    1.5044428822105846,
                    -4.6926407898738605,
                    -0.1895046228849712,
                    1.045311718549333,
                    0.39918816181159994,
                    -1.3686674435099282,
                    0.1895046228849712,
                    -1.0453117471021263,
                    -1.3304102563362856,
                    4.426997386700979,
                    -0.39918816181159994,
                    1.368667414957135,
                    -0.1895046228849712,
                    1.045311718549333,
                    1.3304102563362856,
                    -4.42699725345461,
                ],
                "671680": [
                    2.2902441047566056,
                    -6.601201361509957,
                    -0.971715092049978,
                    2.44058252553087,
                    -0.5321178196948625,
                    1.8244336807787838,
                    -2.2902441047566056,
                    6.601201461469723,
                    0.971715092049978,
                    -2.4405825469508198,
                    0.5321178196948625,
                    -1.8244337021987336,
                    -0.971715092049978,
                    2.44058252553087,
                    2.0054223619867093,
                    -6.255290250559498,
                    -0.2526096623056667,
                    1.3934005374671847,
                    0.971715092049978,
                    -2.4405825469508198,
                    -2.0054223619867093,
                    6.255290350519265,
                    0.2526096623056667,
                    -1.3934005588871345,
                    -0.5321178196948625,
                    1.8244336807787838,
                    -0.2526096623056667,
                    1.3934005374671847,
                    1.7734368716962685,
                    -5.901187416512638,
                    0.5321178196948625,
                    -1.8244337021987336,
                    0.2526096623056667,
                    -1.3934005588871345,
                    -1.7734368716962685,
                    5.901187516472405,
                    -2.2902441047566056,
                    6.601201461469723,
                    0.971715092049978,
                    -2.4405825469508198,
                    0.5321178196948625,
                    -1.8244337021987336,
                    2.2902441047566056,
                    -6.601201361509957,
                    -0.971715092049978,
                    2.44058252553087,
                    -0.5321178196948625,
                    1.8244336807787838,
                    0.971715092049978,
                    -2.4405825469508198,
                    -2.0054223619867093,
                    6.255290350519265,
                    0.2526096623056667,
                    -1.3934005588871345,
                    -0.971715092049978,
                    2.44058252553087,
                    2.0054223619867093,
                    -6.255290250559498,
                    -0.2526096623056667,
                    1.3934005374671847,
                    0.5321178196948625,
                    -1.8244337021987336,
                    0.2526096623056667,
                    -1.3934005588871345,
                    -1.7734368716962685,
                    5.901187516472405,
                    -0.5321178196948625,
                    1.8244336807787838,
                    -0.2526096623056667,
                    1.3934005374671847,
                    1.7734368716962685,
                    -5.901187416512638,
                ],
                "671684": [
                    7.175068362002635,
                    -6.675422241131079,
                    -2.407733520011465,
                    0.9993426902982676,
                    -7.175068362002635,
                    6.675422271119008,
                    2.407733520011465,
                    -0.9993426967242526,
                    -2.407733520011465,
                    0.9993426902982676,
                    7.224938066978001,
                    -6.644943412265743,
                    2.407733520011465,
                    -0.9993426967242526,
                    -7.224938066978001,
                    6.644943442253672,
                    -7.175068362002635,
                    6.675422271119008,
                    2.407733520011465,
                    -0.9993426967242526,
                    7.175068362002635,
                    -6.675422241131079,
                    -2.407733520011465,
                    0.9993426902982676,
                    2.407733520011465,
                    -0.9993426967242526,
                    -7.224938066978001,
                    6.644943442253672,
                    -2.407733520011465,
                    0.9993426902982676,
                    7.224938066978001,
                    -6.644943412265743,
                ],
                "671692": [
                    10000000.0,
                    0.0,
                    0.0,
                    0.0,
                    0.0,
                    0.0,
                    -10000000.0,
                    0.0,
                    0.0,
                    0.0,
                    0.0,
                    0.0,
                    0.0,
                    0.0,
                    10000000.0,
                    0.0,
                    0.0,
                    0.0,
                    0.0,
                    0.0,
                    -10000000.0,
                    0.0,
                    0.0,
                    0.0,
                    0.0,
                    0.0,
                    0.0,
                    0.0,
                    10000000.0,
                    0.0,
                    0.0,
                    0.0,
                    0.0,
                    0.0,
                    -10000000.0,
                    0.0,
                    -10000000.0,
                    0.0,
                    0.0,
                    0.0,
                    0.0,
                    0.0,
                    10000000.0,
                    0.0,
                    0.0,
                    0.0,
                    0.0,
                    0.0,
                    0.0,
                    0.0,
                    -10000000.0,
                    0.0,
                    0.0,
                    0.0,
                    0.0,
                    0.0,
                    10000000.0,
                    0.0,
                    0.0,
                    0.0,
                    0.0,
                    0.0,
                    0.0,
                    0.0,
                    -10000000.0,
                    0.0,
                    0.0,
                    0.0,
                    0.0,
                    0.0,
                    10000000.0,
                    0.0,
                ],
                "684611": [
                    6.5300017720164165,
                    -6.619904715567382,
                    -6.5300017720164165,
                    6.619904745555312,
                    -6.5300017720164165,
                    6.619904745555312,
                    6.5300017720164165,
                    -6.619904715567382,
                ],
                "684652": [
                    4.291089932048226,
                    -1.6377992048699221,
                    -4.291089932048226,
                    1.6378059450141607,
                    -4.291089932048226,
                    1.6378059450141607,
                    4.291089932048226,
                    -1.6377992048699221,
                ],
                "692675": [
                    10.412767372774814,
                    -7.836560993228165,
                    -2.428601675914292,
                    3.079395289523384,
                    -1.0809513347493518,
                    2.4925941140824843,
                    -10.412767372774814,
                    7.836567846683939,
                    2.428601675914292,
                    -3.079395289523384,
                    1.0809513347493518,
                    -2.4925941140824843,
                    -2.428601675914292,
                    3.079395289523384,
                    11.546745157318384,
                    -8.197432541942769,
                    -2.4286016759142925,
                    3.079395289523383,
                    2.428601675914292,
                    -3.079395289523384,
                    -11.546745157318384,
                    8.197439395398543,
                    2.4286016759142925,
                    -3.079395289523383,
                    -1.0809513347493518,
                    2.4925941140824843,
                    -2.4286016759142925,
                    3.079395289523383,
                    10.412767372774814,
                    -7.836560993228164,
                    1.0809513347493518,
                    -2.4925941140824843,
                    2.4286016759142925,
                    -3.079395289523383,
                    -10.412767372774814,
                    7.836567846683938,
                    -10.412767372774814,
                    7.836567846683939,
                    2.428601675914292,
                    -3.079395289523384,
                    1.0809513347493518,
                    -2.4925941140824843,
                    10.412767372774814,
                    -7.836560993228165,
                    -2.428601675914292,
                    3.079395289523384,
                    -1.0809513347493518,
                    2.4925941140824843,
                    2.428601675914292,
                    -3.079395289523384,
                    -11.546745157318384,
                    8.197439395398543,
                    2.4286016759142925,
                    -3.079395289523383,
                    -2.428601675914292,
                    3.079395289523384,
                    11.546745157318384,
                    -8.197432541942769,
                    -2.4286016759142925,
                    3.079395289523383,
                    1.0809513347493518,
                    -2.4925941140824843,
                    2.4286016759142925,
                    -3.079395289523383,
                    -10.412767372774814,
                    7.836567846683938,
                    -1.0809513347493518,
                    2.4925941140824843,
                    -2.4286016759142925,
                    3.079395289523383,
                    10.412767372774814,
                    -7.836560993228164,
                ],
            },
            "Idx": {
                "650632": 1,
                "632670": 2,
                "670671": 3,
                "671680": 4,
                "632633": 5,
                "632645": 6,
                "645646": 7,
                "692675": 8,
                "671684": 9,
                "684611": 10,
                "684652": 11,
                "671692": 12,
            },
            "IsSwitch": {
                "650632": False,
                "632670": False,
                "670671": False,
                "671680": False,
                "632633": False,
                "632645": False,
                "645646": False,
                "692675": False,
                "671684": False,
                "684611": False,
                "684652": False,
                "671692": True,
            },
            # Starting in DSS C-API 0.10.6, returns the NormAmps value,
            # mirroring the official code
            "SeasonRating": {
                "650632": 400.0,
                "632670": 400.0,
                "670671": 400.0,
                "671680": 400.0,
                "632633": 400.0,
                "632645": 400.0,
                "645646": 400.0,
                "692675": 400.0,
                "671684": 400.0,
                "684611": 400.0,
                "684652": 400.0,
                "671692": 400.0,
            },
        }
    ).to_dict()

    actual_dict = dss.utils.lines_to_dataframe().to_dict()
    assert_dict_equal(actual_dict, expected_dict)


def test_loads_to_dataframe(dss):
    expected_dict = pd.DataFrame(
        {
            "AllocationFactor": {
                "611": 0.5,
                "634a": 0.5,
                "634b": 0.5,
                "634c": 0.5,
                "645": 0.5,
                "646": 0.5,
                "652": 0.5,
                "670a": 0.5,
                "670b": 0.5,
                "670c": 0.5,
                "671": 0.5,
                "675a": 0.5,
                "675b": 0.5,
                "675c": 0.5,
                "692": 0.5,
            },
            "CFactor": {
                "611": 4.0,
                "634a": 4.0,
                "634b": 4.0,
                "634c": 4.0,
                "645": 4.0,
                "646": 4.0,
                "652": 4.0,
                "670a": 4.0,
                "670b": 4.0,
                "670c": 4.0,
                "671": 4.0,
                "675a": 4.0,
                "675b": 4.0,
                "675c": 4.0,
                "692": 4.0,
            },
            "CVRCurve": {
                "611": "",
                "634a": "",
                "634b": "",
                "634c": "",
                "645": "",
                "646": "",
                "652": "",
                "670a": "",
                "670b": "",
                "670c": "",
                "671": "",
                "675a": "",
                "675b": "",
                "675c": "",
                "692": "",
            },
            "CVRvars": {
                "611": 2.0,
                "634a": 2.0,
                "634b": 2.0,
                "634c": 2.0,
                "645": 2.0,
                "646": 2.0,
                "652": 2.0,
                "670a": 2.0,
                "670b": 2.0,
                "670c": 2.0,
                "671": 2.0,
                "675a": 2.0,
                "675b": 2.0,
                "675c": 2.0,
                "692": 2.0,
            },
            "CVRwatts": {
                "611": 1.0,
                "634a": 1.0,
                "634b": 1.0,
                "634c": 1.0,
                "645": 1.0,
                "646": 1.0,
                "652": 1.0,
                "670a": 1.0,
                "670b": 1.0,
                "670c": 1.0,
                "671": 1.0,
                "675a": 1.0,
                "675b": 1.0,
                "675c": 1.0,
                "692": 1.0,
            },
            "Class": {
                "611": 1,
                "634a": 1,
                "634b": 1,
                "634c": 1,
                "645": 1,
                "646": 1,
                "652": 1,
                "670a": 1,
                "670b": 1,
                "670c": 1,
                "671": 1,
                "675a": 1,
                "675b": 1,
                "675c": 1,
                "692": 1,
            },
            "Daily": {
                "611": "",
                "634a": "",
                "634b": "",
                "634c": "",
                "645": "",
                "646": "",
                "652": "",
                "670a": "",
                "670b": "",
                "670c": "",
                "671": "",
                "675a": "",
                "675b": "",
                "675c": "",
                "692": "",
            },
            "Duty": {
                "611": "",
                "634a": "",
                "634b": "",
                "634c": "",
                "645": "",
                "646": "",
                "652": "",
                "670a": "",
                "670b": "",
                "670c": "",
                "671": "",
                "675a": "",
                "675b": "",
                "675c": "",
                "692": "",
            },
            "Growth": {
                "611": "",
                "634a": "",
                "634b": "",
                "634c": "",
                "645": "",
                "646": "",
                "652": "",
                "670a": "",
                "670b": "",
                "670c": "",
                "671": "",
                "675a": "",
                "675b": "",
                "675c": "",
                "692": "",
            },
            "Idx": {
                "611": 11,
                "634a": 2,
                "634b": 3,
                "634c": 4,
                "645": 5,
                "646": 6,
                "652": 12,
                "670a": 13,
                "670b": 14,
                "670c": 15,
                "671": 1,
                "675a": 8,
                "675b": 9,
                "675c": 10,
                "692": 7,
            },
            "IsDelta": {
                "611": 0,
                "634a": 0,
                "634b": 0,
                "634c": 0,
                "645": 0,
                "646": 1,
                "652": 0,
                "670a": 0,
                "670b": 0,
                "670c": 0,
                "671": 1,
                "675a": 0,
                "675b": 0,
                "675c": 0,
                "692": 1,
            },
            "Model": {
                "611": 5,
                "634a": 1,
                "634b": 1,
                "634c": 1,
                "645": 1,
                "646": 2,
                "652": 2,
                "670a": 1,
                "670b": 1,
                "670c": 1,
                "671": 1,
                "675a": 1,
                "675b": 1,
                "675c": 1,
                "692": 5,
            },
            "Name": {
                "611": "611",
                "634a": "634a",
                "634b": "634b",
                "634c": "634c",
                "645": "645",
                "646": "646",
                "652": "652",
                "670a": "670a",
                "670b": "670b",
                "670c": "670c",
                "671": "671",
                "675a": "675a",
                "675b": "675b",
                "675c": "675c",
                "692": "692",
            },
            "NumCust": {
                "611": 1,
                "634a": 1,
                "634b": 1,
                "634c": 1,
                "645": 1,
                "646": 1,
                "652": 1,
                "670a": 1,
                "670b": 1,
                "670c": 1,
                "671": 1,
                "675a": 1,
                "675b": 1,
                "675c": 1,
                "692": 1,
            },
            "PF": {
                "611": 0.9048187022009941,
                "634a": 0.8240419241993675,
                "634b": 0.8,
                "634c": 0.8,
                "645": 0.8056510126494245,
                "646": 0.8673133941933718,
                "652": 0.8300495997825932,
                "670a": 0.8619342151577695,
                "670b": 0.8666224568741688,
                "670c": 0.8645818496218686,
                "671": 0.8682431421244591,
                "675a": 0.9311010850748034,
                "675b": 0.7498378553650925,
                "675c": 0.8072891017918288,
                "692": 0.7476519144858309,
            },
            "PctMean": {
                "611": 50.0,
                "634a": 50.0,
                "634b": 50.0,
                "634c": 50.0,
                "645": 50.0,
                "646": 50.0,
                "652": 50.0,
                "670a": 50.0,
                "670b": 50.0,
                "670c": 50.0,
                "671": 50.0,
                "675a": 50.0,
                "675b": 50.0,
                "675c": 50.0,
                "692": 50.0,
            },
            "PctStdDev": {
                "611": 10.0,
                "634a": 10.0,
                "634b": 10.0,
                "634c": 10.0,
                "645": 10.0,
                "646": 10.0,
                "652": 10.0,
                "670a": 10.0,
                "670b": 10.0,
                "670c": 10.0,
                "671": 10.0,
                "675a": 10.0,
                "675b": 10.0,
                "675c": 10.0,
                "692": 10.0,
            },
            "RelWeighting": {
                "611": 1.0,
                "634a": 1.0,
                "634b": 1.0,
                "634c": 1.0,
                "645": 1.0,
                "646": 1.0,
                "652": 1.0,
                "670a": 1.0,
                "670b": 1.0,
                "670c": 1.0,
                "671": 1.0,
                "675a": 1.0,
                "675b": 1.0,
                "675c": 1.0,
                "692": 1.0,
            },
            "Rneut": {
                "611": -1.0,
                "634a": -1.0,
                "634b": -1.0,
                "634c": -1.0,
                "645": -1.0,
                "646": -1.0,
                "652": -1.0,
                "670a": -1.0,
                "670b": -1.0,
                "670c": -1.0,
                "671": -1.0,
                "675a": -1.0,
                "675b": -1.0,
                "675c": -1.0,
                "692": -1.0,
            },
            "Spectrum": {
                "611": "defaultload",
                "634a": "defaultload",
                "634b": "defaultload",
                "634c": "defaultload",
                "645": "defaultload",
                "646": "defaultload",
                "652": "defaultload",
                "670a": "defaultload",
                "670b": "defaultload",
                "670c": "defaultload",
                "671": "defaultload",
                "675a": "defaultload",
                "675b": "defaultload",
                "675c": "defaultload",
                "692": "defaultload",
            },
            "Status": {
                "611": 0,
                "634a": 0,
                "634b": 0,
                "634c": 0,
                "645": 0,
                "646": 0,
                "652": 0,
                "670a": 0,
                "670b": 0,
                "670c": 0,
                "671": 0,
                "675a": 0,
                "675b": 0,
                "675c": 0,
                "692": 0,
            },
            "Vmaxpu": {
                "611": 1.05,
                "634a": 1.05,
                "634b": 1.05,
                "634c": 1.05,
                "645": 1.05,
                "646": 1.05,
                "652": 1.05,
                "670a": 1.05,
                "670b": 1.05,
                "670c": 1.05,
                "671": 1.05,
                "675a": 1.05,
                "675b": 1.05,
                "675c": 1.05,
                "692": 1.05,
            },
            "VminEmerg": {
                "611": 0.0,
                "634a": 0.0,
                "634b": 0.0,
                "634c": 0.0,
                "645": 0.0,
                "646": 0.0,
                "652": 0.0,
                "670a": 0.0,
                "670b": 0.0,
                "670c": 0.0,
                "671": 0.0,
                "675a": 0.0,
                "675b": 0.0,
                "675c": 0.0,
                "692": 0.0,
            },
            "VminNorm": {
                "611": 0.0,
                "634a": 0.0,
                "634b": 0.0,
                "634c": 0.0,
                "645": 0.0,
                "646": 0.0,
                "652": 0.0,
                "670a": 0.0,
                "670b": 0.0,
                "670c": 0.0,
                "671": 0.0,
                "675a": 0.0,
                "675b": 0.0,
                "675c": 0.0,
                "692": 0.0,
            },
            "Vminpu": {
                "611": 0.95,
                "634a": 0.95,
                "634b": 0.95,
                "634c": 0.95,
                "645": 0.95,
                "646": 0.95,
                "652": 0.95,
                "670a": 0.95,
                "670b": 0.95,
                "670c": 0.95,
                "671": 0.95,
                "675a": 0.95,
                "675b": 0.95,
                "675c": 0.95,
                "692": 0.95,
            },
            "XfkVA": {
                "611": 0.0,
                "634a": 0.0,
                "634b": 0.0,
                "634c": 0.0,
                "645": 0.0,
                "646": 0.0,
                "652": 0.0,
                "670a": 0.0,
                "670b": 0.0,
                "670c": 0.0,
                "671": 0.0,
                "675a": 0.0,
                "675b": 0.0,
                "675c": 0.0,
                "692": 0.0,
            },
            "Xneut": {
                "611": 0.0,
                "634a": 0.0,
                "634b": 0.0,
                "634c": 0.0,
                "645": 0.0,
                "646": 0.0,
                "652": 0.0,
                "670a": 0.0,
                "670b": 0.0,
                "670c": 0.0,
                "671": 0.0,
                "675a": 0.0,
                "675b": 0.0,
                "675c": 0.0,
                "692": 0.0,
            },
            "Yearly": {
                "611": "",
                "634a": "",
                "634b": "",
                "634c": "",
                "645": "",
                "646": "",
                "652": "",
                "670a": "",
                "670b": "",
                "670c": "",
                "671": "",
                "675a": "",
                "675b": "",
                "675c": "",
                "692": "",
            },
            "ZipV": {
                "611": [0, 0, 0, 0, 0, 0, 0],
                "634a": [0, 0, 0, 0, 0, 0, 0],
                "634b": [0, 0, 0, 0, 0, 0, 0],
                "634c": [0, 0, 0, 0, 0, 0, 0],
                "645": [0, 0, 0, 0, 0, 0, 0],
                "646": [0, 0, 0, 0, 0, 0, 0],
                "652": [0, 0, 0, 0, 0, 0, 0],
                "670a": [0, 0, 0, 0, 0, 0, 0],
                "670b": [0, 0, 0, 0, 0, 0, 0],
                "670c": [0, 0, 0, 0, 0, 0, 0],
                "671": [0, 0, 0, 0, 0, 0, 0],
                "675a": [0, 0, 0, 0, 0, 0, 0],
                "675b": [0, 0, 0, 0, 0, 0, 0],
                "675c": [0, 0, 0, 0, 0, 0, 0],
                "692": [0, 0, 0, 0, 0, 0, 0],
            },
            "kV": {
                "611": 2.4,
                "634a": 0.277,
                "634b": 0.277,
                "634c": 0.277,
                "645": 2.4,
                "646": 4.16,
                "652": 2.4,
                "670a": 2.4,
                "670b": 2.4,
                "670c": 2.4,
                "671": 4.16,
                "675a": 2.4,
                "675b": 2.4,
                "675c": 2.4,
                "692": 4.16,
            },
            "kVABase": {
                "611": 187.88294228055935,
                "634a": 194.164878389476,
                "634b": 150.0,
                "634c": 150.0,
                "645": 211.00947846009194,
                "646": 265.18672666632466,
                "652": 154.20765220960988,
                "670a": 19.72308292331602,
                "670b": 76.15773105863909,
                "670c": 135.32553343696821,
                "671": 1330.2725284692608,
                "675a": 520.8886637276722,
                "675b": 90.68627239003708,
                "675c": 359.22694776422327,
                "692": 227.37853900489378,
            },
            "kW": {
                "611": 170.0,
                "634a": 160.0,
                "634b": 120.0,
                "634c": 120.0,
                "645": 170.0,
                "646": 230.0,
                "652": 128.0,
                "670a": 17.0,
                "670b": 66.0,
                "670c": 117.0,
                "671": 1155.0,
                "675a": 485.0,
                "675b": 68.0,
                "675c": 290.0,
                "692": 170.0,
            },
            "kWh": {
                "611": 0.0,
                "634a": 0.0,
                "634b": 0.0,
                "634c": 0.0,
                "645": 0.0,
                "646": 0.0,
                "652": 0.0,
                "670a": 0.0,
                "670b": 0.0,
                "670c": 0.0,
                "671": 0.0,
                "675a": 0.0,
                "675b": 0.0,
                "675c": 0.0,
                "692": 0.0,
            },
            "kWhDays": {
                "611": 30.0,
                "634a": 30.0,
                "634b": 30.0,
                "634c": 30.0,
                "645": 30.0,
                "646": 30.0,
                "652": 30.0,
                "670a": 30.0,
                "670b": 30.0,
                "670c": 30.0,
                "671": 30.0,
                "675a": 30.0,
                "675b": 30.0,
                "675c": 30.0,
                "692": 30.0,
            },
            "kvar": {
                "611": 80.0,
                "634a": 110.0,
                "634b": 90.0,
                "634c": 90.0,
                "645": 125.0,
                "646": 132.0,
                "652": 86.0,
                "670a": 10.0,
                "670b": 38.0,
                "670c": 68.0,
                "671": 660.0,
                "675a": 190.0,
                "675b": 60.0,
                "675c": 212.0,
                "692": 151.0,
            },
            "puSeriesRL": {
                "611": 50.0,
                "634a": 50.0,
                "634b": 50.0,
                "634c": 50.0,
                "645": 50.0,
                "646": 50.0,
                "652": 50.0,
                "670a": 50.0,
                "670b": 50.0,
                "670c": 50.0,
                "671": 50.0,
                "675a": 50.0,
                "675b": 50.0,
                "675c": 50.0,
                "692": 50.0,
            },
            "Phases": {
                "671": 3,
                "634a": 1,
                "634b": 1,
                "634c": 1,
                "645": 1,
                "646": 1,
                "692": 1,
                "675a": 1,
                "675b": 1,
                "675c": 1,
                "611": 1,
                "652": 1,
                "670a": 1,
                "670b": 1,
                "670c": 1,
            },
        }
    ).to_dict()

    actual_dict = dss.utils.loads_to_dataframe().to_dict()
    assert_dict_equal(actual_dict, expected_dict)


def test_loadshape_to_dataframe(dss):
    expected_dict = pd.DataFrame(
        {
            "HrInterval": {"default": 1.0},
            "Idx": {"default": 1},
            "MinInterval": {"default": 60.0},
            "Name": {"default": "default"},
            "Npts": {"default": 24},
            "PBase": {"default": 0.0},
            "PMult": {
                "default": [
                    0.677,
                    0.6256,
                    0.6087,
                    0.5833,
                    0.58028,
                    0.6025,
                    0.657,
                    0.7477,
                    0.832,
                    0.88,
                    0.94,
                    0.989,
                    0.985,
                    0.98,
                    0.9898,
                    0.999,
                    1.0,
                    0.958,
                    0.936,
                    0.913,
                    0.876,
                    0.876,
                    0.828,
                    0.756,
                ]
            },
            "QBase": {"default": 0.0},
            "QMult": {"default": [0.0]},
            "SInterval": {"default": 3600.0},
            "TimeArray": {"default": [0.0]},
            "UseActual": {"default": 0},
        }
    ).to_dict()

    actual_dict = dss.utils.loadshape_to_dataframe().to_dict()
    assert_dict_equal(actual_dict, expected_dict)


def test_meters_to_dataframe(dss):
    expected_dict = {}
    actual_dict = dss.utils.meters_to_dataframe().to_dict()
    assert_dict_equal(actual_dict, expected_dict)


def test_pvsystems_to_dataframe(dss):
    dss.run_command("New PVSystem.631")

    expected_dict = pd.DataFrame(
        {
            "Idx": {"631": 1},
            "Irradiance": {"631": 1.0},
            "IrradianceNow": {"631": 1.0},
            "Name": {"631": "631"},
            "Pmpp": {"631": 500.0},
            "kVARated": {"631": 500.0},
            "kW": {"631": 499.99999999999994},
            "kvar": {"631": 0.0},
            "pf": {"631": 1.0},
            "RegisterNames": {
                "631": ["kWh", "kvarh", "Max kW", "Max kVA", "Hours", "Price($)"]
            },
            "RegisterValues": {"631": [0.0, 0.0, 0.0, 0.0, 0.0, 0.0]},
            "Tdaily": {"631": ""},
            "Tduty": {"631": ""},
            "Tyearly": {"631": ""},
            "daily": {"631": ""},
            "duty": {"631": ""},
            "yearly": {"631": ""},
        }
    ).to_dict()

    actual_dict = dss.utils.pvsystems_to_dataframe().to_dict()
    assert_dict_equal(actual_dict, expected_dict)


def test_reclosers_to_dataframe(dss):
    expected_dict = {}
    actual_dict = dss.utils.reclosers_to_dataframe().to_dict()

    assert_dict_equal(actual_dict, expected_dict)


def test_regcontrols_to_dataframe(dss):
    expected_dict = pd.DataFrame(
        {
            "CTPrimary": {"reg1": 700.0, "reg2": 700.0, "reg3": 700.0},
            "Delay": {"reg1": 15.0, "reg2": 15.0, "reg3": 15.0},
            "ForwardBand": {"reg1": 2.0, "reg2": 2.0, "reg3": 2.0},
            "ForwardR": {"reg1": 3.0, "reg2": 3.0, "reg3": 3.0},
            "ForwardVreg": {"reg1": 122.0, "reg2": 122.0, "reg3": 122.0},
            "ForwardX": {"reg1": 9.0, "reg2": 9.0, "reg3": 9.0},
            "Idx": {"reg1": 1, "reg2": 2, "reg3": 3},
            "IsInverseTime": {"reg1": 0, "reg2": 0, "reg3": 0},
            "IsReversible": {"reg1": 0, "reg2": 0, "reg3": 0},
            "MaxTapChange": {"reg1": 16, "reg2": 16, "reg3": 16},
            "MonitoredBus": {"reg1": "", "reg2": "", "reg3": ""},
            "Name": {"reg1": "reg1", "reg2": "reg2", "reg3": "reg3"},
            "PTRatio": {"reg1": 20.0, "reg2": 20.0, "reg3": 20.0},
            "ReverseBand": {"reg1": 3.0, "reg2": 3.0, "reg3": 3.0},
            "ReverseR": {"reg1": 0.0, "reg2": 0.0, "reg3": 0.0},
            "ReverseVreg": {"reg1": 120.0, "reg2": 120.0, "reg3": 120.0},
            "ReverseX": {"reg1": 0.0, "reg2": 0.0, "reg3": 0.0},
            "TapDelay": {"reg1": 2.0, "reg2": 2.0, "reg3": 2.0},
            "TapNumber": {"reg1": 9, "reg2": 6, "reg3": 9},
            "TapWinding": {"reg1": 2, "reg2": 2, "reg3": 2},
            "Transformer": {"reg1": "reg1", "reg2": "reg2", "reg3": "reg3"},
            "VoltageLimit": {"reg1": 0.0, "reg2": 0.0, "reg3": 0.0},
            "Winding": {"reg1": 2, "reg2": 2, "reg3": 2},
        }
    ).to_dict()

    actual_dict = dss.utils.regcontrols_to_dataframe().to_dict()
    assert_dict_equal(actual_dict, expected_dict)


def test_relays_to_dataframe(dss):
    expected_dict = {}
    actual_dict = dss.utils.relays_to_dataframe().to_dict()
    assert_dict_equal(actual_dict, expected_dict)


def test_sensors_to_dataframe(dss):
    expected_dict = {}
    actual_dict = dss.utils.sensors_to_dataframe().to_dict()
    assert_dict_equal(actual_dict, expected_dict)


def test_transformers_to_dataframe(dss):
    expected_dict = pd.DataFrame(
        {
            "IsDelta": {"reg1": 0, "reg2": 0, "reg3": 0, "sub": 0, "xfm1": 0},
            "MaxTap": {"reg1": 1.1, "reg2": 1.1, "reg3": 1.1, "sub": 1.1, "xfm1": 1.1},
            "MinTap": {"reg1": 0.9, "reg2": 0.9, "reg3": 0.9, "sub": 0.9, "xfm1": 0.9},
            "Name": {
                "reg1": "reg1",
                "reg2": "reg2",
                "reg3": "reg3",
                "sub": "sub",
                "xfm1": "xfm1",
            },
            "NumTaps": {"reg1": 32, "reg2": 32, "reg3": 32, "sub": 32, "xfm1": 32},
            "NumWindings": {"reg1": 2, "reg2": 2, "reg3": 2, "sub": 2, "xfm1": 2},
            "R": {
                "reg1": 5e-03,
                "reg2": 5e-03,
                "reg3": 5e-03,
                "sub": 5e-04,
                "xfm1": 0.55000000000000005,
            },
            "Rneut": {
                "reg1": -1.0,
                "reg2": -1.0,
                "reg3": -1.0,
                "sub": -1.0,
                "xfm1": -1.0,
            },
            "Tap": {
                "reg1": 1.05625,
                "reg2": 1.0375,
                "reg3": 1.05625,
                "sub": 1.0,
                "xfm1": 1.0,
            },
            "Wdg": {"reg1": 2, "reg2": 2, "reg3": 2, "sub": 2, "xfm1": 2},
            "XfmrCode": {"reg1": "", "reg2": "", "reg3": "", "sub": "", "xfm1": ""},
            "Xhl": {
                "reg1": 0.01,
                "reg2": 0.01,
                "reg3": 0.01,
                "sub": 8e-03,
                "xfm1": 2,
            },
            "Xht": {
                "reg1": 35,
                "reg2": 35,
                "reg3": 35,
                "sub": 4,
                "xfm1": 1,
            },
            "Xlt": {"reg1": 30, "reg2": 30, "reg3": 30, "sub": 4, "xfm1": 1},
            "Xneut": {"reg1": 0.0, "reg2": 0.0, "reg3": 0.0, "sub": 0.0, "xfm1": 0.0},
            "kV": {"reg1": 2.4, "reg2": 2.4, "reg3": 2.4, "sub": 4.16, "xfm1": 0.48},
            "kVA": {
                "reg1": 1666.0,
                "reg2": 1666.0,
                "reg3": 1666.0,
                "sub": 5000.0,
                "xfm1": 500.0,
            },
            "Idx": {"sub": 1, "reg1": 2, "reg2": 3, "reg3": 4, "xfm1": 5},
            "CoreType": {"sub": 0, "reg1": 0, "reg2": 0, "reg3": 0, "xfm1": 0},
            "RdcOhms": {
                "sub": 4.903253333333334e-06,
                "reg1": 0.0001469387755102041,
                "reg2": 0.0001469387755102041,
                "reg3": 0.0001469387755102041,
                "xfm1": 0.0007180800000000002,
            },
            "WdgCurrents": {
                "sub": [
                    10.886838403101137,
                    -5.9590983105881605,
                    -10.886834219418233,
                    5.959098309889669,
                    -521.274920007214,
                    285.3283304721117,
                    521.2749199396931,
                    -285.32867740653455,
                    -7.086427293397719,
                    -5.676531811608584,
                    7.08642520106514,
                    5.6765281889238395,
                    339.30622841697186,
                    271.79939795983955,
                    -339.3065288569778,
                    -271.7992244265042,
                    -0.771324589062715,
                    13.032053531249403,
                    0.771322497719666,
                    -13.03204990789527,
                    36.93235703371465,
                    -623.9901740448549,
                    -36.932056532241404,
                    623.9903474440798,
                ],
                "reg1": [
                    521.2749200067483,
                    -285.3283304735087,
                    -521.2749200742692,
                    285.3279831642285,
                    -493.51471731392667,
                    270.13263500947505,
                    493.51471723010764,
                    -270.13300181226805,
                ],
                "reg2": [
                    -339.30622841604054,
                    -271.7993979600724,
                    339.3059276519343,
                    271.7995716808364,
                    327.0415459657088,
                    261.97567100822926,
                    -327.04185797739774,
                    -261.97549077658914,
                ],
                "reg3": [
                    -36.93235703278333,
                    623.9901740467176,
                    36.932657858822495,
                    -623.9900004593655,
                    34.966147642349824,
                    -590.7595804324374,
                    -34.965829925844446,
                    590.759763748385,
                ],
                "xfm1": [
                    64.7216815965744,
                    -50.18299905784306,
                    -64.7216831851581,
                    50.182964005225585,
                    -560.9212712562512,
                    434.91872502353,
                    560.9212542713685,
                    -434.9190213786205,
                    -57.87251294138969,
                    -22.04935809275935,
                    57.87248265804055,
                    22.049376873065285,
                    501.56125998063,
                    191.0947614815741,
                    -501.56151636968207,
                    -191.0945995665661,
                    10.604495125653102,
                    62.685128147381874,
                    -10.60446437542032,
                    -62.68511196150439,
                    -91.90509532533542,
                    -543.2708349826607,
                    91.90535792030641,
                    543.2709703330329,
                ],
            },
            "WdgVoltages": {
                "sub": [
                    2401.562774320432,
                    -0.46690091155609226,
                    -1201.2376790663666,
                    -2079.7175126796437,
                    -1200.3116016198273,
                    2080.1419403490627,
                ],
                "reg1": [2536.356120228099, -0.5793286234950956],
                "reg2": [-1246.2598772664523, -2157.4877137350218],
                "reg3": [-1267.5877694598496, 2196.935539327288],
                "xfm1": [
                    273.1208520924334,
                    -15.653268696155022,
                    -149.22087189563985,
                    -236.28815213487727,
                    -124.73890495654813,
                    242.00752558006548,
                ],
            },
            "LossesByType": {
                "sub": [
                    32.28780525899492,
                    262.4687364427373,
                    32.28780525899492,
                    262.4687364427373,
                    0.0,
                    0.0,
                ],
                "reg1": [
                    122.09388323919848,
                    123.85831108468119,
                    122.09388323919848,
                    123.85831108468119,
                    0.0,
                    0.0,
                ],
                "reg2": [
                    65.34575459547341,
                    67.07771651400253,
                    65.34575459547341,
                    67.07771651400253,
                    0.0,
                    0.0,
                ],
                "reg3": [
                    135.08947523473762,
                    136.85396666557062,
                    135.08947523473762,
                    136.85396666557062,
                    0.0,
                    0.0,
                ],
                "xfm1": [
                    5552.6587844858295,
                    10096.246342088038,
                    5552.6587844858295,
                    10096.246342088038,
                    0.0,
                    0.0,
                ],
            },
        }
    ).to_dict()

    actual_dict = dss.utils.transformers_to_dataframe().to_dict()
    assert_dict_equal(actual_dict, expected_dict)


def test_vsources_to_dataframe(dss):
    expected_dict = pd.DataFrame(
        {
            "Idx": {"source": 1},
            "AngleDeg": {"source": 30.0},
            "BasekV": {"source": 115.0},
            "Frequency": {"source": 60.0},
            "Name": {"source": "source"},
            "PU": {"source": 1.0001},
            "Phases": {"source": 3},
        }
    ).to_dict()

    actual_dict = dss.utils.vsources_to_dataframe().to_dict()
    assert_dict_equal(actual_dict, expected_dict)


def test_xycurves_to_dataframe(dss):
    expected_dict = {}

    actual_dict = dss.utils.xycurves_to_dataframe().to_dict()
    assert_dict_equal(actual_dict, expected_dict)


def test_storage_to_dataframe(dss):
    assert not dss.dss_lib.DSS_Get_LegacyModels()

    assert (
        dss.utils.run_command("Redirect {}".format(PATH_TO_DSS)) == ""
    ), "Unable to find test data"

    dss.run_command("New Storage.631")

    expected_dict = pd.DataFrame(
        {
            "%Charge": {"Storage.631": "100"},
            "%Discharge": {"Storage.631": "100"},
            "%EffCharge": {"Storage.631": "90"},
            "%EffDischarge": {"Storage.631": "90"},
            "%IdlingkW": {"Storage.631": "1"},
            "%R": {"Storage.631": "0"},
            "%X": {"Storage.631": "50"},
            "%reserve": {"Storage.631": "20"},
            "%stored": {"Storage.631": "100"},
            "Balanced": {"Storage.631": "No"},
            "ChargeTrigger": {"Storage.631": "0"},
            "DischargeTrigger": {"Storage.631": "0"},
            "DispMode": {"Storage.631": "Default"},
            "DynaDLL": {"Storage.631": ""},
            "DynaData": {"Storage.631": ""},
            "LimitCurrent": {"Storage.631": "No"},
            "State": {"Storage.631": "Idling"},
            "TimeChargeTrig": {"Storage.631": "2"},
            "UserData": {"Storage.631": ""},
            "UserModel": {"Storage.631": ""},
            "Vmaxpu": {"Storage.631": "1.1"},
            "Vminpu": {"Storage.631": "0.9"},
            "basefreq": {"Storage.631": "60"},
            "bus1": {"Storage.631": "631_1"},
            "class": {"Storage.631": "1"},
            "conn": {"Storage.631": "wye"},
            "daily": {"Storage.631": ""},
            "debugtrace": {"Storage.631": "No"},
            "duty": {"Storage.631": ""},
            "enabled": {"Storage.631": "Yes"},
            "kVA": {"Storage.631": "25"},
            "kW": {"Storage.631": "-0.25"},
            "kWhrated": {"Storage.631": "50"},
            "kWhstored": {"Storage.631": "50"},
            "kWrated": {"Storage.631": "25"},
            "kv": {"Storage.631": "12.47"},
            "kvar": {"Storage.631": "0"},
            "like": {"Storage.631": ""},
            "model": {"Storage.631": "1"},
            "pf": {"Storage.631": "1"},
            "phases": {"Storage.631": "3"},
            "spectrum": {"Storage.631": ""},
            "yearly": {"Storage.631": ""},
            "%Cutin": {"Storage.631": "0"},
            "%Cutout": {"Storage.631": "0"},
            "%PminNoVars": {"Storage.631": "-1"},
            "%PminkvarMax": {"Storage.631": "-1"},
            "%kWrated": {"Storage.631": "100"},
            "EffCurve": {"Storage.631": ""},
            "PFPriority": {"Storage.631": "No"},
            "VarFollowInverter": {"Storage.631": "No"},
            "WattPriority": {"Storage.631": "No"},
            "kvarMax": {"Storage.631": "25"},
            "kvarMaxAbs": {"Storage.631": "25"},
            "%Idlingkvar": {"Storage.631": ""},
            "ControlMode": {"Storage.631": "GFL"},
            "DynOut": {"Storage.631": []},
            "DynamicEq": {"Storage.631": ""},
            "Kp": {"Storage.631": "0.01"},
            "PITol": {"Storage.631": "0"},
            "SafeMode": {"Storage.631": "No"},
            "SafeVoltage": {"Storage.631": "80"},
            "kVDC": {"Storage.631": "8"},
            "AmpLimit": {"Storage.631": "-1"},
            "AmpLimitGain": {"Storage.631": "0.8"},
        }
    ).to_dict()

    actual_dict = dss.utils.class_to_dataframe("Storage").to_dict()

    assert_dict_equal(actual_dict, expected_dict)


def test_linegeometry_class_to_dataframe():
    string = """Clear

    New Circuit.test_circuit

    New Wiredata.ACSR336 GMR=0.0255000 DIAM=0.7410000 RAC=0.3060000 NormAmps=530.0000 Runits=mi radunits=in gmrunits=ft
    New Wiredata.ACSR1/0 GMR=0.0044600 DIAM=0.3980000 RAC=1.120000 NormAmps=230.0000 Runits=mi radunits=in gmrunits=ft


    New Linegeometry.HC2_336_1neut_0Mess nconds=4 nphases=3
    ~ cond=1 Wire=acsr336 x=-1.2909 h=13.716 units=m
    ~ cond=2 Wire=acsr336 x=-0.1530096 h=4.1806368 units=ft
    ~ cond=3 Wire=acsr336 x=0.5737 h=13.716 units=m
    ~ cond=4 Wire= ACSR1/0 x=0 h=14.648 ! units=m ! neutral

    New Line.Line1 Bus1=bus1.1.2.3 Bus2=bus2.1.2.3
    ~ Geometry= HC2_336_1neut_0Mess
    ~ Length=300 units=ft

    Set Voltagebases=[4.8,34.5,115.0]
    Calcvoltagebases
    Solve"""

    import opendssdirect as dss

    dss.run_command(string).strip()
    is_pandas_installed = dss.utils.is_pandas_installed
    dss.utils.is_pandas_installed = False
    data = dss.utils.class_to_dataframe("linegeometry")
    dss.utils.is_pandas_installed = is_pandas_installed
    assert data == {
        "linegeometry.hc2_336_1neut_0mess": {
            "Seasons": "1",
            "Ratings": ["0"],
            "LineType": "oh",
            "nconds": "4",
            "nphases": "3",
            "cond": "4",
            "wire": "acsr1/0",
            "x": [-1.2909, -0.1530096, 0.5737, 0.0],
            "h": [13.716, 4.1806368, 13.716, 14.648],
            "units": ["m", "ft", "m", "m"],
            "normamps": "530",
            "emergamps": "795",
            "reduce": "No",
            "spacing": "",
            "wires": ["acsr336", "acsr336", "acsr336", "acsr1/0"],
            "cncable": "acsr1/0",
            "tscable": "acsr1/0",
            "cncables": ["acsr336", "acsr336", "acsr336", "acsr1/0"],
            "tscables": ["acsr336", "acsr336", "acsr336", "acsr1/0"],
            "like": "",
        }
    }


def test_ymatrix(dss):
    expected_Y_data = (
        np.array([
            0.8178822742754986-4.636999108384914j,
            -0.13055025449836521+1.4833269062112926j,
            -0.13055025449836524+1.4833269062112926j,
            -9.283352668986776+74.26682135189421j,
            9.283352668986776-74.26682135189421j,
            -0.13055025449836521+1.4833269062112926j,
            0.8178822742754985-4.636999108384914j,
            -0.13055025449836524+1.4833269062112926j,
            -9.283352668986776+74.26682135189421j,
            9.283352668986776-74.26682135189421j,
            -0.13055025449836524+1.4833269062112926j,
            -0.13055025449836524+1.4833269062112926j,
            0.8178822742754985-4.636999108384913j,
            9.283352668986776-74.26682135189421j,
            -9.283352668986776+74.26682135189421j,
            -9.283352668986776+74.26682135189421j,
            9.283352668986776-74.26682135189421j,
            1890.6787348910132-5002.165990528294j,
            -1369.165023011177+1369.165023011177j,
            9.283352668986776-74.26682135189421j,
            -9.283352668986776+74.26682135189421j,
            1890.6787348910132-5002.165990528294j,
            -1393.9089692101743+1393.9089692101743j,
            9.283352668986776-74.26682135189421j,
            -9.283352668986776+74.26682135189421j,
            1890.6787348910132-5002.165990528294j,
            -1369.165023011177+1369.165023011177j,
            -1369.165023011177+1369.165023011177j,
            1297.3960314120725-1299.5515100351274j,
            -0.485857546024989+1.22029123063551j,
            -0.26605890984743125+0.9122168082594669j,
            -1.1451220523783028+3.3006007307348617j,
            0.485857546024989-1.2202912734754099j,
            0.26605890984743125-0.9122168510993668j,
            -1393.9089692101743+1393.9089692101743j,
            -0.485857546024989+1.22029123063551j,
            1344.5294284920049-1346.6543624309695j,
            -0.12630483115283336+0.6967002366036674j,
            0.485857546024989-1.2202912734754099j,
            -1.0027111809933547+3.1276451752596324j,
            0.12630483115283336-0.6967002794435673j,
            -1369.165023011177+1369.165023011177j,
            -0.26605890984743125+0.9122168082594669j,
            -0.12630483115283336+0.6967002366036674j,
            1297.1376277955421-1299.201503062629j,
            0.26605890984743125-0.9122168510993668j,
            0.12630483115283336-0.6967002794435673j,
            -0.8867184358481343+2.9505937582362023j,
            6.174634422355675-8.24293119603154j,
            -1.495155595100418+1.5059091102776052j,
            -2.1394799752143716+1.6901170943579362j,
            -5.286769772134453+9.612308676608098j,
            -5.564622525570931+7.133818691956606j,
            1.495155595100418-1.5059091209875801j,
            2.1394799752143716-1.6901171050679111j,
            -1.495155595100418+1.5059091102776052j,
            5.5185532759822955-8.172535006552001j,
            -1.0880240059003325+1.3823966977507467j,
            -5.286769772134453+9.612308676608098j,
            1.495155595100418-1.5059091209875801j,
            -4.908541379197551+7.063422502477067j,
            1.0880240059003325-1.3823967084607216j,
            -2.1394799752143716+1.6901170943579362j,
            -1.0880240059003325+1.3823966977507467j,
            5.799215580883693-8.194725900906395j,
            -5.286769772134453+9.612308676608098j,
            2.1394799752143716-1.6901171050679111j,
            1.0880240059003325-1.3823967084607216j,
            -5.189203684098949+7.085613396831461j,
            -5.286769772134453+9.612308676608098j,
            47.90393247228869-84.7402932980703j,
            -5.286769772134453+9.612308676608098j,
            47.38261719384117-84.47963565884653j,
            -5.286769772134453+9.612308676608098j,
            47.38261719384117-84.47963565884653j,
            10000011.227919342-18.25418789613767j,
            -1.7229307871034956+4.284189778778654j,
            -3.3612866353936672+4.205156433963181j,
            -10000000+0j,
            -1.718112606719134+4.952139130885014j,
            0.7289685611777779-1.8308946338715828j,
            0.39918816181159994-1.3686674435099282j,
            -2.2902441047566056+6.601201461469723j,
            0.971715092049978-2.4405825469508198j,
            0.5321178196948625-1.8244337021987336j,
            -7.175068362002635+6.675422271119008j,
            2.407733520011465-0.9993426967242526j,
            -1.7229307871034956+4.284189778778654j,
            10000003.554359512-10.973356336291346j,
            -0.46436141906637757+2.4514249039455116j,
            0.7289685611777779-1.8308946338715828j,
            -1.5044428822105846+4.692640923120229j,
            0.1895046228849712-1.0453117471021263j,
            0.971715092049978-2.4405825469508198j,
            -2.0054223619867093+6.255290350519265j,
            0.2526096623056667-1.3934005588871345j,
            -10000000+0j,
            -3.3612866353936672+4.205156433963181j,
            -0.46436141906637757+2.4514249039455116j,
            10000010.373279463-16.99855337809098j,
            -10000000+0j,
            0.39918816181159994-1.3686674435099282j,
            0.1895046228849712-1.0453117471021263j,
            -1.3304102563362856+4.426997386700979j,
            0.5321178196948625-1.8244337021987336j,
            0.2526096623056667-1.3934005588871345j,
            -1.7734368716962685+5.901187516472405j,
            2.407733520011465-0.9993426967242526j,
            -7.224938066978001+6.644943442253672j,
            11.58941479605369-10.653610816526951j,
            -7.224938066978001+6.644943442253672j,
            2.407733520011465-0.9993426967242526j,
            -4.3349628401868+3.9869660653522025j,
            1.4446401120068793-0.5996056180345513j,
            -3.8523736320183444+1.598948297622844j,
            -7.224938066978001+6.644943442253672j,
            7.238228562540131-6.65257100102314j,
            -2.421024015573595+1.006970279055664j,
            2.407733520011465-0.9993426967242526j,
            2.407733520011465-0.9993426967242526j,
            -2.421024015573595+1.006970279055664j,
            7.188358857564766-6.683049829888476j,
            -7.175068362002635+6.675422271119008j,
            -10000000+0j,
            10000010.422590783-7.845286492488519j,
            -1.0907747445126654+2.5013196133428393j,
            1.0809513347493518-2.4925941140824843j,
            2.4286016759142925-3.079395289523383j,
            -10.412767372774814+7.836567846683938j,
            -2.4286016759142925+3.079395289523383j,
            -10000000+0j,
            -1.0907747445126654+2.5013196133428393j,
            10000010.422590783-7.84528649248852j,
            -10.412767372774814+7.836567846683939j,
            2.428601675914292-3.079395289523384j,
            1.0809513347493518-2.4925941140824843j,
            -2.428601675914292+3.079395289523384j,
            1.0809513347493518-2.4925941140824843j,
            -10.412767372774814+7.836567846683939j,
            10.496968761663704-7.834876246351111j,
            -2.428601675914292+3.079395289523384j,
            -1.0809513347493518+2.4925941140824843j,
            2.428601675914292-3.079395289523384j,
            2.4286016759142925-3.079395289523383j,
            2.428601675914292-3.079395289523384j,
            -2.428601675914292+3.079395289523384j,
            11.55855071287394-8.17317835062127j,
            -2.4286016759142925+3.079395289523383j,
            -11.546745157318384+8.197439395398543j,
            -10.412767372774814+7.836567846683938j,
            1.0809513347493518-2.4925941140824843j,
            -1.0809513347493518+2.4925941140824843j,
            -2.4286016759142925+3.079395289523383j,
            10.463114594997036-7.838695690795554j,
            2.4286016759142925-3.079395289523383j,
            6.559515660905306-6.61643249334516j,
            -6.5300017720164165+6.619904745555312j,
            4.313312154270448-1.6527297604254776j,
            -4.291089932048226+1.6378059450141607j,
            -1.718112606719134+4.952139130885014j,
            0.7289685611777779-1.8308946338715828j,
            0.39918816181159994-1.3686674435099282j,
            5.1547133280766975-14.850728807398516j,
            -2.1858127771447613+5.489938889308774j,
            -1.196966002433583+4.103950312512208j,
            -3.4336493324686748+9.896853765321925j,
            1.4568442159669834-3.6590442982770908j,
            0.7977778406219831-2.73528291184218j,
            0.7289685611777779-1.8308946338715828j,
            -1.5044428822105846+4.692640923120229j,
            0.1895046228849712-1.0453117471021263j,
            -2.1858127771447613+5.489938889308774j,
            4.522531443410049-14.077484348000528j,
            -0.5682297537780246+3.1343680144378414j,
            1.4568442159669834-3.6590442982770908j,
            -3.0066302278661308+9.37824640257761j,
            0.3787251308930535-2.0890563101756148j,
            0.39918816181159994-1.3686674435099282j,
            0.1895046228849712-1.0453117471021263j,
            -1.3304102563362856+4.426997386700979j,
            -1.196966002433583+4.103950312512208j,
            -0.5682297537780246+3.1343680144378414j,
            4.00954865093339-13.286160338247655j,
            0.7977778406219831-2.73528291184218j,
            0.3787251308930535-2.0890563101756148j,
            -2.6588258945971046+8.847357595910653j,
            -1.1451220523783028+3.3006007307348617j,
            0.485857546024989-1.2202912734754099j,
            0.26605890984743125-0.9122168510993668j,
            -5.564622525570931+7.133818691956606j,
            1.495155595100418-1.5059091209875801j,
            2.1394799752143716-1.6901171050679111j,
            -3.4336493324686748+9.896853765321925j,
            1.4568442159669834-3.6590442982770908j,
            0.7977778406219831-2.73528291184218j,
            10.143393910417908-20.33127287144081j,
            -3.4378573570923905+6.3852446249031j,
            -3.203316725683786+5.337616800172476j,
            0.485857546024989-1.2202912734754099j,
            -1.0027111809933547+3.1276451752596324j,
            0.12630483115283336-0.6967002794435673j,
            1.495155595100418-1.5059091209875801j,
            -4.908541379197551+7.063422502477067j,
            1.0880240059003325-1.3823967084607216j,
            -4.3349628401868+3.9869660653522025j,
            1.4568442159669834-3.6590442982770908j,
            -3.0066302278661308+9.37824640257761j,
            0.3787251308930535-2.0890563101756148j,
            -3.4378573570923905+6.3852446249031j,
            13.252845628243836-23.55627977911405j,
            -3.0376940799530985+4.767758837567499j,
            1.4446401120068793-0.5996056180345513j,
            0.26605890984743125-0.9122168510993668j,
            0.12630483115283336-0.6967002794435673j,
            -0.8867184358481343+2.9505937582362023j,
            2.1394799752143716-1.6901171050679111j,
            1.0880240059003325-1.3823967084607216j,
            -5.189203684098949+7.085613396831461j,
            1.4446401120068793-0.5996056180345513j,
            0.7977778406219831-2.73528291184218j,
            0.3787251308930535-2.0890563101756148j,
            -2.6588258945971046+8.847357595910653j,
            -3.203316725683786+5.337616800172476j,
            -3.0376940799530985+4.767758837567499j,
            13.03978903174577-22.888817747097256j,
            -4.3050410172015825+4.0052533626714055j,
            -2.2902441047566056+6.601201461469723j,
            0.971715092049978-2.4405825469508198j,
            0.5321178196948625-1.8244337021987336j,
            2.2902441047566056-6.601201361509957j,
            -0.971715092049978+2.44058252553087j,
            -0.5321178196948625+1.8244336807787838j,
            0.971715092049978-2.4405825469508198j,
            -2.0054223619867093+6.255290350519265j,
            0.2526096623056667-1.3934005588871345j,
            -0.971715092049978+2.44058252553087j,
            2.0054223619867093-6.255290250559498j,
            -0.2526096623056667+1.3934005374671847j,
            0.5321178196948625-1.8244337021987336j,
            0.2526096623056667-1.3934005588871345j,
            -1.7734368716962685+5.901187516472405j,
            -0.5321178196948625+1.8244336807787838j,
            -0.2526096623056667+1.3934005374671847j,
            1.7734368716962685-5.901187416512638j,
            -3.8523736320183444+1.598948297622844j,
            2.407733520011465-0.9993426967242526j,
            -7.175068362002635+6.675422271119008j,
            1.4446401120068793-0.5996056180345513j,
            -4.3050410172015825+4.0052533626714055j,
            11.480109379204219-10.680675553822601j,
            -10000000+0j,
            -2.4286016759142925+3.079395289523383j,
            -2.428601675914292+3.079395289523384j,
            2.428601675914292-3.079395289523384j,
            -11.546745157318384+8.197439395398543j,
            2.4286016759142925-3.079395289523383j,
            10000011.546745157-8.197432541942769j,
            -7.175068362002635+6.675422271119008j,
            2.407733520011465-0.9993426967242526j,
            -4.291089932048226+1.6378059450141607j,
            11.46615829405086-8.313221446001002j,
            -2.407733520011465+0.9993426902982676j,
            2.407733520011465-0.9993426967242526j,
            -7.224938066978001+6.644943442253672j,
            -6.5300017720164165+6.619904745555312j,
            -2.407733520011465+0.9993426902982676j,
            13.754939838994417-13.264848127833126j
        ], dtype=complex), 
        np.array([
            0,  1,  2,  3,  4,  0,  1,  2,  4,  5,  0,  1,  2,  3,  5,  0,  2,
            3,  6,  0,  1,  4,  7,  1,  2,  5,  8,  3,  6,  7,  8, 31, 32, 33,
            4,  6,  7,  8, 31, 32, 33,  5,  6,  7,  8, 31, 32, 33,  9, 10, 11,
           12, 31, 32, 33,  9, 10, 11, 13, 31, 32, 33,  9, 10, 11, 14, 31, 32,
           33,  9, 12, 10, 13, 11, 14, 15, 16, 17, 22, 28, 29, 30, 34, 35, 36,
           39, 40, 15, 16, 17, 28, 29, 30, 34, 35, 36, 38, 15, 16, 17, 21, 28,
           29, 30, 34, 35, 36, 39, 40, 18, 19, 20, 32, 33, 37, 18, 19, 20, 37,
           18, 19, 20, 37, 17, 21, 22, 23, 24, 25, 38, 15, 21, 22, 23, 24, 25,
           38, 21, 22, 23, 24, 25, 38, 21, 22, 23, 24, 25, 38, 21, 22, 23, 24,
           25, 38, 26, 40, 27, 39, 15, 16, 17, 28, 29, 30, 31, 32, 33, 15, 16,
           17, 28, 29, 30, 31, 32, 33, 15, 16, 17, 28, 29, 30, 31, 32, 33,  6,
            7,  8,  9, 10, 11, 28, 29, 30, 31, 32, 33,  6,  7,  8,  9, 10, 11,
           18, 28, 29, 30, 31, 32, 33, 37,  6,  7,  8,  9, 10, 11, 18, 28, 29,
           30, 31, 32, 33, 37, 15, 16, 17, 34, 35, 36, 15, 16, 17, 34, 35, 36,
           15, 16, 17, 34, 35, 36, 18, 19, 20, 32, 33, 37, 16, 21, 22, 23, 24,
           25, 38, 15, 17, 27, 39, 40, 15, 17, 26, 39, 40], dtype=np.int32), 
        np.array([  
            0,   5,  10,  15,  19,  23,  27,  34,  41,  48,  55,  62,  69,
            71,  73,  75,  87,  97, 109, 115, 119, 123, 130, 137, 143, 149,
            155, 157, 159, 168, 177, 186, 198, 212, 226, 232, 238, 244, 250,
            257, 262, 267], dtype=np.int32)
    )
    
    expected_V = [
        0.0, 0.0, 57502.68622482564, 33189.47561163729, -10.988868660972098, -66394.86888242468, 
        -57491.697356164674, 33205.39328374589, 2401.562774320432, -0.46690091155609226, 
        -1201.2376790663666, -2079.7175126796437, -1200.3116016198273, 2080.1419403490627, 
        2536.356120228099, -0.5793286234950956, -1246.2598772664523, -2157.4877137350218, 
        -1267.5877694598496, 2196.935539327288, 2426.426283208282, -109.96557825373475, 
        -1300.0178453618112, -2096.2860825922016, -1120.4252829545615, 2128.6048961933866, 
        273.1208520924334, -15.653268696155022, -149.22087189563985, -236.28815213487727, 
        -124.73890495654813, 242.00752558006548, 2350.0787848280174, -221.0796482325268, 
        -1338.403130602016, -2109.8005657418075, -1015.4071554561624, 2083.115730276635, 
        -1295.6847720988385, -2078.36830798424, -1296.2419078314422, -2073.161856729391, 
        -1121.791131783235, 2124.3537662394715, -1015.4071496666254, 2083.115713199053, 
        2350.078762918045, -221.07964093085445, 2333.5003985622425, -229.7550420165232, 
        -1347.980749354996, -2110.413577571908, -1013.968224484203, 2078.6483630432745, 
        -1002.1266180672616, 2078.753428367296, 2332.4291296649067, -217.30934684181196, 
        2407.055227539434, -145.37221180195166, -1312.3003350597062, -2102.372937700745, 
        -1083.0006449663492, 2116.1077231577597, 2433.850246648693, -107.5228592594183, 
        -1300.761594930117, -2101.270878230695, -1123.5656240409862, 2134.1389201731336, 
        2350.078813428112, -221.07966574213293, -1338.4031538526608, -2109.8005932052947, 
        -1015.4071597837608, 2083.1157650090267, -1122.389508981748, 2129.5620039280097, 
        -1338.4031344410685, -2109.8005600677157, 2345.3898452775716, -221.5997955616163, 
        -1009.5693326805173, 2080.5326334201427
    ]
    
    expected_I = [
        45.06668904138904, 24.807535582766718, 69802.42815021734, -72191.08720768025, 
        -97420.52952591579, -24355.13240711842, 27618.10139734361, 96546.21962201368, 
        0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 
        0.0, 0.0, -13.833771377298945, 10.726871597152865, -8.968504770843197, 
        -3.417089130031627, -3.12498992294411, -18.470505046170956, -2.667048628795584,
        3.832056283537952, -0.46758569533298555, -1.9484679417918613, 3.1346343241285695,
        -1.8835883417461048, -3.31446662403701, -1.321239610087268, -7.105427357601002e-15,
        0.0, 7.105427357601002e-15, 0.0, 0.25870863043271797, -1.0385283598223651,
        -0.25870863043271797, 1.0385283598223651, -9.011574972517224, 4.59535774077078,
        -3.0888821721242508, -0.8862751281506647, -1.9603496363737634, -10.9319093354963,
        0.028161796268869943, -3.0158125881806797, 0.0, 0.0, 0.06464719014600195,
        -0.04347962137929162, -1.7990236975013012, -0.9604538679363639, -0.05795649932674607,
        -1.0830078082714039, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 
        0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0
    ]

    actual_Y_data = dss.YMatrix.getYsparse()

    np.testing.assert_array_almost_equal(
        expected_Y_data[0], actual_Y_data[0], decimal=4
    )
    assert np.all(expected_Y_data[1] == actual_Y_data[1])
    assert np.all(expected_Y_data[2] == actual_Y_data[2])

    np.testing.assert_array_almost_equal(expected_V, dss.YMatrix.getV(), decimal=4)
    np.testing.assert_array_almost_equal(expected_I, dss.YMatrix.getI(), decimal=4)


def test_wiredata_class_to_dataframe():
    commands = """Clear

    New Circuit.test_circuit

    New Wiredata.ACSR336 GMR=0.0255000 DIAM=0.7410000 RAC=0.3060000 NormAmps=530.0000 Runits=mi radunits=in gmrunits=ft
    New Wiredata.ACSR1/0 GMR=0.0044600 DIAM=0.3980000 RAC=1.120000 NormAmps=230.0000 Runits=mi radunits=in gmrunits=ft


    New Linegeometry.HC2_336_1neut_0Mess nconds=4 nphases=3
    ~ cond=1 Wire=acsr336 x=-1.2909 h=13.716 units=m
    ~ cond=2 Wire=acsr336 x=-0.1530096 h=4.1806368 units=ft
    ~ cond=3 Wire=acsr336 x=0.5737 h=13.716 units=m
    ~ cond=4 Wire= ACSR1/0 x=0 h=14.648 ! units=m ! neutral

    New Line.Line1 Bus1=bus1.1.2.3 Bus2=bus2.1.2.3
    ~ Geometry= HC2_336_1neut_0Mess
    ~ Length=300 units=ft

    Set Voltagebases=[4.8,34.5,115.0]
    Calcvoltagebases
    Solve"""

    import opendssdirect as dss

    dss.run_command(commands)
    is_pandas_installed = dss.utils.is_pandas_installed
    dss.utils.is_pandas_installed = False
    data = dss.utils.class_to_dataframe("wiredata")
    dss.utils.is_pandas_installed = is_pandas_installed

    assert data == {
        "wiredata.acsr1/0": {
            "Capradius": "0.199",
            "Seasons": "1",
            "Ratings": ["-1"],
            "GMRac": "0.00446",
            "GMRunits": "ft",
            "Rac": "1.12",
            "Rdc": "1.09803921568627",
            "Runits": "mi",
            "diam": "0.398",
            "emergamps": "345",
            "like": "",
            "normamps": "230",
            "radius": "0.199",
            "radunits": "in",
        },
        "wiredata.acsr336": {
            "Capradius": "0.3705",
            "Seasons": "1",
            "Ratings": ["-1"],
            "GMRac": "0.0255",
            "GMRunits": "ft",
            "Rac": "0.306",
            "Rdc": "0.3",
            "Runits": "mi",
            "diam": "0.741",
            "emergamps": "795",
            "like": "",
            "normamps": "530",
            "radius": "0.3705",
            "radunits": "in",
        },
    }


def test_long_path():

    import opendssdirect as dss
    import tempfile, shutil
    import warnings

    long_name = "-".join(["40242748-21fd-4a61-8ad9-cefdd3ff6a05"] * 6)
    original_working_dir = os.getcwd()
    try:
        # TODO: use tempfile.TemporaryDirectory when Python 2.7 is dropped
        tmp_dir_path = tempfile.mkdtemp()
        inner_dir_path = os.path.join(tmp_dir_path, long_name)
        os.mkdir(inner_dir_path)
        long_file_path = os.path.join(inner_dir_path, long_name + ".dss")

        with open(long_file_path, "w") as f:
            f.write("clear\nnew circuit.test\n")

        # Try running with the full path
        dss.run_command("redirect '{}'".format(long_file_path))

        # Then try going to the folder and using only the filename
        os.chdir(inner_dir_path)
        dss.run_command("redirect '{}'".format(long_name + ".dss"))
    except (IOError, OSError):  # FileNotFoundError:
        warnings.warn(
            "Could not create a file with a long path in Python. Skipping test."
        )
    finally:
        os.chdir(original_working_dir)
        if os.path.exists(tmp_dir_path):
            shutil.rmtree(tmp_dir_path)


def test_dss_extensions_debug():
    import opendssdirect
    import dss

    # Check if the loaded version is correct
    expects_debug = os.environ.get("DSS_EXTENSIONS_DEBUG") == "1"
    if expects_debug:
        assert "DEBUG" in opendssdirect.Basic.Version()
    else:
        assert "DEBUG" not in opendssdirect.Basic.Version()


def test_exception_control(dss):
    # Default behavior
    assert dss.Error.UseExceptions()
    with pt.raises(dss.DSSException):
        dss.Text.Command('this_is_an_invalid_command1')

    # Behavior without exceptions
    dss.Error.UseExceptions(False)
    assert not dss.Error.UseExceptions()
    dss.Text.Command('this_is_an_invalid_command2')
    # There should be an error code waiting for us...
    assert dss.Error.Number() != 0
    # ...but it should be gone after we read it
    assert dss.Error.Number() == 0


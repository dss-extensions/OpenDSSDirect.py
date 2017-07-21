import os

def test_import():

    import opendssdirect


def test_ActiveClass():

    import opendssdirect as dss

    assert dss.dss_lib.DSSPut_Command('Redirect {}'.format(os.path.abspath(os.path.join('.', './data/13Bus/IEEE13Nodeckt.dss'))).encode('utf-8')) == b"", "Unable to find test data"

    assert dss.ActiveClass.ActiveClassName() == u'Line'
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
    assert dss.ActiveClass.Name() == u'650632'
    assert dss.ActiveClass.Next() == 2
    assert dss.ActiveClass.Next() == 3
    assert dss.ActiveClass.Name(u'650632') == u'0'
    assert dss.ActiveClass.Name() == u'650632'
    assert dss.ActiveClass.NumElements() == 12


def test_configuration():

    import opendssdirect as dss

    assert dss.Basic.AllowForms() == 1, "Allow forms should be disabled"


def test_13Node():

    import opendssdirect as dss

    assert dss.dss_lib.DSSPut_Command('Redirect {}'.format(os.path.abspath(os.path.join('.', './data/13Bus/IEEE13Nodeckt.dss'))).encode('ascii')) == b"", "Unable to find test data"

    assert dss.ActiveClass.ActiveClassName() == u'Line'
    assert dss.ActiveClass.AllNames() == [u'650632', u'632670', u'670671', u'671680', u'632633', u'632645', u'645646', u'692675', u'671684', u'684611', u'684652', u'671692']
    assert dss.ActiveClass.Count() == 12
    assert dss.ActiveClass.First() == 1
    assert dss.ActiveClass.Name() == u'650632'
    assert dss.ActiveClass.Next() == 2
    assert dss.ActiveClass.NumElements() == 12

def test_13Node_Basic():

    import opendssdirect as dss

    assert dss.dss_lib.DSSPut_Command('Redirect {}'.format(os.path.abspath(os.path.join('.', './data/13Bus/IEEE13Nodeckt.dss'))).encode('ascii')) == b"", "Unable to find test data"

    assert dss.Basic.AllowForms() == 1
    assert dss.Basic.Classes() == [u'Solution', u'LineCode', u'LoadShape', u'TShape', u'PriceShape', u'XYcurve', u'GrowthShape', u'TCC_Curve', u'Spectrum', u'WireData', u'CNData', u'TSData', u'LineGeometry', u'LineSpacing', u'XfmrCode', u'Line', u'Vsource', u'Isource', u'VCCS', u'Load', u'Transformer', u'RegControl', u'Capacitor', u'Reactor', u'CapControl', u'Fault', u'Generator', u'GenDispatcher', u'Storage', u'StorageController', u'Relay', u'Recloser', u'Fuse', u'SwtControl', u'PVSystem', u'UPFC', u'UPFCControl', u'InvControl', u'ExpControl', u'GICLine', u'GICTransformer', u'VSConverter', u'Monitor', u'EnergyMeter', u'Sensor']
    assert dss.Basic.ClearAll() == 0
    assert os.path.abspath(dss.Basic.DataPath()) == os.path.abspath('.')
    # assert dss.Basic.DefaultEditor() == u'open -t'
    assert dss.Basic.NewCircuit() == u'New Circuit'
    assert dss.Basic.NumCircuits() == 1
    assert dss.Basic.NumClasses() == 45
    assert dss.Basic.NumUserClasses() == 0
    assert dss.Basic.Reset() == 0
    assert dss.Basic.ShowPanel() == -1
    assert dss.Basic.Start() == 1
    assert dss.Basic.UserClasses() == []
    assert dss.Basic.Version() == u'Version Unknown. (64-bit build); License Status: Open '

def test_13Node_Bus():

    import opendssdirect as dss

    assert dss.dss_lib.DSSPut_Command('Redirect {}'.format(os.path.abspath(os.path.join('.', './data/13Bus/IEEE13Nodeckt.dss'))).encode('ascii')) == b"", "Unable to find test data"

    assert dss.Bus.Coorddefined() == 1
    assert dss.Bus.CplxSeqVoltages() == [7.275957614183426e-12, 4.31951048085466e-06, 57503.46213437529, 33187.98898326319, -0.7758574371237046, 1.4866859858011594]
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
    assert dss.Bus.PuVoltage() == [0.866065862637831, 0.4998770273321037, -0.0001655104421677343, -0.9999937910431469, -0.8659003521956633, 0.5001167639062155]
    assert dss.Bus.SectionID() == 0
    assert dss.Bus.SeqVoltages() == [4.3195104808607886e-06, 66393.45427218509, 1.6769585514012348]
    assert dss.Bus.TotalMiles() == 0.0
    assert dss.Bus.VLL() == [57513.67538924719, 99584.34438494075, 57480.70805232015, -99600.26176213453, -114994.38344156733, 15.917377193771244]
    assert dss.Bus.VMagAngle() == [66393.52547161786, 29.992738890948125, 66394.86962078432, -90.00948310376482, 66391.9676657127, 149.99062328146098]
    assert dss.Bus.Voc() == [0.0, 0.0, 0.0, 0.0, 0.0, 0.0]
    assert dss.Bus.Voltages() == [57502.68627693818, 33189.4756735685, -10.98911230901207, -66394.86871137226, -57491.697164629164, 33205.39305076227]
    assert dss.Bus.X() == 200.0
    assert dss.Bus.Y() == 400.0
    assert dss.Bus.YscMatrix() == [0.0]
    assert dss.Bus.Zsc0() == [0.0, 0.0]
    assert dss.Bus.Zsc1() == [0.0, 0.0]
    assert dss.Bus.ZscMatrix() == [0.0]
    assert dss.Bus.ZscRefresh() == 1
    assert dss.Bus.kVBase() == 66.39528095680697
    assert dss.Bus.puVLL() == [1.693378168100472e-11, -4.667955969702419e-11, -1.395316990173399e-06, -5.577283842337346e-06, 1.3953000563917182e-06, 5.577330521897042e-06]
    assert dss.Bus.puVmagAngle() == [5.239275814449394e-07, -79.42845561076332, 5.238427215809797e-07, -79.4299867740603, 9.484135993651139e-06, 74.63582918382964]

def test_13Node_Circuit():

    import opendssdirect as dss

    assert dss.dss_lib.DSSPut_Command('Redirect {}'.format(os.path.abspath(os.path.join('.', './data/13Bus/IEEE13Nodeckt.dss'))).encode('ascii')) == b"", "Unable to find test data"

    assert dss.Circuit.AllBusDistances() == [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0]
    assert dss.Circuit.AllBusMagPu() == [0.9999735600909612, 0.9999938047400851, 0.9999500974911693, 0.9999107734075059, 0.9999708382014062, 0.9999310912254219, 1.0560331208541838, 1.0373856699381676, 1.0560496734277571, 1.011300431272264, 1.0270174666164649, 1.0015359172418576, 0.9871584562161683, 1.0084198145936507, 0.9824418963411172, 0.9827959271001375, 1.0402765227909403, 0.964869605360475, 1.019729240260045, 1.0022697678941448, 1.0180132408663718, 1.0002355078501333, 0.9648695979124887, 0.9827959177333715, 1.040276521652259, 0.9762713001854915, 1.0426333240830927, 0.9629347471054315, 0.9608229488014672, 0.9753328230988354, 1.004024331469046, 1.0318708269152446, 0.9897380852516064, 1.0143428459400463, 1.0289449404033275, 1.0041840427671582, 0.9827959396392048, 1.0402765376331038, 0.9648696191496499, 0.9808725592235161, 0.9628392247223574]
    assert dss.Circuit.AllBusNames() == [u'sourcebus', u'650', u'rg60', u'633', u'634', u'671', u'645', u'646', u'692', u'675', u'611', u'652', u'670', u'632', u'680', u'684']
    assert dss.Circuit.AllBusVMag() == [0.9999735600909612, 0.9999938047400851, 0.9999500974911693, 0.9999107734075059, 0.9999708382014062, 0.9999310912254219, 1.0560331208541838, 1.0373856699381676, 1.0560496734277571, 1.011300431272264, 1.0270174666164649, 1.0015359172418576, 0.9871584562161683, 1.0084198145936507, 0.9824418963411172, 0.9827959271001375, 1.0402765227909403, 0.964869605360475, 1.019729240260045, 1.0022697678941448, 1.0180132408663718, 1.0002355078501333, 0.9648695979124887, 0.9827959177333715, 1.040276521652259, 0.9762713001854915, 1.0426333240830927, 0.9629347471054315, 0.9608229488014672, 0.9753328230988354, 1.004024331469046, 1.0318708269152446, 0.9897380852516064, 1.0143428459400463, 1.0289449404033275, 1.0041840427671582, 0.9827959396392048, 1.0402765376331038, 0.9648696191496499, 0.9808725592235161, 0.9628392247223574]
    assert dss.Circuit.AllBusVolts() == [57502.68627693818, 33189.4756735685, -10.98911230901207, -66394.86871137226, -57491.697164629164, 33205.39305076227, 2401.562772055762, -0.4668925451039482, -1201.2376854909323, -2079.7175095625, -1200.3115874754303, 2080.141929910249, 2536.3561212894438, -0.5793172973319122, -1246.2598833517864, -2157.4877090219084, -1267.587749407154, 2196.935519634186, 2426.4276379311646, -109.96690599537264, -1300.0162579690939, -2096.283396703043, -1120.4139031363902, 2128.6003868309604, 273.12117506928445, -15.653348732054143, -149.22067946929405, -236.2877841616899, -124.73744800718065, 242.00686102787685, 2350.0805301839578, -221.08294871607683, -1338.4006550620513, -2109.7980124414166, -1015.3876288957937, 2083.1079654828877, -1295.6831435171484, -2078.3650896480167, -1122.3784857728665, 2129.5577123236694, -1296.2402814635552, -2073.1585039035635, -1121.7801053097155, 2124.3493400045577, -1015.3876231065364, 2083.107948404428, 2350.080508274622, -221.08294141465848, -1338.400658901049, -2109.798006767321, 2333.5022250500942, -229.75875811896063, -1347.9783594336611, -2110.41134996152, -1013.9483472387761, 2078.6396489285494, -1002.1065310288469, 2078.745142088486, 2332.4304274000037, -217.31255727308186, 2407.056725017637, -145.37420380313188, -1312.2984849124346, -2102.3703908080543, -1082.9865109797865, 2116.1022239294853, 2433.8514624314753, -107.52417704907307, -1300.7601876895642, -2101.268404324189, -1123.5546141566904, 2134.134702369962, 2350.0805587856653, -221.08296622672697, -1338.4006783138987, -2109.7980399064168, -1015.3876332233444, 2083.108000216942, 2345.391500510206, -221.60314314042807, -1009.5495489075352, 2080.524597665617]
    assert dss.Circuit.AllElementLosses() == [-3567.2317221830845, -1736.6105734708244, 0.03228838509740308, 0.26247332685953007, 0.12209068980929441, 0.12385511858400423, 0.0, 0.0, 0.06534666416840627, 0.06707862443476915, 0.0, 0.0, 0.13509748949622735, 0.13686198239726946, 0.0, 0.0, 5.5526721532734085, 10.096270647399884, 1155.0168946622257, 660.0436384952801, 159.99892650617605, 110.00542923577791, 120.00015747507646, 89.99764493365784, 120.00492260783774, 90.00952390501756, 170.00027419023695, 124.99693537687827, 234.56562985851542, 134.6270475273679, 166.6736550753605, 148.05222349379017, 484.99675064222447, 190.0228608055384, 68.00032507676042, 59.997846126968334, 290.01666583912, 212.03346194114658, 163.45696048067904, 76.93101512773492, 121.93923493761854, 81.93523562163435, 16.999798182421245, 10.000536316150352, 66.00002389593134, 37.998647503238885, 117.00497287474145, 68.00811702391309, -1.4551915228366852e-14, -593.4866454474861, 0.0, -92.45484141123522, 60.738506098096956, 196.01888910912663, 12.990842590497573, 41.49525104173738, 22.7289781935591, 72.33498233978072, 7.693588522863128e-12, -0.004169224402815679, 0.8244852537013503, 1.0561387185878994, 2.7673862000581577, 2.4007964145294536, 0.5274843376703211, 0.4197453440363606, 4.162853304240387, 2.4192732671323176, 0.5795023244819895, 0.470693780053145, 0.3824189497624757, 0.38736389633078216, 0.7998310440541245, 0.23088042051736557, 9.05452249571681e-06, -1.4551915228366852e-14]
    assert dss.Circuit.AllElementNames() == [u'Vsource.source', u'Transformer.sub', u'Transformer.reg1', u'RegControl.reg1', u'Transformer.reg2', u'RegControl.reg2', u'Transformer.reg3', u'RegControl.reg3', u'Transformer.xfm1', u'Load.671', u'Load.634a', u'Load.634b', u'Load.634c', u'Load.645', u'Load.646', u'Load.692', u'Load.675a', u'Load.675b', u'Load.675c', u'Load.611', u'Load.652', u'Load.670a', u'Load.670b', u'Load.670c', u'Capacitor.cap1', u'Capacitor.cap2', u'Line.650632', u'Line.632670', u'Line.670671', u'Line.671680', u'Line.632633', u'Line.632645', u'Line.645646', u'Line.692675', u'Line.671684', u'Line.684611', u'Line.684652', u'Line.671692']
    assert dss.Circuit.AllNodeDistances() == [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0]
    assert dss.Circuit.AllNodeNames() == [u'sourcebus.1', u'sourcebus.2', u'sourcebus.3', u'650.1', u'650.2', u'650.3', u'rg60.1', u'rg60.2', u'rg60.3', u'633.1', u'633.2', u'633.3', u'634.1', u'634.2', u'634.3', u'671.1', u'671.2', u'671.3', u'645.2', u'645.3', u'646.2', u'646.3', u'692.3', u'692.1', u'692.2', u'675.1', u'675.2', u'675.3', u'611.3', u'652.1', u'670.1', u'670.2', u'670.3', u'632.1', u'632.2', u'632.3', u'680.1', u'680.2', u'680.3', u'684.1', u'684.3']
    assert dss.Circuit.Capacity() == 0.0
    assert dss.Circuit.Disable() == u''
    assert dss.Circuit.Enable() == u''
    assert dss.Circuit.EndOfTimeStepUpdate() == 0
    assert dss.Circuit.FirstElement() == 1
    assert dss.Circuit.FirstPCElement() == 1
    assert dss.Circuit.FirstPDElement() == 1
    assert dss.Circuit.LineLosses() == [106.50229735065263, 317.2298451074293]
    assert dss.Circuit.Losses() == [112409.79273249737, 327916.3848071047]
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
    assert dss.Circuit.TotalPower() == [-3567.2317221830845, -1736.6105734708244]
    assert dss.Circuit.UpdateStorage() == 0
    assert dss.Circuit.YCurrents() == [69802.42815021457, -72191.08720767738, -97420.52952591189, -24355.132407117453, 27618.101397342507, 96546.21962200984, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, -13.819481227119581, 10.715709888633683, -8.9625106416662, -3.414850873765033, -3.1289140707121987, -18.49184953395263, -2.667902859232754, 3.8347722723473936, -0.4672472800431251, -1.9471898670746128, 3.135150139275879, -1.8875824052727808, -3.3135886635147926, -1.3209068014917555, 7.105427357601002e-15, 1.4210854715202004e-14, -7.105427357601002e-15, -1.4210854715202004e-14, 0.2588941552615527, -1.0392702554685158, -0.2588941552615527, 1.0392702554685158, -9.005000094089581, 4.591965873291912, -3.088362344352049, -0.8861563878518304, -1.9622176477142474, -10.940625499462755, 0.028098534526863506, -3.017966109087453, 0.0, 0.0, 0.06480217600793559, -0.0435836257331399, -1.7986925506572469, -0.9602909725739117, -0.05809415121825623, -1.0852001390951926, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0]
    assert dss.Circuit.YNodeOrder() == [u'SOURCEBUS.1', u'SOURCEBUS.2', u'SOURCEBUS.3', u'650.1', u'650.2', u'650.3', u'RG60.1', u'RG60.2', u'RG60.3', u'633.1', u'633.2', u'633.3', u'634.1', u'634.2', u'634.3', u'671.1', u'671.2', u'671.3', u'645.2', u'646.2', u'646.3', u'692.3', u'692.1', u'675.1', u'675.2', u'675.3', u'611.3', u'652.1', u'670.1', u'670.2', u'670.3', u'632.1', u'632.2', u'632.3', u'680.1', u'680.2', u'680.3', u'645.3', u'692.2', u'684.1', u'684.3']
    assert dss.Circuit.YNodeVArray() == [57502.68627693818, 33189.4756735685, -10.98911230901207, -66394.86871137226, -57491.697164629164, 33205.39305076227, 2401.562772055762, -0.4668925451039482, -1201.2376854909323, -2079.7175095625, -1200.3115874754303, 2080.141929910249, 2536.3561212894438, -0.5793172973319122, -1246.2598833517864, -2157.4877090219084, -1267.587749407154, 2196.935519634186, 2426.4276379311646, -109.96690599537264, -1300.0162579690939, -2096.283396703043, -1120.4139031363902, 2128.6003868309604, 273.12117506928445, -15.653348732054143, -149.22067946929405, -236.2877841616899, -124.73744800718065, 242.00686102787685, 2350.0805301839578, -221.08294871607683, -1338.4006550620513, -2109.7980124414166, -1015.3876288957937, 2083.1079654828877, -1295.6831435171484, -2078.3650896480167, -1296.2402814635552, -2073.1585039035635, -1121.7801053097155, 2124.3493400045577, -1015.3876231065364, 2083.107948404428, 2350.080508274622, -221.08294141465848, 2333.5022250500942, -229.75875811896063, -1347.9783594336611, -2110.41134996152, -1013.9483472387761, 2078.6396489285494, -1002.1065310288469, 2078.745142088486, 2332.4304274000037, -217.31255727308186, 2407.056725017637, -145.37420380313188, -1312.2984849124346, -2102.3703908080543, -1082.9865109797865, 2116.1022239294853, 2433.8514624314753, -107.52417704907307, -1300.7601876895642, -2101.268404324189, -1123.5546141566904, 2134.134702369962, 2350.0805587856653, -221.08296622672697, -1338.4006783138987, -2109.7980399064168, -1015.3876332233444, 2083.108000216942, -1122.3784857728665, 2129.5577123236694, -1338.400658901049, -2109.798006767321, 2345.391500510206, -221.60314314042807, -1009.5495489075352, 2080.524597665617]

def test_13Node_CktElement():

    import opendssdirect as dss

    assert dss.dss_lib.DSSPut_Command('Redirect {}'.format(os.path.abspath(os.path.join('.', './data/13Bus/IEEE13Nodeckt.dss'))).encode('ascii')) == b"", "Unable to find test data"

    assert dss.CktElement.AllPropertyNames() == [u'bus1', u'bus2', u'linecode', u'length', u'phases', u'r1', u'x1', u'r0', u'x0', u'C1', u'C0', u'rmatrix', u'xmatrix', u'cmatrix', u'Switch', u'Rg', u'Xg', u'rho', u'geometry', u'units', u'spacing', u'wires', u'EarthModel', u'cncables', u'tscables', u'B1', u'B0', u'normamps', u'emergamps', u'faultrate', u'pctperm', u'repair', u'basefreq', u'enabled', u'like']
    assert dss.CktElement.AllVariableNames() == []
    assert dss.CktElement.AllVariableValues() == [0.0]
    assert dss.CktElement.BusNames() == [u'671', u'692']
    assert dss.CktElement.Close() == 0
    assert dss.CktElement.CplxSeqCurrents() == [66.53025245666505, 13.676485538482666, 141.9625213874072, -15.550956740585985, 10.600583242109401, -71.13971231916744, -66.53025245666505, -13.676485538482666, -141.9625213874072, 15.550956740585985, -10.600583242109401, 71.13971231916744]
    assert dss.CktElement.CplxSeqVoltages() == [-1.2359179246288363, -82.59099855820193, 2386.0459226713465, -162.491803967821, -34.72947456275983, 23.999853809946103, -1.2359245776542025, -82.5909999258505, 2386.045908475094, -162.49180241272535, -34.7294756228182, 23.999860923917254]
    assert dss.CktElement.Currents() == [219.09335708618164, -73.01418352127075, 38.38997459411621, -56.7409553527832, -57.892574310302734, 170.78459548950195, -219.09335708618164, 73.01418352127075, -38.38997459411621, 56.7409553527832, 57.892574310302734, -170.78459548950195]
    assert dss.CktElement.CurrentsMagAng() == [230.9393212828229, -18.430962758395474, 68.50785475902325, -55.918380174918454, 180.33005355954046, 108.72563470506053, 230.9393212828229, 161.56903723193298, 68.50785475902325, 124.08161981541, 180.33005355954046, -71.27436528526792]
    assert dss.CktElement.DisplayName() == u'Line_671692'
    assert dss.CktElement.EmergAmps() == 600.0
    assert dss.CktElement.Enabled() == 1
    assert dss.CktElement.EnergyMeter() == u''
    from six import string_types
    assert isinstance(dss.CktElement.GUID(), string_types)
    assert dss.CktElement.HasSwitchControl() == 0
    assert dss.CktElement.HasVoltControl() == 0
    assert dss.CktElement.IsOpen() == 0
    assert dss.CktElement.Losses() == [0.00905452249571681, -1.4551915228366852e-11]
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
    assert dss.CktElement.PhaseLosses() == [5.3332970710471275e-06, 1.4551915228366852e-14, 4.693326191045344e-07, 0.0, 3.2518928055651486e-06, -2.9103830456733704e-14]
    assert dss.CktElement.Powers() == [531.0292237718563, 123.15140569189936, 68.33078768274852, -156.93722390935451, 414.5461550055662, 52.81608277791104, -531.0292184385592, -123.15140569189934, -68.3307872134159, 156.93722390935451, -414.54615175367337, -52.81608277791107]
    assert dss.CktElement.Residuals() == [203.7642921065592, 11.61634976990784, 203.7642921065592, -168.3836502204206]
    assert dss.CktElement.SeqCurrents() == [67.92143070218641, 142.81172827963962, 71.92517663465829, 67.92143070218641, 142.81172827963962, 71.92517663465829]
    assert dss.CktElement.SeqPowers() == [-3.635341586794097, -16.43369091330689, 1023.7679950283105, 42.112652185360545, -6.2264861453966915, -6.648697143839365, 3.635342970790345, 16.433690913306886, -1023.7679889097534, -42.112652185360524, 6.226487697365985, 6.648697143839375]
    assert dss.CktElement.SeqVoltages() == [82.60024537467991, 2391.5724390980245, 42.215274324634755, 82.6002468417225, 2391.5724248289184, 42.21527924109106]
    assert dss.CktElement.Variablei() == 0.0
    assert dss.CktElement.Voltages() == [2350.0805301839578, -221.08294871607683, -1338.4006550620513, -2109.7980124414166, -1015.3876288957937, 2083.1079654828877, 2350.080508274622, -221.08294141465848, -1338.400658901049, -2109.798006767321, -1015.3876231065364, 2083.107948404428]
    assert dss.CktElement.VoltagesMagAng() == [2360.456771170086, -5.374262178524929, 2498.5123507343887, -122.3899728004033, 2317.4017417730743, 115.98639992871324, 2360.4567486732017, -5.3742620518852195, 2498.5123479995295, -122.3899729444441, 2317.4017238846714, 115.98639998506223]
    assert dss.CktElement.YPrim() == [10000000.0, 0.0, 0.0, 0.0, 0.0, 0.0, -10000000.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 10000000.0, 0.0, 0.0, 0.0, 0.0, 0.0, -10000000.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 10000000.0, 0.0, 0.0, 0.0, 0.0, 0.0, -10000000.0, 0.0, -10000000.0, 0.0, 0.0, 0.0, 0.0, 0.0, 10000000.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, -10000000.0, 0.0, 0.0, 0.0, 0.0, 0.0, 10000000.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, -10000000.0, 0.0, 0.0, 0.0, 0.0, 0.0, 10000000.0, 0.0]

def test_13Node_Capacitors():

    import opendssdirect as dss

    assert dss.dss_lib.DSSPut_Command('Redirect {}'.format(os.path.abspath(os.path.join('.', './data/13Bus/IEEE13Nodeckt.dss'))).encode('ascii')) == b"", "Unable to find test data"

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

def test_13Node_CapControls():

    import opendssdirect as dss

    assert dss.dss_lib.DSSPut_Command('Redirect {}'.format(os.path.abspath(os.path.join('.', './data/13Bus/IEEE13Nodeckt.dss'))).encode('ascii')) == b"", "Unable to find test data"

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

def test_13Node_Element():

    import opendssdirect as dss

    assert dss.dss_lib.DSSPut_Command('Redirect {}'.format(os.path.abspath(os.path.join('.', './data/13Bus/IEEE13Nodeckt.dss'))).encode('ascii')) == b"", "Unable to find test data"

    assert dss.Element.AllPropertyNames() == [u'bus1', u'bus2', u'linecode', u'length', u'phases', u'r1', u'x1', u'r0', u'x0', u'C1', u'C0', u'rmatrix', u'xmatrix', u'cmatrix', u'Switch', u'Rg', u'Xg', u'rho', u'geometry', u'units', u'spacing', u'wires', u'EarthModel', u'cncables', u'tscables', u'B1', u'B0', u'normamps', u'emergamps', u'faultrate', u'pctperm', u'repair', u'basefreq', u'enabled', u'like']
    assert dss.Element.Name() == u'Line.671692'
    assert dss.Element.NumProperties () == 35

def test_13Node_Executive():

    import opendssdirect as dss

    assert dss.dss_lib.DSSPut_Command('Redirect {}'.format(os.path.abspath(os.path.join('.', './data/13Bus/IEEE13Nodeckt.dss'))).encode('ascii')) == b"", "Unable to find test data"

    assert dss.Executive.Command() == u'New'
    assert dss.Executive.CommandHelp() == u'Create a new object within the DSS. Object becomes the active object\r\nExample: New Line.line1 ...'
    assert dss.Executive.NumCommands() == 104
    assert dss.Executive.NumOptions() == 108
    assert dss.Executive.Option() == u'type'
    assert dss.Executive.OptionHelp() == u'Sets the active DSS class type.  Same as Class=...'
    assert dss.Executive.OptionValue() == u'Line'

def test_13Node_Fuses():

    import opendssdirect as dss

    assert dss.dss_lib.DSSPut_Command('Redirect {}'.format(os.path.abspath(os.path.join('.', './data/13Bus/IEEE13Nodeckt.dss'))).encode('ascii')) == b"", "Unable to find test data"

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

def test_13Node_Generators():

    import opendssdirect as dss

    assert dss.dss_lib.DSSPut_Command('Redirect {}'.format(os.path.abspath(os.path.join('.', './data/13Bus/IEEE13Nodeckt.dss'))).encode('ascii')) == b"", "Unable to find test data"

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
    assert dss.Generators.RegisterNames() == [u'kWh', u'kvarh', u'Max kW', u'Max kVA', u'Hours', u'$']
    assert dss.Generators.RegisterValues() == [0.0]
    assert dss.Generators.Vmaxpu() == -1.0
    assert dss.Generators.Vminpu() == -1.0
    assert dss.Generators.kV() == -1.0
    assert dss.Generators.kVARated() == -1.0
    assert dss.Generators.kW() == 0.0
    assert dss.Generators.kvar() == 0.0

def test_13Node_Isource():

    import opendssdirect as dss

    assert dss.dss_lib.DSSPut_Command('Redirect {}'.format(os.path.abspath(os.path.join('.', './data/13Bus/IEEE13Nodeckt.dss'))).encode('ascii')) == b"", "Unable to find test data"

    assert dss.Isource.AllNames() == []
    assert dss.Isource.Amps() == 0.0
    assert dss.Isource.AngleDeg() == 0.0
    assert dss.Isource.Count() == 0
    assert dss.Isource.First() == 0
    assert dss.Isource.Frequency() == 0.0
    assert dss.Isource.Name() == u'671692'
    assert dss.Isource.Next() == 0

def test_13Node_Lines():

    import opendssdirect as dss

    assert dss.dss_lib.DSSPut_Command('Redirect {}'.format(os.path.abspath(os.path.join('.', './data/13Bus/IEEE13Nodeckt.dss'))).encode('ascii')) == b"", "Unable to find test data"

    assert dss.Lines.AllNames() == [u'650632', u'632670', u'670671', u'671680', u'632633', u'632645', u'645646', u'692675', u'671684', u'684611', u'684652', u'671692']
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
    assert dss.Lines.RMatrix() == [0.3465, 0.156, 0.158, 0.156, 0.3375, 0.1535, 0.158, 0.1535, 0.3414]
    assert dss.Lines.Rg() == 0.01805
    assert dss.Lines.Rho() == 100.0
    assert dss.Lines.Spacing() == u''
    assert dss.Lines.Units() == 5
    assert dss.Lines.X0() == 0.4047
    assert dss.Lines.X1() == 0.1206
    assert dss.Lines.XMatrix() == [1.0179, 0.5017, 0.4236, 0.5017, 1.0478, 0.3849, 0.4236, 0.3849, 1.0348]
    assert dss.Lines.Xg() == 0.155081
    assert dss.Lines.Yprim() == [3.4335554553543783, -9.8965831153747, -1.4568043853617796, 3.658944244501999, -0.7977560291105917, 2.7352081140105042, -3.4335554553543783, 9.896583182049687, 1.4568043853617796, -3.6589442587894965, 0.7977560291105917, -2.7352081282980016, -1.4568043853617796, 3.658944244501999, 3.006548025596122, -9.377989931528099, -0.3787147764220645, 2.0889991803940724, 1.4568043853617796, -3.6589442587894965, -3.006548025596122, 9.377989998203086, 0.3787147764220645, -2.08899919468157, -0.7977560291105917, 2.7352081140105042, -0.3787147764220645, 2.0889991803940724, 2.658753201413196, -8.847115639537611, 0.7977560291105917, -2.7352081282980016, 0.3787147764220645, -2.08899919468157, -2.658753201413196, 8.847115706212598, -3.4335554553543783, 9.896583182049687, 1.4568043853617796, -3.6589442587894965, 0.7977560291105917, -2.7352081282980016, 3.4335554553543783, -9.8965831153747, -1.4568043853617796, 3.658944244501999, -0.7977560291105917, 2.7352081140105042, 1.4568043853617796, -3.6589442587894965, -3.006548025596122, 9.377989998203086, 0.3787147764220645, -2.08899919468157, -1.4568043853617796, 3.658944244501999, 3.006548025596122, -9.377989931528099, -0.3787147764220645, 2.0889991803940724, 0.7977560291105917, -2.7352081282980016, 0.3787147764220645, -2.08899919468157, -2.658753201413196, 8.847115706212598, -0.7977560291105917, 2.7352081140105042, -0.3787147764220645, 2.0889991803940724, 2.658753201413196, -8.847115639537611]

def test_13Node_Loads():

    import opendssdirect as dss

    assert dss.dss_lib.DSSPut_Command('Redirect {}'.format(os.path.abspath(os.path.join('.', './data/13Bus/IEEE13Nodeckt.dss'))).encode('ascii')) == b"", "Unable to find test data"

    assert dss.Loads.AllNames() == [u'671', u'634a', u'634b', u'634c', u'645', u'646', u'692', u'675a', u'675b', u'675c', u'611', u'652', u'670a', u'670b', u'670c']
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

def test_13Node_LoadShape():

    import opendssdirect as dss

    assert dss.dss_lib.DSSPut_Command('Redirect {}'.format(os.path.abspath(os.path.join('.', './data/13Bus/IEEE13Nodeckt.dss'))).encode('ascii')) == b"", "Unable to find test data"

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
    assert dss.LoadShape.PMult() == [0.677, 0.6256, 0.6087, 0.5833, 0.58028, 0.6025, 0.657, 0.7477, 0.832, 0.88, 0.94, 0.989, 0.985, 0.98, 0.9898, 0.999, 1.0, 0.958, 0.936, 0.913, 0.876, 0.876, 0.828, 0.756]
    assert dss.LoadShape.QBase() == 0.0
    assert dss.LoadShape.QMult() == [0.0]
    assert dss.LoadShape.SInterval() == 3600.0
    assert dss.LoadShape.TimeArray() == [0.0]
    assert dss.LoadShape.UseActual() == 0

def test_13Node_Meters():

    import opendssdirect as dss

    assert dss.dss_lib.DSSPut_Command('Redirect {}'.format(os.path.abspath(os.path.join('.', './data/13Bus/IEEE13Nodeckt.dss'))).encode('ascii')) == b"", "Unable to find test data"

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
    assert dss.Meters.Totals() == [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0]

def test_13Node_Monitors():

    import opendssdirect as dss

    assert dss.dss_lib.DSSPut_Command('Redirect {}'.format(os.path.abspath(os.path.join('.', './data/13Bus/IEEE13Nodeckt.dss'))).encode('ascii')) == b"", "Unable to find test data"

    assert dss.Monitors.AllNames() == []
    assert dss.Monitors.ByteStream() == []
    assert dss.Monitors.Count() == 0
    assert dss.Monitors.Element() == u'0'
    assert dss.Monitors.FileName() == u''
    assert isinstance(dss.Monitors.FileVersion(), int)
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

def test_13Node_PDElements():

    import opendssdirect as dss

    assert dss.dss_lib.DSSPut_Command('Redirect {}'.format(os.path.abspath(os.path.join('.', './data/13Bus/IEEE13Nodeckt.dss'))).encode('ascii')) == b"", "Unable to find test data"

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

def test_13Node_Properties():

    import opendssdirect as dss

    assert dss.dss_lib.DSSPut_Command('Redirect {}'.format(os.path.abspath(os.path.join('.', './data/13Bus/IEEE13Nodeckt.dss'))).encode('ascii')) == b"", "Unable to find test data"

    # Does not work on Linux

    # assert dss.Properties.Description() == u'Name of bus to which first terminal is connected.\r\nExample:\r\nbus1=busname   (assumes all terminals connected in normal phase order)\r\nbus1=busname.3.1.2.0 (specify terminal to node connections explicitly)'
    # assert dss.Properties.Name() == u'bus1'

def test_13Node_PVsystems():

    import opendssdirect as dss

    assert dss.dss_lib.DSSPut_Command('Redirect {}'.format(os.path.abspath(os.path.join('.', './data/13Bus/IEEE13Nodeckt.dss'))).encode('ascii')) == b"", "Unable to find test data"

    assert dss.PVsystems.Count() == 0
    assert dss.PVsystems.First() == 0
    assert dss.PVsystems.Idx() == 0
    assert dss.PVsystems.Irradiance() == -1.0
    assert dss.PVsystems.Next() == 0
    assert dss.PVsystems.kVARated() == -1.0
    assert dss.PVsystems.kW() == 0.0
    assert dss.PVsystems.kvar() == 0.0
    assert dss.PVsystems.pf() == 0.0

def test_13Node_Reclosers():

    import opendssdirect as dss

    assert dss.dss_lib.DSSPut_Command('Redirect {}'.format(os.path.abspath(os.path.join('.', './data/13Bus/IEEE13Nodeckt.dss'))).encode('ascii')) == b"", "Unable to find test data"

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

def test_13Node_RegControls():

    import opendssdirect as dss

    assert dss.dss_lib.DSSPut_Command('Redirect {}'.format(os.path.abspath(os.path.join('.', './data/13Bus/IEEE13Nodeckt.dss'))).encode('ascii')) == b"", "Unable to find test data"

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

def test_13Node_Relays():

    import opendssdirect as dss

    assert dss.dss_lib.DSSPut_Command('Redirect {}'.format(os.path.abspath(os.path.join('.', './data/13Bus/IEEE13Nodeckt.dss'))).encode('ascii')) == b"", "Unable to find test data"

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

def test_13Node_Sensors():

    import opendssdirect as dss

    assert dss.dss_lib.DSSPut_Command('Redirect {}'.format(os.path.abspath(os.path.join('.', './data/13Bus/IEEE13Nodeckt.dss'))).encode('ascii')) == b"", "Unable to find test data"

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

def test_13Node_Settings():

    import opendssdirect as dss

    assert dss.dss_lib.DSSPut_Command('Redirect {}'.format(os.path.abspath(os.path.join('.', './data/13Bus/IEEE13Nodeckt.dss'))).encode('ascii')) == b"", "Unable to find test data"

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

def test_13Node_Solution():

    import opendssdirect as dss

    assert dss.dss_lib.DSSPut_Command('Redirect {}'.format(os.path.abspath(os.path.join('.', './data/13Bus/IEEE13Nodeckt.dss'))).encode('ascii')) == b"", "Unable to find test data"

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
    assert dss.Solution.EventLog() == [u'Hour=0, Sec=0, ControlIter=1, Element=Regulator.reg3, Action= CHANGED 7 TAPS TO 1.04375.', u'Hour=0, Sec=0, ControlIter=1, Element=Regulator.reg2, Action= CHANGED 5 TAPS TO 1.03125.', u'Hour=0, Sec=0, ControlIter=1, Element=Regulator.reg1, Action= CHANGED 7 TAPS TO 1.04375.', u'Hour=0, Sec=0, ControlIter=2, Element=Regulator.reg3, Action= CHANGED 2 TAPS TO 1.05625.', u'Hour=0, Sec=0, ControlIter=2, Element=Regulator.reg2, Action= CHANGED 1 TAPS TO 1.0375.', u'Hour=0, Sec=0, ControlIter=2, Element=Regulator.reg1, Action= CHANGED 2 TAPS TO 1.05625.']
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
    assert dss.Solution.ProcessTime() == 0.0
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
    assert dss.Solution.TimeTimeStep() == 0.0
    assert dss.Solution.TotalIterations() == 2
    assert dss.Solution.TotalTime() == 0.0
    assert dss.Solution.Year() == 0

def test_13Node_SwtControls():

    import opendssdirect as dss

    assert dss.dss_lib.DSSPut_Command('Redirect {}'.format(os.path.abspath(os.path.join('.', './data/13Bus/IEEE13Nodeckt.dss'))).encode('ascii')) == b"", "Unable to find test data"

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

def test_13Node_Topology():

    import opendssdirect as dss

    assert dss.dss_lib.DSSPut_Command('Redirect {}'.format(os.path.abspath(os.path.join('.', './data/13Bus/IEEE13Nodeckt.dss'))).encode('ascii')) == b"", "Unable to find test data"

    assert dss.Topology.ActiveBranch() == 0
    assert dss.Topology.ActiveLevel() == 0
    assert dss.Topology.AllIsolatedBranches() == []
    assert dss.Topology.AllIsolatedLoads() == []
    assert dss.Topology.AllLoopedPairs() == [u'Transformer.reg3', u'Transformer.reg2', u'Transformer.reg2', u'Line.650632', u'Transformer.reg1', u'Line.650632']
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

def test_13Node_Transformers():

    import opendssdirect as dss

    assert dss.dss_lib.DSSPut_Command('Redirect {}'.format(os.path.abspath(os.path.join('.', './data/13Bus/IEEE13Nodeckt.dss'))).encode('ascii')) == b"", "Unable to find test data"

    assert dss.Transformers.AllNames() == [u'sub', u'reg1', u'reg2', u'reg3', u'xfm1']
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

def test_13Node_Vsources():

    import opendssdirect as dss

    assert dss.dss_lib.DSSPut_Command('Redirect {}'.format(os.path.abspath(os.path.join('.', './data/13Bus/IEEE13Nodeckt.dss'))).encode('ascii')) == b"", "Unable to find test data"

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

def test_13Node_XYCurves():

    import opendssdirect as dss

    assert dss.dss_lib.DSSPut_Command('Redirect {}'.format(os.path.abspath(os.path.join('.', './data/13Bus/IEEE13Nodeckt.dss'))).encode('ascii')) == b"", "Unable to find test data"

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


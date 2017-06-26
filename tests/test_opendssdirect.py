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
    assert dss.Bus.CplxSeqVoltages() == [0.0, 0.078125, 0.0, 0.4103854298591614, -1687792.875, 7.377432823181152]
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
    assert dss.Bus.PuVoltage() == [-16.846050262451172, 1.841516375541687, 9.205183232552372e-06, 1.7499384880065918, -1.5929539745265222e+19, -0.6472412943840027]
    assert dss.Bus.SectionID() == 0
    assert dss.Bus.SeqVoltages() == [1.0138394389390052e-41, 0.4103854298591614, 1431.2860107421875]
    assert dss.Bus.TotalMiles() == 0.0
    assert dss.Bus.VLL() == [-1.336131757201121e-21, 7.377588748931885, -2.2596473593770433e-37, 7.759768009185791, -1.2286799893756074e-14, 7.3770856857299805]
    assert dss.Bus.VMagAngle() == [4.0220805198195656e+24, 7.506542205810547, 5.586067309036966e-18, 2.9686365127563477, -3.739865453972065e+25, 7.506552219390869]
    assert dss.Bus.Voc() == [0.0, 0.0, 0.0, 0.0, 0.0, 0.0]
    assert dss.Bus.Voltages() == [-6.364961170632467e+32, 7.377420902252197, 8.763100049691275e-05, 7.0064311027526855, -7.062284317736295e+27, -2.593409538269043]
    assert dss.Bus.X() == 200.0
    assert dss.Bus.Y() == 400.0
    assert dss.Bus.YscMatrix() == [0.0]
    assert dss.Bus.Zsc0() == [0.0, 0.0]
    assert dss.Bus.Zsc1() == [0.0, 0.0]
    assert dss.Bus.ZscMatrix() == [0.0]
    assert dss.Bus.ZscRefresh() == 1
    assert dss.Bus.kVBase() == 66.39528095680697
    assert dss.Bus.puVLL() == [-8.780364570269341e-29, 0.08721625059843063, 3.5549153103337384e+20, -0.09846794605255127, 13.008642196655273, -0.35822173953056335]
    assert dss.Bus.puVmagAngle() == [-9.041031077744916e+28, 0.3155860900878906, -39997968384.0, -3.310267210006714, 1570335358976.0, 0.3155805468559265]

def test_13Node_Circuit():

    import opendssdirect as dss

    assert dss.dss_lib.DSSPut_Command('Redirect {}'.format(os.path.abspath(os.path.join('.', './data/13Bus/IEEE13Nodeckt.dss'))).encode('ascii')) == b"", "Unable to find test data"

    assert dss.Circuit.AllBusDistances() == [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0]
    assert dss.Circuit.AllBusMagPu() == [-5.37940915529515e-31, 1.8749933242797852, 8.888236614310995e-38, 1.8749984502792358, 1789219219439616.0, 1.8749874830245972, -1.2365413870006069e+20, 1.8749775886535645, -494604105285632.0, 1.8749926090240479, 9.393361302299493e+36, 1.8749827146530151, -4.5065929576063726e+36, 1.8820040225982666, -1.3087730621919036e-05, 1.8796731233596802, 363232799752192.0, 1.8820061683654785, 2.65623558091178e+17, 1.8764125108718872, -2.239332176459989e+18, 1.878377079963684, -6.213014550254996e-35, 1.8751919269561768, 5957473533952.0, 1.871789574623108, -26452946944.0, 1.8760523796081543, -9.311668193193084e+36, 1.8706103563308716, 1.754774112173656e+30, 1.8706989288330078, -1.295591850522316e+38, 1.8800344467163086, 0.00012096658610971645, 1.8662173748016357, -2.565403431682594e-22, 1.877466082572937, 3.2725349467159773e-35, 1.8752837181091309, 4.208018779754639]
    assert dss.Circuit.AllBusNames() == [u'sourcebus', u'650', u'rg60', u'633', u'634', u'671', u'645', u'646', u'692', u'675', u'611', u'652', u'670', u'632', u'680', u'684']
    assert dss.Circuit.AllBusVMag() == [-5.37940915529515e-31, 1.8749933242797852, 8.888236614310995e-38, 1.8749984502792358, 1789219219439616.0, 1.8749874830245972, -1.2365413870006069e+20, 1.8749775886535645, -494604105285632.0, 1.8749926090240479, 9.393361302299493e+36, 1.8749827146530151, -4.5065929576063726e+36, 1.8820040225982666, -1.3087730621919036e-05, 1.8796731233596802, 363232799752192.0, 1.8820061683654785, 2.65623558091178e+17, 1.8764125108718872, -2.239332176459989e+18, 1.878377079963684, -6.213014550254996e-35, 1.8751919269561768, 5957473533952.0, 1.871789574623108, -26452946944.0, 1.8760523796081543, -9.311668193193084e+36, 1.8706103563308716, 1.754774112173656e+30, 1.8706989288330078, -1.295591850522316e+38, 1.8800344467163086, 0.00012096658610971645, 1.8662173748016357, -2.565403431682594e-22, 1.877466082572937, 3.2725349467159773e-35, 1.8752837181091309, 4.208018779754639]
    assert dss.Circuit.AllBusVolts() == [-6.364961170632467e+32, 7.377420902252197, 8.763100049691275e-05, 7.0064311027526855, -7.062284317736295e+27, -2.593409538269043, -2.2418947768087944e+23, -7.506552219390869, 2888975872.0, -7.377253532409668, -5.6341632223730406e-27, 7.006673812866211, 1.8287949220116452e-17, 5.0863189697265625, 2031.443115234375, -1.7334462404251099, 7.795068362883152e+21, -4.586541652679443, 1.0530508018716508e+18, -5.0077433586120605, 7.948276769299665e-29, -4.586089611053467, -4.885770607532258e-13, 5.007846832275391, 18635401723904.0, 5.119227409362793, 7.486653878761273e+27, -1.769829273223877, 2.3347499137910252e-20, -4.608525276184082, -4.753682958380523e-07, -5.026730060577393, -3.5329441051705344e+16, -4.61893892288208, -4.942027452745619e+36, 5.036360740661621, -1.7420837458368517e+31, 5.092389106750488, -1434484.375, -3.429558038711548, -4.1258114592919914e-16, -4.634773254394531, 1.1549575251543325e-23, -5.0117878913879395, -50931903234048.0, -4.54707670211792, 1.364133211443112e+23, 5.019677639007568, 13536307707904.0, 3.7667198181152344, -0.00029394382727332413, -2.7391669750213623, -956047872.0, -3.5414464473724365, -1.2138294715722582e-34, -3.7114994525909424, 2820648636252160.0, -3.487255573272705, 2.9484462515938503e-07, 3.7226696014404297, 0.00293856137432158, 5.073750019073486, -1.7026964642644275e-36, -3.68180251121521, 3361.121826171875, -4.653515815734863, -3.033278340800467e-26, -5.015087127685547, -7.822778528704758e+17, -4.491589069366455, 49268.19921875, 5.008571147918701, -6.0037205820737205e-33, -4.632657527923584, -2.6261404673933794e+27, -5.007412910461426, -3.1279476005505168e-28, -4.548036098480225, -1.912372380292027e-31, 5.019911289215088, 1.6644614445496521e-31, -4.632929801940918]
    assert dss.Circuit.AllElementLosses() == [-4.385276841626195e-17, -5.370905876159668, 0.0006561873015016317, -4.847954273223877, 7.031499653356326e+26, 1.2541534900665283, -1.8160580470763858e+27, 1.6312365531921387, -3.2355588155308507e+19, 1.4941812753677368, 4.9146161506645365e-27, 1.4977102279663086, 0.0, 0.0, 0.0, 0.0, 1.3393708011452968e-23, 1.3806933164596558, -5.719178488646657e-28, 1.3841571807861328, 0.0, 0.0, 0.0, 0.0, -3.4178127194589076e+20, 1.5100973844528198, -8.799092508035524e-36, 1.5118619203567505, 0.0, 0.0, 0.0, 0.0, -8.108209104129571e-10, 2.3470418453216553, 2.1056450579281467e+21, 2.5655083656311035, 111982480.0, 4.5639729499816895, 1.1795095649362379e+19, 4.14457368850708, 3.43456321161284e-07, 3.562497854232788, -3.5102370098330373e+31, 3.429708480834961, -1.2903282270903427e-26, 3.468750476837158, 4.919425209942853e+25, 3.351553201675415, -1.6231358849011176e-15, 3.468769073486328, 8.047746566416317e-33, 3.35159969329834, 0.5186038017272949, 3.582031726837158, -2260654.5, 3.488269090652466, -2.190040742817436e-17, 3.7081358432769775, -7996.3310546875, 3.5129432678222656, -3.043003208498854e-26, 3.5755343437194824, -20768710656.0, 3.5391643047332764, -1.4927632463468399e-09, 3.9736294746398926, 19138.361328125, 3.621138334274292, 1067358093312.0, 3.2656261920928955, 6.232478195933834e+26, 3.218733072280884, 230.12379455566406, 3.783219337463379, 2.1055191021244013e-20, 3.664127826690674]
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
    assert dss.Circuit.LineLosses() == [-2.18445181429066e-17, 3.4160244464874268]
    assert dss.Circuit.Losses() == [-1.239379016082509e-10, 7.85761833190918]
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
    assert dss.Circuit.TotalPower() == [-4.385276841626195e-17, -5.370905876159668]
    assert dss.Circuit.UpdateStorage() == 0
    assert dss.Circuit.YCurrents() == [-6334573176684544.0, 7.532549858093262, 5.3090472538074606e+22, -7.550774097442627, 3.896860694124838e+34, -7.743259429931641, 7.129749277122868e+34, -6.743259429931641, 1.6887780737806497e+37, 6.842837333679199, -8.602772611053406e-37, 7.736588954925537, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 3.0107889787837217e-32, -2.681858777999878, -7.606330070583317e-35, 2.5848658084869385, 6.5197411913686665e-09, -2.530078411102295, 25880130748416.0, -2.176856279373169, 1.795240423181493e-23, -2.1411142349243164, -7841871548121088.0, -2.7889349460601807, 6.41673839963184e+31, -2.0834877490997314, 8.187685942902034e-26, 2.229346513748169, 5.083044716473056e-18, -1.7336236238479614, -2.2384794854121184e-29, -1.993398666381836, -4.1854813929364685e-24, 2.1418936252593994, -2.9518069405925504e-22, -1.9859477281570435, -7729.25, -2.164198398590088, 1.0767341879214243e-12, -1.9151133298873901, 0.0, 0.03125, 0.0, 0.03515625, 0.0, -0.03125]
    assert dss.Circuit.YNodeOrder() == [u'SOURCEBUS.1', u'SOURCEBUS.2', u'SOURCEBUS.3', u'650.1', u'650.2', u'650.3', u'RG60.1', u'RG60.2', u'RG60.3', u'633.1', u'633.2', u'633.3', u'634.1', u'634.2', u'634.3', u'671.1', u'671.2', u'671.3', u'645.2', u'646.2', u'646.3', u'692.3', u'692.1', u'675.1', u'675.2', u'675.3', u'611.3', u'652.1', u'670.1', u'670.2', u'670.3', u'632.1', u'632.2', u'632.3', u'680.1', u'680.2', u'680.3', u'645.3', u'692.2', u'684.1', u'684.3']
    assert dss.Circuit.YNodeVArray() == [-6.364961170632467e+32, 7.377420902252197, 8.763100049691275e-05, 7.0064311027526855, -7.062284317736295e+27, -2.593409538269043, -2.2418947768087944e+23, -7.506552219390869, 2888975872.0, -7.377253532409668, -5.6341632223730406e-27, 7.006673812866211, 1.8287949220116452e-17, 5.0863189697265625, 2031.443115234375, -1.7334462404251099, 7.795068362883152e+21, -4.586541652679443, 1.0530508018716508e+18, -5.0077433586120605, 7.948276769299665e-29, -4.586089611053467, -4.885770607532258e-13, 5.007846832275391, 18635401723904.0, 5.119227409362793, 7.486653878761273e+27, -1.769829273223877, 2.3347499137910252e-20, -4.608525276184082, -4.753682958380523e-07, -5.026730060577393, -3.5329441051705344e+16, -4.61893892288208, -4.942027452745619e+36, 5.036360740661621, -1.7420837458368517e+31, 5.092389106750488, -1434484.375, -3.429558038711548, -4.1258114592919914e-16, -4.634773254394531, 1.1549575251543325e-23, -5.0117878913879395, -50931903234048.0, -4.54707670211792, 1.364133211443112e+23, 5.019677639007568, 13536307707904.0, 3.7667198181152344, -0.00029394382727332413, -2.7391669750213623, -956047872.0, -3.5414464473724365, -1.2138294715722582e-34, -3.7114994525909424, 2820648636252160.0, -3.487255573272705, 2.9484462515938503e-07, 3.7226696014404297, 0.00293856137432158, 5.073750019073486, -1.7026964642644275e-36, -3.68180251121521, 3361.121826171875, -4.653515815734863, -3.033278340800467e-26, -5.015087127685547, -7.822778528704758e+17, -4.491589069366455, 49268.19921875, 5.008571147918701, -6.0037205820737205e-33, -4.632657527923584, -2.6261404673933794e+27, -5.007412910461426, 1.6644614445496521e-31, -4.632929801940918, 3.2814564596399948e-15, -5.0061421394348145, -2036977369088.0, -4.547743797302246]

def test_13Node_CktElement():

    import opendssdirect as dss

    assert dss.dss_lib.DSSPut_Command('Redirect {}'.format(os.path.abspath(os.path.join('.', './data/13Bus/IEEE13Nodeckt.dss'))).encode('ascii')) == b"", "Unable to find test data"

    assert dss.CktElement.AllPropertyNames() == [u'bus1', u'bus2', u'linecode', u'length', u'phases', u'r1', u'x1', u'r0', u'x0', u'C1', u'C0', u'rmatrix', u'xmatrix', u'cmatrix', u'Switch', u'Rg', u'Xg', u'rho', u'geometry', u'units', u'spacing', u'wires', u'EarthModel', u'cncables', u'tscables', u'B1', u'B0', u'normamps', u'emergamps', u'faultrate', u'pctperm', u'repair', u'basefreq', u'enabled', u'like']
    assert dss.CktElement.AllVariableNames() == []
    assert dss.CktElement.AllVariableValues() == [0.0]
    assert dss.CktElement.BusNames() == [u'671', u'692']
    assert dss.CktElement.Close() == 0
    assert dss.CktElement.CplxSeqCurrents() == [-7.105428204633949e-15, 3.2598836421966553, 8589934592.0, 2.6773900985717773, -1.0843905124317663e+35, 3.5272703170776367, 1.1447764871858232e-38, -2.7359673976898193, -2.4766830449153955e-16, 2.581268072128296, 9.260569181159348e-32, -3.2778894901275635]
    assert dss.CktElement.CplxSeqVoltages() == [-2.495163078549281e+19, -1.9044896364212036, -3.816944205629996e+26, -3.3226208686828613, -5.088507984364439e-37, 5.082530498504639, -9.723793932235571e+16, -3.567366600036621, 8.083298320560386e+26, -3.0213239192962646, 2.593139980115276e+26, 2.874997615814209]
    assert dss.CktElement.Currents() == [-131072.0, 3.6779165267944336, 5.902958103587057e+20, -3.2852115631103516, -4.656612873077393e-10, 3.0499215126037598, -1.0842021724855044e-19, -3.193288564682007, -3.6893488147419103e+19, -3.2022855281829834, 2.4178516392292583e+24, 3.5835635662078857]
    assert dss.CktElement.CurrentsMagAng() == [-3.1376494959435086e+26, 3.7010531425476074, -2.5382705109274133e-27, -2.7879836559295654, -2.7835005411702696e-09, 3.267608642578125, 1.0399379276758067e+36, -3.1868622303009033, -65934284.0, 3.6022069454193115, -73279416.0, 3.4247093200683594]
    assert dss.CktElement.DisplayName() == u'Line_671692'
    assert dss.CktElement.EmergAmps() == 600.0
    assert dss.CktElement.Enabled() == 1
    assert dss.CktElement.EnergyMeter() == u''
    assert isinstance(dss.CktElement.GUID(), str)
    assert dss.CktElement.HasSwitchControl() == 0
    assert dss.CktElement.HasVoltControl() == 0
    assert dss.CktElement.IsOpen() == 0
    assert dss.CktElement.Losses() == [1.5845632502852868e+29, 1.0198723077774048]
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
    assert dss.CktElement.PhaseLosses() == [-2.2063454074728387e-33, 0.41869035363197327, -518969491456.0, 0.035249996930360794, -5.848705963984457e-10, 0.31151634454727173]
    assert dss.CktElement.Powers() == [-6060935441547264.0, 4.018582820892334, -8.666298899414473e-19, 3.481060028076172, -1.3030003625467593e-19, 3.2669169902801514, -0.031123457476496696, -3.5565178394317627, 4.189771256443769e-31, 3.90483021736145, 3.1398631830545553e+23, 3.162625551223755]
    assert dss.CktElement.Residuals() == [1.86078112697246e-26, 3.647977113723755, 1.4045659746386718e-08, 2.613010883331299]
    assert dss.CktElement.SeqCurrents() == [-5.980854984954931e-05, 3.265317916870117, -1.7028732590684825e-11, 3.5289289951324463, 1.8510772996735297e-24, 3.2809576988220215]
    assert dss.CktElement.SeqPowers() == [-1.6270965179490578e+34, -2.2044174671173096, 2.904379755979604e+18, -2.7567763328552246, -2.0803129364709376e+16, 4.499773025512695, 2.4713699987679294e+21, 3.079005002975464, -2.4705318606883976e+36, -2.389155149459839, 4.559511851404519e-29, -2.415543556213379]
    assert dss.CktElement.SeqVoltages() == [3.5652763830370214e+26, 3.3226571083068848, 3.050047613122961e-25, 5.0838799476623535, 3.904083727100333e-22, 3.0798068046569824]
    assert dss.CktElement.Variablei() == 0.0
    assert dss.CktElement.Voltages() == [0.00293856137432158, 5.073750019073486, -1.7026964642644275e-36, -3.68180251121521, 3361.121826171875, -4.653515815734863, -3.033278340800467e-26, -5.015087127685547, -7.822778528704758e+17, -4.491589069366455, 49268.19921875, 5.008571147918701]
    assert dss.CktElement.VoltagesMagAng() == [-2.1001745488748216e+18, 5.076282978057861, -6.606827794064175e-26, -2.3358912467956543, 459297783808.0, 5.109988212585449, 16778251264.0, -3.47808575630188, -2.226532958005123e-09, 5.065771579742432, 9.700330816375669e-12, 3.4530718326568604]
    assert dss.CktElement.YPrim() == [0.0, 14.192092895507812, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, -14.192092895507812, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 14.192092895507812, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, -14.192092895507812, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 14.192092895507812, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, -14.192092895507812, 0.0, 0.0]

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

    assert dss.CapControls.AllNames() == [u'NONE']
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

    assert dss.Fuses.AllNames() == [u'NONE']
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

    assert dss.Generators.AllNames() == [u'NONE']
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

    assert dss.Isource.AllNames() == [u'NONE']
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
    assert dss.Lines.RMatrix() == [36310270083072.0, 1.6732499599456787, -2648116578746368.0, 1.5309998989105225, 4.4630594742302834e-29, 1.5329999923706055, -2648116578746368.0, 1.5309998989105225, -1.5881868392106856e-23]
    assert dss.Lines.Rg() == 0.01805
    assert dss.Lines.Rho() == 100.0
    assert dss.Lines.Spacing() == u''
    assert dss.Lines.Units() == 5
    assert dss.Lines.X0() == 0.4047
    assert dss.Lines.X1() == 0.1206
    assert dss.Lines.XMatrix() == [-2.4916718928146493e-37, 1.8772374391555786, 1.564330940175343e-14, 1.7504249811172485, 4.7031788186213674e-12, 1.7117999792099, 1.564330940175343e-14, 1.7504249811172485, -3.156450063325947e+28]
    assert dss.Lines.Xg() == 0.155081
    assert dss.Lines.Yprim() == [-8.413908246547038e+26, 2.179194211959839, -8.58438428348052e+29, -2.559267997741699, 3.345404154138751e-21, -1.932100534439087, -1.1053327229482605e-29, 2.2073678970336914, -1.6024549402191934e-15, -1.8244389295578003, -5617472.0, 2.0919008255004883, -8.413908246547038e+26, -2.179194211959839, -1.854684063816414e+31, 2.559267997741699, 3.345404154138751e-21, 1.932100534439087, -1.602198454105241e-28, -2.2073678970336914, -1.6024549402191934e-15, 1.8244389295578003, -78824768.0, -2.0919008255004883, 3.345404154138751e-21, -1.932100534439087, -1.1053327229482605e-29, 2.2073678970336914, 4.8782949731441286e-31, 2.1258184909820557, -7.2093100417390125e+22, -2.5430619716644287, -4.9032807636447305e+23, -1.6893572807312012, 9.37407662604528e-08, 2.011124849319458, 3.345404154138751e-21, 1.932100534439087, -1.602198454105241e-28, -2.2073678970336914, 4.8782949731441286e-31, -2.1258184909820557, -1.671667726965592e+24, 2.5430619716644287, -4.9032807636447305e+23, 1.6893572807312012, 1.3427543308353052e-06, -2.011124849319458, -1.6024549402191934e-15, -1.8244389295578003, -5617472.0, 2.0919008255004883, -4.9032807636447305e+23, -1.6893572807312012, 9.37407662604528e-08, 2.011124849319458, 1.5305168081644715e+23, 2.0823440551757812, 3.458351812961318e-17, -2.526472330093384, -1.6024549402191934e-15, 1.8244389295578003, -78824768.0, -2.0919008255004883, -4.9032807636447305e+23, 1.6893572807312012, 1.3427543308353052e-06, -2.011124849319458, 1.5305168081644715e+23, -2.0823440551757812, 7.640489176535597e-16, 2.526472330093384]

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
    assert dss.LoadShape.PMult() == [-1.1170474872998765e+24, 1.7942498922348022, 4590246.5, 1.7813999652862549, 7.853491734369164e+26, 1.777174949645996, -124.10880279541016, 1.770824909210205, 4.700230445726433e+17, 1.77006995677948, 1.2666203376237269e-26, 1.7756249904632568, -7.885983267432694e+17, 1.7892498970031738, -3.559340470561047e-31, 1.811924934387207, 2.0353803153142307e+33, 1.8329999446868896, -71.68000030517578, 1.84499990940094, -2.302153575956459e+20, 1.8599998950958252, 2128654499840.0, 1.872249960899353]
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
    assert dss.Meters.AllNames() == [u'NONE']
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

    assert dss.Monitors.AllNames() == [u'NONE']
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

    assert dss.Properties.Description() == u''
    assert dss.Properties.Name() == u''

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

    assert dss.Reclosers.AllNames() == [u'NONE']
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
    assert dss.Reclosers.RecloseIntervals() == [0.0]
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

    assert dss.Relays.AllNames() == [u'NONE']
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

    assert dss.Sensors.AllNames() == [u'NONE']
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
    assert dss.Settings.VoltageBases() == [0.0, 3.44921875, 9.121204334167384e-33]
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
    assert dss.SwtControls.AllNames() == [u'NONE']
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
    assert dss.Topology.AllIsolatedBranches() == [u'NONE']
    assert dss.Topology.AllIsolatedLoads() == [u'NONE']
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


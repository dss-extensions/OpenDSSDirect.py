# opendssdirect package reference

Since version 0.9, OpenDSSDirect.py is organized in classes, also exposed as submodules for compatibility with previous versions. That is, prefer to import it as `from opendssdirect import dss`. The submodules expose functions bound to the methods of the interface classes, using the default DSS instance. Check [Upgrading to OpenDSSDirect.py v0.9+](updating_to_0.9) for a more complete overview of the changes.

For the enum classes that can be used in many of the API methods, see [Enumerations](enumerations). For the utils module, see [`opendssdirect.utils`](opendssdirect_utils_ref).

On the docstrings in this document, when a function/method has an equivalent in the official COM implementation, links are now provided to the new EPRI documentation site, introduced in January 2024. Despite the examples from the official OpenDSS being mostly written in MATLAB using the COM API, users should be able to map the general use logic to OpenDSSDirect.py. On the other hand, if the function is an API extension, it is marked as such.

## The OpenDSSDirect class

This class, as exposed in the default instance `dss` (`from opendssdirect import dss`), has attributes representing all the submodules listed in the next section, plus extra functions.

```{autodoc2-object} opendssdirect.OpenDSSDirect.OpenDSSDirect
```

## Iterable base class

The `Iterable` base class is used by most of the interface classes that expose DSS objects. This includes the common `Name()`, `First()`, `Next()`, `Count()`, `AllNames()`, `Idx()`, and [Python dunder methods](https://docs.python.org/3/reference/datamodel.html#special-method-names) to allow using `len()` and iteration.

```{autodoc2-object} opendssdirect.Bases.Iterable
```

## opendssdirect.ActiveClass

```{autodoc2-object} opendssdirect.ActiveClass.IActiveClass
```

## opendssdirect.Basic

```{autodoc2-object} opendssdirect.Basic.IBasic
```

## opendssdirect.Bus

```{autodoc2-object} opendssdirect.Bus.IBus
```

## opendssdirect.CapControls

```{autodoc2-object} opendssdirect.CapControls.ICapControls
```

## opendssdirect.Capacitors

```{autodoc2-object} opendssdirect.Capacitors.ICapacitors
```

## opendssdirect.Circuit

```{autodoc2-object} opendssdirect.Circuit.ICircuit
```

## opendssdirect.CktElement

```{autodoc2-object} opendssdirect.CktElement.ICktElement
```

## opendssdirect.CNData

```{autodoc2-object} opendssdirect.CNData.ICNData
```

## opendssdirect.CtrlQueue

```{autodoc2-object} opendssdirect.CtrlQueue.ICtrlQueue
```

## opendssdirect.Element

```{autodoc2-object} opendssdirect.Element.IElement
```

## opendssdirect.Error

```{autodoc2-object} opendssdirect.Error.IError
```

## opendssdirect.Executive

```{autodoc2-object} opendssdirect.Executive.IExecutive
```

## opendssdirect.Fuses

```{autodoc2-object} opendssdirect.Fuses.IFuses
```

## opendssdirect.Generators

```{autodoc2-object} opendssdirect.Generators.IGenerators
```

## opendssdirect.GICSources

```{autodoc2-object} opendssdirect.GICSources.IGICSources
```

## opendssdirect.Isource

```{autodoc2-object} opendssdirect.Isource.IIsource
```

## opendssdirect.LineCodes

```{autodoc2-object} opendssdirect.LineCodes.ILineCodes
```

## opendssdirect.LineGeometries

```{autodoc2-object} opendssdirect.LineGeometries.ILineGeometries
```

## opendssdirect.LineSpacings

```{autodoc2-object} opendssdirect.LineSpacings.ILineSpacings
```

## opendssdirect.Lines

```{autodoc2-object} opendssdirect.Lines.ILines
```

## opendssdirect.LoadShape

```{autodoc2-object} opendssdirect.LoadShape.ILoadShape
```

## opendssdirect.Loads

```{autodoc2-object} opendssdirect.Loads.ILoads
```

## opendssdirect.Meters

```{autodoc2-object} opendssdirect.Meters.IMeters
```

## opendssdirect.Monitors

```{autodoc2-object} opendssdirect.Monitors.IMonitors
```

## opendssdirect.Parallel

```{autodoc2-object} opendssdirect.Parallel.IParallel
```

## opendssdirect.PDElements

```{autodoc2-object} opendssdirect.PDElements.IPDElements
```

## opendssdirect.PVsystems

```{autodoc2-object} opendssdirect.PVsystems.IPVsystems
```

## opendssdirect.Parser

```{autodoc2-object} opendssdirect.Parser.IParser
```

## opendssdirect.Progress

```{autodoc2-object} opendssdirect.Progress.IProgress
```

## opendssdirect.Properties

```{autodoc2-object} opendssdirect.Properties.IProperties
```

## opendssdirect.RegControls

```{autodoc2-object} opendssdirect.RegControls.IRegControls
```

## opendssdirect.Relays

```{autodoc2-object} opendssdirect.Relays.IRelays
```

## opendssdirect.Reactors

```{autodoc2-object} opendssdirect.Reactors.IReactors
```

## opendssdirect.Reclosers

```{autodoc2-object} opendssdirect.Reclosers.IReclosers
```

## opendssdirect.ReduceCkt

```{autodoc2-object} opendssdirect.ReduceCkt.IReduceCkt
```

## opendssdirect.Sensors

```{autodoc2-object} opendssdirect.Sensors.ISensors
```

## opendssdirect.Settings

```{autodoc2-object} opendssdirect.Settings.ISettings
```

## opendssdirect.Solution

```{autodoc2-object} opendssdirect.Solution.ISolution
```

## opendssdirect.Storages

```{autodoc2-object} opendssdirect.Storages.IStorages
```

## opendssdirect.SwtControls

```{autodoc2-object} opendssdirect.SwtControls.ISwtControls
```

## opendssdirect.Text

```{autodoc2-object} opendssdirect.Text.IText
```

## opendssdirect.Topology

```{autodoc2-object} opendssdirect.Topology.ITopology
```

## opendssdirect.Transformers

```{autodoc2-object} opendssdirect.Transformers.ITransformers
```

## opendssdirect.TSData

```{autodoc2-object} opendssdirect.TSData.ITSData
```

## opendssdirect.Vsources

```{autodoc2-object} opendssdirect.Vsources.IVsources
```

## opendssdirect.XYCurves

```{autodoc2-object} opendssdirect.XYCurves.IXYCurves
```

## opendssdirect.YMatrix

```{autodoc2-object} opendssdirect.YMatrix.IYMatrix
```

## opendssdirect.WireData

```{autodoc2-object} opendssdirect.WireData.IWireData
```

## opendssdirect.ZIP

```{autodoc2-object} opendssdirect.ZIP.IZIP
```

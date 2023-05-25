# OpenDSSDirect.py
[![Appveyor Build Status](https://ci.appveyor.com/api/projects/status/github/dss-extensions/OpenDSSDirect.py?branch=master&svg=true)](https://ci.appveyor.com/project/PMeira/opendssdirect-py)
[![codecov](https://codecov.io/gh/dss-extensions/OpenDSSDirect.py/branch/master/graph/badge.svg)](https://codecov.io/gh/dss-extensions/OpenDSSDirect.py)
[![PyPI](https://img.shields.io/pypi/v/OpenDSSDirect.py.svg)](https://pypi.python.org/pypi/OpenDSSDirect.py/)
[![Documentation](https://img.shields.io/badge/docs-ready-blue.svg)](http://dss-extensions.org/OpenDSSDirect.py)

OpenDSSDirect.py is a cross-platform Python package implements a "direct" library interface [our customized implementation](https://github.com/dss-extensions/dss_capi) of [OpenDSS](http://smartgrid.epri.com/SimulationTool.aspx) using [DSS-Python](https://github.com/dss-extensions/dss_python/).
OpenDSS is an open-source distribution system simulator. See [OpenDSSDirect.jl](https://github.com/dss-extensions/OpenDSSDirect.jl) for a similar package in Julia, and for more context about this project and its components (including alternatives in MATLAB, C++ and C#/.NET), please check [https://dss-extensions.org/](https://dss-extensions.org/) and our hub repository at [dss-extensions/dss-extensions](https://github.com/dss-extensions/dss-extensions) for more documentation, discussions and the [FAQ](https://github.com/dss-extensions/dss-extensions#faq).

*As a reminder, although very compatible, this project is not supported by EPRI.*

**This package is available for Windows, Mac and Linux, including ARM and x86 variants.**

### Documentation

The documentation for this package can be found [here](http://dss-extensions.org/OpenDSSDirect.py).

### Installation

**Recommended**: Install Python using Miniconda or Anaconda

Open a command line interface and type the following.

```bash
pip install 'OpenDSSDirect.py[extras]'
```

See [installation](https://dss-extensions.org/OpenDSSDirect.py/notebooks/Installation.html) instructions for more information.

### Troubleshooting

It is recommended to use `conda` to install pandas, which is currently a dependency of this package.
This package interfaces with OpenDSS using the "direct" library interface, so a good understanding of OpenDSS will help troubleshooting.
There are plenty of useful resources located [here](https://sourceforge.net/p/electricdss/code/HEAD/tree/trunk/Doc/).

If you are having issues using this Python interface, feel free to open an Issue on GitHub [here](https://github.com/dss-extensions/OpenDSSDirect.py/issues/new).

### Thanks

Thanks to @tshort, Davis, @temcdrm, @GordStephen, @Muxelmann and @PMeira for their contributions, as well as all the users for their valuable feedback.

See also our repositories for [DSS-Python](https://github.com/dss-extensions/dss_python) for the underlying Python package used in this package, and 
[DSS C-API](https://github.com/dss-extensions/dss_capi) for the modified and extended OpenDSS codebase used in DSS-Extensions.

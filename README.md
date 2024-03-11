# OpenDSSDirect.py
[![GitHub Build Status](https://github.com/dss-extensions/OpenDSSDirect.py/actions/workflows/tests.yml/badge.svg)](https://github.com/dss-extensions/OpenDSSDirect.py/actions/workflows/tests.yml)
[![codecov](https://codecov.io/gh/dss-extensions/OpenDSSDirect.py/branch/master/graph/badge.svg)](https://codecov.io/gh/dss-extensions/OpenDSSDirect.py)
[![PyPI](https://img.shields.io/pypi/v/OpenDSSDirect.py.svg)](https://pypi.python.org/pypi/OpenDSSDirect.py/)
[![PyPI Download stats](https://static.pepy.tech/badge/opendssdirect-py/month)](https://pepy.tech/project/opendssdirect-py)
[![Documentation](https://img.shields.io/badge/docs-ready-blue.svg)](http://dss-extensions.org/OpenDSSDirect.py)

OpenDSSDirect.py is a cross-platform Python package implements a "direct" library interface to [our customized/alternative implementation](https://github.com/dss-extensions/dss_capi) of [OpenDSS](http://smartgrid.epri.com/SimulationTool.aspx) using [DSS-Python](https://github.com/dss-extensions/DSS-Python/).
OpenDSS is an open-source distribution system simulator [distributed by EPRI](https://sourceforge.net/p/electricdss/). See [OpenDSSDirect.jl](https://github.com/dss-extensions/OpenDSSDirect.jl) for a similar package in Julia, and for more context about this project and its components (including alternatives in MATLAB, C++, C#/.NET, Go, and Rust), please check [https://dss-extensions.org/](https://dss-extensions.org/) and our hub repository at [dss-extensions/dss-extensions](https://github.com/dss-extensions/dss-extensions) for more documentation, discussions and the [FAQ](https://dss-extensions.org/faq.html).

An alternative Python package is being developed in [AltDSS-Python](https://dss-extensions.org/AltDSS-Python/). It can be used together with OpenDSSDirect.py.


<p align="center">
    <img alt="Overview of related projects" src="https://github.com/dss-extensions/dss-extensions/blob/main/images/repomap.png?raw=true">
</p>


*As a reminder, although very compatible, this project is not supported by EPRI.*

**This package is available for Windows, Mac and Linux, including ARM and x86 variants.**

## Documentation

The documentation for this package can be found [here](http://dss-extensions.org/OpenDSSDirect.py).

## Installation

**Recommended**: Install Python using Miniconda or Anaconda

Open a command line interface and type the following.

```bash
pip install 'OpenDSSDirect.py[extras]'
```

See the [installation](https://dss-extensions.org/OpenDSSDirect.py/notebooks/Installation.html) instructions for more information.

Updating from pre-v0.9 versions? [See the upgrade guide for recommendations.](https://dss-extensions.org/OpenDSSDirect.py/updating_to_0.9.html)

## Troubleshooting

It is recommended to use `conda` to install pandas, which is currently a dependency of this package.
This package interfaces with OpenDSS using the "direct" library interface, so a good understanding of OpenDSS will help troubleshooting.

If you are having issues using this Python interface, feel free to open an Issue on GitHub [here](https://github.com/dss-extensions/OpenDSSDirect.py/issues/new).

## Thanks

Thanks to @tshort, Davis, @temcdrm, @GordStephen, @Muxelmann and @PMeira for their contributions, as well as all the users for their valuable feedback.

See also our repositories for [DSS-Python](https://github.com/dss-extensions/DSS-Python) for the underlying Python package used in this package, and 
[AltDSS/DSS C-API](https://github.com/dss-extensions/dss_capi) for the modified and extended OpenDSS codebase used in DSS-Extensions.

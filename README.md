# OpenDSSDirect.py - Library Update [![Build Status](https://img.shields.io/travis/Muxelmann/OpenDSSDirect.py.svg?branch=lib-update)](https://travis-ci.org/NREL/OpenDSSDirect.py)

The main branch of **OpenDSSDirect.py** can be found [here](https://github.com/NREL/OpenDSSDirect.py).
This is a Python package that implements a "direct" library interface to [OpenDSS](http://smartgrid.epri.com/SimulationTool.aspx).
OpenDSS is an open-source distribution system simulator. See [OpenDSSDirect.jl](https://github.com/tshort/OpenDSSDirect.jl) for a similar package in Julia.

This branch develops the updating procedure for the main **OpenDSSDirect.py** project.
It does so by downloading and compiling the original OpenDSS source code from [Subversion Repository](https://sourceforge.net/projects/electricdss/).
The finished library (i.e. `libopendssdirect.so`) is then saved into the correct folder for **OpenDSSDirect.py**.

**This package is available for Linux only. Mac and Windows are still to come.**

## Usage

### Setup

Run the following or follow the steps below manually:

```
make -C update setup_Ubuntu
```

<hr>

Start by installing all prerequisites, including the standard compiler and lazarus (with Free Pascal). Also two additional symbolic links need to be added for the compilation to function correctly.

```
sudo apt update
sudo apt upgrade
sudo apt install build-essential lazarus subversion
sudo ln -sfv /usr/lib/x86_64-linux-gnu/libstdc++.so.6 /usr/lib/x86_64-linux-gnu/libstdc++.so
sudo ln -sfv /lib/x86_64-linux-gnu/libgcc_s.so.1 /lib/x86_64-linux-gnu/libgcc_s.so
```

### Compile

Fully compile the library using:

```
make -C update
```

This will save the final `libopendssdirect.so` in the `lib` directory, and a full copy of the OpenDSS source is stored in `electricdss`. If you want the OpenDSS source saved somewhere else, you can build like so:

```
make -C update OPENDSS_DIR=some_other_dir
```

Also, making the project will download and compile a standalone KLUSolve, to assure it is compiled for the correct CPU architecture.


## Thanks

Thanks to @kdheepak and Davis for their input.


OPENDSS_DIR ?= electricdss

CC		  = /usr/bin/fpc
MACROS	= -MDelphi -Scghi -Ct -O2  -k-lc -k-lm -k-lgcc_s -k-lstdc++ -l -vewnhibq
CFLAGS	= -dBorland -dVer150 -dDelphi7 -dCompiler6_Up -dPUREPASCAL -dCPU64
TMP		  = ./tmp
LIB		  = ./lib

KLUSOLVE      = KLUSolve
KLUSOLVE_LIB  = ${KLUSOLVE}/Lib
KLUSOLVE_TEST = ${KLUSOLVE}/Test

OUT = libopendssdirect.so

INPUT_DIRS = \
-Fi${OPENDSS_DIR}/Source/LazDSS/Forms \
-Fi${OPENDSS_DIR}/Source/LazDSS/Shared \
-Fi${OPENDSS_DIR}/Source/LazDSS/Common \
-Fi${OPENDSS_DIR}/Source/LazDSS/PDElements \
-Fi${OPENDSS_DIR}/Source/LazDSS/Controls \
-Fi${OPENDSS_DIR}/Source/LazDSS/General \
-Fi${OPENDSS_DIR}/Source/LazDSS/Plot \
-Fi${OPENDSS_DIR}/Source/LazDSS/Meters \
-Fi${OPENDSS_DIR}/Source/LazDSS/PCElements \
-Fi${OPENDSS_DIR}/Source/LazDSS/Executive \
-Fi${OPENDSS_DIR}/Source/LazDSS/Parser \
-Fi${OPENDSS_DIR}/Source/LazDSS/units/x86_64-linux

# LIB_DIRS = -Fl${OPENDSS_DIR}/Source/LazDSS/lib
LIB_DIRS = -Fl${KLUSOLVE_LIB}

USE_DIRS = \
-Fu${OPENDSS_DIR}/Source/LazDSS/Shared \
-Fu${OPENDSS_DIR}/Source/LazDSS/Common \
-Fu${OPENDSS_DIR}/Source/LazDSS/PDElements \
-Fu${OPENDSS_DIR}/Source/LazDSS/Controls \
-Fu${OPENDSS_DIR}/Source/LazDSS/General \
-Fu${OPENDSS_DIR}/Source/LazDSS/Meters \
-Fu${OPENDSS_DIR}/Source/LazDSS/PCElements \
-Fu${OPENDSS_DIR}/Source/LazDSS/Executive \
-Fu${OPENDSS_DIR}/Source/LazDSS/Parser \
-Fu${OPENDSS_DIR}/Source/LazDSS/DirectDLL \

# Build for x86_64 on Linux

all: ${TMP} ${LIB} update_klusolve update_dss
	$(CC) \
	-Px86_64 -Cg $(MACROS) \
	${INPUT_DIRS} ${LIB_DIRS} ${USE_DIRS} -FU${TMP} -FE${LIB} \
	-o${OUT} \
	${CFLAGS} \
	${OPENDSS_DIR}/Source/LazDSS/DirectDLL/OpenDSSDirect.lpr

# Bild for x86_64 on Linux and delete unnecessary files afterwards

light: all
	rm -fr ${TMP}

# Build for 64bit ARM

arm: ${TMP} ${LIB} update_klusolve update_dss
	$(CC) \
	-Parm  $(MACROS) \
	${INPUT_DIRS} ${LIB_DIRS} ${USE_DIRS} -Fu${TMP} -FE${LIB} \
	-Fl/usr/lib/gcc/arm-linux-gnueabihf/4.9/ \
	-o${OUT} \
	${CFLAGS} \
	${OPENDSS_DIR}/Source/LazDSS/DirectDLL/OpenDSSDirect.lpr

# Bild for x86_64 on Linux and delete unnecessary files afterwards

light_arm: arm
	rm -fr ${TMP}

# Clean

clean:
	rm -rf ${TMP}
	rm -rf ${LIB}

# SVN code management

update_klusolve: ${KLUSOLVE}
	svn update ${KLUSOLVE}
	mkdir -p ${KLUSOLVE_LIB}
	mkdir -p ${KLUSOLVE_TEST}
	make -C ${KLUSOLVE} all

${KLUSOLVE}:
	mkdir -p ${KLUSOLVE}
	svn checkout https://svn.code.sf.net/p/klusolve/code/ ${KLUSOLVE}

update_dss: ${OPENDSS_DIR}
	svn update ${OPENDSS_DIR}

${OPENDSS_DIR}:
	mkdir -p ${OPENDSS_DIR}
	svn checkout https://svn.code.sf.net/p/electricdss/code/trunk ${OPENDSS_DIR}

# Directory management

${TMP}:
	mkdir -p ${TMP}

${LIB}:
	mkdir -p ${LIB}

# Setup functions

setup_Ubuntu:
	sudo apt update
	sudo apt upgrade
	sudo apt install build-essential lazarus subversion
	sudo ln -sfv /usr/lib/x86_64-linux-gnu/libstdc++.so.6 /usr/lib/x86_64-linux-gnu/libstdc++.so
	sudo ln -sfv /lib/x86_64-linux-gnu/libgcc_s.so.1 /lib/x86_64-linux-gnu/libgcc_s.so

setup_RPi:
	sudo apt-get update
	sudo apt-get upgrade
	sudo apt-get install build-essential subversion
	sudo ln -sfv /usr/lib/arm-linux-gnueabihf/libstdc++.so.6 /usr/lib/arm-linux-gnueabihf/libstdc++.so
	sudo ln -sfv /lib/arm-linux-gnueabihf/libgcc_s.so.1 /lib/arm-linux-gnueabihf/libgcc_s.so
	# Install FPC 3.0.2
	# wget ftp://ftp.hu.freepascal.org/pub/fpc/dist/3.0.2/arm-linux/fpc-3.0.2.arm-linux-eabihf-raspberry.tar
	# tar -xvf fpc-3.0.2.arm-linux-eabihf-raspberry.tar
	# cd fpc-3.0.2.arm-linux && sudo ./install.sh
	# Install FPC 3.0.0
	wget ftp://ftp.hu.freepascal.org/pub/fpc/dist/3.0.0/arm-linux/fpc-3.0.0.arm-linux-raspberry1wq.tar
	tar -xvf fpc-3.0.0.arm-linux-raspberry1wq.tar
	cd fpc-3.0.0.arm-linux && sudo ./install.sh

INCLUDE(FindPkgConfig)
PKG_CHECK_MODULES(PC_GMSK gmsk)

FIND_PATH(
    GMSK_INCLUDE_DIRS
    NAMES gmsk/api.h
    HINTS $ENV{GMSK_DIR}/include
        ${PC_GMSK_INCLUDEDIR}
    PATHS ${CMAKE_INSTALL_PREFIX}/include
          /usr/local/include
          /usr/include
)

FIND_LIBRARY(
    GMSK_LIBRARIES
    NAMES gnuradio-gmsk
    HINTS $ENV{GMSK_DIR}/lib
        ${PC_GMSK_LIBDIR}
    PATHS ${CMAKE_INSTALL_PREFIX}/lib
          ${CMAKE_INSTALL_PREFIX}/lib64
          /usr/local/lib
          /usr/local/lib64
          /usr/lib
          /usr/lib64
)

INCLUDE(FindPackageHandleStandardArgs)
FIND_PACKAGE_HANDLE_STANDARD_ARGS(GMSK DEFAULT_MSG GMSK_LIBRARIES GMSK_INCLUDE_DIRS)
MARK_AS_ADVANCED(GMSK_LIBRARIES GMSK_INCLUDE_DIRS)


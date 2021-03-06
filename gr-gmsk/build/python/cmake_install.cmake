# Install script for directory: /home/saurabh/Desktop/EE340_Course_Project/gr-gmsk/python

# Set the install prefix
IF(NOT DEFINED CMAKE_INSTALL_PREFIX)
  SET(CMAKE_INSTALL_PREFIX "/usr/local")
ENDIF(NOT DEFINED CMAKE_INSTALL_PREFIX)
STRING(REGEX REPLACE "/$" "" CMAKE_INSTALL_PREFIX "${CMAKE_INSTALL_PREFIX}")

# Set the install configuration name.
IF(NOT DEFINED CMAKE_INSTALL_CONFIG_NAME)
  IF(BUILD_TYPE)
    STRING(REGEX REPLACE "^[^A-Za-z0-9_]+" ""
           CMAKE_INSTALL_CONFIG_NAME "${BUILD_TYPE}")
  ELSE(BUILD_TYPE)
    SET(CMAKE_INSTALL_CONFIG_NAME "Release")
  ENDIF(BUILD_TYPE)
  MESSAGE(STATUS "Install configuration: \"${CMAKE_INSTALL_CONFIG_NAME}\"")
ENDIF(NOT DEFINED CMAKE_INSTALL_CONFIG_NAME)

# Set the component getting installed.
IF(NOT CMAKE_INSTALL_COMPONENT)
  IF(COMPONENT)
    MESSAGE(STATUS "Install component: \"${COMPONENT}\"")
    SET(CMAKE_INSTALL_COMPONENT "${COMPONENT}")
  ELSE(COMPONENT)
    SET(CMAKE_INSTALL_COMPONENT)
  ENDIF(COMPONENT)
ENDIF(NOT CMAKE_INSTALL_COMPONENT)

# Install shared libraries without execute permission?
IF(NOT DEFINED CMAKE_INSTALL_SO_NO_EXE)
  SET(CMAKE_INSTALL_SO_NO_EXE "1")
ENDIF(NOT DEFINED CMAKE_INSTALL_SO_NO_EXE)

IF(NOT CMAKE_INSTALL_COMPONENT OR "${CMAKE_INSTALL_COMPONENT}" STREQUAL "Unspecified")
  FILE(INSTALL DESTINATION "${CMAKE_INSTALL_PREFIX}/lib/python2.7/dist-packages/gmsk" TYPE FILE FILES
    "/home/saurabh/Desktop/EE340_Course_Project/gr-gmsk/python/__init__.py"
    "/home/saurabh/Desktop/EE340_Course_Project/gr-gmsk/python/gmsk_py_cc.py"
    "/home/saurabh/Desktop/EE340_Course_Project/gr-gmsk/python/gmsk_demod_py_cc.py"
    "/home/saurabh/Desktop/EE340_Course_Project/gr-gmsk/python/channel_est_py_ccc.py"
    )
ENDIF(NOT CMAKE_INSTALL_COMPONENT OR "${CMAKE_INSTALL_COMPONENT}" STREQUAL "Unspecified")

IF(NOT CMAKE_INSTALL_COMPONENT OR "${CMAKE_INSTALL_COMPONENT}" STREQUAL "Unspecified")
  FILE(INSTALL DESTINATION "${CMAKE_INSTALL_PREFIX}/lib/python2.7/dist-packages/gmsk" TYPE FILE FILES
    "/home/saurabh/Desktop/EE340_Course_Project/gr-gmsk/build/python/__init__.pyc"
    "/home/saurabh/Desktop/EE340_Course_Project/gr-gmsk/build/python/gmsk_py_cc.pyc"
    "/home/saurabh/Desktop/EE340_Course_Project/gr-gmsk/build/python/gmsk_demod_py_cc.pyc"
    "/home/saurabh/Desktop/EE340_Course_Project/gr-gmsk/build/python/channel_est_py_ccc.pyc"
    "/home/saurabh/Desktop/EE340_Course_Project/gr-gmsk/build/python/__init__.pyo"
    "/home/saurabh/Desktop/EE340_Course_Project/gr-gmsk/build/python/gmsk_py_cc.pyo"
    "/home/saurabh/Desktop/EE340_Course_Project/gr-gmsk/build/python/gmsk_demod_py_cc.pyo"
    "/home/saurabh/Desktop/EE340_Course_Project/gr-gmsk/build/python/channel_est_py_ccc.pyo"
    )
ENDIF(NOT CMAKE_INSTALL_COMPONENT OR "${CMAKE_INSTALL_COMPONENT}" STREQUAL "Unspecified")


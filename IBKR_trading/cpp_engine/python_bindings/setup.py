from setuptools import setup, Extension
from pybind11.setup_helpers import Pybind11Extension, build_ext
from pybind11 import get_cmake_dir
import pybind11
import numpy

# Define the extension module
ext_modules = [
    Pybind11Extension(
        "ibkr_trading_engine_py",
        [
            "trading_kernels.cpp",
        ],
        include_dirs=[
            # Path to pybind11 headers
            pybind11.get_include(),
            # Path to numpy headers
            numpy.get_include(),
            # Path to Eigen headers (adjust as needed)
            "/usr/include/eigen3",
            # Local include directory
            "../include",
        ],
        libraries=["m"],  # Math library
        language='c++',
        cxx_std=17,
    ),
]

setup(
    name="ibkr_trading_engine_py",
    ext_modules=ext_modules,
    cmdclass={"build_ext": build_ext},
    zip_safe=False,
    python_requires=">=3.8",
)

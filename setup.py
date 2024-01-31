from setuptools import find_packages, setup

setup(
    name="flitton_fib_py",
    version="0.0.1",
    author="Stanislav Sys",
    author_email="github@stasys.org",
    description="Test Library for Rust submodules in Python",
    url="https://github.com/stasys-hub/pyrust-lib",
    install_requires=[],
    packages=find_packages(exclude=("tests",)),
    classifiers=[
        "Development Status :: 4 - Beta",
        "Programming Language :: Python :: 3",
        "Operating System :: OS Independent",
    ],
    entry_points={
        'console_scripts': [
            'fib-number = flitton_fib_py.cmd.fib_numb:fib_numb',
        ],
    },
    python_requires='>=3',
    tests_require=['pytest'],
)

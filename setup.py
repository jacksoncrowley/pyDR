from setuptools import setup, find_packages

# Every subfolder that has an __init__.py becomes pyDR.<folder>
subpackages = find_packages(exclude=["tests", "tests.*", "examples*", "nmr*", "Tutorial*"])

setup(
    packages=["pyDR"] + [f"pyDR.{p}" for p in subpackages],
    package_dir={"pyDR": "."},   # child packages resolve relative to this
)

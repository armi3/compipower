from setuptools import setup

setup(
    name="compiler",
    version="1.0",
    py_modules=["compiler"],
    include_package_data=True,
    install_requires=[
        "click",
    ],
    entry_points="""
        [console_scripts]
        compiler=example:cli
    """,
)
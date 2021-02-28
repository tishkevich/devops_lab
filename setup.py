from setuptools import setup, find_packages

setup(
    name="snapshot",
    packages=find_packages(),
    entry_points={
        "console_scripts": [
            "snapshot = snapshot.snapshot:main",
        ],
    },
    install_requires=[
        'psutil',
        'argparse',

    ],
    version="0.1",
    author="Aliaksandr Tsishkevich",
    author_email="alex.tishkevich@gmail.com",
    description="The snapshot is saved to the file(Homework3)",
)
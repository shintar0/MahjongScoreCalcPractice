from setuptools import setup

setup(
    # install_requires=["requests","beautifulsoup4"],
    package_dir={"": "src"},
    entry_points={
        "console_scripts": [
            "mscp =app:main"
        ]
    }
)
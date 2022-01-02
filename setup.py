from setuptools import setup

setup(
    name="wooly-discogs-browser",
    version="1.0.0",
    description="Views Will's Discogs Catalog.",
    author="Will Kronberg",
    author_email="will@willkronberg.dev",
    url="https://willkronberg.dev",
    install_requires=[
        "certifi==2020.12.5",
        "chardet==4.0.0; python_version >= '2.7' and python_version not in '3.0, 3.1, 3.2, 3.3, 3.4'",
        "idna==2.10; python_version >= '2.7' and python_version not in '3.0, 3.1, 3.2, 3.3'",
        "requests==2.25.1",
        "urllib3==1.26.4; python_version >= '2.7' and python_version not in '3.0, 3.1, 3.2, 3.3, 3.4' and python_version < '4'",
    ],
    setup_requires=["pytest-runner", "flake8"],
    tests_require=["pytest"],
)

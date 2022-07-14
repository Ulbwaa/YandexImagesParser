from setuptools import setup

# Metadata goes in setup.cfg. These are here for GitHub's dependency graph.
setup(
    name="yandex_image_parser",
    install_requires=[
        "beautifulsoup4>=4.11.1",
        "fake-headers>=1.0.2",
        "fake-useragent>=0.1.11",
        "selenium>=4.3.0",
        "selenium-requests>=2.0.0",
    ],
)
from setuptools import setup
import os

VERSION = "0.1a3"


def get_long_description():
    with open(
        os.path.join(os.path.dirname(os.path.abspath(__file__)), "README.md"),
        encoding="utf8",
    ) as fp:
        return fp.read()


setup(
    name="datasette-graphql",
    description="A GraphQL endpoint for Datasette",
    long_description=get_long_description(),
    long_description_content_type="text/markdown",
    author="Simon Willison",
    url="https://github.com/simonw/datasette-graphql",
    project_urls={
        "Issues": "https://github.com/simonw/datasette-graphql/issues",
        "CI": "https://github.com/simonw/datasette-graphql/actions",
        "Changelog": "https://github.com/simonw/datasette-graphql/releases",
    },
    license="Apache License, Version 2.0",
    version=VERSION,
    packages=["datasette_graphql"],
    entry_points={"datasette": ["graphql = datasette_graphql"]},
    install_requires=["datasette", "graphene>=2.0", "sqlite-utils"],
    extras_require={"test": ["pytest", "pytest-asyncio", "httpx"]},
    tests_require=["datasette-graphql[test]"],
    package_data={"datasette_graphql": ["templates/*.html"]},
)
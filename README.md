# datasette-graphql

[![PyPI](https://img.shields.io/pypi/v/datasette-graphql.svg)](https://pypi.org/project/datasette-graphql/)
[![Changelog](https://img.shields.io/github/v/release/simonw/datasette-graphql?include_prereleases&label=changelog)](https://github.com/simonw/datasette-graphql/releases)
[![License](https://img.shields.io/badge/license-Apache%202.0-blue.svg)](https://github.com/simonw/datasette-graphql/blob/master/LICENSE)

A GraphQL endpoint for Datasette

**Work in progress alpha** - this has many missing features.

Try out a live demo at [datasette-graphql-demo.datasette.io/graphql](https://datasette-graphql-demo.datasette.io/graphql?query=%7B%0A%20%20repos%20%7B%0A%20%20%20%20full_name%0A%20%20%20%20id%0A%20%20%7D%0A%7D).

## Installation

Install this plugin in the same environment as Datasette.

    $ pip install datasette-graphql

## Usage

This sets up `/graphql` as a GraphQL endpoint for the first attached database. Individual tables can be queried like this:
```grophql
{
  repos {
    id
    full_name
    description
  }
}
```

If a column is a foreign key to another table, you can request columns of that table using a nested query like this:
```graphql
{
  repos {
    id
    full_name
    owner {
      id
      login
    }
  }
}
```

You can filter the rows returned for a specific table using the `filters:` argument. This accepts a list of filters, where a filter is a string of the form `column=value` or `column__op=value`. For example, to return just repositories with the Apache 2 license and more than 10 stars:

```graphql
{
  repos(filters: ["license=apache-2.0", "stargazers_count__gt=10"]) {
    full_name
    stargazers_count
    license {
      key
    }
  }
}
```
This is the same format used for querystring arguments to the Datasette table view, see [column filter arguments](https://datasette.readthedocs.io/en/stable/json_api.html#column-filter-arguments) in the Datasette documentation.

## Still to come

See [issues](https://github.com/simonw/datasette-graphql/issues) for a full list. Planned improvements include:

- Pagination
- Canned query support
- Ability to allowlist specific tables, views and canned queries

## Development

To set up this plugin locally, first checkout the code. Then create a new virtual environment:

    cd datasette-graphql
    python3 -mvenv venv
    source venv/bin/activate

Or if you are using `pipenv`:

    pipenv shell

Now install the dependencies and tests:

    pip install -e '.[test]'

To run the tests:

    pytest
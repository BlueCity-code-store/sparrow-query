[![Project Status](https://img.shields.io/badge/status-under%20development-yellow)](https://github.com/BlueCity-code-store/sparrow-query)
![GitHub License](https://img.shields.io/github/license/BlueCity-code-store/sparrow-query)

# sparrow-query

This repository provides a small example of how to query the [sparrow](https://sparrow.city/) API from Python, using the API key provided by sparrow and the [requests](https://github.com/psf/requests) package.

## Installation

Start by cloning the repository, for instance using

```bash
git clone git@github.com:BlueCity-code-store/sparrow-query.git
```

To set up the backend environment, you need [pip](https://pip.pypa.io/en/stable/installation/). Then, install the dependencies: 

```bash
pip install -e .
```

## Usage

Create a `.env` file based on the example `.env.example` file, replacing `YOUR_API_KEY` with the actual API key. Then, you can query the API using the following

```bash
python3 -m sparrow_query.get_data
```


# Reporter
Reporter is a simple tool which calculates success rate of the application servers through the REST API

## Getting Started

These instructions will get you a copy of the project up and running on your local machine for development and testing purposes.

### Prerequisites
```
Bash - 4.x
Python - 2.7
Pip - 2.7
virtualenv
mock
requests
```

## Running the script
It's possible to run the script in 2 modes

### I. Fully automated mode with unit test coverage, inside virtualenv
```
bash run.sh [input] [output]
```
where

* `[input]` - file with servers
* `[output]` - output file for reporting

### II. In standalone mode
```
pip2.7 install -r requirements.txt && python2.7 reporter.py [--input] [--output] [--debug]
```
* `--input` - file with servers
* `--output` - output file for reporting
* `--debug` - enable debug output

## Deployment
Deployment could be accomplished with this one-linear
```
mkdir -p $HOME/deploy && mv reporter.tar.gz $HOME/deploy && cd $HOME/deploy && tar -xzvf reporter.tar.gz
```
## Versioning
`1.0.0`

## Authors
* **Evgenii Seliavka** - *Complete work*

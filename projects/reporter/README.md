# Reporter

`projects/reporter` polls application server `/status` endpoints, aggregates request and success counts, and writes a tab-separated report.

## Requirements

- Python 3.10+
- `requests` if you want to run real HTTP requests

## Run

From the repository root:

```bash
python3 -m projects.reporter.reporter --input projects/reporter/servers.txt --output /tmp/output.tsv
```

Options:

- `--input`: file containing server names
- `--output`: destination TSV file
- `--debug`: enable debug logging

## Test

```bash
python3 -m unittest projects.reporter.test_status_reporter -v
```

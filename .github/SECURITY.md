# Security Policy

We take the security of our users and their data very seriously. If you believe you have found a security vulnerability in any of our applications, please let us know right away. We investigate all legitimate reports and do our best to quickly fix the problem.

## Supported Versions

| Version | Supported          |
|---------|--------------------|
| > 0.1   | :white_check_mark: |
| < 0.1   | :x:                |


## Reporting a Vulnerability

If you have any vulnerability please report at daniel@kilobyte.no

## Dependency audit notes

CI runs `pip-audit` against exported requirements. `CVE-2026-4539` is currently ignored in the Code workflow as not applicable to this project's usage; revisit that ignore when the advisory or affected dependency changes.

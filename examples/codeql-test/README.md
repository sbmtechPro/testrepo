# CodeQL custom-query test

This directory contains a deliberately unsafe Python example for testing the
custom CodeQL query in `.github/codeql/custom-queries/avoid-eval.ql`.

The CodeQL workflow runs on every pull request and analyzes Python in addition
to GitHub Actions workflow files. The expected result is a finding on the
`eval(expression)` call in `vulnerable_eval.py`.

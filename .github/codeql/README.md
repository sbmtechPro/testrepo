# CodeQL configuration

This repository enables GitHub's `security-extended` CodeQL query suite via `.github/codeql/codeql-config.yml`.

If you add future custom `.ql` queries, place them under `.github/codeql/` (for example `.github/codeql/queries/`) and reference them from the `queries` section in the config file.

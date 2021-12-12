# Releases

Each release is `MAJOR.MINOR.PATCH`. Some release commands (in the home folder)

```pwsh
Remove-Item .\dist\*
pip uninstall datalines -y
python -m build .
python -m twine upload ./dist/*
pip install datalines
```

Notes:

- When a brand new dataloader or pipeline is added, increment `MINOR`
- When a bug-fix happens, increment `PATCH`
- Currently the package is in alpha, so `MAJOR` is `0`. Once it is more stable, `MAJOR` will become `1`.

## Table of contents

- [Releases](#releases)
    - [Table of contents](#table-of-contents)
    - [Major 0](#major-0)
        - [Minor 1](#minor-1)
            - [Patch 0](#patch-0)

## Major 0

### Minor 1

#### Patch 0

**Version**: `0.1.0` <br>
**Date**: Sunday, 12th December 2021 at 11:20 PM (IST)

- Resolved the [issue 1](https://github.com/TheProjectsGuy/DataLines/issues/1): Addition of BSDS500 dataset

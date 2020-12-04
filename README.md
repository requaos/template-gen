## Email Template Generator

This utility expects a valid MIME formatted email file named `test.eml` located within the `data` directory

#### Repository Structure:
```
data
 \- test.eml
src
 |- requirements.txt
 \- template.py
.gitignore
Dockerfile
Makefile
README.md
```

#### Running this requires `Docker` to be installed:
```
$ make generate
```

If all goes well you will see the output file in your current directory: `output.et`
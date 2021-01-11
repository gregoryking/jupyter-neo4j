# Running Neo4j and VS Code with Binder

[![Binder](https://mybinder.org/badge_logo.svg)](https://mybinder.org/v2/gh/gregoryking/jupyter-neo4j/urlpath=lab)

This repository is a work in progress to get vscode and Neo4j running alongside JupyterLab on binder:

* VSCode - Running and procide
* Neo4j - Runing, but as yet web UI not proxied

For local development use:

```repo2docker -p 8888:8888  . jupyter lab --ip 0.0.0.0 --NotebookApp.token=''```
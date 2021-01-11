import os

def setup_neo4j():
  return {
    'command': ['echo'],
    'port': 7474,
    #The following needs a the labextension installing.
    #eg in postBuild: jupyter labextension install jupyterlab-server-proxy
    'launcher_entry': {
        'title': 'Neo4j',
    },
  }
import setuptools

setuptools.setup(
  name="jupyter-neo4j-server",
  # py_modules rather than packages, since we only have 1 file
  py_modules=['neo4j'],
  entry_points={
      'jupyter_serverproxy_servers': [
          # name = packagename:function_name
          'neo4j = neo4j:setup_neo4j',
      ]
  },
)
"""Common util functions for reading inputs."""
import os


def read_file(relpath: str) -> str:
  root = os.path.dirname(os.path.dirname(__file__))
  abspath = os.path.join(root, relpath)
  with open(abspath) as f:
    content = f.read()
  return content

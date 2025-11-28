"""Common util functions for reading inputs."""
import os

from util import global_vars


def read_input() -> str:
  return read_file_from_workdir("input.txt")


def read_file_from_workdir(filename) -> str:
  module_components = global_vars.VARS["MODULE_COMPONENTS"]
  relpath_segments = module_components[:-1]
  relpath_segments.append(filename)
  return read_file(os.path.join(*relpath_segments))



def read_file(file_relpath) -> str:
  root = os.path.dirname(os.path.dirname(__file__))
  abspath = os.path.join(root, file_relpath)
  with open(abspath) as f:
    content = f.read()
  return content

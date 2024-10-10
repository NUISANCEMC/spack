#!/usr/bin/env python3

import subprocess
from yaml import safe_load, dump
try:
    from yaml import CLoader as Loader, CDumper as Dumper
except ImportError:
    from yaml import Loader, Dumper
from pathlib import Path

rootv = subprocess.run(["root-config", "--version"], capture_output=True, text=True).stdout.rstrip()
root_prefix = subprocess.run(["root-config", "--prefix"], capture_output=True, text=True).stdout.rstrip()
gccv = subprocess.run(["gcc", "-dumpfullversion"], capture_output=True, text=True).stdout.rstrip()
spacka = subprocess.run(["spack", "arch"], capture_output=True, text=True).stdout.rstrip()

root_spec=f"root@{rootv}%gcc@{gccv} arch={spacka}"

print(f"adding root spec: {root_spec} to ~/.spack/packages.yaml as an external")

packages_file = Path("~/.spack/packages.yaml");

if packages_file.is_file():
  doc = safe_load(packages_file.read_text())
  doc["packages"]["root"] = safe_load(f"""packages:
externals:
  - spec: "{root_spec}"
    prefix: {root_prefix}
    extra_attributes:
      environment:
        prepend_path:
          CMAKE_PREFIX_PATH: {root_prefix}
  buildable: False
""")
else:
  doc = safe_load(f"""packages:
  root:
    externals:
    - spec: "{root_spec}"
      prefix: {root_prefix}
      extra_attributes:
        environment:
          prepend_path:
            CMAKE_PREFIX_PATH: {root_prefix}
    buildable: False
""")

docstr = dump(doc)

with open(packages_file.expanduser(), 'w') as f:
  f.write(docstr)
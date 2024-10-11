# Copyright 2013-2024 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *

class Proselecta(CMakePackage):
    """"""

    homepage = "https://github.com/NUISANCEMC/ProSelecta"
    git = "https://github.com/NUISANCEMC/ProSelecta.git"

    tags = ["hep"]

    version("main", branch="main")
    version("v1-RC4", tag="v1-RC4")

    maintainers("luketpickering")

    license("MIT")

    depends_on("cmake@3.18:", type="build")
    depends_on("nuhepmc@v1-RC1+python")
    depends_on("root@6.10:")
    depends_on("catch2@3.3.2:", type="test")

    def cmake_args(self):
        spec = self.spec
        from_variant = self.define_from_variant
        args = [
            self.define("ProSelecta_ENABLE_TESTS", self.run_tests),

        ]
        return args

    def setup_run_environment(self, env):
        env.prepend_path("ProSelecta_INCLUDE_PATH", f"{self.prefix}/include")
        env.prepend_path("ProSelecta_INCLUDE_PATH", f"{self.spec['hepmc3'].prefix}/include")

        py_ver = self.spec["python"].version.up_to(2)
        env.prepend_path("PYTHONPATH", f"{self.prefix}/python/{py_ver}")

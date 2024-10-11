# Copyright 2013-2024 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *

class NuisanceHepdata(CMakePackage):
    """"""

    homepage = "https://github.com/NUISANCEMC/HEPData"
    git = "https://github.com/NUISANCEMC/HEPData.git"

    tags = ["hep"]

    version("main", branch="main")
    version("v1-RC1", tag="v1-RC1")

    maintainers("luketpickering")

    license("MIT")

    variant("python", default=True, description="Enable Python bindings")

    depends_on("cmake@3.17:", type="build")
    depends_on("cpr@1.10.4")
    depends_on("yaml-cpp@0.8:")
    # depends_on("spdlog@1.14.1") # this version of spdlog doesn't allow us to use it's fmt, build our own
    depends_on("python", when="+python")

    def cmake_args(self):
        spec = self.spec
        from_variant = self.define_from_variant
        args = [
            from_variant("NUISANCEHEPData_PYTHON_ENABLED", "python"),
        ]
        return args

    def setup_run_environment(self, env):
        env.set("NUISANCEDB", "~/.nuisance/db")
        if "+python" in self.spec:
          py_ver = self.spec["python"].version.up_to(2)
          env.prepend_path("PYTHONPATH", f"{self.prefix}/python/{py_ver}")
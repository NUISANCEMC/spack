# Copyright 2013-2024 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *

class Nuhepmc(CMakePackage):
    """"""

    homepage = "https://github.com/NuHepMC/cpputils"
    git = "https://github.com/NuHepMC/cpputils.git"

    tags = ["hep"]

    version("stable", tag="stable")

    maintainers("luketpickering")

    license("MIT")

    variant("python", default=True, description="Enable Python bindings")

    depends_on("cmake@3.17:", type="build")
    depends_on("hepmc3@3.3:+protobuf")
    depends_on("eigen@3.4:")
    depends_on("fmt@8.1.1")
    depends_on("python", when="+python")
    depends_on("catch2@3.3.2:", type="test")

    def cmake_args(self):
        spec = self.spec
        from_variant = self.define_from_variant
        args = [
            from_variant("NuHepMC_CPPUtils_PYTHON_ENABLED", "python"),
            self.define("NuHepMC_CPPUtils_ENABLE_TESTS", self.run_tests),

        ]
        return args

    def setup_run_environment(self, env):
        if "+python" in self.spec:
          py_ver = self.spec["python"].version.up_to(2)
          env.prepend_path("PYTHONPATH", f"{self.prefix}/python/{py_ver}")
# Copyright 2013-2024 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *

class Nuisance3(CMakePackage):
    """"""

    homepage = "https://github.com/NUISANCEMC/nuisance3"
    git = "https://github.com/NUISANCEMC/nuisance3.git"

    tags = ["hep"]

    version("main", branch="main")

    maintainers("luketpickering")

    license("MIT")

    variant("arrow", default=True, description="Enable Apache arrow support")
    variant("tests", default=False, description="Build test suite")

    depends_on("cmake@3.17:", type="build")
    depends_on("eigen@3.4:")
    depends_on("yaml-cpp@0.8:")
    # depends_on("spdlog@1.14.1") # this version of spdlog doesn't allow us to use it's fmt, build our own
    depends_on("arrow", when="+arrow")
    depends_on("py-arrow", when="+arrow")
    # don't use these currently before we have proper versioning
    depends_on("nuisance_hepdata@v1-RC1")
    depends_on("proselecta@v1-RC4")

    def cmake_args(self):
        spec = self.spec
        from_variant = self.define_from_variant
        args = [
            from_variant("NUISANCE_USE_ARROW", "arrow"),
            from_variant("NUISANCE_ENABLE_TESTS", "tests"),
            self.define("BUILTIN_NuWro", False),

        ]
        return args

    def setup_run_environment(self, env):
        py_ver = self.spec["python"].version.up_to(2)
        env.prepend_path("PYTHONPATH", f"{self.prefix}/python/{py_ver}")

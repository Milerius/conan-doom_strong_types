from conans import ConanFile, CMake, tools


class DoomstrongtypesConan(ConanFile):
    name = "doom_strong_types"
    version = "1.0.0"
    license = "MIT"
    author = "Doom"
    url = "https://github.com/Milerius/conan-doom_strong_types"
    repo_url = "https://github.com/doom/strong_type"

    description = "C++ implementation of strong types"

    def source(self):
        tools.get("%s/archive/%s.zip" % (self.repo_url, self.version))

    def package(self):
        self.copy("*.hpp", dst="include/st", src="strong_type-%s/include/st/" % self.version)

    def package_id(self):
        self.info.header_only()

from conans import ConanFile, CMake, tools


class HelloWxWidgetsConanFile(ConanFile):
    build_requires = "cmake/3.17.3"
    requires = "sdl2/2.0.12@bincrafters/stable"
    settings = "arch", "build_type", "compiler"
    options = { "sound": ["sdl", "oss"] }
    default_options  = { "sound": "sdl" }
    generators = "virtualenv", "cmake_find_package"
    build_folder = "build"

    def build(self):
        self.build_folder = "build"
        cmake = CMake(self)
        cmake.configure(defs={"SND_BACKEND": self.options.sound})
        cmake.build()


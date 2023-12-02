from pyglet.sprite import Sprite
from Module import Module


class Object(Sprite):
    def __init__(self, img, modules=None, **kwargs):
        super().__init__(img, **kwargs)
        if modules is None:
            modules = {}
        self.modules: dict = modules

    def update_modules(self, dt: float):
        for module in self.modules.values():
            module.update(dt)

    def get_module(self, name: str):
        return self.modules[name]

    def find_modules(self, module_class: str):
        k = []
        for mod in self.modules.values():
            mod: Module
            if module_class == mod.get_module_name():
                k.append(mod)
        return k

    def add_module(self, name: str, module: Module):
        if name in self.modules.keys():
            n = 1
            while name + "_" + str(n) in self.modules.keys():
                n += 1
            name += "_" + str(n)
        self.modules[name] = module

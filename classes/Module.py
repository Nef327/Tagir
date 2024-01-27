class Module:
    def __init__(self, g_object, *args, **kwargs):
        self.object = g_object

    def object(self, g_object):
        self.object = g_object

    def update(self, dt: float):
        pass

    def get_module_name(self):
        st = str(type(self))
        return st[st.find(".") + 1:-2]


if __name__ == "__main__":
    md = Module()
    print(md.get_module_name())
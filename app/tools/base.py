class Tool:

    name = ""
    description = ""
    usage = ""
    example = ""

    def execute(self, *args, **kwargs):
        raise NotImplementedError
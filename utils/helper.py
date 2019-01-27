# utils/helper.py


def load_modules(module_path):
    """
    Dynamically loads python module given it's path
    :param module_path: module path
    :return: python module
    """
    components = module_path.split('.')
    module = __import__(module_path)
    for component in components[1:]:
        module = getattr(module, component)
    return module

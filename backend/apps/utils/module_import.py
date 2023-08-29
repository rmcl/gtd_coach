import importlib


def get_class_by_name(handler_class_path):
    components = handler_class_path.rsplit('.', 1)
    try:
        class_module = importlib.import_module(components[0])
    except ImportError:
        return None

    try:
        handler_class = getattr(class_module, components[1])
    except AttributeError:
        return None

    return handler_class

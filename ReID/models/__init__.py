
from .ResNet import *

__factory = {
    'resnet50': ResNet50,
    'resnet101': ResNet101,
}

def get_names():
    return list(__factory.keys())

def init_model(name, *args, **kwargs):
    if name not in __factory.keys():
        raise KeyError("Unknown model: {}".format(name))
    return __factory[name](*args, **kwargs)
#!/usr/bin/env python3

from trojanzoo.defenses import Defense

from .adv import *
from .backdoor import *

from . import adv, backdoor

from trojanvision.configs import config
import trojanzoo.defenses

import argparse
from trojanzoo.configs import Config
from trojanvision.datasets import ImageSet
from typing import Union

module_list = [adv, backdoor]
__all__ = ['Defense', 'add_argument', 'create']
class_dict: dict[str, type[Defense]] = {}
for module in module_list:
    __all__.extend(module.__all__)
    class_dict.update(module.class_dict)


def add_argument(parser: argparse.ArgumentParser, defense_name: str = None, defense: Union[str, Defense] = None,
                 class_dict: dict[str, type[Defense]] = class_dict):
    return trojanzoo.defenses.add_argument(parser=parser, defense_name=defense_name, defense=defense,
                                           class_dict=class_dict)


def create(defense_name: str = None, defense: Union[str, Defense] = None,
           dataset_name: str = None, dataset: Union[str, ImageSet] = None,
           config: Config = config, class_dict: dict[str, type[Defense]] = class_dict, **kwargs):
    return trojanzoo.defenses.create(defense_name=defense_name, defense=defense,
                                     dataset_name=dataset_name, dataset=dataset,
                                     config=config, class_dict=class_dict, **kwargs)

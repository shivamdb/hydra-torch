# Copyright (c) Facebook, Inc. and its affiliates. All Rights Reserved
#
# Generated by configen, do not edit.
# See https://github.com/facebookresearch/hydra/tree/master/tools/configen
# fmt: off
# isort:skip_file
# flake8: noqa

from dataclasses import dataclass, field
from typing import Any


@dataclass
class SqueezeNetConf:
    _target_: str = "torchvision.models.squeezenet.SqueezeNet"
    version: Any = "1_0"
    num_classes: Any = 1000

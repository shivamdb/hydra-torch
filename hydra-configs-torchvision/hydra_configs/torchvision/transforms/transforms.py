# Copyright (c) Facebook, Inc. and its affiliates. All Rights Reserved
#
# Generated by configen, do not edit.
# See https://github.com/facebookresearch/hydra/tree/master/tools/configen
# fmt: off
# isort:skip_file
# flake8: noqa

from dataclasses import dataclass, field
from omegaconf import MISSING
from typing import Any


@dataclass
class CenterCropConf:
    _target_: str = "torchvision.transforms.transforms.CenterCrop"
    _convert_: str = "ALL"
    size: Any = MISSING


@dataclass
class ColorJitterConf:
    _target_: str = "torchvision.transforms.transforms.ColorJitter"
    _convert_: str = "ALL"
    brightness: Any = 0
    contrast: Any = 0
    saturation: Any = 0
    hue: Any = 0


@dataclass
class ComposeConf:
    _target_: str = "torchvision.transforms.transforms.Compose"
    _convert_: str = "ALL"
    transforms: Any = MISSING


@dataclass
class ConvertImageDtypeConf:
    _target_: str = "torchvision.transforms.transforms.ConvertImageDtype"
    _convert_: str = "ALL"
    dtype: Any = MISSING  # dtype


@dataclass
class FiveCropConf:
    _target_: str = "torchvision.transforms.transforms.FiveCrop"
    _convert_: str = "ALL"
    size: Any = MISSING


@dataclass
class GrayscaleConf:
    _target_: str = "torchvision.transforms.transforms.Grayscale"
    _convert_: str = "ALL"
    num_output_channels: Any = 1


@dataclass
class LambdaConf:
    _target_: str = "torchvision.transforms.transforms.Lambda"
    _convert_: str = "ALL"
    lambd: Any = MISSING


@dataclass
class LinearTransformationConf:
    _target_: str = "torchvision.transforms.transforms.LinearTransformation"
    _convert_: str = "ALL"
    transformation_matrix: Any = MISSING
    mean_vector: Any = MISSING


@dataclass
class NormalizeConf:
    _target_: str = "torchvision.transforms.transforms.Normalize"
    _convert_: str = "ALL"
    mean: Any = MISSING
    std: Any = MISSING
    inplace: Any = False


@dataclass
class PadConf:
    _target_: str = "torchvision.transforms.transforms.Pad"
    _convert_: str = "ALL"
    padding: Any = MISSING
    fill: Any = 0
    padding_mode: Any = "constant"


@dataclass
class PILToTensorConf:
    _target_: str = "torchvision.transforms.transforms.PILToTensor"
    _convert_: str = "ALL"


@dataclass
class RandomAffineConf:
    _target_: str = "torchvision.transforms.transforms.RandomAffine"
    _convert_: str = "ALL"
    degrees: Any = MISSING
    translate: Any = None
    scale: Any = None
    shear: Any = None
    resample: Any = 0
    fillcolor: Any = 0


@dataclass
class RandomApplyConf:
    _target_: str = "torchvision.transforms.transforms.RandomApply"
    _convert_: str = "ALL"
    transforms: Any = MISSING
    p: Any = 0.5


@dataclass
class RandomChoiceConf:
    _target_: str = "torchvision.transforms.transforms.RandomChoice"
    _convert_: str = "ALL"
    transforms: Any = MISSING


@dataclass
class RandomCropConf:
    _target_: str = "torchvision.transforms.transforms.RandomCrop"
    _convert_: str = "ALL"
    size: Any = MISSING
    padding: Any = None
    pad_if_needed: Any = False
    fill: Any = 0
    padding_mode: Any = "constant"


@dataclass
class RandomErasingConf:
    _target_: str = "torchvision.transforms.transforms.RandomErasing"
    _convert_: str = "ALL"
    p: Any = 0.5
    scale: Any = (0.02, 0.33)
    ratio: Any = (0.3, 3.3)
    value: Any = 0
    inplace: Any = False


@dataclass
class RandomGrayscaleConf:
    _target_: str = "torchvision.transforms.transforms.RandomGrayscale"
    _convert_: str = "ALL"
    p: Any = 0.1


@dataclass
class RandomHorizontalFlipConf:
    _target_: str = "torchvision.transforms.transforms.RandomHorizontalFlip"
    _convert_: str = "ALL"
    p: Any = 0.5


@dataclass
class RandomOrderConf:
    _target_: str = "torchvision.transforms.transforms.RandomOrder"
    _convert_: str = "ALL"
    transforms: Any = MISSING


@dataclass
class RandomPerspectiveConf:
    _target_: str = "torchvision.transforms.transforms.RandomPerspective"
    _convert_: str = "ALL"
    distortion_scale: Any = 0.5
    p: Any = 0.5
    interpolation: Any = 2
    fill: Any = 0


@dataclass
class RandomResizedCropConf:
    _target_: str = "torchvision.transforms.transforms.RandomResizedCrop"
    _convert_: str = "ALL"
    size: Any = MISSING
    scale: Any = (0.08, 1.0)
    ratio: Any = (0.75, 1.3333333333333333)
    interpolation: Any = 2


@dataclass
class RandomRotationConf:
    _target_: str = "torchvision.transforms.transforms.RandomRotation"
    _convert_: str = "ALL"
    degrees: Any = MISSING
    resample: Any = False
    expand: Any = False
    center: Any = None
    fill: Any = None


@dataclass
class RandomTransformsConf:
    _target_: str = "torchvision.transforms.transforms.RandomTransforms"
    _convert_: str = "ALL"
    transforms: Any = MISSING


@dataclass
class RandomVerticalFlipConf:
    _target_: str = "torchvision.transforms.transforms.RandomVerticalFlip"
    _convert_: str = "ALL"
    p: Any = 0.5


@dataclass
class ResizeConf:
    _target_: str = "torchvision.transforms.transforms.Resize"
    _convert_: str = "ALL"
    size: Any = MISSING
    interpolation: Any = 2


@dataclass
class TenCropConf:
    _target_: str = "torchvision.transforms.transforms.TenCrop"
    _convert_: str = "ALL"
    size: Any = MISSING
    vertical_flip: Any = False


@dataclass
class ToPILImageConf:
    _target_: str = "torchvision.transforms.transforms.ToPILImage"
    _convert_: str = "ALL"
    mode: Any = None


@dataclass
class ToTensorConf:
    _target_: str = "torchvision.transforms.transforms.ToTensor"
    _convert_: str = "ALL"

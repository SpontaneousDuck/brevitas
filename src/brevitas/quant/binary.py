from brevitas.quant.base import SignedBinaryClampedConst
from brevitas.core.function_wrapper import InplaceTensorClampSte, TensorClamp
from brevitas.quant.solver import WeightQuantSolver, ActQuantSolver


__all__ = [
    'SignedBinaryClampedConst',
    'SignedBinaryActClampedConst'
]


class SignedBinaryWeightInplaceClampedConst(SignedBinaryClampedConst, WeightQuantSolver):
    """
    Signed binary weight quantizer with constant scale factor and inplace clipping to the scale.

    Examples:
        >>> from brevitas.nn import QuantLinear
        >>> fc = QuantLinear(10, 5, bias=False, weight_quant=SignedBinaryWeightInplaceClampedConst)
        >>> fc.quant_weight()
    """
    tensor_clamp_impl = InplaceTensorClampSte
    scaling_const = 1.0


class SignedBinaryActClampedConst(SignedBinaryClampedConst, ActQuantSolver):
    """
    Examples:
        >>> from brevitas.nn import QuantIdentity
        >>> act = QuantIdentity(act_quant=SignedBinaryActClampedConst)
    """
    tensor_clamp_impl = TensorClamp
    min_val = -1.0
    max_val = 1.0



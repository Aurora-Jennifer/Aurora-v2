"""
Live Trading System - IBKR Integration
=====================================

Complete live trading system integrating all trained models (tabular + sequential + multi-task)
across all horizons and strategies for IBKR trading.
"""

__version__ = "2.0.0"
__author__ = "Trading System Team"

# Import main components
from .main_loop import LiveTradingSystem, LiveTradingManager
from .model_predictor import ModelPredictor, ModelRegistry
from .horizon_blender import HorizonBlender, AdvancedBlender
from .barrier_gate import BarrierGate, AdvancedBarrierGate, BarrierProbabilityProvider
from .cost_arbitrator import CostArbitrator, CostModel, AdvancedCostModel
from .position_sizer import PositionSizer, AdvancedPositionSizer, PositionValidator

__all__ = [
    # Main system
    'LiveTradingSystem',
    'LiveTradingManager',
    
    # Core components
    'ModelPredictor',
    'ModelRegistry',
    'HorizonBlender',
    'AdvancedBlender',
    'BarrierGate',
    'AdvancedBarrierGate',
    'BarrierProbabilityProvider',
    'CostArbitrator',
    'CostModel',
    'AdvancedCostModel',
    'PositionSizer',
    'AdvancedPositionSizer',
    'PositionValidator',
]

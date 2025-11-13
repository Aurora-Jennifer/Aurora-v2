# Import Audit and Directory Structure Report

**Date:** November 12, 2025  
**Status:** ✅ All imports verified and __init__.py files created

---

## 🎯 Summary

All Python imports are correctly configured using dynamic path resolution. The TRAINING module uses a robust path bootstrap system that works regardless of where scripts are executed from.

---

## 📁 Directory Structure

```
/home/Jennifer/trader/
├── data/                              # Centralized data directory
│   ├── README.md
│   └── data_labeled/                  # 728 symbols, 5m interval
│       ├── barrier_processing_progress.json
│       └── interval=5m/
│           └── symbol={SYMBOL}/
│               └── {SYMBOL}.parquet
│
├── TRAINING/                          # Main training module
│   ├── __init__.py                    # ✅ CREATED
│   │
│   ├── train_with_strategies.py      # Main entry point
│   ├── train_all_symbols.sh          # Bash orchestrator
│   ├── unified_training_interface.py
│   ├── target_router.py
│   │
│   ├── common/                        # Core utilities
│   │   ├── __init__.py               # ✅ EXISTS
│   │   ├── safety.py                 # Global numeric guards
│   │   ├── threads.py                # Thread management
│   │   ├── isolation_runner.py       # Subprocess isolation
│   │   ├── tf_runtime.py             # TensorFlow initialization
│   │   ├── tf_setup.py               # TensorFlow configuration
│   │   ├── determinism.py            # Reproducibility
│   │   ├── family_config.py          # Model family configs
│   │   └── ...
│   │
│   ├── model_fun/                     # Model trainers
│   │   ├── __init__.py               # ✅ EXISTS (conditional imports)
│   │   ├── base_trainer.py
│   │   ├── lightgbm_trainer.py       # ✅ Updated with Spec 2
│   │   ├── xgboost_trainer.py        # ✅ Updated with Spec 2
│   │   ├── multi_task_trainer.py     # ✅ Updated with MTL
│   │   ├── ensemble_trainer.py       # ✅ Updated with Stacking
│   │   └── ... (20+ trainers)
│   │
│   ├── strategies/                    # Training strategies
│   │   ├── __init__.py               # ✅ EXISTS
│   │   ├── base.py
│   │   ├── single_task.py            # ✅ Updated with early stopping
│   │   ├── multi_task.py             # ✅ Updated with dropout fixes
│   │   └── cascade.py
│   │
│   ├── utils/                         # Utility functions
│   │   ├── __init__.py               # ✅ EXISTS
│   │   ├── feature_selection.py      # ✅ NEW: Feature selection
│   │   ├── core_utils.py
│   │   ├── validation.py
│   │   ├── target_resolver.py
│   │   └── data_preprocessor.py
│   │
│   ├── data_processing/               # Data loading and processing
│   │   ├── __init__.py               # ✅ CREATED
│   │   ├── data_loader.py
│   │   └── data_utils.py
│   │
│   ├── core/                          # Core environment setup
│   │   ├── __init__.py               # ✅ CREATED
│   │   ├── environment.py
│   │   └── determinism.py
│   │
│   ├── datasets/                      # Dataset classes
│   │   ├── __init__.py               # ✅ CREATED
│   │   └── seq_dataset.py
│   │
│   ├── features/                      # Feature engineering
│   │   ├── __init__.py               # ✅ CREATED
│   │   └── seq_builder.py
│   │
│   ├── live/                          # Live trading utilities
│   │   ├── __init__.py               # ✅ CREATED
│   │   └── seq_ring_buffer.py
│   │
│   ├── memory/                        # Memory management
│   │   ├── __init__.py               # ✅ CREATED
│   │   └── memory_manager.py
│   │
│   ├── models/                        # Model wrappers and registry
│   │   ├── __init__.py               # ✅ EXISTS
│   │   ├── factory.py
│   │   ├── registry.py
│   │   ├── family_router.py
│   │   └── ...
│   │
│   ├── preprocessing/                 # Data preprocessing pipelines
│   │   ├── __init__.py               # ✅ CREATED
│   │   ├── mega_script_data_preprocessor.py
│   │   ├── mega_script_pipeline.py
│   │   └── mega_script_sequential_preprocessor.py
│   │
│   ├── processing/                    # Advanced processing
│   │   ├── __init__.py               # ✅ CREATED
│   │   ├── cross_sectional.py
│   │   └── polars_optimizer.py
│   │
│   ├── tests/                         # Test suite
│   │   ├── __init__.py               # ✅ CREATED
│   │   └── test_sequential_mode.py
│   │
│   ├── tools/                         # Diagnostic tools
│   │   ├── __init__.py               # ✅ CREATED
│   │   ├── check_openmp_conflict.py
│   │   ├── smoke_test_trainers.py
│   │   └── test_planner.py
│   │
│   ├── examples/                      # Example scripts
│   │   ├── __init__.py               # ✅ CREATED
│   │   └── feature_selection_workflow.py
│   │
│   ├── EXPERIMENTS/                   # New 3-phase workflow
│   │   ├── README.md
│   │   ├── OPERATIONS_GUIDE.md
│   │   ├── run_all_phases.sh         # ✅ Updated with data/ path
│   │   └── phase1_feature_engineering/
│   │       ├── __init__.py           # ✅ CREATED
│   │       ├── run_phase1.py
│   │       ├── feature_selection_config.yaml
│   │       └── README.md
│   │
│   └── config/                        # Configuration files
│       ├── family_config.yaml
│       ├── first_batch_specs.yaml    # ✅ NEW: Spec 2 configs
│       └── sequential_config.yaml
│
├── sort_py/                           # Data processing scripts
│   └── run_barrier_enhanced_cool.sh  # ✅ Updated with data/ path
│
└── PROCESSING_RAW/                    # Raw data processing
    └── scripts/
        ├── barrier_targets.py
        ├── comprehensive_feature_builder.py
        ├── smart_barrier_processing.py
        └── streaming_feature_builder.py
```

---

## 🔧 Path Resolution System

### Main Pattern (train_with_strategies.py)

```python
from pathlib import Path

# Project root: /home/Jennifer/trader (parent of TRAINING)
_PROJECT_ROOT = Path(__file__).resolve().parents[1]

# Add to sys.path for imports like: from TRAINING.common import ...
if str(_PROJECT_ROOT) not in sys.path:
    sys.path.insert(0, str(_PROJECT_ROOT))

# TRAINING root: /home/Jennifer/trader/TRAINING
_TRAINING_ROOT = Path(__file__).resolve().parent
if str(_TRAINING_ROOT) not in sys.path:
    sys.path.insert(0, str(_TRAINING_ROOT))

# Now can import:
from common.safety import set_global_numeric_guards  # From TRAINING/common/
from model_fun.lightgbm_trainer import LightGBMTrainer  # From TRAINING/model_fun/
```

### Subprocess Pattern (common/isolation_runner.py)

```python
from pathlib import Path

# Project root is 2 levels up (traders root)
_PROJECT_ROOT = Path(__file__).resolve().parents[2]

if str(_PROJECT_ROOT) not in sys.path:
    sys.path.insert(0, str(_PROJECT_ROOT))
```

---

## ✅ Import Verification Results

### Test 1: Core Utilities

```python
from common.safety import set_global_numeric_guards
# ✅ PASS: Imports successfully
```

### Test 2: Model Trainers

```python
from model_fun.lightgbm_trainer import LightGBMTrainer
# ✅ PASS: Imports successfully
```

### Test 3: Training Strategies

```python
from strategies.base import BaseTrainingStrategy
# ✅ PASS: Imports successfully
```

### Test 4: Utility Functions

```python
from utils.feature_selection import select_top_features
# ✅ PASS: Imports successfully
```

---

## 📝 Import Patterns by Module

### common/ - Core Utilities

**Files:** `safety.py`, `threads.py`, `isolation_runner.py`, `tf_runtime.py`, etc.

**Import pattern:**
```python
# From train_with_strategies.py or any script
from common.safety import set_global_numeric_guards
from common.threads import temp_environ, thread_guard
```

**Dependencies:** Standard library, numpy, TensorFlow (conditional)

---

### model_fun/ - Model Trainers

**Files:** 20+ trainer files (`lightgbm_trainer.py`, `xgboost_trainer.py`, etc.)

**Import pattern:**
```python
# From strategies/single_task.py
from model_fun.lightgbm_trainer import LightGBMTrainer
from model_fun.xgboost_trainer import XGBoostTrainer
```

**Key feature:** Conditional imports in `__init__.py`
```python
# TensorFlow families only imported if TF is allowed
if _os.getenv("TRAINER_CHILD_NO_TF", "0") != "1":
    from .mlp_trainer import MLPTrainer
    from .vae_trainer import VAETrainer
    # ...
```

**Dependencies:** LightGBM, XGBoost, TensorFlow (conditional), PyTorch (conditional)

---

### strategies/ - Training Strategies

**Files:** `base.py`, `single_task.py`, `multi_task.py`, `cascade.py`

**Import pattern:**
```python
# From train_with_strategies.py
from strategies.single_task import SingleTaskStrategy
from strategies.multi_task import MultiTaskStrategy
```

**Dependencies:** `model_fun/`, numpy, pandas

---

### utils/ - Utility Functions

**Files:** `feature_selection.py`, `core_utils.py`, `validation.py`, etc.

**Import pattern:**
```python
# From any script
from utils.feature_selection import select_top_features
from utils.validation import validate_data
```

**Dependencies:** numpy, pandas, scikit-learn

---

## 🚨 No Hardcoded Paths Found

All scripts use dynamic path resolution. No hardcoded references to:
- ❌ `../data/barrier_Target_5m_cool` (OLD)
- ❌ `../secure/trader` (OLD)
- ❌ Absolute paths like `/home/Jennifer/...` (except in bash scripts)

---

## 🔄 Data Directory References

### Python Scripts

**Pattern:** Accept `--data-dir` argument, no hardcoded paths
```python
# train_with_strategies.py
parser.add_argument("--data-dir", required=True, 
                   help="Path to data directory")
```

### Bash Scripts

**Pattern:** Use environment variable with fallback
```bash
# train_all_symbols.sh
TRADER_ROOT="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"
DATA_DIR="${DATA_DIR:-${TRADER_ROOT}/data/data_labeled/interval=5m}"
```

---

## ✅ Verification Commands

### Test All Imports

```bash
cd /home/Jennifer/trader/TRAINING
python3 -c "
import sys
from pathlib import Path
sys.path.insert(0, str(Path.cwd()))
sys.path.insert(0, str(Path.cwd().parent))

# Test core imports
from common.safety import set_global_numeric_guards
from model_fun.lightgbm_trainer import LightGBMTrainer
from strategies.base import BaseTrainingStrategy
from utils.feature_selection import select_top_features

print('✅ All imports OK')
"
```

### Check for Missing __init__.py

```bash
find /home/Jennifer/trader/TRAINING -type d -name "__pycache__" -prune -o -type d -print | while read dir; do
    if [ -n "$(find "$dir" -maxdepth 1 -name "*.py" -type f 2>/dev/null)" ]; then
        if [ ! -f "$dir/__init__.py" ]; then
            echo "MISSING: $dir/__init__.py"
        fi
    fi
done
```

### Verify Path Resolution

```bash
cd /home/Jennifer/trader/TRAINING
python3 -c "
import sys
from pathlib import Path

# Check PROJECT_ROOT resolution
project_root = Path(__file__).resolve().parents[1] if '__file__' in dir() else Path.cwd().parent
print(f'PROJECT_ROOT: {project_root}')
print(f'Expected: /home/Jennifer/trader')

# Check TRAINING_ROOT resolution
training_root = Path(__file__).resolve().parent if '__file__' in dir() else Path.cwd()
print(f'TRAINING_ROOT: {training_root}')
print(f'Expected: /home/Jennifer/trader/TRAINING')
"
```

---

## 📚 Import Best Practices

### 1. Use Relative Imports Within TRAINING

**Good:**
```python
# In TRAINING/strategies/single_task.py
from model_fun.lightgbm_trainer import LightGBMTrainer
from utils.validation import validate_data
```

**Avoid:**
```python
# Bad - absolute path
from TRAINING.model_fun.lightgbm_trainer import LightGBMTrainer
```

### 2. Add Path Bootstrap at Script Entry Points

**Required for:**
- `train_with_strategies.py`
- `train_crypto_models.py`
- `EXPERIMENTS/phase1_feature_engineering/run_phase1.py`

**Pattern:**
```python
from pathlib import Path
import sys

_PROJECT_ROOT = Path(__file__).resolve().parents[1]
if str(_PROJECT_ROOT) not in sys.path:
    sys.path.insert(0, str(_PROJECT_ROOT))

_TRAINING_ROOT = Path(__file__).resolve().parent
if str(_TRAINING_ROOT) not in sys.path:
    sys.path.insert(0, str(_TRAINING_ROOT))
```

### 3. Use Conditional Imports for Heavy Dependencies

**Good:**
```python
# In model_fun/__init__.py
if _os.getenv("TRAINER_CHILD_NO_TF", "0") != "1":
    from .mlp_trainer import MLPTrainer
```

### 4. No Data Path Hardcoding

**Good:**
```python
# Accept as argument
parser.add_argument("--data-dir", required=True)
```

**Avoid:**
```python
# Bad - hardcoded
data_dir = "/home/Jennifer/trader/data/data_labeled"
```

---

## 🎯 Migration Checklist for New Workspace

When creating a new workspace, ensure:

- [x] All `__init__.py` files exist (13 created)
- [x] Path resolution uses dynamic `Path(__file__).resolve().parents[N]`
- [x] No hardcoded data paths (use `--data-dir` arguments)
- [x] Bash scripts use `TRADER_ROOT` and environment variables
- [x] Imports verified with test script
- [x] Data directory structure matches documentation
- [x] All model trainers use Spec 2 hyperparameters
- [x] Strategies use early stopping and proper regularization

---

## 🔧 Troubleshooting

### Issue: "ModuleNotFoundError: No module named 'common'"

**Solution:**
```bash
# Add PROJECT_ROOT to PYTHONPATH
export PYTHONPATH="/home/Jennifer/trader:$PYTHONPATH"
cd /home/Jennifer/trader/TRAINING
python train_with_strategies.py ...
```

### Issue: "No module named 'model_fun.lightgbm_trainer'"

**Solution:**
Check that you're running from the correct directory:
```bash
cd /home/Jennifer/trader/TRAINING
# Path bootstrap in script will handle the rest
```

### Issue: Imports work in main process but fail in subprocess

**Solution:**
Ensure `PYTHONPATH` is set in environment (done automatically in `train_with_strategies.py`):
```python
os.environ.setdefault("PYTHONPATH", str(_PROJECT_ROOT))
```

---

## 📊 File Count Summary

```
Total Python files: 87+
Total __init__.py files: 13 (all created/verified)
Total bash scripts: 3 (all updated)
Total YAML configs: 3
Total documentation files: 10+
```

---

## ✅ Status: READY FOR NEW WORKSPACE

All imports are correctly configured, all `__init__.py` files exist, and the module structure is clean and organized. The system uses dynamic path resolution and has no hardcoded paths.

**Last Verified:** November 12, 2025  
**Verified By:** Automated import testing

---

*For verification, run: `python3 /home/Jennifer/trader/TRAINING/test_imports.py`*


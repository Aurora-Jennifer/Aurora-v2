# Environment Setup Guide

Complete guide to setting up the trading system environment with GPU support.

## Quick Setup (Recommended)

### 1. Create Conda Environment

```bash
cd /home/Jennifer/trader
conda env create -f environment.yml
```

This will create a new `trader_env` environment with all dependencies.

### 2. Activate Environment

```bash
conda activate trader_env
```

### 3. Build LightGBM with CUDA

```bash
bash scripts/build_lightgbm_cuda.sh
```

Or manually:

```bash
cd /tmp
git clone --recursive --depth 1 https://github.com/microsoft/LightGBM
cd LightGBM
mkdir build && cd build
cmake -DUSE_CUDA=1 -DCUDA_ARCHITECTURES=86 ..  # 86 for RTX 3080
make -j$(nproc)
cd ../python-package
pip install -e .
```

### 4. Verify Setup

```bash
cd /home/Jennifer/trader
python scripts/check_gpu_setup.py
```

Should show:
```
✅ CUDA: ENABLED
✅ LightGBM GPU support: ENABLED
```

### 5. Test GPU Feature Selection

```bash
# Test with one symbol
python scripts/select_features.py --symbols AAPL

# Run full pipeline
python scripts/select_features.py
```

## Alternative: Update Existing Environment

If you already have `trader_env`:

```bash
# Update with new packages
conda activate trader_env
conda env update -f environment.yml --prune

# Rebuild LightGBM with CUDA
bash scripts/build_lightgbm_cuda.sh
```

## Alternative: Pure Pip Installation

If not using conda:

```bash
# Create virtual environment
python -m venv trader_env
source trader_env/bin/activate  # On Linux/Mac
# or: trader_env\Scripts\activate  # On Windows

# Install system dependencies first (Arch Linux)
sudo pacman -S cuda cudnn cmake gcc make

# Install Python packages
pip install -r requirements.txt

# Build LightGBM with CUDA
bash scripts/build_lightgbm_cuda.sh
```

## GPU Architecture Reference

If you have a different GPU, change `CUDA_ARCHITECTURES` in the build command:

| GPU Series | Architecture | Code |
|------------|--------------|------|
| GTX 1050/1060 | Pascal | 61 |
| GTX 1070/1080 | Pascal | 61 |
| GTX 1080 Ti | Pascal | 61 |
| RTX 2060/2070/2080 | Turing | 75 |
| RTX 3060/3070/3080/3090 | Ampere | 86 |
| RTX 4070/4080/4090 | Ada Lovelace | 89 |
| Tesla V100 | Volta | 70 |
| A100 | Ampere | 80 |

Example for RTX 2080:
```bash
cmake -DUSE_CUDA=1 -DCUDA_ARCHITECTURES=75 ..
```

## Troubleshooting

### CMake Error

If you get CMAKE_ROOT errors:

```bash
sudo pacman -R cmake
sudo pacman -S cmake
```

### LightGBM Import Error

If `import lightgbm` fails:

```bash
pip uninstall -y lightgbm
# Then rebuild from source (see step 3 above)
```

### CUDA Version Mismatch

Check your CUDA version:

```bash
nvcc --version  # Should show CUDA 13.0 or similar
nvidia-smi      # Shows driver version
```

If using conda, ensure cudatoolkit matches:

```bash
conda install cudatoolkit=12.1  # Closest to CUDA 13.0
```

### Out of Memory (VRAM)

If you get CUDA OOM errors:

Edit `CONFIG/feature_selection_config.yaml`:

```yaml
max_bin: 31           # Reduce from 63
num_leaves: 15        # Reduce from 31
n_estimators: 300     # Reduce from 500
```

Or process fewer symbols at once:

```bash
python scripts/select_features.py --symbols AAPL,MSFT,GOOGL
```

## Verifying Installation

Run these commands to verify everything:

```bash
# Check Python environment
python --version  # Should be 3.10

# Check key packages
python -c "import numpy; print(f'NumPy: {numpy.__version__}')"
python -c "import pandas; print(f'Pandas: {pandas.__version__}')"
python -c "import torch; print(f'PyTorch: {torch.__version__}')"

# Check GPU access
python -c "import torch; print(f'CUDA available: {torch.cuda.is_available()}')"
python -c "import torch; print(f'GPU: {torch.cuda.get_device_name(0)}')"

# Check LightGBM
python scripts/check_gpu_setup.py
```

## Environment Variables (Optional)

Add to `~/.bashrc` or `~/.zshrc`:

```bash
# CUDA paths
export PATH=/opt/cuda/bin:$PATH
export LD_LIBRARY_PATH=/opt/cuda/lib64:$LD_LIBRARY_PATH

# For better CPU performance
export OMP_NUM_THREADS=$(nproc)
export MKL_NUM_THREADS=$(nproc)
```

## Package Versions

The environment file specifies minimum versions. You can update packages:

```bash
conda activate trader_env
conda update --all

# Or specific packages
pip install --upgrade numpy pandas scikit-learn
```

## Clean Installation

To start completely fresh:

```bash
# Remove old environment
conda env remove -n trader_env

# Remove cached packages
conda clean --all

# Recreate
conda env create -f environment.yml
```

## Next Steps

After setup is complete:

1. ✅ Verify GPU: `python scripts/check_gpu_setup.py`
2. ✅ Test feature selection: `python scripts/select_features.py --symbols AAPL`
3. ✅ Check config: Review `CONFIG/feature_selection_config.yaml`
4. ✅ Read guides: `scripts/QUICK_START_GPU.md`
5. ✅ Run pipeline: `python scripts/select_features.py`

## Support

If issues persist:

1. Check logs for specific errors
2. Verify CUDA installation: `nvidia-smi`
3. Check environment: `conda list`
4. Test with CPU mode first (set `device: "cpu"` in config)

---

**Environment ready!** 🚀 Run `python scripts/select_features.py` to start GPU-accelerated feature selection.


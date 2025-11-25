#!/bin/bash
# Quick Setup Script for Trading System with GPU Support
# For Arch Linux with NVIDIA GPU

set -e  # Exit on error

echo "╔════════════════════════════════════════════════════════════╗"
echo "║     Trading System Setup - GPU Accelerated                ║"
echo "╚════════════════════════════════════════════════════════════╝"
echo ""

# Check if we're in the right directory
if [ ! -f "environment.yml" ]; then
    echo "❌ Please run this script from the trader directory"
    exit 1
fi

# Check for conda
if ! command -v conda &> /dev/null; then
    echo "❌ Conda not found. Please install Miniconda or Anaconda first."
    echo "   Visit: https://docs.conda.io/en/latest/miniconda.html"
    exit 1
fi

# Check for CUDA
if ! command -v nvidia-smi &> /dev/null; then
    echo "❌ NVIDIA driver not found. Please install NVIDIA drivers."
    exit 1
fi

GPU_NAME=$(nvidia-smi --query-gpu=name --format=csv,noheader | head -n1)
echo "✅ GPU detected: $GPU_NAME"
echo ""

# Step 1: Create environment
echo "━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━"
echo "Step 1: Creating conda environment..."
echo "━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━"
echo ""

if conda env list | grep -q "^trader_env "; then
    echo "⚠️  Environment 'trader_env' already exists."
    read -p "Remove and recreate? [y/N] " -n 1 -r
    echo
    if [[ $REPLY =~ ^[Yy]$ ]]; then
        conda env remove -n trader_env -y
    else
        echo "Skipping environment creation."
        conda activate trader_env
    fi
fi

if ! conda env list | grep -q "^trader_env "; then
    echo "Creating trader_env environment..."
    conda env create -f environment.yml
fi

echo ""
echo "✅ Environment created/verified"
echo ""

# Step 2: Activate and build LightGBM
echo "━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━"
echo "Step 2: Building LightGBM with CUDA support..."
echo "━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━"
echo ""

# Activate environment
eval "$(conda shell.bash hook)"
conda activate trader_env

echo "Environment activated: $(conda info --envs | grep '*')"
echo ""

# Build LightGBM
if [ -f "scripts/build_lightgbm_cuda.sh" ]; then
    bash scripts/build_lightgbm_cuda.sh
else
    echo "⚠️  Automated build script not found. Building manually..."
    
    cd /tmp
    rm -rf LightGBM_setup
    git clone --recursive --depth 1 https://github.com/microsoft/LightGBM LightGBM_setup
    cd LightGBM_setup
    mkdir build && cd build
    
    # Detect GPU architecture
    COMPUTE_CAP=$(nvidia-smi --query-gpu=compute_cap --format=csv,noheader | head -n1 | tr -d '.' | tr -d ' ')
    echo "Building for compute capability: $COMPUTE_CAP"
    
    cmake -DUSE_CUDA=1 -DCUDA_ARCHITECTURES=$COMPUTE_CAP ..
    make -j$(nproc)
    
    cd ../python-package
    pip uninstall -y lightgbm || true
    pip install -e .
    
    cd /home/Jennifer/trader
fi

# Step 3: Verify
echo ""
echo "━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━"
echo "Step 3: Verifying installation..."
echo "━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━"
echo ""

python scripts/check_gpu_setup.py

echo ""
echo "╔════════════════════════════════════════════════════════════╗"
echo "║                    Setup Complete! 🎉                      ║"
echo "╚════════════════════════════════════════════════════════════╝"
echo ""
echo "Next steps:"
echo ""
echo "  1. Activate environment (if not already):"
echo "     conda activate trader_env"
echo ""
echo "  2. Test with one symbol:"
echo "     python scripts/select_features.py --symbols AAPL"
echo ""
echo "  3. Run full feature selection:"
echo "     python scripts/select_features.py"
echo ""
echo "  4. Monitor GPU usage:"
echo "     watch -n 1 nvidia-smi"
echo ""
echo "Configuration: CONFIG/feature_selection_config.yaml"
echo "Documentation: ENVIRONMENT_SETUP.md"
echo ""


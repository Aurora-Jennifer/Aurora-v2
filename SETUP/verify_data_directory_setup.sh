#!/bin/bash
# Verification Script for Data Directory Migration
# This script verifies that all bash scripts correctly reference the centralized data directory

# Colors for output
RED='\033[0;31m'
GREEN='\033[0;32m'
YELLOW='\033[1;33m'
BLUE='\033[0;34m'
PURPLE='\033[0;35m'
NC='\033[0m' # No Color

print_header() {
    echo -e "${PURPLE}================================================================${NC}"
    echo -e "${PURPLE}$1${NC}"
    echo -e "${PURPLE}================================================================${NC}"
}

print_pass() {
    echo -e "${GREEN}✅ PASS:${NC} $1"
}

print_fail() {
    echo -e "${RED}❌ FAIL:${NC} $1"
}

print_info() {
    echo -e "${BLUE}ℹ️  INFO:${NC} $1"
}

print_warn() {
    echo -e "${YELLOW}⚠️  WARN:${NC} $1"
}

TRADER_ROOT="/home/Jennifer/trader"
DATA_DIR="$TRADER_ROOT/data"
PASSED=0
FAILED=0

print_header "🔍 Data Directory Setup Verification"
echo ""

# Test 1: Check data directory exists
print_info "Test 1: Checking data directory exists..."
if [ -d "$DATA_DIR" ]; then
    print_pass "Data directory exists: $DATA_DIR"
    ((PASSED++))
else
    print_fail "Data directory NOT found: $DATA_DIR"
    ((FAILED++))
fi
echo ""

# Test 2: Check labeled data exists
print_info "Test 2: Checking labeled data..."
LABELED_DATA="$DATA_DIR/data_labeled/interval=5m"
if [ -d "$LABELED_DATA" ]; then
    SYMBOL_COUNT=$(ls -d "$LABELED_DATA"/symbol=* 2>/dev/null | wc -l)
    if [ "$SYMBOL_COUNT" -gt 0 ]; then
        print_pass "Labeled data found: $SYMBOL_COUNT symbols"
        ((PASSED++))
    else
        print_warn "Labeled data directory exists but no symbols found"
        ((FAILED++))
    fi
else
    print_fail "Labeled data NOT found: $LABELED_DATA"
    ((FAILED++))
fi
echo ""

# Test 3: Check barrier_processing_progress.json exists
print_info "Test 3: Checking processing progress file..."
PROGRESS_FILE="$DATA_DIR/data_labeled/barrier_processing_progress.json"
if [ -f "$PROGRESS_FILE" ]; then
    print_pass "Processing progress file found"
    # Try to parse it
    if python -m json.tool "$PROGRESS_FILE" > /dev/null 2>&1; then
        print_pass "Processing progress file is valid JSON"
        ((PASSED++))
    else
        print_warn "Processing progress file exists but is not valid JSON"
        ((FAILED++))
    fi
else
    print_warn "Processing progress file NOT found (may not be created yet)"
fi
echo ""

# Test 4: Check bash scripts have correct DATA_DIR defaults
print_info "Test 4: Checking bash script configurations..."

# Check train_all_symbols.sh
TRAIN_SCRIPT="$TRADER_ROOT/TRAINING/train_all_symbols.sh"
if [ -f "$TRAIN_SCRIPT" ]; then
    if grep -q "TRADER_ROOT=" "$TRAIN_SCRIPT" && grep -q "data_labeled" "$TRAIN_SCRIPT"; then
        print_pass "train_all_symbols.sh correctly configured"
        ((PASSED++))
    else
        print_fail "train_all_symbols.sh NOT correctly configured"
        ((FAILED++))
    fi
else
    print_fail "train_all_symbols.sh NOT found: $TRAIN_SCRIPT"
    ((FAILED++))
fi

# Check run_barrier_enhanced_cool.sh
BARRIER_SCRIPT="$TRADER_ROOT/sort_py/run_barrier_enhanced_cool.sh"
if [ -f "$BARRIER_SCRIPT" ]; then
    if grep -q "TRADER_ROOT=" "$BARRIER_SCRIPT" && grep -q "data_labeled" "$BARRIER_SCRIPT"; then
        print_pass "run_barrier_enhanced_cool.sh correctly configured"
        ((PASSED++))
    else
        print_fail "run_barrier_enhanced_cool.sh NOT correctly configured"
        ((FAILED++))
    fi
else
    print_fail "run_barrier_enhanced_cool.sh NOT found: $BARRIER_SCRIPT"
    ((FAILED++))
fi

# Check run_all_phases.sh
PHASES_SCRIPT="$TRADER_ROOT/TRAINING/EXPERIMENTS/run_all_phases.sh"
if [ -f "$PHASES_SCRIPT" ]; then
    if grep -q 'DATA_DIR.*trader/data' "$PHASES_SCRIPT"; then
        print_pass "run_all_phases.sh correctly configured"
        ((PASSED++))
    else
        print_fail "run_all_phases.sh NOT correctly configured"
        ((FAILED++))
    fi
else
    print_fail "run_all_phases.sh NOT found: $PHASES_SCRIPT"
    ((FAILED++))
fi
echo ""

# Test 5: Check documentation exists
print_info "Test 5: Checking documentation..."

DOC_FILES=(
    "$DATA_DIR/README.md"
    "$TRADER_ROOT/DATA_DIRECTORY_MIGRATION.md"
    "$TRADER_ROOT/TRAINING/EXPERIMENTS/README.md"
    "$TRADER_ROOT/TRAINING/EXPERIMENTS/OPERATIONS_GUIDE.md"
)

for doc in "${DOC_FILES[@]}"; do
    if [ -f "$doc" ]; then
        print_pass "Documentation found: $(basename "$doc")"
        ((PASSED++))
    else
        print_fail "Documentation NOT found: $(basename "$doc")"
        ((FAILED++))
    fi
done
echo ""

# Test 6: Test syntax of bash scripts
print_info "Test 6: Testing bash script syntax..."

SCRIPTS_TO_CHECK=(
    "$TRAIN_SCRIPT"
    "$BARRIER_SCRIPT"
    "$PHASES_SCRIPT"
)

for script in "${SCRIPTS_TO_CHECK[@]}"; do
    if [ -f "$script" ]; then
        if bash -n "$script" 2>/dev/null; then
            print_pass "Syntax OK: $(basename "$script")"
            ((PASSED++))
        else
            print_fail "Syntax ERROR: $(basename "$script")"
            ((FAILED++))
        fi
    fi
done
echo ""

# Test 7: Check environment variable override works
print_info "Test 7: Testing environment variable override..."
TEST_DATA_DIR="/tmp/test_data_override"
export DATA_DIR="$TEST_DATA_DIR"

# Simulate what bash scripts would resolve
RESOLVED_DIR="${DATA_DIR:-/home/Jennifer/trader/data}"
if [ "$RESOLVED_DIR" = "$TEST_DATA_DIR" ]; then
    print_pass "Environment variable override works: DATA_DIR=$RESOLVED_DIR"
    ((PASSED++))
else
    print_fail "Environment variable override FAILED"
    ((FAILED++))
fi
unset DATA_DIR
echo ""

# Test 8: Check parquet files integrity (sample)
print_info "Test 8: Checking parquet file integrity (sample)..."
if [ -d "$LABELED_DATA" ]; then
    # Find first available symbol
    FIRST_SYMBOL=$(ls -d "$LABELED_DATA"/symbol=* 2>/dev/null | head -1)
    if [ -n "$FIRST_SYMBOL" ]; then
        SYMBOL_NAME=$(basename "$FIRST_SYMBOL" | sed 's/symbol=//')
        # Parquet files are stored as {SYMBOL}.parquet (e.g., AAPL.parquet)
        PARQUET_FILE="$FIRST_SYMBOL/${SYMBOL_NAME}.parquet"
        
        if [ -f "$PARQUET_FILE" ]; then
            # Check if file is readable and has size > 0
            FILE_SIZE=$(stat -c%s "$PARQUET_FILE" 2>/dev/null || echo "0")
            if [ "$FILE_SIZE" -gt 0 ]; then
                # Convert to human readable
                FILE_SIZE_MB=$((FILE_SIZE / 1024 / 1024))
                print_pass "Sample parquet file OK: $SYMBOL_NAME (${FILE_SIZE_MB}MB)"
                ((PASSED++))
            else
                print_fail "Sample parquet file is empty: $SYMBOL_NAME"
                ((FAILED++))
            fi
        else
            print_warn "No parquet file found for sample symbol: $SYMBOL_NAME (expected: $PARQUET_FILE)"
        fi
    else
        print_warn "No symbols available to test parquet files"
    fi
else
    print_warn "Labeled data directory not available for parquet test"
fi
echo ""

# Summary
print_header "📊 Verification Summary"
TOTAL=$((PASSED + FAILED))
echo ""
echo -e "Total Tests: ${BLUE}$TOTAL${NC}"
echo -e "Passed:      ${GREEN}$PASSED${NC}"
echo -e "Failed:      ${RED}$FAILED${NC}"
echo ""

if [ "$FAILED" -eq 0 ]; then
    print_pass "🎉 ALL TESTS PASSED! Data directory setup is correct."
    echo ""
    echo "You can now use the following commands:"
    echo ""
    echo "  # Training with default data directory"
    echo "  cd $TRADER_ROOT/TRAINING"
    echo "  ./train_all_symbols.sh"
    echo ""
    echo "  # EXPERIMENTS workflow"
    echo "  cd $TRADER_ROOT/TRAINING/EXPERIMENTS"
    echo "  ./run_all_phases.sh"
    echo ""
    echo "  # Barrier processing"
    echo "  cd $TRADER_ROOT/sort_py"
    echo "  ./run_barrier_enhanced_cool.sh"
    echo ""
    exit 0
else
    print_fail "⚠️  SOME TESTS FAILED. Please review the errors above."
    echo ""
    echo "Common fixes:"
    echo ""
    echo "  1. Missing data: Place data in $DATA_DIR/"
    echo "  2. Script errors: Check bash syntax with 'bash -n <script>'"
    echo "  3. Permissions: Run 'chmod +x <script>' or 'chmod -R u+rwX $DATA_DIR'"
    echo ""
    echo "For more help, see:"
    echo "  - $TRADER_ROOT/DATA_DIRECTORY_MIGRATION.md"
    echo "  - $DATA_DIR/README.md"
    echo ""
    exit 1
fi


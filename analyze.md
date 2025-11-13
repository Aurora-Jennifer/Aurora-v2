for target_dir in DATA_PROCESSING/data/features/*/; do
    python scripts/aggregate_feature_groups.py \
      --input "${target_dir}/feature_importance_summary.csv" \
      --output "${target_dir}/feature_groups_summary.csv"
done

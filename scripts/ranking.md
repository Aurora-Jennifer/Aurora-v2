>_ # Restart the target ranking
python scripts/rank_target_predictability.py \
 --discover-all \
 --symbols AAPL,MSFT,GOOGL,TSLA,JPM \
 --output-dir results/target_rankings
2025-11-13 22:09:58,735 - INFO - Loaded multi-model config from /home/Jennifer/trader/CONFIG/multi_model_feature_selection.yaml
2025-11-13 22:09:58,735 - INFO - Using 11 model families from config: lightgbm, xgboost, random_forest, neural_network, catboost, lasso, mutual_information, univariate_selection, rfe, boruta, stability_selection
2025-11-13 22:09:58,735 - INFO - ================================================================================
2025-11-13 22:09:58,735 - INFO - Target Predictability Ranking
2025-11-13 22:09:58,735 - INFO - ================================================================================
2025-11-13 22:09:58,735 - INFO - Test symbols: AAPL, MSFT, GOOGL, TSLA, JPM
2025-11-13 22:09:58,735 - INFO - Model families: lightgbm, xgboost, random_forest, neural_network, catboost, lasso, mutual_information, univariate_selection, rfe, boruta, stability_selection
2025-11-13 22:09:58,735 - INFO - Auto-discovering ALL targets from data...
2025-11-13 22:09:59,149 - INFO - Discovered 63 valid targets
2025-11-13 22:09:59,149 - INFO - - y_* targets: 53
2025-11-13 22:09:59,149 - INFO - - fwd_ret_* targets: 10
2025-11-13 22:09:59,149 - INFO - Skipped 9 degenerate targets (single class/zero variance)
2025-11-13 22:09:59,149 - INFO - Skipped 1 first_touch targets (leaked)
2025-11-13 22:09:59,151 - INFO - Found 63 valid targets

2025-11-13 22:09:59,151 - INFO -
============================================================
2025-11-13 22:09:59,151 - INFO - Evaluating: peak_60m_0.8 (y_will_peak_60m_0.8)
2025-11-13 22:09:59,151 - INFO - ============================================================
2025-11-13 22:09:59,151 - INFO - AAPL...
2025-11-13 22:09:59,906 - INFO - Using GPU (CUDA) for LightGBM
2025-11-13 22:37:32,989 - INFO - Scores: lightgbm=0.173, random_forest=0.121, neural_network=0.109, xgboost=0.137, catboost=0.195, lasso=0.210, mutual_information=0.174, univariate_selection=0.252, rfe=0.105, boruta=0.124, stability_selection=0.860, importance=0.63
2025-11-13 22:37:32,989 - INFO - MSFT...
2025-11-13 22:37:33,336 - INFO - Using GPU (CUDA) for LightGBM
2025-11-13 23:04:26,689 - INFO - Scores: lightgbm=0.144, random_forest=0.107, neural_network=0.040, xgboost=0.148, catboost=0.181, lasso=0.210, mutual_information=0.175, univariate_selection=0.260, rfe=0.093, boruta=0.101, stability_selection=0.858, importance=0.60
2025-11-13 23:04:26,690 - INFO - GOOGL...
2025-11-13 23:04:27,016 - INFO - Using GPU (CUDA) for LightGBM
2025-11-13 23:33:57,885 - INFO - Scores: lightgbm=0.142, random_forest=0.100, neural_network=0.019, xgboost=0.107, catboost=0.154, lasso=0.214, mutual_information=0.181, univariate_selection=0.255, rfe=0.106, boruta=0.115, stability_selection=0.857, importance=0.62
2025-11-13 23:33:57,885 - INFO - TSLA...
2025-11-13 23:33:58,224 - INFO - Using GPU (CUDA) for LightGBM
2025-11-14 00:00:32,172 - INFO - Scores: lightgbm=0.178, random_forest=0.103, neural_network=0.074, xgboost=0.179, catboost=0.177, lasso=0.218, mutual_information=0.188, univariate_selection=0.257, rfe=0.118, boruta=0.129, stability_selection=0.842, importance=0.61
2025-11-14 00:00:32,172 - INFO - JPM...
2025-11-14 00:00:32,489 - INFO - Using GPU (CUDA) for LightGBM
2025-11-14 00:26:33,784 - INFO - Scores: lightgbm=0.193, random_forest=0.148, neural_network=0.065, xgboost=0.174, catboost=0.203, lasso=0.224, mutual_information=0.164, univariate_selection=0.239, rfe=0.145, boruta=0.150, stability_selection=0.854, importance=0.61
2025-11-14 00:26:33,785 - INFO - Summary: R²=0.219±0.207, importance=0.62, composite=0.555
2025-11-14 00:26:33,806 - INFO -
============================================================
2025-11-14 00:26:33,806 - INFO - Evaluating: valle60m_0.8 (y_will_valley_60m_0.8)
2025-11-14 00:26:33,806 - INFO - ============================================================
2025-11-14 00:26:33,806 - INFO - AAPL...
2025-11-14 00:26:34,110 - INFO - Using GPU (CUDA) for LightGBM
2025-11-14 00:51:29,123 - INFO - Scores: lightgbm=0.206, random_forest=0.185, neural_network=0.120, xgboost=0.198, catboost=0.202, lasso=0.245, mutual_information=0.196, univariate_selection=0.272, rfe=0.181, boruta=0.183, stability_selection=0.824, importance=0.64
2025-11-14 00:51:29,123 - INFO - MSFT...
2025-11-14 00:51:29,466 - INFO - Using GPU (CUDA) for LightGBM
2025-11-14 01:16:10,610 - INFO - Scores: lightgbm=0.187, random_forest=0.143, neural_network=0.082, xgboost=0.177, catboost=0.191, lasso=0.223, mutual_information=0.180, univariate_selection=0.271, rfe=0.143, boruta=0.138, stability_selection=0.833, importance=0.63
2025-11-14 01:16:10,610 - INFO - GOOGL...
2025-11-14 01:16:10,929 - INFO - Using GPU (CUDA) for LightGBM
2025-11-14 01:40:22,215 - INFO - Scores: lightgbm=0.174, random_forest=0.169, neural_network=0.056, xgboost=0.145, catboost=0.189, lasso=0.232, mutual_information=0.202, univariate_selection=0.275, rfe=0.154, boruta=0.156, stability_selection=0.832, importance=0.64
2025-11-14 01:40:22,216 - INFO - TSLA...
2025-11-14 01:40:22,536 - INFO - Using GPU (CUDA) for LightGBM
2025-11-14 02:05:34,610 - INFO - Scores: lightgbm=0.221, random_forest=0.207, neural_network=0.118, xgboost=0.189, catboost=0.198, lasso=0.254, mutual_information=0.200, univariate_selection=0.271, rfe=0.195, boruta=0.193, stability_selection=0.829, importance=0.64
2025-11-14 02:05:34,610 - INFO - JPM...
2025-11-14 02:05:34,931 - INFO - Using GPU (CUDA) for LightGBM
2025-11-14 02:29:16,771 - INFO - Scores: lightgbm=0.172, random_forest=0.150, neural_network=0.069, xgboost=0.167, catboost=0.184, lasso=0.228, mutual_information=0.199, univariate_selection=0.276, rfe=0.145, boruta=0.161, stability_selection=0.834, importance=0.63
2025-11-14 02:29:16,771 - INFO - Summary: R²=0.244±0.190, importance=0.64, composite=0.583
2025-11-14 02:29:16,793 - INFO -
============================================================
2025-11-14 02:29:16,793 - INFO - Evaluating: swing_high_10m_0.05 (y_will_swing_high_10m_0.05)
2025-11-14 02:29:16,793 - INFO - ============================================================
2025-11-14 02:29:16,793 - INFO - AAPL...
2025-11-14 02:29:17,097 - INFO - Using GPU (CUDA) for LightGBM
2025-11-14 02:54:43,995 - INFO - Scores: lightgbm=-0.399, random_forest=-0.392, neural_network=-0.532, xgboost=-0.472, catboost=-0.394, lasso=0.027, mutual_information=0.135, univariate_selection=0.283, rfe=-0.395, boruta=-0.419, stability_selection=0.615, importance=0.42
2025-11-14 02:54:43,995 - INFO - MSFT...
2025-11-14 02:54:44,321 - INFO - Using GPU (CUDA) for LightGBM
2025-11-14 03:19:57,664 - INFO - Scores: lightgbm=-0.403, random_forest=-0.420, neural_network=-0.516, xgboost=-0.491, catboost=-0.430, lasso=0.041, mutual_information=0.131, univariate_selection=0.274, rfe=-0.423, boruta=-0.445, stability_selection=0.626, importance=0.50
2025-11-14 03:19:57,664 - INFO - GOOGL...
2025-11-14 03:19:57,994 - INFO - Using GPU (CUDA) for LightGBM
2025-11-14 03:45:23,517 - INFO - Scores: lightgbm=-0.376, random_forest=-0.408, neural_network=-0.528, xgboost=-0.442, catboost=-0.390, lasso=0.037, mutual_information=0.120, univariate_selection=0.274, rfe=-0.407, boruta=-0.450, stability_selection=0.613, importance=0.50
2025-11-14 03:45:23,517 - INFO - TSLA...
2025-11-14 03:45:23,853 - INFO - Using GPU (CUDA) for LightGBM
2025-11-14 04:11:05,562 - INFO - Scores: lightgbm=-0.405, random_forest=-0.429, neural_network=-0.568, xgboost=-0.465, catboost=-0.407, lasso=0.022, mutual_information=0.128, univariate_selection=0.255, rfe=-0.429, boruta=-0.450, stability_selection=0.601, importance=0.40
2025-11-14 04:11:05,563 - INFO - JPM...
2025-11-14 04:11:05,874 - INFO - Using GPU (CUDA) for LightGBM
2025-11-14 04:35:14,877 - INFO - Scores: lightgbm=-0.388, random_forest=-0.408, neural_network=-0.497, xgboost=-0.448, catboost=-0.399, lasso=0.017, mutual_information=0.129, univariate_selection=0.275, rfe=-0.409, boruta=-0.435, stability_selection=0.626, importance=0.50
2025-11-14 04:35:14,878 - INFO - Summary: R²=-0.183±0.363, importance=0.46, composite=0.314
2025-11-14 04:35:14,900 - INFO -
============================================================
2025-11-14 04:35:14,900 - INFO - Evaluating: swing_low_10m_0.05 (y_will_swing_low_10m_0.05)
2025-11-14 04:35:14,900 - INFO - ============================================================
2025-11-14 04:35:14,900 - INFO - AAPL...
2025-11-14 04:35:15,210 - INFO - Using GPU (CUDA) for LightGBM
2025-11-14 05:00:50,713 - INFO - Scores: lightgbm=-0.329, random_forest=-0.308, neural_network=-0.454, xgboost=-0.454, catboost=-0.338, lasso=0.013, mutual_information=0.124, univariate_selection=0.282, rfe=-0.327, boruta=-0.357, stability_selection=0.606, importance=0.42
2025-11-14 05:00:50,713 - INFO - MSFT...
2025-11-14 05:00:51,034 - INFO - Using GPU (CUDA) for LightGBM
2025-11-14 05:26:17,591 - INFO - Scores: lightgbm=-0.328, random_forest=-0.346, neural_network=-0.447, xgboost=-0.433, catboost=-0.332, lasso=0.013, mutual_information=0.135, univariate_selection=0.228, rfe=-0.334, boruta=-0.344, stability_selection=0.614, importance=0.49
2025-11-14 05:26:17,591 - INFO - GOOGL...
2025-11-14 05:26:17,907 - INFO - Using GPU (CUDA) for LightGBM
2025-11-14 05:51:45,336 - INFO - Scores: lightgbm=-0.386, random_forest=-0.386, neural_network=-0.538, xgboost=-0.501, catboost=-0.424, lasso=0.024, mutual_information=0.125, univariate_selection=0.260, rfe=-0.382, boruta=-0.420, stability_selection=0.606, importance=0.50
2025-11-14 05:51:45,336 - INFO - TSLA...
2025-11-14 05:51:45,655 - INFO - Using GPU (CUDA) for LightGBM
2025-11-14 06:17:45,828 - INFO - Scores: lightgbm=-0.355, random_forest=-0.361, neural_network=-0.495, xgboost=-0.432, catboost=-0.359, lasso=0.017, mutual_information=0.133, univariate_selection=0.260, rfe=-0.373, boruta=-0.382, stability_selection=0.600, importance=0.41
2025-11-14 06:17:45,828 - INFO - JPM...
2025-11-14 06:17:46,146 - INFO - Using GPU (CUDA) for LightGBM
2025-11-14 06:42:29,117 - INFO - Scores: lightgbm=-0.321, random_forest=-0.308, neural_network=-0.435, xgboost=-0.400, catboost=-0.293, lasso=0.024, mutual_information=0.134, univariate_selection=0.234, rfe=-0.307, boruta=-0.354, stability_selection=0.622, importance=0.49
2025-11-14 06:42:29,117 - INFO - Summary: R²=-0.151±0.336, importance=0.46, composite=0.319
2025-11-14 06:42:29,139 - INFO -
============================================================
2025-11-14 06:42:29,139 - INFO - Evaluating: swing_high_10m_0.10 (y_will_swing_high_10m_0.10)
2025-11-14 06:42:29,139 - INFO - ============================================================
2025-11-14 06:42:29,139 - INFO - AAPL...
2025-11-14 06:42:29,439 - INFO - Using GPU (CUDA) for LightGBM
2025-11-14 07:08:17,560 - INFO - Scores: lightgbm=-0.387, random_forest=-0.392, neural_network=-0.532, xgboost=-0.472, catboost=-0.394, lasso=0.027, mutual_information=0.135, univariate_selection=0.283, rfe=-0.395, boruta=-0.419, stability_selection=0.612, importance=0.42
2025-11-14 07:08:17,560 - INFO - MSFT...
2025-11-14 07:08:17,880 - INFO - Using GPU (CUDA) for LightGBM
2025-11-14 07:34:13,409 - INFO - Scores: lightgbm=-0.401, random_forest=-0.420, neural_network=-0.516, xgboost=-0.491, catboost=-0.430, lasso=0.041, mutual_information=0.131, univariate_selection=0.274, rfe=-0.423, boruta=-0.445, stability_selection=0.625, importance=0.50
2025-11-14 07:34:13,409 - INFO - GOOGL...
2025-11-14 07:34:13,746 - INFO - Using GPU (CUDA) for LightGBM
2025-11-14 07:59:44,538 - INFO - Scores: lightgbm=-0.371, random_forest=-0.408, neural_network=-0.528, xgboost=-0.442, catboost=-0.390, lasso=0.037, mutual_information=0.120, univariate_selection=0.274, rfe=-0.407, boruta=-0.450, stability_selection=0.611, importance=0.50
2025-11-14 07:59:44,538 - INFO - TSLA...
2025-11-14 07:59:44,859 - INFO - Using GPU (CUDA) for LightGBM
2025-11-14 08:25:58,243 - INFO - Scores: lightgbm=-0.415, random_forest=-0.429, neural_network=-0.568, xgboost=-0.465, catboost=-0.407, lasso=0.022, mutual_information=0.128, univariate_selection=0.255, rfe=-0.429, boruta=-0.450, stability_selection=0.601, importance=0.40
2025-11-14 08:25:58,243 - INFO - JPM...
2025-11-14 08:25:58,568 - INFO - Using GPU (CUDA) for LightGBM
2025-11-14 08:55:57,839 - INFO - Scores: lightgbm=-0.386, random_forest=-0.408, neural_network=-0.497, xgboost=-0.448, catboost=-0.399, lasso=0.017, mutual_information=0.129, univariate_selection=0.275, rfe=-0.409, boruta=-0.435, stability_selection=0.626, importance=0.50
2025-11-14 08:55:57,839 - INFO - Summary: R²=-0.182±0.363, importance=0.47, composite=0.314
2025-11-14 08:55:57,862 - INFO -
============================================================
2025-11-14 08:55:57,862 - INFO - Evaluating: swing_low_10m_0.10 (y_will_swing_low_10m_0.10)
2025-11-14 08:55:57,862 - INFO - ============================================================
2025-11-14 08:55:57,862 - INFO - AAPL...
2025-11-14 08:55:58,189 - INFO - Using GPU (CUDA) for LightGBM
2025-11-14 09:28:47,522 - INFO - Scores: lightgbm=-0.327, random_forest=-0.308, neural_network=-0.454, xgboost=-0.454, catboost=-0.338, lasso=0.013, mutual_information=0.124, univariate_selection=0.282, rfe=-0.327, boruta=-0.357, stability_selection=0.608, importance=0.42
2025-11-14 09:28:47,522 - INFO - MSFT...
2025-11-14 09:28:47,838 - INFO - Using GPU (CUDA) for LightGBM
2025-11-14 10:02:12,512 - INFO - Scores: lightgbm=-0.330, random_forest=-0.346, neural_network=-0.447, xgboost=-0.433, catboost=-0.332, lasso=0.013, mutual_information=0.135, univariate_selection=0.228, rfe=-0.334, boruta=-0.344, stability_selection=0.614, importance=0.49
2025-11-14 10:02:12,512 - INFO - GOOGL...
2025-11-14 10:02:12,834 - INFO - Using GPU (CUDA) for LightGBM
2025-11-14 10:32:45,378 - INFO - Scores: lightgbm=-0.388, random_forest=-0.386, neural_network=-0.538, xgboost=-0.501, catboost=-0.424, lasso=0.024, mutual_information=0.125, univariate_selection=0.260, rfe=-0.382, boruta=-0.420, stability_selection=0.605, importance=0.50
2025-11-14 10:32:45,378 - INFO - TSLA...
2025-11-14 10:32:45,701 - INFO - Using GPU (CUDA) for LightGBM
2025-11-14 11:03:03,328 - INFO - Scores: lightgbm=-0.351, random_forest=-0.361, neural_network=-0.495, xgboost=-0.432, catboost=-0.359, lasso=0.017, mutual_information=0.133, univariate_selection=0.260, rfe=-0.373, boruta=-0.382, stability_selection=0.601, importance=0.41
2025-11-14 11:03:03,329 - INFO - JPM...
2025-11-14 11:03:03,641 - INFO - Using GPU (CUDA) for LightGBM
2025-11-14 11:32:29,636 - INFO - Scores: lightgbm=-0.322, random_forest=-0.308, neural_network=-0.435, xgboost=-0.400, catboost=-0.293, lasso=0.024, mutual_information=0.134, univariate_selection=0.234, rfe=-0.307, boruta=-0.354, stability_selection=0.622, importance=0.49
2025-11-14 11:32:29,636 - INFO - Summary: R²=-0.151±0.336, importance=0.46, composite=0.319
2025-11-14 11:32:29,658 - INFO -
============================================================
2025-11-14 11:32:29,658 - INFO - Evaluating: swing_high_10m_0.20 (y_will_swing_high_10m_0.20)
2025-11-14 11:32:29,658 - INFO - ============================================================
2025-11-14 11:32:29,658 - INFO - AAPL...
2025-11-14 11:32:29,957 - INFO - Using GPU (CUDA) for LightGBM
2025-11-14 12:02:31,822 - INFO - Scores: lightgbm=-0.385, random_forest=-0.392, neural_network=-0.532, xgboost=-0.472, catboost=-0.394, lasso=0.027, mutual_information=0.135, univariate_selection=0.283, rfe=-0.395, boruta=-0.419, stability_selection=0.613, importance=0.42
2025-11-14 12:02:31,822 - INFO - MSFT...
2025-11-14 12:02:32,147 - INFO - Using GPU (CUDA) for LightGBM
2025-11-14 12:32:18,541 - INFO - Scores: lightgbm=-0.397, random_forest=-0.420, neural_network=-0.516, xgboost=-0.491, catboost=-0.430, lasso=0.041, mutual_information=0.131, univariate_selection=0.274, rfe=-0.423, boruta=-0.445, stability_selection=0.626, importance=0.50
2025-11-14 12:32:18,541 - INFO - GOOGL...
2025-11-14 12:32:18,862 - INFO - Using GPU (CUDA) for LightGBM
2025-11-14 13:02:09,649 - INFO - Scores: lightgbm=-0.361, random_forest=-0.408, neural_network=-0.528, xgboost=-0.442, catboost=-0.390, lasso=0.037, mutual_information=0.120, univariate_selection=0.274, rfe=-0.407, boruta=-0.450, stability_selection=0.614, importance=0.50
2025-11-14 13:02:09,649 - INFO - TSLA...
2025-11-14 13:02:09,976 - INFO - Using GPU (CUDA) for LightGBM
2025-11-14 13:32:41,590 - INFO - Scores: lightgbm=-0.412, random_forest=-0.429, neural_network=-0.568, xgboost=-0.465, catboost=-0.407, lasso=0.022, mutual_information=0.128, univariate_selection=0.255, rfe=-0.429, boruta=-0.450, stability_selection=0.600, importance=0.40
2025-11-14 13:32:41,590 - INFO - JPM...
2025-11-14 13:32:41,904 - INFO - Using GPU (CUDA) for LightGBM
2025-11-14 14:02:58,767 - INFO - Scores: lightgbm=-0.393, random_forest=-0.408, neural_network=-0.497, xgboost=-0.448, catboost=-0.399, lasso=0.017, mutual_information=0.129, univariate_selection=0.275, rfe=-0.409, boruta=-0.435, stability_selection=0.625, importance=0.50
2025-11-14 14:02:58,768 - INFO - Summary: R²=-0.182±0.363, importance=0.46, composite=0.314
2025-11-14 14:02:58,791 - INFO -
============================================================
2025-11-14 14:02:58,791 - INFO - Evaluating: swing_low_10m_0.20 (y_will_swing_low_10m_0.20)
2025-11-14 14:02:58,791 - INFO - ============================================================
2025-11-14 14:02:58,791 - INFO - AAPL...
2025-11-14 14:02:59,094 - INFO - Using GPU (CUDA) for LightGBM
2025-11-14 14:35:14,207 - INFO - Scores: lightgbm=-0.326, random_forest=-0.308, neural_network=-0.454, xgboost=-0.454, catboost=-0.338, lasso=0.013, mutual_information=0.124, univariate_selection=0.282, rfe=-0.327, boruta=-0.357, stability_selection=0.607, importance=0.42
2025-11-14 14:35:14,207 - INFO - MSFT...
2025-11-14 14:35:14,554 - INFO - Using GPU (CUDA) for LightGBM
2025-11-14 15:07:01,603 - INFO - Scores: lightgbm=-0.329, random_forest=-0.346, neural_network=-0.447, xgboost=-0.433, catboost=-0.332, lasso=0.013, mutual_information=0.135, univariate_selection=0.228, rfe=-0.334, boruta=-0.344, stability_selection=0.615, importance=0.49
2025-11-14 15:07:01,603 - INFO - GOOGL...
2025-11-14 15:07:01,918 - INFO - Using GPU (CUDA) for LightGBM
2025-11-14 15:31:47,576 - INFO - Scores: lightgbm=-0.388, random_forest=-0.386, neural_network=-0.538, xgboost=-0.501, catboost=-0.424, lasso=0.024, mutual_information=0.125, univariate_selection=0.260, rfe=-0.382, boruta=-0.420, stability_selection=0.605, importance=0.50
2025-11-14 15:31:47,576 - INFO - TSLA...
2025-11-14 15:31:47,900 - INFO - Using GPU (CUDA) for LightGBM
2025-11-14 15:56:22,997 - INFO - Scores: lightgbm=-0.336, random_forest=-0.361, neural_network=-0.495, xgboost=-0.432, catboost=-0.359, lasso=0.017, mutual_information=0.133, univariate_selection=0.260, rfe=-0.373, boruta=-0.382, stability_selection=0.602, importance=0.41
2025-11-14 15:56:22,997 - INFO - JPM...
2025-11-14 15:56:23,318 - INFO - Using GPU (CUDA) for LightGBM
2025-11-14 16:20:05,684 - INFO - Scores: lightgbm=-0.313, random_forest=-0.308, neural_network=-0.435, xgboost=-0.400, catboost=-0.293, lasso=0.024, mutual_information=0.134, univariate_selection=0.234, rfe=-0.307, boruta=-0.354, stability_selection=0.623, importance=0.49
2025-11-14 16:20:05,684 - INFO - Summary: R²=-0.150±0.335, importance=0.46, composite=0.320
2025-11-14 16:20:05,705 - INFO -
============================================================
2025-11-14 16:20:05,705 - INFO - Evaluating: swing_high_15m_0.05 (y_will_swing_high_15m_0.05)
2025-11-14 16:20:05,705 - INFO - ============================================================
2025-11-14 16:20:05,706 - INFO - AAPL...
2025-11-14 16:20:06,026 - INFO - Using GPU (CUDA) for LightGBM
2025-11-14 16:44:31,795 - INFO - Scores: lightgbm=-0.299, random_forest=-0.349, neural_network=-0.369, xgboost=-0.315, catboost=-0.287, lasso=0.017, mutual_information=0.125, univariate_selection=0.257, rfe=-0.354, boruta=-0.345, stability_selection=0.736, importance=0.42
2025-11-14 16:44:31,795 - INFO - MSFT...
2025-11-14 16:44:32,127 - INFO - Using GPU (CUDA) for LightGBM
2025-11-14 17:09:13,526 - INFO - Scores: lightgbm=-0.321, random_forest=-0.364, neural_network=-0.398, xgboost=-0.348, catboost=-0.318, lasso=0.016, mutual_information=0.140, univariate_selection=0.177, rfe=-0.369, boruta=-0.369, stability_selection=0.725, importance=0.48
2025-11-14 17:09:13,526 - INFO - GOOGL...
2025-11-14 17:09:13,866 - INFO - Using GPU (CUDA) for LightGBM
2025-11-14 17:33:14,706 - INFO - Scores: lightgbm=-0.288, random_forest=-0.324, neural_network=-0.354, xgboost=-0.308, catboost=-0.268, lasso=0.008, mutual_information=0.111, univariate_selection=0.263, rfe=-0.330, boruta=-0.328, stability_selection=0.747, importance=0.51
2025-11-14 17:33:14,706 - INFO - TSLA...
2025-11-14 17:33:15,034 - INFO - Using GPU (CUDA) for LightGBM
2025-11-14 17:58:08,659 - INFO - Scores: lightgbm=-0.316, random_forest=-0.329, neural_network=-0.356, xgboost=-0.335, catboost=-0.305, lasso=0.013, mutual_information=0.128, univariate_selection=0.278, rfe=-0.331, boruta=-0.324, stability_selection=0.753, importance=0.43
2025-11-14 17:58:08,659 - INFO - JPM...
2025-11-14 17:58:08,965 - INFO - Using GPU (CUDA) for LightGBM
2025-11-14 18:21:35,506 - INFO - Scores: lightgbm=-0.374, random_forest=-0.380, neural_network=-0.398, xgboost=-0.374, catboost=-0.329, lasso=0.015, mutual_information=0.127, univariate_selection=0.261, rfe=-0.384, boruta=-0.394, stability_selection=0.727, importance=0.51
2025-11-14 18:21:35,506 - INFO - Summary: R²=-0.115±0.343, importance=0.47, composite=0.324
2025-11-14 18:21:35,528 - INFO -
============================================================
2025-11-14 18:21:35,528 - INFO - Evaluating: swing_low_15m_0.05 (y_will_swing_low_15m_0.05)
2025-11-14 18:21:35,528 - INFO - ============================================================
2025-11-14 18:21:35,528 - INFO - AAPL...
2025-11-14 18:21:35,823 - INFO - Using GPU (CUDA) for LightGBM
2025-11-14 18:45:40,781 - INFO - Scores: lightgbm=-0.332, random_forest=-0.339, neural_network=-0.372, xgboost=-0.370, catboost=-0.313, lasso=0.009, mutual_information=0.124, univariate_selection=0.289, rfe=-0.337, boruta=-0.333, stability_selection=0.749, importance=0.43
2025-11-14 18:45:40,781 - INFO - MSFT...
2025-11-14 18:45:41,101 - INFO - Using GPU (CUDA) for LightGBM
2025-11-14 19:10:16,672 - INFO - Scores: lightgbm=-0.340, random_forest=-0.369, neural_network=-0.376, xgboost=-0.386, catboost=-0.339, lasso=0.022, mutual_information=0.136, univariate_selection=0.281, rfe=-0.363, boruta=-0.366, stability_selection=0.733, importance=0.53
2025-11-14 19:10:16,672 - INFO - GOOGL...
2025-11-14 19:10:17,001 - INFO - Using GPU (CUDA) for LightGBM
2025-11-14 19:34:03,337 - INFO - Scores: lightgbm=-0.329, random_forest=-0.341, neural_network=-0.375, xgboost=-0.364, catboost=-0.320, lasso=0.012, mutual_information=0.127, univariate_selection=0.266, rfe=-0.340, boruta=-0.340, stability_selection=0.750, importance=0.51
2025-11-14 19:34:03,337 - INFO - TSLA...
2025-11-14 19:34:03,667 - INFO - Using GPU (CUDA) for LightGBM
2025-11-14 19:58:52,016 - INFO - Scores: lightgbm=-0.307, random_forest=-0.336, neural_network=-0.390, xgboost=-0.344, catboost=-0.308, lasso=0.013, mutual_information=0.134, univariate_selection=0.289, rfe=-0.326, boruta=-0.338, stability_selection=0.753, importance=0.43
2025-11-14 19:58:52,016 - INFO - JPM...
2025-11-14 19:58:52,328 - INFO - Using GPU (CUDA) for LightGBM
2025-11-14 20:22:04,740 - INFO - Scores: lightgbm=-0.285, random_forest=-0.348, neural_network=-0.399, xgboost=-0.306, catboost=-0.280, lasso=0.007, mutual_information=0.128, univariate_selection=0.287, rfe=-0.349, boruta=-0.348, stability_selection=0.731, importance=0.52
2025-11-14 20:22:04,740 - INFO - Summary: R²=-0.112±0.349, importance=0.48, composite=0.326
2025-11-14 20:22:04,761 - INFO -
============================================================
2025-11-14 20:22:04,761 - INFO - Evaluating: swing_high_15m_0.10 (y_will_swing_high_15m_0.10)
2025-11-14 20:22:04,761 - INFO - ============================================================
2025-11-14 20:22:04,761 - INFO - AAPL...
2025-11-14 20:22:05,058 - INFO - Using GPU (CUDA) for LightGBM
2025-11-14 20:46:19,655 - INFO - Scores: lightgbm=-0.308, random_forest=-0.349, neural_network=-0.369, xgboost=-0.315, catboost=-0.287, lasso=0.017, mutual_information=0.125, univariate_selection=0.257, rfe=-0.354, boruta=-0.345, stability_selection=0.737, importance=0.42
2025-11-14 20:46:19,656 - INFO - MSFT...
2025-11-14 20:46:19,992 - INFO - Using GPU (CUDA) for LightGBM
2025-11-14 21:10:48,823 - INFO - Scores: lightgbm=-0.323, random_forest=-0.364, neural_network=-0.398, xgboost=-0.348, catboost=-0.318, lasso=0.016, mutual_information=0.140, univariate_selection=0.177, rfe=-0.369, boruta=-0.369, stability_selection=0.725, importance=0.48
2025-11-14 21:10:48,823 - INFO - GOOGL...
2025-11-14 21:10:49,144 - INFO - Using GPU (CUDA) for LightGBM
2025-11-14 21:37:34,843 - INFO - Scores: lightgbm=-0.282, random_forest=-0.324, neural_network=-0.354, xgboost=-0.308, catboost=-0.268, lasso=0.008, mutual_information=0.111, univariate_selection=0.263, rfe=-0.330, boruta=-0.328, stability_selection=0.748, importance=0.51
2025-11-14 21:37:34,843 - INFO - TSLA...
2025-11-14 21:37:35,176 - INFO - Using GPU (CUDA) for LightGBM
2025-11-14 22:03:57,604 - INFO - Scores: lightgbm=-0.316, random_forest=-0.329, neural_network=-0.356, xgboost=-0.335, catboost=-0.305, lasso=0.013, mutual_information=0.128, univariate_selection=0.278, rfe=-0.331, boruta=-0.324, stability_selection=0.753, importance=0.43
2025-11-14 22:03:57,604 - INFO - JPM...
2025-11-14 22:03:57,913 - INFO - Using GPU (CUDA) for LightGBM
2025-11-14 22:28:03,950 - INFO - Scores: lightgbm=-0.375, random_forest=-0.380, neural_network=-0.398, xgboost=-0.374, catboost=-0.329, lasso=0.015, mutual_information=0.127, univariate_selection=0.261, rfe=-0.384, boruta=-0.394, stability_selection=0.725, importance=0.51
2025-11-14 22:28:03,951 - INFO - Summary: R²=-0.115±0.343, importance=0.47, composite=0.324
2025-11-14 22:28:03,971 - INFO -
============================================================
2025-11-14 22:28:03,971 - INFO - Evaluating: swing_low_15m_0.10 (y_will_swing_low_15m_0.10)
2025-11-14 22:28:03,972 - INFO - ============================================================
2025-11-14 22:28:03,972 - INFO - AAPL...
2025-11-14 22:28:04,368 - INFO - Using GPU (CUDA) for LightGBM
2025-11-14 22:52:09,599 - INFO - Scores: lightgbm=-0.328, random_forest=-0.339, neural_network=-0.372, xgboost=-0.370, catboost=-0.313, lasso=0.009, mutual_information=0.124, univariate_selection=0.289, rfe=-0.337, boruta=-0.333, stability_selection=0.749, importance=0.43
2025-11-14 22:52:09,599 - INFO - MSFT...
2025-11-14 22:52:09,998 - INFO - Using GPU (CUDA) for LightGBM
2025-11-14 23:16:46,923 - INFO - Scores: lightgbm=-0.369, random_forest=-0.369, neural_network=-0.376, xgboost=-0.386, catboost=-0.339, lasso=0.022, mutual_information=0.136, univariate_selection=0.281, rfe=-0.363, boruta=-0.366, stability_selection=0.734, importance=0.53
2025-11-14 23:16:46,923 - INFO - GOOGL...
2025-11-14 23:16:47,333 - INFO - Using GPU (CUDA) for LightGBM
2025-11-14 23:42:13,004 - INFO - Scores: lightgbm=-0.363, random_forest=-0.341, neural_network=-0.375, xgboost=-0.364, catboost=-0.320, lasso=0.012, mutual_information=0.127, univariate_selection=0.266, rfe=-0.340, boruta=-0.340, stability_selection=0.750, importance=0.51
2025-11-14 23:42:13,004 - INFO - TSLA...
2025-11-14 23:42:13,329 - INFO - Using GPU (CUDA) for LightGBM
2025-11-15 00:07:15,827 - INFO - Scores: lightgbm=-0.316, random_forest=-0.336, neural_network=-0.390, xgboost=-0.344, catboost=-0.308, lasso=0.013, mutual_information=0.134, univariate_selection=0.289, rfe=-0.326, boruta=-0.338, stability_selection=0.752, importance=0.43
2025-11-15 00:07:15,828 - INFO - JPM...
2025-11-15 00:07:16,133 - INFO - Using GPU (CUDA) for LightGBM
2025-11-15 00:32:00,855 - INFO - Scores: lightgbm=-0.291, random_forest=-0.348, neural_network=-0.399, xgboost=-0.306, catboost=-0.280, lasso=0.007, mutual_information=0.128, univariate_selection=0.287, rfe=-0.349, boruta=-0.348, stability_selection=0.731, importance=0.52
2025-11-15 00:32:00,855 - INFO - Summary: R²=-0.113±0.350, importance=0.48, composite=0.326
2025-11-15 00:32:00,874 - INFO -
============================================================
2025-11-15 00:32:00,874 - INFO - Evaluating: swing_high_15m_0.20 (y_will_swing_high_15m_0.20)
2025-11-15 00:32:00,874 - INFO - ============================================================
2025-11-15 00:32:00,875 - INFO - AAPL...
2025-11-15 00:32:01,175 - INFO - Using GPU (CUDA) for LightGBM
2025-11-15 00:56:20,922 - INFO - Scores: lightgbm=-0.296, random_forest=-0.349, neural_network=-0.369, xgboost=-0.315, catboost=-0.287, lasso=0.017, mutual_information=0.125, univariate_selection=0.257, rfe=-0.354, boruta=-0.345, stability_selection=0.735, importance=0.42
2025-11-15 00:56:20,922 - INFO - MSFT...
2025-11-15 00:56:21,246 - INFO - Using GPU (CUDA) for LightGBM
2025-11-15 01:20:57,479 - INFO - Scores: lightgbm=-0.321, random_forest=-0.364, neural_network=-0.398, xgboost=-0.348, catboost=-0.318, lasso=0.016, mutual_information=0.140, univariate_selection=0.177, rfe=-0.369, boruta=-0.369, stability_selection=0.726, importance=0.48
2025-11-15 01:20:57,479 - INFO - GOOGL...
2025-11-15 01:20:57,801 - INFO - Using GPU (CUDA) for LightGBM
2025-11-15 01:44:58,798 - INFO - Scores: lightgbm=-0.273, random_forest=-0.324, neural_network=-0.354, xgboost=-0.308, catboost=-0.268, lasso=0.008, mutual_information=0.111, univariate_selection=0.263, rfe=-0.330, boruta=-0.328, stability_selection=0.747, importance=0.51
2025-11-15 01:44:58,798 - INFO - TSLA...
2025-11-15 01:44:59,122 - INFO - Using GPU (CUDA) for LightGBM
2025-11-15 02:10:06,337 - INFO - Scores: lightgbm=-0.309, random_forest=-0.329, neural_network=-0.356, xgboost=-0.335, catboost=-0.305, lasso=0.013, mutual_information=0.128, univariate_selection=0.278, rfe=-0.331, boruta=-0.324, stability_selection=0.754, importance=0.43
2025-11-15 02:10:06,337 - INFO - JPM...
2025-11-15 02:10:06,642 - INFO - Using GPU (CUDA) for LightGBM
2025-11-15 02:33:35,034 - INFO - Scores: lightgbm=-0.373, random_forest=-0.380, neural_network=-0.398, xgboost=-0.374, catboost=-0.329, lasso=0.015, mutual_information=0.127, univariate_selection=0.261, rfe=-0.384, boruta=-0.394, stability_selection=0.726, importance=0.51
2025-11-15 02:33:35,034 - INFO - Summary: R²=-0.114±0.343, importance=0.47, composite=0.324
2025-11-15 02:33:35,054 - INFO -
============================================================
2025-11-15 02:33:35,054 - INFO - Evaluating: swing_low_15m_0.20 (y_will_swing_low_15m_0.20)
2025-11-15 02:33:35,054 - INFO - ============================================================
2025-11-15 02:33:35,054 - INFO - AAPL...
2025-11-15 02:33:35,361 - INFO - Using GPU (CUDA) for LightGBM
2025-11-15 02:57:44,816 - INFO - Scores: lightgbm=-0.330, random_forest=-0.339, neural_network=-0.372, xgboost=-0.370, catboost=-0.313, lasso=0.009, mutual_information=0.124, univariate_selection=0.289, rfe=-0.337, boruta=-0.333, stability_selection=0.750, importance=0.43
2025-11-15 02:57:44,816 - INFO - MSFT...
2025-11-15 02:57:45,138 - INFO - Using GPU (CUDA) for LightGBM
2025-11-15 03:22:27,277 - INFO - Scores: lightgbm=-0.335, random_forest=-0.369, neural_network=-0.376, xgboost=-0.386, catboost=-0.339, lasso=0.022, mutual_information=0.136, univariate_selection=0.281, rfe=-0.363, boruta=-0.366, stability_selection=0.734, importance=0.53
2025-11-15 03:22:27,277 - INFO - GOOGL...
2025-11-15 03:22:27,587 - INFO - Using GPU (CUDA) for LightGBM
2025-11-15 03:46:37,056 - INFO - Scores: lightgbm=-0.324, random_forest=-0.341, neural_network=-0.375, xgboost=-0.364, catboost=-0.320, lasso=0.012, mutual_information=0.127, univariate_selection=0.266, rfe=-0.340, boruta=-0.340, stability_selection=0.751, importance=0.51
2025-11-15 03:46:37,056 - INFO - TSLA...
2025-11-15 03:46:37,374 - INFO - Using GPU (CUDA) for LightGBM
2025-11-15 04:11:55,377 - INFO - Scores: lightgbm=-0.316, random_forest=-0.336, neural_network=-0.390, xgboost=-0.344, catboost=-0.308, lasso=0.013, mutual_information=0.134, univariate_selection=0.289, rfe=-0.326, boruta=-0.338, stability_selection=0.753, importance=0.43
2025-11-15 04:11:55,377 - INFO - JPM...
2025-11-15 04:11:55,690 - INFO - Using GPU (CUDA) for LightGBM
2025-11-15 04:35:11,450 - INFO - Scores: lightgbm=-0.294, random_forest=-0.348, neural_network=-0.399, xgboost=-0.306, catboost=-0.280, lasso=0.007, mutual_information=0.128, univariate_selection=0.287, rfe=-0.349, boruta=-0.348, stability_selection=0.731, importance=0.52
2025-11-15 04:35:11,450 - INFO - Summary: R²=-0.112±0.349, importance=0.48, composite=0.327
2025-11-15 04:35:11,470 - INFO -
============================================================
2025-11-15 04:35:11,470 - INFO - Evaluating: swing_high_30m_0.05 (y_will_swing_high_30m_0.05)
2025-11-15 04:35:11,470 - INFO - ============================================================
2025-11-15 04:35:11,470 - INFO - AAPL...
2025-11-15 04:35:11,760 - INFO - Using GPU (CUDA) for LightGBM
2025-11-15 04:59:13,185 - INFO - Scores: lightgbm=-0.013, random_forest=-0.013, neural_network=-0.013, xgboost=-0.021, catboost=-0.013, lasso=-0.002, mutual_information=0.099, univariate_selection=0.169, rfe=-0.013, boruta=-0.021, stability_selection=0.987, importance=0.45
2025-11-15 04:59:13,185 - INFO - MSFT...
2025-11-15 04:59:13,511 - INFO - Using GPU (CUDA) for LightGBM
2025-11-15 05:23:18,391 - INFO - Scores: lightgbm=-0.049, random_forest=-0.015, neural_network=-0.015, xgboost=-0.022, catboost=-0.015, lasso=-0.003, mutual_information=0.105, univariate_selection=0.100, rfe=-0.015, boruta=-0.015, stability_selection=0.985, importance=0.42
2025-11-15 05:23:18,392 - INFO - GOOGL...
2025-11-15 05:23:18,698 - INFO - Using GPU (CUDA) for LightGBM
2025-11-15 05:47:14,236 - INFO - Scores: lightgbm=-0.013, random_forest=-0.013, neural_network=-0.013, xgboost=-0.013, catboost=-0.005, lasso=-0.008, mutual_information=0.097, univariate_selection=0.144, rfe=-0.013, boruta=-0.013, stability_selection=0.988, importance=0.44
2025-11-15 05:47:14,236 - INFO - TSLA...
2025-11-15 05:47:14,571 - INFO - Using GPU (CUDA) for LightGBM
2025-11-15 06:11:26,860 - INFO - Scores: lightgbm=-0.010, random_forest=-0.010, neural_network=-0.010, xgboost=-0.020, catboost=-0.010, lasso=-0.004, mutual_information=0.090, univariate_selection=0.138, rfe=-0.010, boruta=-0.010, stability_selection=0.991, importance=0.45
2025-11-15 06:11:26,860 - INFO - JPM...
2025-11-15 06:11:27,172 - INFO - Using GPU (CUDA) for LightGBM
2025-11-15 06:34:19,136 - INFO - Scores: lightgbm=-0.013, random_forest=-0.013, neural_network=-0.013, xgboost=-0.013, catboost=-0.013, lasso=-0.006, mutual_information=0.101, univariate_selection=0.195, rfe=-0.013, boruta=-0.013, stability_selection=0.987, importance=0.44
2025-11-15 06:34:19,137 - INFO - Summary: R²=0.103±0.285, importance=0.44, composite=0.404
2025-11-15 06:34:19,156 - INFO -
============================================================
2025-11-15 06:34:19,156 - INFO - Evaluating: swing_low_30m_0.05 (y_will_swing_low_30m_0.05)
2025-11-15 06:34:19,156 - INFO - ============================================================
2025-11-15 06:34:19,156 - INFO - AAPL...
2025-11-15 06:34:19,451 - INFO - Using GPU (CUDA) for LightGBM
2025-11-15 06:58:28,466 - INFO - Scores: lightgbm=-0.010, random_forest=-0.010, neural_network=-0.010, xgboost=-0.010, catboost=-0.020, lasso=-0.009, mutual_information=0.111, univariate_selection=0.239, rfe=-0.010, boruta=-0.010, stability_selection=0.990, importance=0.48
2025-11-15 06:58:28,467 - INFO - MSFT...
2025-11-15 06:58:28,782 - INFO - Using GPU (CUDA) for LightGBM
2025-11-15 07:22:11,979 - INFO - Scores: lightgbm=-0.016, random_forest=-0.016, neural_network=-0.016, xgboost=-0.016, catboost=-0.016, lasso=-0.004, mutual_information=0.114, univariate_selection=0.169, rfe=-0.016, boruta=-0.016, stability_selection=0.984, importance=0.45
2025-11-15 07:22:11,979 - INFO - GOOGL...
2025-11-15 07:22:12,285 - INFO - Using GPU (CUDA) for LightGBM
2025-11-15 07:46:09,930 - INFO - Scores: lightgbm=-0.013, random_forest=-0.013, neural_network=-0.013, xgboost=-0.020, catboost=-0.013, lasso=-0.004, mutual_information=0.107, univariate_selection=0.210, rfe=-0.013, boruta=-0.013, stability_selection=0.987, importance=0.48
2025-11-15 07:46:09,930 - INFO - TSLA...
2025-11-15 07:46:10,246 - INFO - Using GPU (CUDA) for LightGBM
2025-11-15 08:10:29,320 - INFO - Scores: lightgbm=-0.008, random_forest=-0.021, neural_network=-0.008, xgboost=-0.008, catboost=-0.008, lasso=-0.018, mutual_information=0.096, univariate_selection=0.246, rfe=-0.021, boruta=-0.021, stability_selection=0.992, importance=0.50
2025-11-15 08:10:29,320 - INFO - JPM...
2025-11-15 08:10:29,621 - INFO - Using GPU (CUDA) for LightGBM
2025-11-15 08:33:07,385 - INFO - Scores: lightgbm=-0.014, random_forest=-0.014, neural_network=-0.014, xgboost=-0.021, catboost=-0.014, lasso=-0.004, mutual_information=0.098, univariate_selection=0.191, rfe=-0.014, boruta=-0.014, stability_selection=0.986, importance=0.45
2025-11-15 08:33:07,385 - INFO - Summary: R²=0.109±0.286, importance=0.47, composite=0.418
2025-11-15 08:33:07,404 - INFO -
============================================================
2025-11-15 08:33:07,404 - INFO - Evaluating: swing_high_30m_0.10 (y_will_swing_high_30m_0.10)
2025-11-15 08:33:07,404 - INFO - ============================================================
2025-11-15 08:33:07,404 - INFO - AAPL...
2025-11-15 08:33:07,702 - INFO - Using GPU (CUDA) for LightGBM
2025-11-15 08:57:13,681 - INFO - Scores: lightgbm=-0.013, random_forest=-0.013, neural_network=-0.013, xgboost=-0.021, catboost=-0.013, lasso=-0.002, mutual_information=0.099, univariate_selection=0.169, rfe=-0.013, boruta=-0.021, stability_selection=0.987, importance=0.45
2025-11-15 08:57:13,681 - INFO - MSFT...
2025-11-15 08:57:14,003 - INFO - Using GPU (CUDA) for LightGBM
2025-11-15 09:21:12,869 - INFO - Scores: lightgbm=-0.015, random_forest=-0.015, neural_network=-0.015, xgboost=-0.022, catboost=-0.015, lasso=-0.003, mutual_information=0.105, univariate_selection=0.100, rfe=-0.015, boruta=-0.015, stability_selection=0.985, importance=0.42
2025-11-15 09:21:12,869 - INFO - GOOGL...
2025-11-15 09:21:13,181 - INFO - Using GPU (CUDA) for LightGBM
2025-11-15 09:45:19,265 - INFO - Scores: lightgbm=-0.013, random_forest=-0.013, neural_network=-0.013, xgboost=-0.013, catboost=-0.005, lasso=-0.008, mutual_information=0.097, univariate_selection=0.144, rfe=-0.013, boruta=-0.013, stability_selection=0.988, importance=0.44
2025-11-15 09:45:19,265 - INFO - TSLA...
2025-11-15 09:45:19,588 - INFO - Using GPU (CUDA) for LightGBM
2025-11-15 10:09:25,322 - INFO - Scores: lightgbm=-0.010, random_forest=-0.010, neural_network=-0.010, xgboost=-0.020, catboost=-0.010, lasso=-0.004, mutual_information=0.090, univariate_selection=0.138, rfe=-0.010, boruta=-0.010, stability_selection=0.990, importance=0.45
2025-11-15 10:09:25,322 - INFO - JPM...
2025-11-15 10:09:25,625 - INFO - Using GPU (CUDA) for LightGBM
2025-11-15 10:32:21,063 - INFO - Scores: lightgbm=-0.013, random_forest=-0.013, neural_network=-0.013, xgboost=-0.013, catboost=-0.013, lasso=-0.006, mutual_information=0.101, univariate_selection=0.195, rfe=-0.013, boruta=-0.013, stability_selection=0.987, importance=0.45
2025-11-15 10:32:21,063 - INFO - Summary: R²=0.103±0.285, importance=0.44, composite=0.405
2025-11-15 10:32:21,082 - INFO -
============================================================
2025-11-15 10:32:21,082 - INFO - Evaluating: swing_low_30m_0.10 (y_will_swing_low_30m_0.10)
2025-11-15 10:32:21,082 - INFO - ============================================================
2025-11-15 10:32:21,082 - INFO - AAPL...
2025-11-15 10:32:21,378 - INFO - Using GPU (CUDA) for LightGBM
2025-11-15 10:56:28,618 - INFO - Scores: lightgbm=-0.010, random_forest=-0.010, neural_network=-0.010, xgboost=-0.010, catboost=-0.020, lasso=-0.009, mutual_information=0.111, univariate_selection=0.239, rfe=-0.010, boruta=-0.010, stability_selection=0.990, importance=0.48
2025-11-15 10:56:28,618 - INFO - MSFT...
2025-11-15 10:56:28,944 - INFO - Using GPU (CUDA) for LightGBM
2025-11-15 11:20:18,621 - INFO - Scores: lightgbm=-0.016, random_forest=-0.016, neural_network=-0.016, xgboost=-0.016, catboost=-0.016, lasso=-0.004, mutual_information=0.114, univariate_selection=0.169, rfe=-0.016, boruta=-0.016, stability_selection=0.984, importance=0.45
2025-11-15 11:20:18,621 - INFO - GOOGL...
2025-11-15 11:20:18,929 - INFO - Using GPU (CUDA) for LightGBM
2025-11-15 11:44:32,954 - INFO - Scores: lightgbm=-0.013, random_forest=-0.013, neural_network=-0.013, xgboost=-0.020, catboost=-0.013, lasso=-0.004, mutual_information=0.107, univariate_selection=0.210, rfe=-0.013, boruta=-0.013, stability_selection=0.988, importance=0.48
2025-11-15 11:44:32,954 - INFO - TSLA...
2025-11-15 11:44:33,269 - INFO - Using GPU (CUDA) for LightGBM
2025-11-15 12:08:56,124 - INFO - Scores: lightgbm=-0.008, random_forest=-0.021, neural_network=-0.008, xgboost=-0.008, catboost=-0.008, lasso=-0.018, mutual_information=0.096, univariate_selection=0.246, rfe=-0.021, boruta=-0.021, stability_selection=0.992, importance=0.50
2025-11-15 12:08:56,124 - INFO - JPM...
2025-11-15 12:08:56,449 - INFO - Using GPU (CUDA) for LightGBM
2025-11-15 12:32:16,418 - INFO - Scores: lightgbm=-0.014, random_forest=-0.014, neural_network=-0.014, xgboost=-0.021, catboost=-0.014, lasso=-0.004, mutual_information=0.098, univariate_selection=0.191, rfe=-0.014, boruta=-0.014, stability_selection=0.986, importance=0.44
2025-11-15 12:32:16,418 - INFO - Summary: R²=0.109±0.286, importance=0.47, composite=0.417
2025-11-15 12:32:16,436 - INFO -
============================================================
2025-11-15 12:32:16,437 - INFO - Evaluating: swing_high_30m_0.20 (y_will_swing_high_30m_0.20)
2025-11-15 12:32:16,437 - INFO - ============================================================
2025-11-15 12:32:16,437 - INFO - AAPL...
2025-11-15 12:32:16,726 - INFO - Using GPU (CUDA) for LightGBM
2025-11-15 12:56:25,011 - INFO - Scores: lightgbm=-0.013, random_forest=-0.013, neural_network=-0.013, xgboost=-0.021, catboost=-0.013, lasso=-0.002, mutual_information=0.099, univariate_selection=0.169, rfe=-0.013, boruta=-0.021, stability_selection=0.987, importance=0.45
2025-11-15 12:56:25,011 - INFO - MSFT...
2025-11-15 12:56:25,339 - INFO - Using GPU (CUDA) for LightGBM
2025-11-15 13:20:20,979 - INFO - Scores: lightgbm=-0.015, random_forest=-0.015, neural_network=-0.015, xgboost=-0.022, catboost=-0.015, lasso=-0.003, mutual_information=0.105, univariate_selection=0.100, rfe=-0.015, boruta=-0.015, stability_selection=0.985, importance=0.42
2025-11-15 13:20:20,979 - INFO - GOOGL...
2025-11-15 13:20:21,282 - INFO - Using GPU (CUDA) for LightGBM
2025-11-15 13:44:41,136 - INFO - Scores: lightgbm=-0.013, random_forest=-0.013, neural_network=-0.013, xgboost=-0.013, catboost=-0.005, lasso=-0.008, mutual_information=0.097, univariate_selection=0.144, rfe=-0.013, boruta=-0.013, stability_selection=0.987, importance=0.44
2025-11-15 13:44:41,136 - INFO - TSLA...
2025-11-15 13:44:41,459 - INFO - Using GPU (CUDA) for LightGBM
2025-11-15 14:08:52,830 - INFO - Scores: lightgbm=-0.010, random_forest=-0.010, neural_network=-0.010, xgboost=-0.020, catboost=-0.010, lasso=-0.004, mutual_information=0.090, univariate_selection=0.138, rfe=-0.010, boruta=-0.010, stability_selection=0.991, importance=0.45
2025-11-15 14:08:52,830 - INFO - JPM...
2025-11-15 14:08:53,131 - INFO - Using GPU (CUDA) for LightGBM
2025-11-15 14:32:10,406 - INFO - Scores: lightgbm=-0.013, random_forest=-0.013, neural_network=-0.013, xgboost=-0.013, catboost=-0.013, lasso=-0.006, mutual_information=0.101, univariate_selection=0.195, rfe=-0.013, boruta=-0.013, stability_selection=0.987, importance=0.43
2025-11-15 14:32:10,406 - INFO - Summary: R²=0.103±0.285, importance=0.44, composite=0.404
2025-11-15 14:32:10,427 - INFO -
============================================================
2025-11-15 14:32:10,427 - INFO - Evaluating: swing_low_30m_0.20 (y_will_swing_low_30m_0.20)
2025-11-15 14:32:10,427 - INFO - ============================================================
2025-11-15 14:32:10,427 - INFO - AAPL...
2025-11-15 14:32:10,718 - INFO - Using GPU (CUDA) for LightGBM
2025-11-15 14:56:13,909 - INFO - Scores: lightgbm=-0.010, random_forest=-0.010, neural_network=-0.010, xgboost=-0.010, catboost=-0.020, lasso=-0.009, mutual_information=0.111, univariate_selection=0.239, rfe=-0.010, boruta=-0.010, stability_selection=0.990, importance=0.48
2025-11-15 14:56:13,909 - INFO - MSFT...
2025-11-15 14:56:14,227 - INFO - Using GPU (CUDA) for LightGBM
2025-11-15 15:20:13,911 - INFO - Scores: lightgbm=-0.707, random_forest=-0.016, neural_network=-0.016, xgboost=-0.016, catboost=-0.016, lasso=-0.004, mutual_information=0.114, univariate_selection=0.169, rfe=-0.016, boruta=-0.016, stability_selection=0.984, importance=0.45
2025-11-15 15:20:13,912 - INFO - GOOGL...
2025-11-15 15:20:14,215 - INFO - Using GPU (CUDA) for LightGBM
2025-11-15 15:44:15,648 - INFO - Scores: lightgbm=-0.013, random_forest=-0.013, neural_network=-0.013, xgboost=-0.020, catboost=-0.013, lasso=-0.004, mutual_information=0.107, univariate_selection=0.210, rfe=-0.013, boruta=-0.013, stability_selection=0.988, importance=0.48
2025-11-15 15:44:15,648 - INFO - TSLA...
2025-11-15 15:44:15,966 - INFO - Using GPU (CUDA) for LightGBM
2025-11-15 16:08:37,612 - INFO - Scores: lightgbm=-0.008, random_forest=-0.021, neural_network=-0.008, xgboost=-0.008, catboost=-0.008, lasso=-0.018, mutual_information=0.096, univariate_selection=0.246, rfe=-0.021, boruta=-0.021, stability_selection=0.992, importance=0.50
2025-11-15 16:08:37,612 - INFO - JPM...
2025-11-15 16:08:37,924 - INFO - Using GPU (CUDA) for LightGBM
2025-11-15 16:31:58,764 - INFO - Scores: lightgbm=-0.014, random_forest=-0.014, neural_network=-0.014, xgboost=-0.021, catboost=-0.014, lasso=-0.004, mutual_information=0.098, univariate_selection=0.191, rfe=-0.014, boruta=-0.014, stability_selection=0.986, importance=0.44
2025-11-15 16:31:58,765 - INFO - Summary: R²=0.096±0.294, importance=0.47, composite=0.407
2025-11-15 16:31:58,783 - INFO -
============================================================
2025-11-15 16:31:58,783 - INFO - Evaluating: swing_high_60m_0.05 (y_will_swing_high_60m_0.05)
2025-11-15 16:31:58,783 - INFO - ============================================================
2025-11-15 16:31:58,783 - INFO - AAPL...
2025-11-15 16:31:59,062 - WARNING - ️ Skipping: Target has only 1 unique value(s) in sample
2025-11-15 16:31:59,062 - INFO - MSFT...
2025-11-15 16:31:59,368 - WARNING - ️ Skipping: Smallest class has only 1 sample(s) (too few for CV)
2025-11-15 16:31:59,368 - INFO - GOOGL...
2025-11-15 16:31:59,639 - WARNING - ️ Skipping: Target has only 1 unique value(s) in sample
2025-11-15 16:31:59,639 - INFO - TSLA...
2025-11-15 16:31:59,929 - WARNING - ️ Skipping: Target has only 1 unique value(s) in sample
2025-11-15 16:31:59,929 - INFO - JPM...
2025-11-15 16:32:00,200 - WARNING - ️ Skipping: Smallest class has only 1 sample(s) (too few for CV)
2025-11-15 16:32:00,200 - WARNING - ️ No successful evaluations for swing_high_60m_0.05 (skipping)
2025-11-15 16:32:00,212 - INFO -
============================================================
2025-11-15 16:32:00,212 - INFO - Evaluating: swing_high_60m_0.10 (y_will_swing_high_60m_0.10)
2025-11-15 16:32:00,212 - INFO - ============================================================
2025-11-15 16:32:00,212 - INFO - AAPL...
2025-11-15 16:32:00,477 - WARNING - ️ Skipping: Target has only 1 unique value(s) in sample
2025-11-15 16:32:00,477 - INFO - MSFT...
2025-11-15 16:32:00,772 - WARNING - ️ Skipping: Smallest class has only 1 sample(s) (too few for CV)
2025-11-15 16:32:00,772 - INFO - GOOGL...
2025-11-15 16:32:01,048 - WARNING - ️ Skipping: Target has only 1 unique value(s) in sample
2025-11-15 16:32:01,048 - INFO - TSLA...
2025-11-15 16:32:01,345 - WARNING - ️ Skipping: Target has only 1 unique value(s) in sample
2025-11-15 16:32:01,345 - INFO - JPM...
2025-11-15 16:32:01,612 - WARNING - ️ Skipping: Smallest class has only 1 sample(s) (too few for CV)
2025-11-15 16:32:01,612 - WARNING - ️ No successful evaluations for swing_high_60m_0.10 (skipping)
2025-11-15 16:32:01,623 - INFO -
============================================================
2025-11-15 16:32:01,623 - INFO - Evaluating: swing_high_60m_0.20 (y_will_swing_high_60m_0.20)
2025-11-15 16:32:01,623 - INFO - ============================================================
2025-11-15 16:32:01,623 - INFO - AAPL...
2025-11-15 16:32:01,882 - WARNING - ️ Skipping: Target has only 1 unique value(s) in sample
2025-11-15 16:32:01,882 - INFO - MSFT...
2025-11-15 16:32:02,165 - WARNING - ️ Skipping: Smallest class has only 1 sample(s) (too few for CV)
2025-11-15 16:32:02,165 - INFO - GOOGL...
2025-11-15 16:32:02,454 - WARNING - ️ Skipping: Target has only 1 unique value(s) in sample
2025-11-15 16:32:02,454 - INFO - TSLA...
2025-11-15 16:32:02,740 - WARNING - ️ Skipping: Target has only 1 unique value(s) in sample
2025-11-15 16:32:02,740 - INFO - JPM...
2025-11-15 16:32:03,008 - WARNING - ️ Skipping: Smallest class has only 1 sample(s) (too few for CV)
2025-11-15 16:32:03,008 - WARNING - ️ No successful evaluations for swing_high_60m_0.20 (skipping)
2025-11-15 16:32:03,018 - INFO -
============================================================
2025-11-15 16:32:03,018 - INFO - Evaluating: peak_mfe_5m_0.001 (y_will_peak_mfe_5m_0.001)
2025-11-15 16:32:03,018 - INFO - ============================================================
2025-11-15 16:32:03,018 - INFO - AAPL...
2025-11-15 16:32:03,302 - INFO - Using GPU (CUDA) for LightGBM
2025-11-15 17:00:18,981 - INFO - Scores: lightgbm=-0.458, random_forest=-0.502, neural_network=-0.556, xgboost=-0.488, catboost=-0.437, lasso=0.030, mutual_information=0.075, univariate_selection=0.145, rfe=-0.530, boruta=-0.531, stability_selection=0.587, importance=0.37
2025-11-15 17:00:18,981 - INFO - MSFT...
2025-11-15 17:00:19,316 - INFO - Using GPU (CUDA) for LightGBM
2025-11-15 17:28:15,827 - INFO - Scores: lightgbm=-0.423, random_forest=-0.511, neural_network=-0.586, xgboost=-0.476, catboost=-0.421, lasso=0.032, mutual_information=0.080, univariate_selection=0.150, rfe=-0.554, boruta=-0.529, stability_selection=0.583, importance=0.46
2025-11-15 17:28:15,827 - INFO - GOOGL...
2025-11-15 17:28:16,129 - INFO - Using GPU (CUDA) for LightGBM
2025-11-15 17:56:16,434 - INFO - Scores: lightgbm=-0.436, random_forest=-0.497, neural_network=-0.591, xgboost=-0.496, catboost=-0.439, lasso=0.028, mutual_information=0.076, univariate_selection=0.142, rfe=-0.547, boruta=-0.578, stability_selection=0.576, importance=0.46
2025-11-15 17:56:16,434 - INFO - TSLA...
2025-11-15 17:56:16,743 - INFO - Using GPU (CUDA) for LightGBM
2025-11-15 18:22:52,089 - INFO - Scores: lightgbm=-0.424, random_forest=-0.477, neural_network=-0.609, xgboost=-0.491, catboost=-0.428, lasso=0.015, mutual_information=0.091, univariate_selection=0.113, rfe=-0.513, boruta=-0.549, stability_selection=0.614, importance=0.35
2025-11-15 18:22:52,089 - INFO - JPM...
2025-11-15 18:22:52,395 - INFO - Using GPU (CUDA) for LightGBM
2025-11-15 18:49:12,462 - INFO - Scores: lightgbm=-0.432, random_forest=-0.478, neural_network=-0.657, xgboost=-0.484, catboost=-0.430, lasso=0.034, mutual_information=0.078, univariate_selection=0.147, rfe=-0.534, boruta=-0.542, stability_selection=0.569, importance=0.46
2025-11-15 18:49:12,462 - INFO - Summary: R²=-0.245±0.370, importance=0.42, composite=0.298
2025-11-15 18:49:12,481 - INFO -
============================================================
2025-11-15 18:49:12,481 - INFO - Evaluating: vallemdd_5m_0.001 (y_will_valley_mdd_5m_0.001)
2025-11-15 18:49:12,481 - INFO - ============================================================
2025-11-15 18:49:12,481 - INFO - AAPL...
2025-11-15 18:49:12,768 - INFO - Using GPU (CUDA) for LightGBM
2025-11-15 19:16:43,497 - INFO - Scores: lightgbm=-0.441, random_forest=-0.489, neural_network=-0.588, xgboost=-0.476, catboost=-0.422, lasso=0.029, mutual_information=0.081, univariate_selection=0.154, rfe=-0.549, boruta=-0.544, stability_selection=0.577, importance=0.47
2025-11-15 19:16:43,497 - INFO - MSFT...
2025-11-15 19:16:43,812 - INFO - Using GPU (CUDA) for LightGBM
2025-11-15 19:46:37,448 - INFO - Scores: lightgbm=-0.386, random_forest=-0.467, neural_network=-0.582, xgboost=-0.467, catboost=-0.402, lasso=0.040, mutual_information=0.072, univariate_selection=0.164, rfe=-0.504, boruta=-0.526, stability_selection=0.584, importance=0.46
2025-11-15 19:46:37,448 - INFO - GOOGL...
2025-11-15 19:46:37,744 - INFO - Using GPU (CUDA) for LightGBM
2025-11-15 20:14:40,686 - INFO - Scores: lightgbm=-0.420, random_forest=-0.500, neural_network=-0.599, xgboost=-0.497, catboost=-0.420, lasso=0.028, mutual_information=0.078, univariate_selection=0.144, rfe=-0.542, boruta=-0.562, stability_selection=0.561, importance=0.46
2025-11-15 20:14:40,686 - INFO - TSLA...
2025-11-15 20:14:41,001 - INFO - Using GPU (CUDA) for LightGBM
2025-11-15 20:40:49,917 - INFO - Scores: lightgbm=-0.442, random_forest=-0.522, neural_network=-0.575, xgboost=-0.487, catboost=-0.450, lasso=0.010, mutual_information=0.094, univariate_selection=0.131, rfe=-0.551, boruta=-0.564, stability_selection=0.623, importance=0.35
2025-11-15 20:40:49,917 - INFO - JPM...
2025-11-15 20:40:50,214 - INFO - Using GPU (CUDA) for LightGBM
2025-11-15 21:07:26,076 - INFO - Scores: lightgbm=-0.408, random_forest=-0.475, neural_network=-0.610, xgboost=-0.461, catboost=-0.403, lasso=0.024, mutual_information=0.081, univariate_selection=0.155, rfe=-0.527, boruta=-0.536, stability_selection=0.585, importance=0.46
2025-11-15 21:07:26,076 - INFO - Summary: R²=-0.240±0.369, importance=0.44, composite=0.303
2025-11-15 21:07:26,095 - INFO -
============================================================
2025-11-15 21:07:26,095 - INFO - Evaluating: peak_mfe_5m_0.002 (y_will_peak_mfe_5m_0.002)
2025-11-15 21:07:26,095 - INFO - ============================================================
2025-11-15 21:07:26,095 - INFO - AAPL...
2025-11-15 21:07:26,381 - INFO - Using GPU (CUDA) for LightGBM
2025-11-15 21:36:47,442 - INFO - Scores: lightgbm=-0.249, random_forest=-0.316, neural_network=-0.356, xgboost=-0.293, catboost=-0.267, lasso=0.073, mutual_information=0.074, univariate_selection=0.153, rfe=-0.327, boruta=-0.329, stability_selection=0.715, importance=0.46
2025-11-15 21:36:47,442 - INFO - MSFT...
2025-11-15 21:36:47,756 - INFO - Using GPU (CUDA) for LightGBM
2025-11-15 22:05:53,762 - INFO - Scores: lightgbm=-0.219, random_forest=-0.288, neural_network=-0.335, xgboost=-0.289, catboost=-0.233, lasso=0.076, mutual_information=0.072, univariate_selection=0.156, rfe=-0.324, boruta=-0.309, stability_selection=0.735, importance=0.46
2025-11-15 22:05:53,763 - INFO - GOOGL...
2025-11-15 22:05:54,062 - INFO - Using GPU (CUDA) for LightGBM
2025-11-15 22:34:36,278 - INFO - Scores: lightgbm=-0.285, random_forest=-0.339, neural_network=-0.378, xgboost=-0.312, catboost=-0.279, lasso=0.074, mutual_information=0.073, univariate_selection=0.144, rfe=-0.348, boruta=-0.343, stability_selection=0.709, importance=0.46
2025-11-15 22:34:36,278 - INFO - TSLA...
2025-11-15 22:34:36,595 - INFO - Using GPU (CUDA) for LightGBM
2025-11-15 23:03:00,612 - INFO - Scores: lightgbm=-0.459, random_forest=-0.520, neural_network=-0.613, xgboost=-0.478, catboost=-0.435, lasso=0.036, mutual_information=0.072, univariate_selection=0.124, rfe=-0.549, boruta=-0.564, stability_selection=0.572, importance=0.36
2025-11-15 23:03:00,612 - INFO - JPM...
2025-11-15 23:03:00,906 - INFO - Using GPU (CUDA) for LightGBM
2025-11-15 23:30:31,654 - INFO - Scores: lightgbm=-0.241, random_forest=-0.291, neural_network=-0.356, xgboost=-0.275, catboost=-0.239, lasso=0.082, mutual_information=0.073, univariate_selection=0.152, rfe=-0.301, boruta=-0.302, stability_selection=0.729, importance=0.44
2025-11-15 23:30:31,655 - INFO - Summary: R²=-0.130±0.325, importance=0.44, composite=0.317
2025-11-15 23:30:31,673 - INFO -
============================================================
2025-11-15 23:30:31,673 - INFO - Evaluating: vallemdd_5m_0.002 (y_will_valley_mdd_5m_0.002)
2025-11-15 23:30:31,673 - INFO - ============================================================
2025-11-15 23:30:31,673 - INFO - AAPL...
2025-11-15 23:30:31,965 - INFO - Using GPU (CUDA) for LightGBM
2025-11-15 23:59:07,832 - INFO - Scores: lightgbm=-0.278, random_forest=-0.322, neural_network=-0.404, xgboost=-0.319, catboost=-0.254, lasso=0.071, mutual_information=0.081, univariate_selection=0.165, rfe=-0.352, boruta=-0.351, stability_selection=0.716, importance=0.47
2025-11-15 23:59:07,832 - INFO - MSFT...
2025-11-15 23:59:08,148 - INFO - Using GPU (CUDA) for LightGBM
2025-11-16 00:28:38,410 - INFO - Scores: lightgbm=-0.228, random_forest=-0.276, neural_network=-0.328, xgboost=-0.261, catboost=-0.225, lasso=0.085, mutual_information=0.070, univariate_selection=0.163, rfe=-0.316, boruta=-0.315, stability_selection=0.729, importance=0.46
2025-11-16 00:28:38,410 - INFO - GOOGL...
2025-11-16 00:28:38,709 - INFO - Using GPU (CUDA) for LightGBM
2025-11-16 00:57:24,680 - INFO - Scores: lightgbm=-0.295, random_forest=-0.348, neural_network=-0.410, xgboost=-0.339, catboost=-0.298, lasso=0.068, mutual_information=0.076, univariate_selection=0.144, rfe=-0.372, boruta=-0.384, stability_selection=0.700, importance=0.46
2025-11-16 00:57:24,680 - INFO - TSLA...
2025-11-16 00:57:24,999 - INFO - Using GPU (CUDA) for LightGBM
2025-11-16 01:25:23,631 - INFO - Scores: lightgbm=-0.481, random_forest=-0.535, neural_network=-0.599, xgboost=-0.536, catboost=-0.453, lasso=0.032, mutual_information=0.076, univariate_selection=0.129, rfe=-0.586, boruta=-0.581, stability_selection=0.563, importance=0.37
2025-11-16 01:25:23,631 - INFO - JPM...
2025-11-16 01:25:23,934 - INFO - Using GPU (CUDA) for LightGBM
2025-11-16 01:52:39,296 - INFO - Scores: lightgbm=-0.255, random_forest=-0.296, neural_network=-0.355, xgboost=-0.296, catboost=-0.246, lasso=0.059, mutual_information=0.083, univariate_selection=0.159, rfe=-0.328, boruta=-0.316, stability_selection=0.731, importance=0.46
2025-11-16 01:52:39,296 - INFO - Summary: R²=-0.139±0.331, importance=0.44, composite=0.317
2025-11-16 01:52:39,315 - INFO -
============================================================
2025-11-16 01:52:39,315 - INFO - Evaluating: peak_mfe_5m_0.005 (y_will_peak_mfe_5m_0.005)
2025-11-16 01:52:39,315 - INFO - ============================================================
2025-11-16 01:52:39,315 - INFO - AAPL...
2025-11-16 01:52:39,610 - INFO - Using GPU (CUDA) for LightGBM
2025-11-16 02:17:56,907 - INFO - Scores: lightgbm=-0.250, random_forest=-0.085, neural_network=-0.118, xgboost=-0.085, catboost=-0.053, lasso=0.110, mutual_information=0.077, univariate_selection=0.151, rfe=-0.065, boruta=-0.072, stability_selection=0.920, importance=0.48
2025-11-16 02:17:56,907 - INFO - MSFT...
2025-11-16 02:17:57,233 - INFO - Using GPU (CUDA) for LightGBM
2025-11-16 02:45:10,339 - INFO - Scores: lightgbm=-0.022, random_forest=-0.084, neural_network=-0.097, xgboost=-0.067, catboost=-0.031, lasso=0.124, mutual_information=0.078, univariate_selection=0.153, rfe=-0.087, boruta=-0.075, stability_selection=0.927, importance=0.48
2025-11-16 02:45:10,339 - INFO - GOOGL...
2025-11-16 02:45:10,655 - INFO - Using GPU (CUDA) for LightGBM
2025-11-16 03:12:53,980 - INFO - Scores: lightgbm=-0.063, random_forest=-0.072, neural_network=-0.134, xgboost=-0.070, catboost=-0.063, lasso=0.101, mutual_information=0.079, univariate_selection=0.155, rfe=-0.067, boruta=-0.082, stability_selection=0.915, importance=0.47
2025-11-16 03:12:53,980 - INFO - TSLA...
2025-11-16 03:12:54,298 - INFO - Using GPU (CUDA) for LightGBM
2025-11-16 03:40:54,444 - INFO - Scores: lightgbm=-0.194, random_forest=-0.242, neural_network=-0.302, xgboost=-0.212, catboost=-0.200, lasso=0.079, mutual_information=0.075, univariate_selection=0.146, rfe=-0.259, boruta=-0.262, stability_selection=0.772, importance=0.37
2025-11-16 03:40:54,445 - INFO - JPM...
2025-11-16 03:40:54,754 - INFO - Using GPU (CUDA) for LightGBM
2025-11-16 04:06:58,683 - INFO - Scores: lightgbm=-0.050, random_forest=-0.071, neural_network=-0.124, xgboost=-0.046, catboost=-0.064, lasso=0.105, mutual_information=0.084, univariate_selection=0.154, rfe=-0.085, boruta=-0.075, stability_selection=0.930, importance=0.44
2025-11-16 04:06:58,684 - INFO - Summary: R²=0.040±0.288, importance=0.45, composite=0.364
2025-11-16 04:06:58,701 - INFO -
============================================================
2025-11-16 04:06:58,701 - INFO - Evaluating: vallemdd_5m_0.005 (y_will_valley_mdd_5m_0.005)
2025-11-16 04:06:58,702 - INFO - ============================================================
2025-11-16 04:06:58,702 - INFO - AAPL...
2025-11-16 04:06:58,997 - INFO - Using GPU (CUDA) for LightGBM
2025-11-16 04:32:34,495 - INFO - Scores: lightgbm=-0.064, random_forest=-0.069, neural_network=-0.121, xgboost=-0.102, catboost=-0.087, lasso=0.077, mutual_information=0.077, univariate_selection=0.161, rfe=-0.081, boruta=-0.077, stability_selection=0.919, importance=0.48
2025-11-16 04:32:34,496 - INFO - MSFT...
2025-11-16 04:32:34,814 - INFO - Using GPU (CUDA) for LightGBM
2025-11-16 04:59:55,382 - INFO - Scores: lightgbm=-0.084, random_forest=-0.068, neural_network=-0.099, xgboost=-0.120, catboost=-0.081, lasso=0.103, mutual_information=0.072, univariate_selection=0.155, rfe=-0.074, boruta=-0.068, stability_selection=0.924, importance=0.48
2025-11-16 04:59:55,382 - INFO - GOOGL...
2025-11-16 04:59:55,694 - INFO - Using GPU (CUDA) for LightGBM
2025-11-16 05:26:32,057 - INFO - Scores: lightgbm=-0.110, random_forest=-0.100, neural_network=-0.186, xgboost=-0.138, catboost=-0.105, lasso=0.054, mutual_information=0.078, univariate_selection=0.152, rfe=-0.105, boruta=-0.111, stability_selection=0.910, importance=0.47
2025-11-16 05:26:32,057 - INFO - TSLA...
2025-11-16 05:26:32,375 - INFO - Using GPU (CUDA) for LightGBM
2025-11-16 05:54:30,099 - INFO - Scores: lightgbm=-0.209, random_forest=-0.277, neural_network=-0.282, xgboost=-0.277, catboost=-0.243, lasso=0.072, mutual_information=0.076, univariate_selection=0.137, rfe=-0.288, boruta=-0.274, stability_selection=0.757, importance=0.36
2025-11-16 05:54:30,099 - INFO - JPM...
2025-11-16 05:54:30,408 - INFO - Using GPU (CUDA) for LightGBM
2025-11-16 06:20:21,976 - INFO - Scores: lightgbm=-0.047, random_forest=-0.047, neural_network=-0.088, xgboost=-0.077, catboost=-0.066, lasso=0.073, mutual_information=0.084, univariate_selection=0.151, rfe=-0.058, boruta=-0.047, stability_selection=0.933, importance=0.46
2025-11-16 06:20:21,976 - INFO - Summary: R²=0.030±0.290, importance=0.45, composite=0.357
2025-11-16 06:20:22,002 - INFO -
============================================================
2025-11-16 06:20:22,002 - INFO - Evaluating: peak_mfe_10m_0.001 (y_will_peak_mfe_10m_0.001)
2025-11-16 06:20:22,002 - INFO - ============================================================
2025-11-16 06:20:22,002 - INFO - AAPL...
2025-11-16 06:20:22,295 - INFO - Using GPU (CUDA) for LightGBM
2025-11-16 06:48:17,979 - INFO - Scores: lightgbm=-0.287, random_forest=-0.306, neural_network=-0.389, xgboost=-0.313, catboost=-0.268, lasso=0.091, mutual_information=0.097, univariate_selection=0.194, rfe=-0.331, boruta=-0.336, stability_selection=0.621, importance=0.40
2025-11-16 06:48:17,979 - INFO - MSFT...
2025-11-16 06:48:18,297 - INFO - Using GPU (CUDA) for LightGBM
2025-11-16 07:16:03,664 - INFO - Scores: lightgbm=-0.260, random_forest=-0.284, neural_network=-0.395, xgboost=-0.342, catboost=-0.258, lasso=0.096, mutual_information=0.103, univariate_selection=0.211, rfe=-0.342, boruta=-0.333, stability_selection=0.611, importance=0.51
2025-11-16 07:16:03,664 - INFO - GOOGL...
2025-11-16 07:16:03,974 - INFO - Using GPU (CUDA) for LightGBM
2025-11-16 07:43:35,516 - INFO - Scores: lightgbm=-0.280, random_forest=-0.306, neural_network=-0.370, xgboost=-0.338, catboost=-0.251, lasso=0.091, mutual_information=0.105, univariate_selection=0.218, rfe=-0.346, boruta=-0.350, stability_selection=0.625, importance=0.50
2025-11-16 07:43:35,516 - INFO - TSLA...
2025-11-16 07:43:35,832 - INFO - Using GPU (CUDA) for LightGBM
2025-11-16 08:10:16,070 - INFO - Scores: lightgbm=-0.286, random_forest=-0.324, neural_network=-0.364, xgboost=-0.351, catboost=-0.308, lasso=0.058, mutual_information=0.108, univariate_selection=0.211, rfe=-0.366, boruta=-0.364, stability_selection=0.715, importance=0.41
2025-11-16 08:10:16,070 - INFO - JPM...
2025-11-16 08:10:16,374 - INFO - Using GPU (CUDA) for LightGBM
2025-11-16 08:36:08,831 - INFO - Scores: lightgbm=-0.247, random_forest=-0.300, neural_network=-0.415, xgboost=-0.301, catboost=-0.254, lasso=0.102, mutual_information=0.110, univariate_selection=0.226, rfe=-0.330, boruta=-0.312, stability_selection=0.614, importance=0.51
2025-11-16 08:36:08,832 - INFO - Summary: R²=-0.109±0.311, importance=0.47, composite=0.328
2025-11-16 08:36:08,849 - INFO -
============================================================
2025-11-16 08:36:08,849 - INFO - Evaluating: vallemdd_10m_0.001 (y_will_valley_mdd_10m_0.001)
2025-11-16 08:36:08,849 - INFO - ============================================================
2025-11-16 08:36:08,849 - INFO - AAPL...
2025-11-16 08:36:09,139 - INFO - Using GPU (CUDA) for LightGBM
2025-11-16 09:01:54,286 - INFO - Scores: lightgbm=-0.259, random_forest=-0.355, neural_network=-0.378, xgboost=-0.320, catboost=-0.286, lasso=0.086, mutual_information=0.089, univariate_selection=0.201, rfe=-0.367, boruta=-0.367, stability_selection=0.607, importance=0.40
2025-11-16 09:01:54,286 - INFO - MSFT...
2025-11-16 09:01:54,605 - INFO - Using GPU (CUDA) for LightGBM
2025-11-16 09:29:54,629 - INFO - Scores: lightgbm=-0.265, random_forest=-0.327, neural_network=-0.379, xgboost=-0.304, catboost=-0.262, lasso=0.100, mutual_information=0.089, univariate_selection=0.207, rfe=-0.344, boruta=-0.332, stability_selection=0.598, importance=0.49
2025-11-16 09:29:54,630 - INFO - GOOGL...
2025-11-16 09:29:54,942 - INFO - Using GPU (CUDA) for LightGBM
2025-11-16 09:57:29,638 - INFO - Scores: lightgbm=-0.223, random_forest=-0.294, neural_network=-0.399, xgboost=-0.326, catboost=-0.242, lasso=0.082, mutual_information=0.096, univariate_selection=0.202, rfe=-0.332, boruta=-0.331, stability_selection=0.621, importance=0.49
2025-11-16 09:57:29,639 - INFO - TSLA...
2025-11-16 09:57:29,961 - INFO - Using GPU (CUDA) for LightGBM
2025-11-16 10:23:51,550 - INFO - Scores: lightgbm=-0.259, random_forest=-0.320, neural_network=-0.358, xgboost=-0.343, catboost=-0.267, lasso=0.052, mutual_information=0.117, univariate_selection=0.248, rfe=-0.344, boruta=-0.350, stability_selection=0.720, importance=0.41
2025-11-16 10:23:51,551 - INFO - JPM...
2025-11-16 10:23:51,854 - INFO - Using GPU (CUDA) for LightGBM
2025-11-16 10:50:41,768 - INFO - Scores: lightgbm=-0.236, random_forest=-0.287, neural_network=-0.428, xgboost=-0.296, catboost=-0.222, lasso=0.089, mutual_information=0.092, univariate_selection=0.216, rfe=-0.331, boruta=-0.323, stability_selection=0.602, importance=0.50
2025-11-16 10:50:41,768 - INFO - Summary: R²=-0.108±0.308, importance=0.46, composite=0.327
2025-11-16 10:50:41,787 - INFO -
============================================================
2025-11-16 10:50:41,787 - INFO - Evaluating: peak_mfe_10m_0.002 (y_will_peak_mfe_10m_0.002)
2025-11-16 10:50:41,787 - INFO - ============================================================
2025-11-16 10:50:41,787 - INFO - AAPL...
2025-11-16 10:50:42,084 - INFO - Using GPU (CUDA) for LightGBM
2025-11-16 11:20:01,475 - INFO - Scores: lightgbm=-0.130, random_forest=-0.179, neural_network=-0.224, xgboost=-0.161, catboost=-0.122, lasso=0.147, mutual_information=0.079, univariate_selection=0.169, rfe=-0.192, boruta=-0.198, stability_selection=0.611, importance=0.48
2025-11-16 11:20:01,475 - INFO - MSFT...
2025-11-16 11:20:01,798 - INFO - Using GPU (CUDA) for LightGBM
2025-11-16 11:49:20,215 - INFO - Scores: lightgbm=-0.072, random_forest=-0.114, neural_network=-0.187, xgboost=-0.131, catboost=-0.088, lasso=0.153, mutual_information=0.080, univariate_selection=0.175, rfe=-0.136, boruta=-0.128, stability_selection=0.620, importance=0.48
2025-11-16 11:49:20,215 - INFO - GOOGL...
2025-11-16 11:49:20,525 - INFO - Using GPU (CUDA) for LightGBM
2025-11-16 12:16:09,170 - INFO - Scores: lightgbm=-0.143, random_forest=-0.184, neural_network=-0.260, xgboost=-0.182, catboost=-0.139, lasso=0.142, mutual_information=0.081, univariate_selection=0.169, rfe=-0.191, boruta=-0.199, stability_selection=0.597, importance=0.48
2025-11-16 12:16:09,170 - INFO - TSLA...
2025-11-16 12:16:09,488 - INFO - Using GPU (CUDA) for LightGBM
2025-11-16 12:43:59,954 - INFO - Scores: lightgbm=-0.286, random_forest=-0.314, neural_network=-0.413, xgboost=-0.342, catboost=-0.287, lasso=0.096, mutual_information=0.092, univariate_selection=0.182, rfe=-0.374, boruta=-0.360, stability_selection=0.618, importance=0.40
2025-11-16 12:43:59,954 - INFO - JPM...
2025-11-16 12:44:00,255 - INFO - Using GPU (CUDA) for LightGBM
2025-11-16 13:10:28,830 - INFO - Scores: lightgbm=-0.108, random_forest=-0.154, neural_network=-0.235, xgboost=-0.141, catboost=-0.122, lasso=0.164, mutual_information=0.082, univariate_selection=0.175, rfe=-0.175, boruta=-0.171, stability_selection=0.615, importance=0.48
2025-11-16 13:10:28,831 - INFO - Summary: R²=-0.033±0.252, importance=0.46, composite=0.344
2025-11-16 13:10:28,849 - INFO -
============================================================
2025-11-16 13:10:28,849 - INFO - Evaluating: vallemdd_10m_0.002 (y_will_valley_mdd_10m_0.002)
2025-11-16 13:10:28,849 - INFO - ============================================================
2025-11-16 13:10:28,849 - INFO - AAPL...
2025-11-16 13:10:29,147 - INFO - Using GPU (CUDA) for LightGBM
2025-11-16 13:39:00,669 - INFO - Scores: lightgbm=-0.104, random_forest=-0.168, neural_network=-0.258, xgboost=-0.170, catboost=-0.108, lasso=0.138, mutual_information=0.074, univariate_selection=0.164, rfe=-0.187, boruta=-0.183, stability_selection=0.610, importance=0.47
2025-11-16 13:39:00,669 - INFO - MSFT...
2025-11-16 13:39:00,982 - INFO - Using GPU (CUDA) for LightGBM
2025-11-16 14:08:32,106 - INFO - Scores: lightgbm=-0.074, random_forest=-0.116, neural_network=-0.186, xgboost=-0.118, catboost=-0.096, lasso=0.157, mutual_information=0.070, univariate_selection=0.166, rfe=-0.133, boruta=-0.144, stability_selection=0.621, importance=0.47
2025-11-16 14:08:32,106 - INFO - GOOGL...
2025-11-16 14:08:32,412 - INFO - Using GPU (CUDA) for LightGBM
2025-11-16 14:37:15,266 - INFO - Scores: lightgbm=-0.117, random_forest=-0.185, neural_network=-0.294, xgboost=-0.157, catboost=-0.140, lasso=0.131, mutual_information=0.078, univariate_selection=0.156, rfe=-0.209, boruta=-0.205, stability_selection=0.590, importance=0.47
2025-11-16 14:37:15,266 - INFO - TSLA...
2025-11-16 14:37:15,592 - INFO - Using GPU (CUDA) for LightGBM
2025-11-16 15:04:32,782 - INFO - Scores: lightgbm=-0.268, random_forest=-0.319, neural_network=-0.377, xgboost=-0.308, catboost=-0.282, lasso=0.090, mutual_information=0.102, univariate_selection=0.198, rfe=-0.356, boruta=-0.371, stability_selection=0.618, importance=0.41
2025-11-16 15:04:32,782 - INFO - JPM...
2025-11-16 15:04:33,082 - INFO - Using GPU (CUDA) for LightGBM
2025-11-16 15:32:34,688 - INFO - Scores: lightgbm=-0.110, random_forest=-0.142, neural_network=-0.238, xgboost=-0.139, catboost=-0.092, lasso=0.137, mutual_information=0.081, univariate_selection=0.176, rfe=-0.159, boruta=-0.150, stability_selection=0.615, importance=0.48
2025-11-16 15:32:34,689 - INFO - Summary: R²=-0.031±0.249, importance=0.46, composite=0.344
2025-11-16 15:32:34,707 - INFO -
============================================================
2025-11-16 15:32:34,707 - INFO - Evaluating: peak_mfe_10m_0.005 (y_will_peak_mfe_10m_0.005)
2025-11-16 15:32:34,707 - INFO - ============================================================
2025-11-16 15:32:34,708 - INFO - AAPL...
2025-11-16 15:32:35,000 - INFO - Using GPU (CUDA) for LightGBM
2025-11-16 16:01:48,141 - INFO - Scores: lightgbm=0.101, random_forest=0.040, neural_network=-0.002, xgboost=0.085, catboost=0.093, lasso=0.181, mutual_information=0.068, univariate_selection=0.137, rfe=0.035, boruta=0.042, stability_selection=0.840, importance=0.47
2025-11-16 16:01:48,141 - INFO - MSFT...
2025-11-16 16:01:48,460 - INFO - Using GPU (CUDA) for LightGBM
2025-11-16 16:28:55,018 - INFO - Scores: lightgbm=0.057, random_forest=-0.014, neural_network=-0.088, xgboost=0.035, catboost=0.057, lasso=0.183, mutual_information=0.069, univariate_selection=0.134, rfe=-0.010, boruta=-0.014, stability_selection=0.851, importance=0.47
2025-11-16 16:28:55,018 - INFO - GOOGL...
2025-11-16 16:28:55,328 - INFO - Using GPU (CUDA) for LightGBM
2025-11-16 16:57:26,240 - INFO - Scores: lightgbm=0.043, random_forest=-0.012, neural_network=-0.056, xgboost=0.023, catboost=0.038, lasso=0.148, mutual_information=0.069, univariate_selection=0.130, rfe=-0.011, boruta=-0.013, stability_selection=0.832, importance=0.46
2025-11-16 16:57:26,241 - INFO - TSLA...
2025-11-16 16:57:26,556 - INFO - Using GPU (CUDA) for LightGBM
2025-11-16 17:27:17,078 - INFO - Scores: lightgbm=-0.114, random_forest=-0.145, neural_network=-0.206, xgboost=-0.136, catboost=-0.125, lasso=0.148, mutual_information=0.072, univariate_selection=0.144, rfe=-0.162, boruta=-0.162, stability_selection=0.646, importance=0.38
2025-11-16 17:27:17,078 - INFO - JPM...
2025-11-16 17:27:17,391 - INFO - Using GPU (CUDA) for LightGBM
2025-11-16 17:56:01,794 - INFO - Scores: lightgbm=0.085, random_forest=0.036, neural_network=0.013, xgboost=0.063, catboost=0.074, lasso=0.176, mutual_information=0.071, univariate_selection=0.136, rfe=0.049, boruta=0.047, stability_selection=0.854, importance=0.47
2025-11-16 17:56:01,794 - INFO - Summary: R²=0.102±0.232, importance=0.45, composite=0.415
2025-11-16 17:56:01,812 - INFO -
============================================================
2025-11-16 17:56:01,812 - INFO - Evaluating: vallemdd_10m_0.005 (y_will_valley_mdd_10m_0.005)
2025-11-16 17:56:01,812 - INFO - ============================================================
2025-11-16 17:56:01,812 - INFO - AAPL...
2025-11-16 17:56:02,103 - INFO - Using GPU (CUDA) for LightGBM
2025-11-16 18:25:09,650 - INFO - Scores: lightgbm=0.092, random_forest=0.035, neural_network=-0.044, xgboost=0.058, catboost=0.080, lasso=0.176, mutual_information=0.075, univariate_selection=0.144, rfe=0.031, boruta=0.022, stability_selection=0.840, importance=0.49
2025-11-16 18:25:09,650 - INFO - MSFT...
2025-11-16 18:25:09,968 - INFO - Using GPU (CUDA) for LightGBM
2025-11-16 18:54:59,531 - INFO - Scores: lightgbm=0.075, random_forest=0.035, neural_network=-0.020, xgboost=0.060, catboost=0.076, lasso=0.187, mutual_information=0.064, univariate_selection=0.142, rfe=0.029, boruta=0.026, stability_selection=0.846, importance=0.48
2025-11-16 18:54:59,531 - INFO - GOOGL...
2025-11-16 18:54:59,852 - INFO - Using GPU (CUDA) for LightGBM
2025-11-16 19:24:54,689 - INFO - Scores: lightgbm=0.038, random_forest=-0.010, neural_network=-0.053, xgboost=0.028, catboost=0.051, lasso=0.145, mutual_information=0.072, univariate_selection=0.134, rfe=-0.003, boruta=-0.016, stability_selection=0.819, importance=0.47
2025-11-16 19:24:54,689 - INFO - TSLA...
2025-11-16 19:24:55,008 - INFO - Using GPU (CUDA) for LightGBM
2025-11-16 19:54:41,780 - INFO - Scores: lightgbm=-0.105, random_forest=-0.153, neural_network=-0.210, xgboost=-0.150, catboost=-0.107, lasso=0.156, mutual_information=0.081, univariate_selection=0.147, rfe=-0.170, boruta=-0.156, stability_selection=0.630, importance=0.37
2025-11-16 19:54:41,780 - INFO - JPM...
2025-11-16 19:54:42,081 - INFO - Using GPU (CUDA) for LightGBM
2025-11-16 20:23:31,923 - INFO - Scores: lightgbm=0.116, random_forest=0.034, neural_network=-0.007, xgboost=0.066, catboost=0.117, lasso=0.131, mutual_information=0.073, univariate_selection=0.133, rfe=0.052, boruta=0.039, stability_selection=0.852, importance=0.47
2025-11-16 20:23:31,923 - INFO - Summary: R²=0.105±0.228, importance=0.45, composite=0.420
2025-11-16 20:23:31,942 - INFO -
============================================================
2025-11-16 20:23:31,942 - INFO - Evaluating: peak_mfe_15m_0.001 (y_will_peak_mfe_15m_0.001)
2025-11-16 20:23:31,942 - INFO - ============================================================
2025-11-16 20:23:31,942 - INFO - AAPL...
2025-11-16 20:23:32,234 - INFO - Using GPU (CUDA) for LightGBM
2025-11-16 20:51:27,596 - INFO - Scores: lightgbm=-0.228, random_forest=-0.207, neural_network=-0.316, xgboost=-0.222, catboost=-0.181, lasso=0.128, mutual_information=0.124, univariate_selection=0.236, rfe=-0.236, boruta=-0.232, stability_selection=0.684, importance=0.44
2025-11-16 20:51:27,596 - INFO - MSFT...
2025-11-16 20:51:27,912 - INFO - Using GPU (CUDA) for LightGBM
2025-11-16 21:19:01,852 - INFO - Scores: lightgbm=-0.197, random_forest=-0.229, neural_network=-0.283, xgboost=-0.238, catboost=-0.186, lasso=0.134, mutual_information=0.129, univariate_selection=0.250, rfe=-0.252, boruta=-0.256, stability_selection=0.678, importance=0.54
2025-11-16 21:19:01,853 - INFO - GOOGL...
2025-11-16 21:19:02,163 - INFO - Using GPU (CUDA) for LightGBM
2025-11-16 21:48:15,167 - INFO - Scores: lightgbm=-0.216, random_forest=-0.239, neural_network=-0.307, xgboost=-0.253, catboost=-0.194, lasso=0.122, mutual_information=0.129, univariate_selection=0.257, rfe=-0.272, boruta=-0.268, stability_selection=0.692, importance=0.53
2025-11-16 21:48:15,167 - INFO - TSLA...
2025-11-16 21:48:15,483 - INFO - Using GPU (CUDA) for LightGBM
2025-11-16 22:16:47,587 - INFO - Scores: lightgbm=-0.207, random_forest=-0.264, neural_network=-0.298, xgboost=-0.251, catboost=-0.240, lasso=0.090, mutual_information=0.146, univariate_selection=0.256, rfe=-0.281, boruta=-0.283, stability_selection=0.767, importance=0.44
2025-11-16 22:16:47,587 - INFO - JPM...
2025-11-16 22:16:47,891 - INFO - Using GPU (CUDA) for LightGBM
2025-11-16 22:42:46,848 - INFO - Scores: lightgbm=-0.164, random_forest=-0.185, neural_network=-0.281, xgboost=-0.196, catboost=-0.161, lasso=0.142, mutual_information=0.135, univariate_selection=0.261, rfe=-0.243, boruta=-0.224, stability_selection=0.679, importance=0.55
2025-11-16 22:42:46,848 - INFO - Summary: R²=-0.041±0.297, importance=0.50, composite=0.346
2025-11-16 22:42:46,867 - INFO -
============================================================
2025-11-16 22:42:46,867 - INFO - Evaluating: vallemdd_15m_0.001 (y_will_valley_mdd_15m_0.001)
2025-11-16 22:42:46,867 - INFO - ============================================================
2025-11-16 22:42:46,867 - INFO - AAPL...
2025-11-16 22:42:47,161 - INFO - Using GPU (CUDA) for LightGBM
2025-11-16 23:09:57,091 - INFO - Scores: lightgbm=-0.202, random_forest=-0.256, neural_network=-0.314, xgboost=-0.221, catboost=-0.186, lasso=0.118, mutual_information=0.116, univariate_selection=0.234, rfe=-0.279, boruta=-0.267, stability_selection=0.665, importance=0.44
2025-11-16 23:09:57,092 - INFO - MSFT...
2025-11-16 23:09:57,418 - INFO - Using GPU (CUDA) for LightGBM
2025-11-16 23:38:39,000 - INFO - Scores: lightgbm=-0.217, random_forest=-0.233, neural_network=-0.288, xgboost=-0.228, catboost=-0.186, lasso=0.136, mutual_information=0.110, univariate_selection=0.237, rfe=-0.252, boruta=-0.253, stability_selection=0.658, importance=0.52
2025-11-16 23:38:39,001 - INFO - GOOGL...
2025-11-16 23:38:39,309 - INFO - Using GPU (CUDA) for LightGBM
2025-11-17 00:05:59,998 - INFO - Scores: lightgbm=-0.171, random_forest=-0.226, neural_network=-0.327, xgboost=-0.264, catboost=-0.190, lasso=0.121, mutual_information=0.119, univariate_selection=0.233, rfe=-0.255, boruta=-0.257, stability_selection=0.681, importance=0.52
2025-11-17 00:05:59,999 - INFO - TSLA...
2025-11-17 00:06:00,325 - INFO - Using GPU (CUDA) for LightGBM
2025-11-17 00:32:00,844 - INFO - Scores: lightgbm=-0.229, random_forest=-0.274, neural_network=-0.302, xgboost=-0.275, catboost=-0.211, lasso=0.074, mutual_information=0.150, univariate_selection=0.269, rfe=-0.284, boruta=-0.288, stability_selection=0.766, importance=0.44
2025-11-17 00:32:00,844 - INFO - JPM...
2025-11-17 00:32:01,153 - INFO - Using GPU (CUDA) for LightGBM
2025-11-17 00:58:31,652 - INFO - Scores: lightgbm=-0.162, random_forest=-0.214, neural_network=-0.332, xgboost=-0.208, catboost=-0.158, lasso=0.127, mutual_information=0.121, univariate_selection=0.251, rfe=-0.244, boruta=-0.252, stability_selection=0.662, importance=0.53
2025-11-17 00:58:31,653 - INFO - Summary: R²=-0.048±0.295, importance=0.49, composite=0.343
2025-11-17 00:58:31,670 - INFO -
============================================================
2025-11-17 00:58:31,670 - INFO - Evaluating: peak_mfe_15m_0.002 (y_will_peak_mfe_15m_0.002)
2025-11-17 00:58:31,670 - INFO - ============================================================
2025-11-17 00:58:31,670 - INFO - AAPL...
2025-11-17 00:58:31,965 - INFO - Using GPU (CUDA) for LightGBM
2025-11-17 01:29:01,362 - INFO - Scores: lightgbm=-0.058, random_forest=-0.077, neural_network=-0.152, xgboost=-0.077, catboost=-0.051, lasso=0.195, mutual_information=0.102, univariate_selection=0.203, rfe=-0.092, boruta=-0.083, stability_selection=0.593, importance=0.42
2025-11-17 01:29:01,362 - INFO - MSFT...
2025-11-17 01:29:01,689 - INFO - Using GPU (CUDA) for LightGBM
2025-11-17 01:58:55,067 - INFO - Scores: lightgbm=-0.008, random_forest=-0.046, neural_network=-0.097, xgboost=-0.044, catboost=-0.008, lasso=0.204, mutual_information=0.109, univariate_selection=0.213, rfe=-0.061, boruta=-0.056, stability_selection=0.580, importance=0.51
2025-11-17 01:58:55,067 - INFO - GOOGL...
2025-11-17 01:58:55,376 - INFO - Using GPU (CUDA) for LightGBM
2025-11-17 02:28:37,955 - INFO - Scores: lightgbm=-0.033, random_forest=-0.103, neural_network=-0.141, xgboost=-0.090, catboost=-0.041, lasso=0.191, mutual_information=0.105, univariate_selection=0.211, rfe=-0.102, boruta=-0.096, stability_selection=0.578, importance=0.51
2025-11-17 02:28:37,955 - INFO - TSLA...
2025-11-17 02:28:38,273 - INFO - Using GPU (CUDA) for LightGBM
2025-11-17 02:56:15,782 - INFO - Scores: lightgbm=-0.207, random_forest=-0.249, neural_network=-0.304, xgboost=-0.259, catboost=-0.212, lasso=0.136, mutual_information=0.135, univariate_selection=0.230, rfe=-0.267, boruta=-0.263, stability_selection=0.680, importance=0.44
2025-11-17 02:56:15,782 - INFO - JPM...
2025-11-17 02:56:16,097 - INFO - Using GPU (CUDA) for LightGBM
2025-11-17 03:24:28,909 - INFO - Scores: lightgbm=-0.007, random_forest=-0.064, neural_network=-0.172, xgboost=-0.051, catboost=-0.035, lasso=0.212, mutual_information=0.113, univariate_selection=0.220, rfe=-0.067, boruta=-0.077, stability_selection=0.579, importance=0.52
2025-11-17 03:24:28,909 - INFO - Summary: R²=0.033±0.220, importance=0.48, composite=0.380
2025-11-17 03:24:28,927 - INFO -
============================================================
2025-11-17 03:24:28,927 - INFO - Evaluating: vallemdd_15m_0.002 (y_will_valley_mdd_15m_0.002)
2025-11-17 03:24:28,927 - INFO - ============================================================
2025-11-17 03:24:28,927 - INFO - AAPL...
2025-11-17 03:24:29,244 - INFO - Using GPU (CUDA) for LightGBM
2025-11-17 03:53:38,641 - INFO - Scores: lightgbm=-0.051, random_forest=-0.111, neural_network=-0.196, xgboost=-0.098, catboost=-0.049, lasso=0.176, mutual_information=0.098, univariate_selection=0.199, rfe=-0.119, boruta=-0.110, stability_selection=0.589, importance=0.50
2025-11-17 03:53:38,641 - INFO - MSFT...
2025-11-17 03:53:38,962 - INFO - Using GPU (CUDA) for LightGBM
2025-11-17 04:23:23,765 - INFO - Scores: lightgbm=-0.007, random_forest=-0.050, neural_network=-0.119, xgboost=-0.042, catboost=-0.013, lasso=0.210, mutual_information=0.094, univariate_selection=0.205, rfe=-0.052, boruta=-0.068, stability_selection=0.586, importance=0.51
2025-11-17 04:23:23,765 - INFO - GOOGL...
2025-11-17 04:23:24,072 - INFO - Using GPU (CUDA) for LightGBM
2025-11-17 04:50:46,176 - INFO - Scores: lightgbm=-0.047, random_forest=-0.088, neural_network=-0.177, xgboost=-0.084, catboost=-0.021, lasso=0.194, mutual_information=0.104, univariate_selection=0.201, rfe=-0.105, boruta=-0.100, stability_selection=0.568, importance=0.51
2025-11-17 04:50:46,176 - INFO - TSLA...
2025-11-17 04:50:46,495 - INFO - Using GPU (CUDA) for LightGBM
2025-11-17 05:18:03,333 - INFO - Scores: lightgbm=-0.199, random_forest=-0.243, neural_network=-0.330, xgboost=-0.248, catboost=-0.192, lasso=0.115, mutual_information=0.137, univariate_selection=0.237, rfe=-0.269, boruta=-0.273, stability_selection=0.679, importance=0.45
2025-11-17 05:18:03,333 - INFO - JPM...
2025-11-17 05:18:03,635 - INFO - Using GPU (CUDA) for LightGBM
2025-11-17 05:46:17,662 - INFO - Scores: lightgbm=-0.000, random_forest=-0.063, neural_network=-0.141, xgboost=-0.052, catboost=0.003, lasso=0.189, mutual_information=0.101, univariate_selection=0.216, rfe=-0.085, boruta=-0.082, stability_selection=0.581, importance=0.51
2025-11-17 05:46:17,663 - INFO - Summary: R²=0.029±0.221, importance=0.49, composite=0.381
2025-11-17 05:46:17,683 - INFO -
============================================================
2025-11-17 05:46:17,683 - INFO - Evaluating: peak_mfe_15m_0.005 (y_will_peak_mfe_15m_0.005)
2025-11-17 05:46:17,683 - INFO - ============================================================
2025-11-17 05:46:17,683 - INFO - AAPL...
2025-11-17 05:46:17,977 - INFO - Using GPU (CUDA) for LightGBM
2025-11-17 06:16:12,911 - INFO - Scores: lightgbm=0.166, random_forest=0.113, neural_network=0.054, xgboost=0.146, catboost=0.190, lasso=0.224, mutual_information=0.086, univariate_selection=0.166, rfe=0.124, boruta=0.129, stability_selection=0.775, importance=0.49
2025-11-17 06:16:12,911 - INFO - MSFT...
2025-11-17 06:16:13,242 - INFO - Using GPU (CUDA) for LightGBM
2025-11-17 06:46:48,348 - INFO - Scores: lightgbm=0.203, random_forest=0.130, neural_network=0.102, xgboost=0.159, catboost=0.195, lasso=0.235, mutual_information=0.079, univariate_selection=0.158, rfe=0.128, boruta=0.143, stability_selection=0.787, importance=0.49
2025-11-17 06:46:48,348 - INFO - GOOGL...
2025-11-17 06:46:48,663 - INFO - Using GPU (CUDA) for LightGBM
2025-11-17 07:15:03,937 - INFO - Scores: lightgbm=0.159, random_forest=0.086, neural_network=0.006, xgboost=0.134, catboost=0.149, lasso=0.209, mutual_information=0.080, univariate_selection=0.159, rfe=0.093, boruta=0.093, stability_selection=0.761, importance=0.49
2025-11-17 07:15:03,937 - INFO - TSLA...
2025-11-17 07:15:04,248 - INFO - Using GPU (CUDA) for LightGBM
2025-11-17 07:45:06,357 - INFO - Scores: lightgbm=0.002, random_forest=-0.018, neural_network=-0.107, xgboost=-0.020, catboost=0.009, lasso=0.215, mutual_information=0.104, univariate_selection=0.188, rfe=-0.034, boruta=-0.035, stability_selection=0.597, importance=0.41
2025-11-17 07:45:06,357 - INFO - JPM...
2025-11-17 07:45:06,657 - INFO - Using GPU (CUDA) for LightGBM
2025-11-17 08:11:10,462 - INFO - Scores: lightgbm=0.174, random_forest=0.107, neural_network=0.069, xgboost=0.159, catboost=0.154, lasso=0.223, mutual_information=0.078, univariate_selection=0.158, rfe=0.123, boruta=0.118, stability_selection=0.789, importance=0.47
2025-11-17 08:11:10,462 - INFO - Summary: R²=0.172±0.187, importance=0.47, composite=0.479
2025-11-17 08:11:10,480 - INFO -
============================================================
2025-11-17 08:11:10,480 - INFO - Evaluating: vallemdd_15m_0.005 (y_will_valley_mdd_15m_0.005)
2025-11-17 08:11:10,481 - INFO - ============================================================
2025-11-17 08:11:10,481 - INFO - AAPL...
2025-11-17 08:11:10,787 - INFO - Using GPU (CUDA) for LightGBM
2025-11-17 08:39:16,242 - INFO - Scores: lightgbm=0.224, random_forest=0.163, neural_network=0.080, xgboost=0.211, catboost=0.213, lasso=0.226, mutual_information=0.082, univariate_selection=0.165, rfe=0.170, boruta=0.157, stability_selection=0.776, importance=0.50
2025-11-17 08:39:16,242 - INFO - MSFT...
2025-11-17 08:39:16,570 - INFO - Using GPU (CUDA) for LightGBM
2025-11-17 09:10:00,293 - INFO - Scores: lightgbm=0.232, random_forest=0.175, neural_network=0.088, xgboost=0.220, catboost=0.238, lasso=0.240, mutual_information=0.074, univariate_selection=0.159, rfe=0.160, boruta=0.158, stability_selection=0.785, importance=0.50
2025-11-17 09:10:00,293 - INFO - GOOGL...
2025-11-17 09:10:00,600 - INFO - Using GPU (CUDA) for LightGBM
2025-11-17 09:40:21,513 - INFO - Scores: lightgbm=0.107, random_forest=0.119, neural_network=0.045, xgboost=0.143, catboost=0.161, lasso=0.214, mutual_information=0.085, univariate_selection=0.157, rfe=0.121, boruta=0.112, stability_selection=0.749, importance=0.49
2025-11-17 09:40:21,514 - INFO - TSLA...
2025-11-17 09:40:21,833 - INFO - Using GPU (CUDA) for LightGBM
2025-11-17 10:09:49,431 - INFO - Scores: lightgbm=0.015, random_forest=-0.046, neural_network=-0.089, xgboost=-0.022, catboost=0.004, lasso=0.217, mutual_information=0.115, univariate_selection=0.192, rfe=-0.050, boruta=-0.046, stability_selection=0.577, importance=0.42
2025-11-17 10:09:49,431 - INFO - JPM...
2025-11-17 10:09:49,746 - INFO - Using GPU (CUDA) for LightGBM
2025-11-17 10:38:50,917 - INFO - Scores: lightgbm=0.206, random_forest=0.149, neural_network=0.087, xgboost=0.182, catboost=0.208, lasso=0.201, mutual_information=0.083, univariate_selection=0.158, rfe=0.157, boruta=0.151, stability_selection=0.794, importance=0.48
2025-11-17 10:38:50,917 - INFO - Summary: R²=0.186±0.180, importance=0.48, composite=0.492
2025-11-17 10:38:50,935 - INFO -
============================================================
2025-11-17 10:38:50,935 - INFO - Evaluating: peak_mfe_30m_0.001 (y_will_peak_mfe_30m_0.001)
2025-11-17 10:38:50,935 - INFO - ============================================================
2025-11-17 10:38:50,935 - INFO - AAPL...
2025-11-17 10:38:51,228 - INFO - Using GPU (CUDA) for LightGBM
2025-11-17 11:04:40,656 - INFO - Scores: lightgbm=-0.159, random_forest=-0.212, neural_network=-0.188, xgboost=-0.195, catboost=-0.135, lasso=0.131, mutual_information=0.145, univariate_selection=0.275, rfe=-0.226, boruta=-0.202, stability_selection=0.786, importance=0.45
2025-11-17 11:04:40,656 - INFO - MSFT...
2025-11-17 11:04:40,972 - INFO - Using GPU (CUDA) for LightGBM
2025-11-17 11:30:32,197 - INFO - Scores: lightgbm=-0.173, random_forest=-0.237, neural_network=-0.202, xgboost=-0.215, catboost=-0.188, lasso=0.142, mutual_information=0.149, univariate_selection=0.279, rfe=-0.231, boruta=-0.232, stability_selection=0.779, importance=0.56
2025-11-17 11:30:32,197 - INFO - GOOGL...
2025-11-17 11:30:32,506 - INFO - Using GPU (CUDA) for LightGBM
2025-11-17 11:56:47,277 - INFO - Scores: lightgbm=-0.142, random_forest=-0.204, neural_network=-0.241, xgboost=-0.225, catboost=-0.169, lasso=0.126, mutual_information=0.142, univariate_selection=0.281, rfe=-0.211, boruta=-0.221, stability_selection=0.784, importance=0.54
2025-11-17 11:56:47,277 - INFO - TSLA...
2025-11-17 11:56:47,590 - INFO - Using GPU (CUDA) for LightGBM
2025-11-17 12:22:42,207 - INFO - Scores: lightgbm=-0.200, random_forest=-0.193, neural_network=-0.231, xgboost=-0.199, catboost=-0.176, lasso=0.097, mutual_information=0.153, univariate_selection=0.281, rfe=-0.192, boruta=-0.193, stability_selection=0.836, importance=0.45
2025-11-17 12:22:42,207 - INFO - JPM...
2025-11-17 12:22:42,513 - INFO - Using GPU (CUDA) for LightGBM
2025-11-17 12:47:21,181 - INFO - Scores: lightgbm=-0.136, random_forest=-0.214, neural_network=-0.274, xgboost=-0.179, catboost=-0.129, lasso=0.146, mutual_information=0.161, univariate_selection=0.284, rfe=-0.222, boruta=-0.219, stability_selection=0.774, importance=0.55
2025-11-17 12:47:21,181 - INFO - Summary: R²=-0.004±0.305, importance=0.51, composite=0.351
2025-11-17 12:47:21,200 - INFO -
============================================================
2025-11-17 12:47:21,200 - INFO - Evaluating: vallemdd_30m_0.001 (y_will_valley_mdd_30m_0.001)
2025-11-17 12:47:21,200 - INFO - ============================================================
2025-11-17 12:47:21,200 - INFO - AAPL...
2025-11-17 12:47:21,494 - INFO - Using GPU (CUDA) for LightGBM
2025-11-17 13:13:41,030 - INFO - Scores: lightgbm=-0.166, random_forest=-0.233, neural_network=-0.249, xgboost=-0.218, catboost=-0.171, lasso=0.128, mutual_information=0.138, univariate_selection=0.262, rfe=-0.234, boruta=-0.239, stability_selection=0.757, importance=0.45
2025-11-17 13:13:41,030 - INFO - MSFT...
2025-11-17 13:13:41,350 - INFO - Using GPU (CUDA) for LightGBM
2025-11-17 13:40:22,501 - INFO - Scores: lightgbm=-0.168, random_forest=-0.219, neural_network=-0.256, xgboost=-0.199, catboost=-0.160, lasso=0.143, mutual_information=0.134, univariate_selection=0.268, rfe=-0.223, boruta=-0.211, stability_selection=0.753, importance=0.54
2025-11-17 13:40:22,501 - INFO - GOOGL...
2025-11-17 13:40:22,813 - INFO - Using GPU (CUDA) for LightGBM
2025-11-17 14:05:50,240 - INFO - Scores: lightgbm=-0.158, random_forest=-0.206, neural_network=-0.266, xgboost=-0.198, catboost=-0.167, lasso=0.128, mutual_information=0.131, univariate_selection=0.261, rfe=-0.233, boruta=-0.220, stability_selection=0.770, importance=0.53
2025-11-17 14:05:50,241 - INFO - TSLA...
2025-11-17 14:05:50,553 - INFO - Using GPU (CUDA) for LightGBM
2025-11-17 14:31:46,919 - INFO - Scores: lightgbm=-0.187, random_forest=-0.199, neural_network=-0.262, xgboost=-0.192, catboost=-0.153, lasso=0.084, mutual_information=0.150, univariate_selection=0.276, rfe=-0.201, boruta=-0.206, stability_selection=0.826, importance=0.45
2025-11-17 14:31:46,919 - INFO - JPM...
2025-11-17 14:31:47,227 - INFO - Using GPU (CUDA) for LightGBM
2025-11-17 14:57:25,648 - INFO - Scores: lightgbm=-0.127, random_forest=-0.193, neural_network=-0.255, xgboost=-0.165, catboost=-0.151, lasso=0.143, mutual_information=0.143, univariate_selection=0.278, rfe=-0.207, boruta=-0.222, stability_selection=0.759, importance=0.55
2025-11-17 14:57:25,648 - INFO - Summary: R²=-0.011±0.302, importance=0.50, composite=0.349
2025-11-17 14:57:25,666 - INFO -
============================================================
2025-11-17 14:57:25,666 - INFO - Evaluating: peak_mfe_30m_0.002 (y_will_peak_mfe_30m_0.002)
2025-11-17 14:57:25,666 - INFO - ============================================================
2025-11-17 14:57:25,666 - INFO - AAPL...
2025-11-17 14:57:25,963 - INFO - Using GPU (CUDA) for LightGBM
2025-11-17 15:26:13,820 - INFO - Scores: lightgbm=-0.060, random_forest=-0.097, neural_network=-0.107, xgboost=-0.119, catboost=-0.078, lasso=0.210, mutual_information=0.136, univariate_selection=0.245, rfe=-0.115, boruta=-0.112, stability_selection=0.665, importance=0.45
2025-11-17 15:26:13,820 - INFO - MSFT...
2025-11-17 15:26:14,134 - INFO - Using GPU (CUDA) for LightGBM
2025-11-17 15:54:28,408 - INFO - Scores: lightgbm=-0.046, random_forest=-0.074, neural_network=-0.102, xgboost=-0.072, catboost=-0.031, lasso=0.231, mutual_information=0.136, univariate_selection=0.260, rfe=-0.073, boruta=-0.084, stability_selection=0.653, importance=0.55
2025-11-17 15:54:28,408 - INFO - GOOGL...
2025-11-17 15:54:28,710 - INFO - Using GPU (CUDA) for LightGBM
2025-11-17 16:22:35,402 - INFO - Scores: lightgbm=-0.092, random_forest=-0.137, neural_network=-0.193, xgboost=-0.121, catboost=-0.078, lasso=0.198, mutual_information=0.133, univariate_selection=0.241, rfe=-0.141, boruta=-0.136, stability_selection=0.667, importance=0.53
2025-11-17 16:22:35,402 - INFO - TSLA...
2025-11-17 16:22:35,717 - INFO - Using GPU (CUDA) for LightGBM
2025-11-17 16:48:37,121 - INFO - Scores: lightgbm=-0.156, random_forest=-0.224, neural_network=-0.253, xgboost=-0.211, catboost=-0.166, lasso=0.153, mutual_information=0.154, univariate_selection=0.266, rfe=-0.237, boruta=-0.219, stability_selection=0.773, importance=0.45
2025-11-17 16:48:37,121 - INFO - JPM...
2025-11-17 16:48:37,412 - INFO - Using GPU (CUDA) for LightGBM
2025-11-17 17:15:25,959 - INFO - Scores: lightgbm=-0.024, random_forest=-0.088, neural_network=-0.100, xgboost=-0.071, catboost=-0.037, lasso=0.229, mutual_information=0.145, univariate_selection=0.265, rfe=-0.087, boruta=-0.089, stability_selection=0.650, importance=0.55
2025-11-17 17:15:25,959 - INFO - Summary: R²=0.043±0.247, importance=0.51, composite=0.390
2025-11-17 17:15:25,977 - INFO -
============================================================
2025-11-17 17:15:25,977 - INFO - Evaluating: vallemdd_30m_0.002 (y_will_valley_mdd_30m_0.002)
2025-11-17 17:15:25,977 - INFO - ============================================================
2025-11-17 17:15:25,977 - INFO - AAPL...
2025-11-17 17:15:26,270 - INFO - Using GPU (CUDA) for LightGBM
2025-11-17 17:43:51,063 - INFO - Scores: lightgbm=-0.061, random_forest=-0.125, neural_network=-0.146, xgboost=-0.096, catboost=-0.084, lasso=0.202, mutual_information=0.130, univariate_selection=0.234, rfe=-0.140, boruta=-0.135, stability_selection=0.631, importance=0.44
2025-11-17 17:43:51,064 - INFO - MSFT...
2025-11-17 17:43:51,379 - INFO - Using GPU (CUDA) for LightGBM
2025-11-17 18:13:01,701 - INFO - Scores: lightgbm=-0.038, random_forest=-0.084, neural_network=-0.101, xgboost=-0.059, catboost=-0.021, lasso=0.229, mutual_information=0.123, univariate_selection=0.241, rfe=-0.103, boruta=-0.081, stability_selection=0.618, importance=0.53
2025-11-17 18:13:01,701 - INFO - GOOGL...
2025-11-17 18:13:02,008 - INFO - Using GPU (CUDA) for LightGBM
2025-11-17 18:41:24,861 - INFO - Scores: lightgbm=-0.054, random_forest=-0.105, neural_network=-0.146, xgboost=-0.094, catboost=-0.036, lasso=0.210, mutual_information=0.126, univariate_selection=0.235, rfe=-0.119, boruta=-0.114, stability_selection=0.646, importance=0.54
2025-11-17 18:41:24,861 - INFO - TSLA...
2025-11-17 18:41:25,176 - INFO - Using GPU (CUDA) for LightGBM
2025-11-17 19:07:58,174 - INFO - Scores: lightgbm=-0.175, random_forest=-0.232, neural_network=-0.263, xgboost=-0.209, catboost=-0.192, lasso=0.133, mutual_information=0.144, univariate_selection=0.256, rfe=-0.238, boruta=-0.241, stability_selection=0.766, importance=0.45
2025-11-17 19:07:58,174 - INFO - JPM...
2025-11-17 19:07:58,474 - INFO - Using GPU (CUDA) for LightGBM
2025-11-17 19:35:10,408 - INFO - Scores: lightgbm=-0.032, random_forest=-0.091, neural_network=-0.136, xgboost=-0.057, catboost=-0.021, lasso=0.222, mutual_information=0.138, univariate_selection=0.259, rfe=-0.114, boruta=-0.093, stability_selection=0.632, importance=0.55
2025-11-17 19:35:10,408 - INFO - Summary: R²=0.039±0.240, importance=0.50, composite=0.386
2025-11-17 19:35:10,428 - INFO -
============================================================
2025-11-17 19:35:10,428 - INFO - Evaluating: peak_mfe_30m_0.005 (y_will_peak_mfe_30m_0.005)
2025-11-17 19:35:10,428 - INFO - ============================================================
2025-11-17 19:35:10,428 - INFO - AAPL...
2025-11-17 19:35:10,726 - INFO - Using GPU (CUDA) for LightGBM
2025-11-17 20:05:24,286 - INFO - Scores: lightgbm=0.137, random_forest=0.088, neural_network=0.031, xgboost=0.121, catboost=0.127, lasso=0.263, mutual_information=0.126, univariate_selection=0.212, rfe=0.101, boruta=0.100, stability_selection=0.631, importance=0.53
2025-11-17 20:05:24,286 - INFO - MSFT...
2025-11-17 20:05:24,612 - INFO - Using GPU (CUDA) for LightGBM
2025-11-17 20:36:05,699 - INFO - Scores: lightgbm=0.140, random_forest=0.116, neural_network=0.065, xgboost=0.108, catboost=0.149, lasso=0.275, mutual_information=0.123, univariate_selection=0.209, rfe=0.116, boruta=0.130, stability_selection=0.648, importance=0.52
2025-11-17 20:36:05,699 - INFO - GOOGL...
2025-11-17 20:36:06,017 - INFO - Using GPU (CUDA) for LightGBM
2025-11-17 21:06:30,797 - INFO - Scores: lightgbm=0.111, random_forest=0.068, neural_network=0.001, xgboost=0.087, catboost=0.107, lasso=0.254, mutual_information=0.119, univariate_selection=0.214, rfe=0.062, boruta=0.068, stability_selection=0.621, importance=0.51
2025-11-17 21:06:30,798 - INFO - TSLA...
2025-11-17 21:06:31,118 - INFO - Using GPU (CUDA) for LightGBM
2025-11-17 21:34:29,810 - INFO - Scores: lightgbm=0.009, random_forest=-0.033, neural_network=-0.066, xgboost=-0.027, catboost=-0.007, lasso=0.265, mutual_information=0.150, univariate_selection=0.239, rfe=-0.028, boruta=-0.041, stability_selection=0.600, importance=0.46
2025-11-17 21:34:29,810 - INFO - JPM...
2025-11-17 21:34:30,118 - INFO - Using GPU (CUDA) for LightGBM
2025-11-17 22:03:50,069 - INFO - Scores: lightgbm=0.120, random_forest=0.056, neural_network=-0.011, xgboost=0.108, catboost=0.121, lasso=0.261, mutual_information=0.122, univariate_selection=0.216, rfe=0.048, boruta=0.062, stability_selection=0.649, importance=0.52
2025-11-17 22:03:50,069 - INFO - Summary: R²=0.155±0.166, importance=0.51, composite=0.483
2025-11-17 22:03:50,087 - INFO -
============================================================
2025-11-17 22:03:50,087 - INFO - Evaluating: vallemdd_30m_0.005 (y_will_valley_mdd_30m_0.005)
2025-11-17 22:03:50,087 - INFO - ============================================================
2025-11-17 22:03:50,087 - INFO - AAPL...
2025-11-17 22:03:50,380 - INFO - Using GPU (CUDA) for LightGBM
2025-11-17 22:33:39,647 - INFO - Scores: lightgbm=0.166, random_forest=0.128, neural_network=0.072, xgboost=0.158, catboost=0.170, lasso=0.266, mutual_information=0.115, univariate_selection=0.195, rfe=0.126, boruta=0.138, stability_selection=0.654, importance=0.52
2025-11-17 22:33:39,647 - INFO - MSFT...
2025-11-17 22:33:39,974 - INFO - Using GPU (CUDA) for LightGBM
2025-11-17 23:04:06,932 - INFO - Scores: lightgbm=0.205, random_forest=0.152, neural_network=0.097, xgboost=0.160, catboost=0.203, lasso=0.289, mutual_information=0.108, univariate_selection=0.200, rfe=0.154, boruta=0.144, stability_selection=0.666, importance=0.52
2025-11-17 23:04:06,932 - INFO - GOOGL...
2025-11-17 23:04:07,240 - INFO - Using GPU (CUDA) for LightGBM
2025-11-17 23:34:41,995 - INFO - Scores: lightgbm=0.109, random_forest=0.075, neural_network=0.006, xgboost=0.084, catboost=0.101, lasso=0.256, mutual_information=0.110, univariate_selection=0.190, rfe=0.062, boruta=0.085, stability_selection=0.630, importance=0.51
2025-11-17 23:34:41,996 - INFO - TSLA...
2025-11-17 23:34:42,315 - INFO - Using GPU (CUDA) for LightGBM
2025-11-18 00:03:10,057 - INFO - Scores: lightgbm=-0.012, random_forest=-0.078, neural_network=-0.123, xgboost=-0.067, catboost=-0.033, lasso=0.245, mutual_information=0.142, univariate_selection=0.219, rfe=-0.078, boruta=-0.073, stability_selection=0.591, importance=0.44
2025-11-18 00:03:10,057 - INFO - JPM...
2025-11-18 00:03:10,364 - INFO - Using GPU (CUDA) for LightGBM
2025-11-18 00:32:50,028 - INFO - Scores: lightgbm=0.126, random_forest=0.130, neural_network=0.034, xgboost=0.144, catboost=0.152, lasso=0.264, mutual_information=0.120, univariate_selection=0.208, rfe=0.125, boruta=0.122, stability_selection=0.663, importance=0.52
2025-11-18 00:32:50,028 - INFO - Summary: R²=0.165±0.163, importance=0.50, composite=0.488
2025-11-18 00:32:50,047 - INFO -
============================================================
2025-11-18 00:32:50,047 - INFO - Evaluating: peak_mfe_60m_0.001 (y_will_peak_mfe_60m_0.001)
2025-11-18 00:32:50,047 - INFO - ============================================================
2025-11-18 00:32:50,047 - INFO - AAPL...
2025-11-18 00:32:50,342 - INFO - Using GPU (CUDA) for LightGBM
2025-11-18 00:57:59,360 - INFO - Scores: lightgbm=-0.143, random_forest=-0.154, neural_network=-0.161, xgboost=-0.171, catboost=-0.140, lasso=0.087, mutual_information=0.136, univariate_selection=0.284, rfe=-0.156, boruta=-0.155, stability_selection=0.862, importance=0.54
2025-11-18 00:57:59,360 - INFO - MSFT...
2025-11-18 00:57:59,680 - INFO - Using GPU (CUDA) for LightGBM
2025-11-18 01:23:40,874 - INFO - Scores: lightgbm=-0.136, random_forest=-0.163, neural_network=-0.175, xgboost=-0.183, catboost=-0.150, lasso=0.093, mutual_information=0.137, univariate_selection=0.280, rfe=-0.160, boruta=-0.160, stability_selection=0.861, importance=0.53
2025-11-18 01:23:40,875 - INFO - GOOGL...
2025-11-18 01:23:41,186 - INFO - Using GPU (CUDA) for LightGBM
2025-11-18 01:49:11,507 - INFO - Scores: lightgbm=-0.147, random_forest=-0.162, neural_network=-0.185, xgboost=-0.180, catboost=-0.155, lasso=0.086, mutual_information=0.135, univariate_selection=0.267, rfe=-0.159, boruta=-0.166, stability_selection=0.856, importance=0.53
2025-11-18 01:49:11,507 - INFO - TSLA...
2025-11-18 01:49:11,823 - INFO - Using GPU (CUDA) for LightGBM
2025-11-18 02:14:54,788 - INFO - Scores: lightgbm=-0.116, random_forest=-0.129, neural_network=-0.139, xgboost=-0.140, catboost=-0.113, lasso=0.074, mutual_information=0.151, univariate_selection=0.287, rfe=-0.130, boruta=-0.134, stability_selection=0.884, importance=0.54
2025-11-18 02:14:54,788 - INFO - JPM...
2025-11-18 02:14:55,097 - INFO - Using GPU (CUDA) for LightGBM
2025-11-18 02:39:02,583 - INFO - Scores: lightgbm=-0.138, random_forest=-0.158, neural_network=-0.166, xgboost=-0.183, catboost=-0.133, lasso=0.106, mutual_information=0.140, univariate_selection=0.277, rfe=-0.161, boruta=-0.160, stability_selection=0.854, importance=0.55
2025-11-18 02:39:02,584 - INFO - Summary: R²=0.027±0.303, importance=0.54, composite=0.378
2025-11-18 02:39:02,602 - INFO -
============================================================
2025-11-18 02:39:02,603 - INFO - Evaluating: vallemdd_60m_0.001 (y_will_valley_mdd_60m_0.001)
2025-11-18 02:39:02,603 - INFO - ============================================================
2025-11-18 02:39:02,603 - INFO - AAPL...
2025-11-18 02:39:02,902 - INFO - Using GPU (CUDA) for LightGBM
2025-11-18 03:04:18,278 - INFO - Scores: lightgbm=-0.154, random_forest=-0.189, neural_network=-0.183, xgboost=-0.190, catboost=-0.157, lasso=0.088, mutual_information=0.137, univariate_selection=0.260, rfe=-0.187, boruta=-0.187, stability_selection=0.826, importance=0.54
2025-11-18 03:04:18,278 - INFO - MSFT...
2025-11-18 03:04:18,589 - INFO - Using GPU (CUDA) for LightGBM
2025-11-18 03:30:04,677 - INFO - Scores: lightgbm=-0.159, random_forest=-0.192, neural_network=-0.225, xgboost=-0.197, catboost=-0.167, lasso=0.109, mutual_information=0.126, univariate_selection=0.268, rfe=-0.188, boruta=-0.189, stability_selection=0.825, importance=0.53
2025-11-18 03:30:04,677 - INFO - GOOGL...
2025-11-18 03:30:05,002 - INFO - Using GPU (CUDA) for LightGBM
2025-11-18 03:55:26,976 - INFO - Scores: lightgbm=-0.146, random_forest=-0.177, neural_network=-0.241, xgboost=-0.185, catboost=-0.157, lasso=0.098, mutual_information=0.135, univariate_selection=0.262, rfe=-0.184, boruta=-0.183, stability_selection=0.837, importance=0.53
2025-11-18 03:55:26,976 - INFO - TSLA...
2025-11-18 03:55:27,305 - INFO - Using GPU (CUDA) for LightGBM
2025-11-18 04:21:08,919 - INFO - Scores: lightgbm=-0.146, random_forest=-0.141, neural_network=-0.186, xgboost=-0.157, catboost=-0.133, lasso=0.060, mutual_information=0.144, univariate_selection=0.270, rfe=-0.142, boruta=-0.143, stability_selection=0.875, importance=0.52
2025-11-18 04:21:08,919 - INFO - JPM...
2025-11-18 04:21:09,230 - INFO - Using GPU (CUDA) for LightGBM
2025-11-18 04:45:40,243 - INFO - Scores: lightgbm=-0.181, random_forest=-0.186, neural_network=-0.270, xgboost=-0.211, catboost=-0.177, lasso=0.101, mutual_information=0.137, univariate_selection=0.279, rfe=-0.186, boruta=-0.178, stability_selection=0.832, importance=0.54
2025-11-18 04:45:40,244 - INFO - Summary: R²=0.007±0.306, importance=0.53, composite=0.362
2025-11-18 04:45:40,263 - INFO -
============================================================
2025-11-18 04:45:40,263 - INFO - Evaluating: peak_mfe_60m_0.002 (y_will_peak_mfe_60m_0.002)
2025-11-18 04:45:40,264 - INFO - ============================================================
2025-11-18 04:45:40,264 - INFO - AAPL...
2025-11-18 04:45:40,573 - INFO - Using GPU (CUDA) for LightGBM
2025-11-18 05:11:25,978 - INFO - Scores: lightgbm=-0.146, random_forest=-0.189, neural_network=-0.217, xgboost=-0.159, catboost=-0.150, lasso=0.146, mutual_information=0.143, univariate_selection=0.274, rfe=-0.200, boruta=-0.197, stability_selection=0.785, importance=0.45
2025-11-18 05:11:25,978 - INFO - MSFT...
2025-11-18 05:11:26,294 - INFO - Using GPU (CUDA) for LightGBM
2025-11-18 05:38:10,248 - INFO - Scores: lightgbm=-0.163, random_forest=-0.188, neural_network=-0.260, xgboost=-0.197, catboost=-0.151, lasso=0.161, mutual_information=0.143, univariate_selection=0.274, rfe=-0.188, boruta=-0.195, stability_selection=0.776, importance=0.54
2025-11-18 05:38:10,248 - INFO - GOOGL...
2025-11-18 05:38:10,560 - INFO - Using GPU (CUDA) for LightGBM
2025-11-18 06:04:48,254 - INFO - Scores: lightgbm=-0.160, random_forest=-0.211, neural_network=-0.214, xgboost=-0.185, catboost=-0.162, lasso=0.141, mutual_information=0.134, univariate_selection=0.247, rfe=-0.211, boruta=-0.226, stability_selection=0.777, importance=0.53
2025-11-18 06:04:48,254 - INFO - TSLA...
2025-11-18 06:04:48,579 - INFO - Using GPU (CUDA) for LightGBM
2025-11-18 06:30:58,976 - INFO - Scores: lightgbm=-0.129, random_forest=-0.157, neural_network=-0.165, xgboost=-0.151, catboost=-0.125, lasso=0.115, mutual_information=0.144, univariate_selection=0.283, rfe=-0.160, boruta=-0.165, stability_selection=0.844, importance=0.45
2025-11-18 06:30:58,976 - INFO - JPM...
2025-11-18 06:30:59,286 - INFO - Using GPU (CUDA) for LightGBM
2025-11-18 06:56:18,846 - INFO - Scores: lightgbm=-0.104, random_forest=-0.159, neural_network=-0.145, xgboost=-0.135, catboost=-0.103, lasso=0.165, mutual_information=0.145, univariate_selection=0.283, rfe=-0.163, boruta=-0.148, stability_selection=0.774, importance=0.55
2025-11-18 06:56:18,846 - INFO - Summary: R²=0.014±0.293, importance=0.50, composite=0.361
2025-11-18 06:56:18,864 - INFO -
============================================================
2025-11-18 06:56:18,865 - INFO - Evaluating: vallemdd_60m_0.002 (y_will_valley_mdd_60m_0.002)
2025-11-18 06:56:18,865 - INFO - ============================================================
2025-11-18 06:56:18,865 - INFO - AAPL...
2025-11-18 06:56:19,166 - INFO - Using GPU (CUDA) for LightGBM
2025-11-18 07:23:13,356 - INFO - Scores: lightgbm=-0.150, random_forest=-0.190, neural_network=-0.289, xgboost=-0.164, catboost=-0.177, lasso=0.156, mutual_information=0.132, univariate_selection=0.241, rfe=-0.206, boruta=-0.212, stability_selection=0.730, importance=0.45
2025-11-18 07:23:13,356 - INFO - MSFT...
2025-11-18 07:23:13,676 - INFO - Using GPU (CUDA) for LightGBM
2025-11-18 07:51:01,265 - INFO - Scores: lightgbm=-0.178, random_forest=-0.221, neural_network=-0.216, xgboost=-0.220, catboost=-0.163, lasso=0.171, mutual_information=0.127, univariate_selection=0.253, rfe=-0.207, boruta=-0.208, stability_selection=0.730, importance=0.54
2025-11-18 07:51:01,265 - INFO - GOOGL...
2025-11-18 07:51:01,575 - INFO - Using GPU (CUDA) for LightGBM
2025-11-18 08:17:37,576 - INFO - Scores: lightgbm=-0.133, random_forest=-0.184, neural_network=-0.261, xgboost=-0.196, catboost=-0.157, lasso=0.163, mutual_information=0.137, univariate_selection=0.240, rfe=-0.193, boruta=-0.195, stability_selection=0.750, importance=0.54
2025-11-18 08:17:37,577 - INFO - TSLA...
2025-11-18 08:17:37,899 - INFO - Using GPU (CUDA) for LightGBM
2025-11-18 08:44:12,627 - INFO - Scores: lightgbm=-0.169, random_forest=-0.201, neural_network=-0.244, xgboost=-0.185, catboost=-0.174, lasso=0.099, mutual_information=0.146, univariate_selection=0.258, rfe=-0.199, boruta=-0.197, stability_selection=0.832, importance=0.45
2025-11-18 08:44:12,627 - INFO - JPM...
2025-11-18 08:44:12,933 - INFO - Using GPU (CUDA) for LightGBM
2025-11-18 09:10:58,169 - INFO - Scores: lightgbm=-0.160, random_forest=-0.193, neural_network=-0.216, xgboost=-0.190, catboost=-0.157, lasso=0.168, mutual_information=0.139, univariate_selection=0.273, rfe=-0.208, boruta=-0.215, stability_selection=0.740, importance=0.55
2025-11-18 09:10:58,171 - INFO - Summary: R²=-0.006±0.294, importance=0.50, composite=0.350
2025-11-18 09:10:58,191 - INFO -
============================================================
2025-11-18 09:10:58,191 - INFO - Evaluating: peak_mfe_60m_0.005 (y_will_peak_mfe_60m_0.005)
2025-11-18 09:10:58,191 - INFO - ============================================================
2025-11-18 09:10:58,191 - INFO - AAPL...
2025-11-18 09:10:58,488 - INFO - Using GPU (CUDA) for LightGBM
2025-11-18 09:39:33,587 - INFO - Scores: lightgbm=-0.110, random_forest=-0.164, neural_network=-0.205, xgboost=-0.136, catboost=-0.113, lasso=0.207, mutual_information=0.140, univariate_selection=0.226, rfe=-0.164, boruta=-0.156, stability_selection=0.591, importance=0.44
2025-11-18 09:39:33,587 - INFO - MSFT...
2025-11-18 09:39:33,903 - INFO - Using GPU (CUDA) for LightGBM
2025-11-18 10:09:03,826 - INFO - Scores: lightgbm=-0.108, random_forest=-0.144, neural_network=-0.207, xgboost=-0.150, catboost=-0.143, lasso=0.214, mutual_information=0.140, univariate_selection=0.237, rfe=-0.150, boruta=-0.155, stability_selection=0.590, importance=0.52
2025-11-18 10:09:03,826 - INFO - GOOGL...
2025-11-18 10:09:04,139 - INFO - Using GPU (CUDA) for LightGBM
2025-11-18 10:38:06,373 - INFO - Scores: lightgbm=-0.115, random_forest=-0.155, neural_network=-0.187, xgboost=-0.148, catboost=-0.125, lasso=0.205, mutual_information=0.135, univariate_selection=0.231, rfe=-0.160, boruta=-0.171, stability_selection=0.591, importance=0.52
2025-11-18 10:38:06,373 - INFO - TSLA...
2025-11-18 10:38:06,703 - INFO - Using GPU (CUDA) for LightGBM
2025-11-18 11:05:35,609 - INFO - Scores: lightgbm=-0.099, random_forest=-0.167, neural_network=-0.234, xgboost=-0.133, catboost=-0.119, lasso=0.193, mutual_information=0.154, univariate_selection=0.271, rfe=-0.160, boruta=-0.181, stability_selection=0.726, importance=0.45
2025-11-18 11:05:35,609 - INFO - JPM...
2025-11-18 11:05:35,927 - INFO - Using GPU (CUDA) for LightGBM
2025-11-18 11:33:35,691 - INFO - Scores: lightgbm=-0.113, random_forest=-0.159, neural_network=-0.201, xgboost=-0.137, catboost=-0.117, lasso=0.214, mutual_information=0.143, univariate_selection=0.261, rfe=-0.158, boruta=-0.156, stability_selection=0.581, importance=0.53
2025-11-18 11:33:35,691 - INFO - Summary: R²=0.014±0.246, importance=0.49, composite=0.365
2025-11-18 11:33:35,710 - INFO -
============================================================
2025-11-18 11:33:35,710 - INFO - Evaluating: vallemdd_60m_0.005 (y_will_valley_mdd_60m_0.005)
2025-11-18 11:33:35,710 - INFO - ============================================================
2025-11-18 11:33:35,710 - INFO - AAPL...
2025-11-18 11:33:36,020 - INFO - Using GPU (CUDA) for LightGBM
2025-11-18 12:03:26,153 - INFO - Scores: lightgbm=-0.047, random_forest=-0.092, neural_network=-0.143, xgboost=-0.088, catboost=-0.067, lasso=0.218, mutual_information=0.127, univariate_selection=0.199, rfe=-0.068, boruta=-0.072, stability_selection=0.575, importance=0.51
2025-11-18 12:03:26,154 - INFO - MSFT...
2025-11-18 12:03:26,477 - INFO - Using GPU (CUDA) for LightGBM
2025-11-18 12:33:51,917 - INFO - Scores: lightgbm=-0.057, random_forest=-0.101, neural_network=-0.128, xgboost=-0.095, catboost=-0.077, lasso=0.231, mutual_information=0.125, univariate_selection=0.210, rfe=-0.089, boruta=-0.094, stability_selection=0.576, importance=0.51
2025-11-18 12:33:51,917 - INFO - GOOGL...
2025-11-18 12:33:52,227 - INFO - Using GPU (CUDA) for LightGBM

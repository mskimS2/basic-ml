import argparse


def catboost_args() -> argparse.Namespace:
    p = argparse.ArgumentParser(description="Catboost")
    
    p.add_argument("--model_name", type=str, default="catboost")
    p.add_argument("--num_folds", type=int, default=5)
    p.add_argument("--random_seed", type=int, default=42)
    p.add_argument("--use_predict_proba", type=bool, default=True)
    p.add_argument("--shuffle", type=bool, default=True)
    p.add_argument("--verbose", type=bool, default=False)
    p.add_argument("--problem_type", type=str, default="binary_classification")
    p.add_argument("--train_data", type=str, default="dataset/binary_classification.csv")
    p.add_argument("--device", type=str, default="cpu", choices=["cpu", "gpu"])
    p.add_argument("--only_one_train", type=bool, default=True)
    p.add_argument("--output_path", type=str, default="results")
    
    # parameters 
    # - https://catboost.ai/en/docs/references/training-parameters/
    p.add_argument("--iterations", type=float, default=1000, help="[1, inf]")
    p.add_argument("--learning_rate", type=float, default=0., help="learning_rate, (0, inf]")
    p.add_argument("--early_stopping_rounds", type=int, default=50)
    p.add_argument("--l2_leaf_reg", type=float, default=3.)
    p.add_argument("--bootstrap_type", type=str, default="Bayesian", choices=["Bayesian", "Bernoulli", "MVS", "Poisson", "No"])
    p.add_argument("--bagging_temperature", type=float, default=1.)
    p.add_argument("--subsample", type=int, default=1)
    p.add_argument("--sampling_frequency", type=str, default="PerTreeLevel", choices=["PerTreeLevel", "PerTree"])
    p.add_argument("--sampling_unit", type=str, default="Object", choices=["Object", "Group"])
    p.add_argument("--mvs_reg", type=float, default=0.)
    p.add_argument("--random_strength", type=float, default=1.)
    p.add_argument("--use_best_model", type=bool, default=False, choices=[True, False])
    p.add_argument("--best_model_min_trees", type=bool, default=None)
    p.add_argument("--depth", type=int, default=6)
    p.add_argument("--grow_policy", type=str, default="SymmetricTree", choices=["SymmetricTree", "Depthwise", "Lossguide"])
    p.add_argument("--min_data_in_leaf", type=int, default=1)
    p.add_argument("--max_leaves", type=int, default=31)
    p.add_argument("--ignore_features", type=list, default=[])
    p.add_argument("--scale_pos_weight", type=float, default=1.)
    p.add_argument("--one_hot_max_size", type=int, default=None)
    p.add_argument("--has_time", type=bool, default=False, choices=[True, False])
    p.add_argument("--rsm", type=float, default=None)
    p.add_argument("--nan_mode", type=str, default="Min", choices=["Forbidden", "Min", "Max"])
    p.add_argument("--input_borders", type=str, default=None)
    p.add_argument("--output_borders", type=str, default=None)
    p.add_argument("--fold_permutation_block", type=int, default=1)
    p.add_argument("--leaf_estimation_method", type=str, default="Newton", choices=["Newton", "Gradient", "Exact"])
    p.add_argument("--leaf_estimation_iterations", type=int, default=None)
    p.add_argument("--leaf_estimation_backtracking", type=str, default="AnyImprovement", choices=["No", "AnyImprovement", "Armijo"])
    p.add_argument("--fold_len_multiplier", type=float, default=2.)
    p.add_argument("--approx_on_full_history", type=bool, default=False, choices=[True, False])
    p.add_argument("--boosting_type", type=str, default="Ordered", choices=["Ordered", "Plain"])
    p.add_argument("--boost_from_average", type=bool, default=True, choices=[True, False])
    p.add_argument("--langevin", type=bool, default=False, choices=[True, False])
    p.add_argument("--diffusion_temperature", type=float, default=10000.)
    p.add_argument("--posterior_sampling", type=bool, default=False)
    p.add_argument("--allow_const_label", type=bool, default=False)
    p.add_argument("--class_weights", type=dict, default={})
    p.add_argument("--class_name", type=str, default=None)
    p.add_argument("--auto_class_weights", type=str, default=None)
    p.add_argument("--score_function", type=str, default="Cosine", choices=["Cosine", "L2", "NewtonL2"])
    
    args, _ = p.parse_known_args(args=[])
    return args
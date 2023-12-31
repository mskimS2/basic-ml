import argparse


def svc_classifier_config() -> argparse.Namespace:
    p = argparse.ArgumentParser(description="SVC")
    
    p.add_argument("--model_name", type=str, default="SVC")
    p.add_argument("--task", type=str, default="classification")
    p.add_argument("--num_folds", type=int, default=5)
    p.add_argument("--random_seed", type=int, default=42)
    p.add_argument("--use_predict_proba", type=bool, default=True, choices=[True, False])
    p.add_argument("--shuffle", type=bool, default=True)
    p.add_argument("--problem_type", type=str, default="binary_classification")
    p.add_argument("--train_data", type=str, default="dataset/binary_classification.csv")
    p.add_argument("--device", type=str, default="cpu", choices=["cpu", "gpu"])
    p.add_argument("--only_one_train", type=bool, default=True)
    p.add_argument("--output_path", type=str, default="results")
    
    # parameters 
    # - https://scikit-learn.org/stable/modules/generated/sklearn.svm.SVC.html
    p.add_argument("--C", type=float, default=1.)
    p.add_argument("--kernel", type=str, default="linear", choices=["linear", "poly", "rbf", "sigmoid", "precomputed"])
    p.add_argument("--degree", type=int, default=3)
    p.add_argument("--gamma", type=str, default="scale", choices=["scale", "auto"])
    p.add_argument("--coef0", type=float, default=0.)
    p.add_argument("--shrinking", type=bool, default=False)
    p.add_argument("--probability", type=bool, default=True)
    p.add_argument("--tol", type=float, default=1e-3)
    p.add_argument("--cache_size", type=float, default=200)
    p.add_argument("--class_weight", type=str, default=None, choices=["balanced", "None"])
    p.add_argument("--verbose", type=bool, default=False, choices=[True, False])
    p.add_argument("--max_iter", type=int, default=-1)
    p.add_argument("--decision_function_shape", type=str, default="ovr", choices=["ovo", "ovr"])
    p.add_argument("--break_ties", type=bool, default=False, choices=[True, False])
    p.add_argument("--random_state", type=int, default=42)
    
    args, _ = p.parse_known_args(args=[])
    return args

def svr_regressor_config() -> argparse.Namespace:
    p = argparse.ArgumentParser(description="SVR")
    
    p.add_argument("--model_name", type=str, default="SVR")
    p.add_argument("--task", type=str, default="regression")
    p.add_argument("--num_folds", type=int, default=5)
    p.add_argument("--random_seed", type=int, default=42)
    p.add_argument("--shuffle", type=bool, default=True)
    p.add_argument("--problem_type", type=str, default="binary_classification")
    p.add_argument("--train_data", type=str, default="dataset/binary_classification.csv")
    p.add_argument("--device", type=str, default="cpu", choices=["cpu", "gpu"])
    p.add_argument("--only_one_train", type=bool, default=True)
    p.add_argument("--output_path", type=str, default="results")
    
    # parameters 
    # - https://scikit-learn.org/stable/modules/generated/sklearn.svm.SVR.html
    p.add_argument("--C", type=float, default=1.)
    p.add_argument("--kernel", type=str, default="linear", choices=["linear", "poly", "rbf", "sigmoid", "precomputed"])
    p.add_argument("--degree", type=int, default=3)
    p.add_argument("--gamma", type=str, default="scale", choices=["scale", "auto"])
    p.add_argument("--coef0", type=float, default=0.)
    p.add_argument("--shrinking", type=bool, default=False)
    p.add_argument("--tol", type=float, default=1e-3)
    p.add_argument("--cache_size", type=float, default=200)
    p.add_argument("--epsilon", type=float, default=0.1)
    p.add_argument("--verbose", type=bool, default=False, choices=[True, False])
    p.add_argument("--max_iter", type=int, default=-1)
    
    args, _ = p.parse_known_args(args=[])
    return args
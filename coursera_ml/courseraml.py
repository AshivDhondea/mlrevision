import coursera_ml.linear_regression as cml


def pull_up_project(project_choice: str):
    if project_choice == 'linear-regression':
        cml.run_linear_regression_project()

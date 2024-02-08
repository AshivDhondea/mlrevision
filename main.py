import coursera_ml.courseraml as coursera
import kaggle_ml.kaggleml as kaggle
import argparse

PROJECTS_DICTIONARY = {
    'coursera-ml': ['linear-regression', 'logistic-regression'],
    'kaggle': ['house-price', ],
    'islp': ['linear-regression', ]
}


def pull_up_topic(selected_source: str, selected_project: str):
    if selected_source == 'coursera-ml':
        coursera.pull_up_project(selected_project)

    if selected_project == 'kaggle':
        kaggle.pull_up_project(selected_project)


def parse_arguments():
    # Argument parsing
    parser = argparse.ArgumentParser()
    parser.add_argument("-s", "--source", help="learning source", type=str,
                        choices=PROJECTS_DICTIONARY.keys(), required=True)
    parser.add_argument("-p", "--project", help="project to run", type=str, required=True)

    args = parser.parse_args()
    learning_source = args.source
    project = args.project

    if learning_source in ['kaggle', 'islp']:
        to_study_error = f"We have not yet studied {learning_source}"
        raise NotImplementedError(to_study_error)

    if project not in PROJECTS_DICTIONARY[learning_source]:
        project_not_found_error = f"Project {project} not found in {learning_source}"
        raise RuntimeError(project_not_found_error)

    pull_up_topic(learning_source, project)


if __name__ == '__main__':
    parse_arguments()

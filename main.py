import argparse
import json
from model_lineage_toolkit.src.model import Model
from model_lineage_toolkit.src.repository import Repository
from model_lineage_toolkit.src.lineage import Lineage

def main():
    parser = argparse.ArgumentParser(description='Model Lineage Toolkit')
    parser.add_argument('--model-path', type=str, help='Path to the model file')
    parser.add_argument('--repository-path', type=str, help='Path to the model repository')
    args = parser.parse_args()

    model = Model(args.model_path)
    repository = Repository(args.repository_path)
    lineage = Lineage(model, repository)

    print(json.dumps(lineage.trace(), indent=4))

if __name__ == '__main__':
    main()
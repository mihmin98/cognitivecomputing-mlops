import sys

if __name__ == "__main__":
    if len(sys.argv) < 4:
        print("bad number of args")
        exit(1)

    new_model_path = sys.argv[1]
    baseline_model_path = sys.argv[2]
    destination_file = sys.argv[3]

    new_model_results = {}
    with open(new_model_path, "r") as f:
        line = f.readline()
        split_line = line.split(",")
        new_model_results = {
            "accuracy": float(split_line[0]),
            "precision": float(split_line[1]),
            "recall": float(split_line[2]),
            "f1": float(split_line[3]),
        }

    baseline_model_results = {}

    with open(baseline_model_path, "r") as f:
        line = f.readline()
        split_line = line.split(",")
        baseline_model_results = {
            "accuracy": float(split_line[0]),
            "precision": float(split_line[1]),
            "recall": float(split_line[2]),
            "f1": float(split_line[3]),
        }

    delta_results = {
        "accuracy": new_model_results["accuracy"] - baseline_model_results["accuracy"],
        "precision": new_model_results["precision"] - baseline_model_results["precision"],
        "recall": new_model_results["recall"] - baseline_model_results["recall"],
        "f1": new_model_results["f1"] - baseline_model_results["f1"],
    }

    # markdown = "### Run results\n\
    #             | Model | Accuracy | Precision | Recall | F1-Score |\n\
    #             |-------|----------|-----------|--------|----------|\n\
    #             | New | " + str(new_model_results["accuracy"]) + " | " + str(new_model_results["precision"]) + " | " + str(new_model_results["recall"]) + " | " + str(new_model_results["f1"]) + " |\n\
    #             | Baseline | " + str(baseline_model_results["accuracy"]) + " | " + str(baseline_model_results["precision"]) + " | " + str(baseline_model_results["recall"]) + " | " + str(baseline_model_results["f1"]) + " |"
    markdown = "### Run results\n\n"
    markdown += '| Category | Accuracy | Precision | Recall | F1-Score |\n'
    markdown += '|----------|----------|-----------|--------|----------|\n'
    markdown += "| New | " + str(new_model_results["accuracy"]) + " | " + str(new_model_results["precision"]) + " | " + str(new_model_results["recall"]) + " | " + str(new_model_results["f1"]) + " |\n"
    markdown += "| Baseline | " + str(baseline_model_results["accuracy"]) + " | " + str(baseline_model_results["precision"]) + " | " + str(baseline_model_results["recall"]) + " | " + str(baseline_model_results["f1"]) + " |\n"
    markdown += "| Change | " + str(delta_results["accuracy"]) + " | " + str(delta_results["precision"]) + " | " + str(delta_results["recall"]) + " | " + str(delta_results["f1"]) + " |\n"

    with open(destination_file, 'w') as f:
        f.write(markdown)

unprinted_designs = ["phone case", "robot pendant", "dodecahedron"]
completed_models = []

def move_from_unprinted_to_completed(unprinted_designs, completed_models):
    while unprinted_designs:
        model = unprinted_designs.pop()
        print(f"Printing model: {model}")
        completed_models.append(model)

    print("\nCompleted models:")
    for model in completed_models:
        print(model)

move_from_unprinted_to_completed(unprinted_designs, completed_models)
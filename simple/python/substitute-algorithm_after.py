def foundPerson(people):
    candidates = ["Don", "John", "Kent"]
    return next(
        (people[i] for i in range(len(people)) if people[i] in candidates), ""
    )
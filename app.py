MAXES = {
    "bench" : 285,
    "squat" : 365,
    "deadlift" : 425
}

PROGRAM = {
    "10s" : {
        "accumulation" : [
            {"pct": 0.60, "reps": 5, "sets": 10}
        ], 
        "intensificaiton" : [
            {"pct": 0.55, "reps": 5, "sets": 1},
            {"pct": 0.625, "reps": 5, "sets": 1},
            {"pct": 0.675, "reps": 3, "sets": 10},
        ], 
        "realization" : [
            {"pct": 0.50, "reps": 5, "sets": 1},
            {"pct": 0.60, "reps": 3, "sets": 1},
            {"pct": 0.70, "reps": 1, "sets": 1},
            {"pct": 0.75, "reps": "AMRAP", "sets": 1},
        ]
        }, 
    "8s" : {
        "accumulation" : [
            {"pct": 0.65, "reps": 5, "sets": 8}
        ], 
        "intensificaiton" : [
            {"pct": 0.60, "reps": 3, "sets": 1},
            {"pct": 0.675, "reps": 3, "sets": 1},
            {"pct": 0.725, "reps": 3, "sets": 8},
        ], 
        "realizaiton" : [
            {"pct": 0.50, "reps": 5, "sets": 1},
            {"pct": 0.60, "reps": 3, "sets": 1},
            {"pct": 0.70, "reps": 2, "sets": 1},
            {"pct": 0.75, "reps": 1, "sets": 1},
            {"pct": 0.80, "reps": "AMRAP", "sets": 1},
        ]
        }, 
    "5s" : {
        "accumulation" : [
            {"pct": 0.70, "reps": 6, "sets": 5}
        ], 
        "intensificaiton" : [
            {"pct": 0.65, "reps": 2, "sets": 1},
            {"pct": 0.725, "reps": 2, "sets": 1},
            {"pct": 0.775, "reps": 4, "sets": 5},
        ], 
        "realizaiton" : [
            {"pct": 0.50, "reps": 5, "sets": 1},
            {"pct": 0.60, "reps": 3, "sets": 1},
            {"pct": 0.70, "reps": 2, "sets": 1},
            {"pct": 0.75, "reps": 1, "sets": 1},
            {"pct": 0.80, "reps": 1, "sets": 1},
            {"pct": 0.85, "reps": "AMRAP", "sets": 1},
        ]
        }, 
    "3s" : {
        "accumulation" : [
            {"pct": 0.75, "reps": 7, "sets": 3}
        ], 
        "intensificaiton" : [
            {"pct": 0.70, "reps": 1, "sets": 1},
            {"pct": 0.775, "reps": 1, "sets": 1},
            {"pct": 0.82, "reps": 5, "sets": 3},
        ], 
        "realization" : [
            {"pct": 0.50, "reps": 5, "sets": 1},
            {"pct": 0.60, "reps": 3, "sets": 1},
            {"pct": 0.70, "reps": 2, "sets": 1},
            {"pct": 0.75, "reps": 1, "sets": 1},
            {"pct": 0.80, "reps": 1, "sets": 1},
            {"pct": 0.85, "reps": 1, "sets": 1},
            {"pct": 0.90, "reps": "AMRAP", "sets": 1},
        ]
        },
}

def generate_phase(working_max, wave, phase):
    prescriptions = PROGRAM[wave][phase]
    results = []

    for item in prescriptions:
        raw_weight = working_max * item["pct"]

        results.append({
            "%" : item["pct"],
            "weight" : raw_weight,
            "sets" : item["sets"],
            "reps" : item["reps"],
        })
    return results


session = generate_phase( MAXES["squat"], "10s", "realization")


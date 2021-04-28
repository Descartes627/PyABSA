We explain the format of our enriched test set below.

First, the original SemEval-14 may have the following entry (just for example), with a **positive** sentiment of the aspect term **Set up**:
```
"359:1_0": {
        "sentence": "Set up was easy.",
        "term": "Set up",
        "polarity": "positive",
        "id": "359:1_0",
        "from": 0,
        "to": 6
}.
```

Our ARTS test set will generate the following entry based on adversarial generation strategy 1 (namely RevTgt):
```
"359:1_0_adv1": {
        "sentence": "Set up was difficult.",
        "term": "Set up",
        "polarity": "negative",
        "id": "359:1_0",
        "from": 0,
        "to": 6
},
```
where the adversarial instance reverts the sentiment of `Set up` to negative polarity.

There are also entries generated by adversarial strategy 2 (namely RevNon) and 3 (namely AddDiff), such as 
```
"359:1_0_adv3": {
        "sentence": "Set up was easy, but USB ports is a mistake, i5 is not as fast and material is cheap.",
        "term": "Set up",
        "polarity": "positive",
        "id": "359:1_0",
        "from": 0,
        "to": 6
    }
```
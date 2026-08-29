# MP1 Writeup — Reflection

| Strategy    | Accuracy (mean) | Parse rate | Judge score | Total cost ($) | Latency p50 (s) |
|-------------|-----------------|------------|-------------|----------------|-----------------|
| cot         | 2.8             | 1.0        | 23.1        | 0.001          | 11.628          |
| few_shot    | 3.0             | 1.0        | 23.6        | 0.000          | 5.632           |
| structured  | 2.9             | 1.0        | 23.7        | 0.000          | 9.121           |
| zero_shot   | 2.6             | 1.0        | 23.3        | 0.000          | 3.897           |


### 1) Which strategy won, and on what dimension?
The few-shot strategy worked best because it gave the highest accuracy. All strategies had similar success in parsing the data, and the cost was about the same since the batch was small. The chain-of-thought (cot) method made accuracy a little better, but it also made the process slower

### 2) What surprised you?
I didn’t expect few-shot to beat structured so clearly. It turns out that giving the model a few concrete examples helped it handle different ways of writing better than just giving it a strict schema. Also, when the input didn’t include years, the zero-shot method often messed up the numbers.

### 3) For your capstone domain, which strategy would you reach for first?
I would start with few-shot. Just two short examples are enough to show the model the exact JSON format and some tricky cases. This gives a good balance: high accuracy, reasonable speed, and easy-to-maintain prompts.

### 4) If you had another day, what would you try next?
Increase snippet diversity and sample size, add fuzzy matching for company/role comparisons, and re-run the judge with a cheaper model or fewer items to explore cost-quality tradeoffs.
I will try adding more variety to the snippets and increasing the sample size.  I will re-run the evaluation using a cheaper model or fewer items to see how cost and quality trade off.




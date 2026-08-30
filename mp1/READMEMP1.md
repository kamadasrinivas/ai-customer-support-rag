# MP1 Prompt Lab Setup and Result Interpretation

This guide explains how to run the notebook `mp1/mp1_prompt_lab.ipynb` and how to interpret the results it produces.

## 1) Prerequisites

Before running the notebook, make sure you have:

- Python 3.10+
- A virtual environment activated
- An OpenAI API key available in the environment
- The project root available on your machine

The notebook expects a `.env` file in the project root with a key like:

```env
OPENAI_API_KEY=your_key_here
OPENAI_BASE_URL=https://api.openai.com/v1
```

The project also supports legacy names such as `OPEN_AI_TIMEOUT`, `OPEN_AI_RETRIES`, and `OPEN_AI_TEMPRATURE`, but the canonical names are `OPENAI_*`.

## 2) Install dependencies

From the project root:

```bash
python -m venv .venv
.venv\Scripts\activate
pip install -r requirements.txt
```

If you want to install only the notebook essentials, these are the most relevant packages:

```bash
pip install openai pandas pydantic-settings python-dotenv httpx
```

## 3) Open the notebook

Open the notebook file:

```text
mp1/mp1_prompt_lab.ipynb
```

Run the cells in order from top to bottom.

## 4) What the notebook does

The notebook compares four prompt strategies:

- zero_shot
- few_shot
- structured
- cot

For each strategy, it:

1. loads job snippets from the dataset
2. builds a prompt
3. calls the OpenAI model
4. parses the returned JSON
5. scores the prediction against the golden dataset
6. saves results to JSONL files
7. aggregates the results into a summary table

## 5) Important output files

After running the notebook, it creates files such as:

- `mp1/mp1_results_httpx.jsonl` — raw results per strategy per snippet
- `mp1/mp1_scored_httpx.jsonl` — scored results including accuracy and judge score

These files are useful for checking:

- whether the model response parsed successfully
- if the extracted fields matched the gold answer
- cost and latency per request
- overall strategy performance

## 6) How to interpret the results

The notebook builds a summary table using the scored data.

The key columns are:

- Accuracy (mean): average number of correct fields out of 3
- Parse rate: percentage of responses that were successfully parsed as JSON
- Judge score: LLM-based quality score from 1 to 25
- Total cost ($): total estimated cost across all requests
- Latency p50 (s): median latency time

Example summary format:

| Strategy | Accuracy (mean) | Parse rate | Judge score | Total cost ($) | Latency p50 (s) |
|---|---:|---:|---:|---:|---:|
| cot | 2.8 | 1.0 | 23.1 | 0.001 | 11.628 |
| few_shot | 3.0 | 1.0 | 23.6 | 0.000 | 5.632 |
| structured | 2.9 | 1.0 | 23.7 | 0.000 | 9.121 |
| zero_shot | 2.6 | 1.0 | 23.3 | 0.000 | 3.897 |

### Interpretation

- Higher `Accuracy (mean)` means the model extracted more correct fields.
- A `Parse rate` of 1.0 means every response was valid JSON and successfully parsed.
- Higher `Judge score` means the model output was judged as more faithful and helpful.
- Lower cost and lower latency are better for efficiency.

### Best strategy

A good overall strategy usually balances:

- correctness
- parse reliability
- judge quality
- cost
- speed

In many cases, a prompt with stronger structure or few-shot examples performs better than a bare zero-shot prompt.

## 7) Typical troubleshooting

### ValidationError on import

If you see an error like `ValidationError` from `settings.py`, check:

- the `.env` file exists in the project root
- the env variables are spelled correctly
- the key names match `OPENAI_API_KEY` and `OPENAI_BASE_URL`

### No API key found

Make sure the key is set in your environment before running the notebook:

```bash
set OPENAI_API_KEY=your_key_here
```

or in `.env`:

```env
OPENAI_API_KEY=your_key_here
```

### Notebook fails during model calls

Check:

- your internet connection
- whether the API key is valid
- whether the base URL is correct
- whether the rate limit or quota has been reached

## 8) Final deliverable

The notebook is meant to produce a comparison of prompting strategies and help you answer questions such as:

- Which prompt format is most accurate?
- Which prompt format is closest to the gold answer?
- Which prompt is cheapest and fastest?
- Which prompt is most reliable in real use?

## 9) Optional write-up

After running the notebook, open the write-up file and answer the required reflection questions for the assignment.

---

This notebook is intended as a practical comparison experiment, not just a code exercise. The real value is in understanding how prompt design affects structured extraction quality, reliability, and cost.

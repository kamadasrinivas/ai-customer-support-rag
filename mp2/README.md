# MP2 Mini-RAG

This project builds a retrieval-augmented question-answering pipeline over five
Sherlock Holmes stories. It loads text files from `mp2/corpus`, splits them into
chunks, embeds them with OpenAI, stores vectors in Qdrant, and answers questions
with source citations.

## Requirements

- Python 3.10 or newer
- An OpenAI API key with access to `text-embedding-3-small` and `gpt-4o-mini`
- A reachable Qdrant instance (local or hosted)

From the repository root, create and activate a virtual environment, then install
the project dependencies:

```powershell
py -m venv .venv
.\.venv\Scripts\Activate.ps1
python -m pip install -e .
```

On macOS or Linux, use:

```sh
python3 -m venv .venv
source .venv/bin/activate
python -m pip install -e .
```

Set the required credentials in the same terminal session used to run the
commands. Do not commit credentials to the repository.

PowerShell:

```powershell
$env:OPENAI_API_KEY = "your-openai-api-key"
$env:QDRANT_URL = "your-qdrant-url"
$env:QDRANT_API_KEY = "your-qdrant-api-key"
```

macOS or Linux:

```sh
export OPENAI_API_KEY="your-openai-api-key"
export QDRANT_URL="your-qdrant-url"
export QDRANT_API_KEY="your-qdrant-api-key"
```

`QDRANT_URL` is required. `QDRANT_API_KEY` can be omitted for a local Qdrant
instance that does not use authentication. The MP2 script reads environment
variables directly; it does not load `.env` by itself.

## Run

Run these commands from the repository root. Ingest the corpus once before
asking questions or validating:

```powershell
python mp2\mp2_rag.py ingest
python mp2\mp2_rag.py ask
python mp2\mp2_rag.py validate
```

The `ask` command starts an interactive question loop; submit an empty question
to exit. Validation runs the predefined questions and then the learner questions
when `mp2/data/learner_questions.jsonl` contains real questions.

**Ingest recreates the `mp2_sherlock` Qdrant collection.** Re-ingesting replaces
its existing points, so only run it when you intend to rebuild the index.

## Add Questions

Edit `mp2/data/learner_questions.jsonl`, keeping one JSON object per line. Each
object needs a unique `id`, a question, an `expected_source` matching a corpus
filename, an `expected_facts` list, and optional guidance. The current file has
an easy single-fact question, a medium question combining two details, and a hard
multi-hop question, each grounded in a different story. Replace or add questions
whose answers can be found in the corpus.

## Interpret Results

- A check mark means the expected source filename appears in the returned
	citations. The final source-match count measures citation/source retrieval,
	not complete answer correctness.
- `Facts matched: x/y` counts expected fact strings found as case-insensitive
	substrings in the generated answer. It is a lightweight check, not semantic
	grading: paraphrases can be missed, and a match does not prove the whole answer
	is faithful.
- Latency is the measured end-to-end time for retrieval, embedding, and answer
	generation, in milliseconds. It varies with network and API conditions.
- Review the answer and cited excerpts as well as the summary metrics, especially
	when expected facts do not match.

### Latest Recorded Run

The 2026-09-26 validation matched the expected source for all five questions
(2/2 predefined and 3/3 learner). Literal expected-fact matches were 10/19, with
mean latency of 3,271 ms. The easy Blue Carbuncle question matched 1/1 facts; the
medium Engineer's Thumb question matched 3/3; the hard, multi-hop Scandal in
Bohemia question matched 2/4. These are substring counts, not semantic grades;
the full output is in `mp2/mp2_validation.txt`.

To save or refresh the validation output on PowerShell:

```powershell
python mp2\mp2_rag.py validate 2>&1 | Tee-Object -FilePath mp2\mp2_validation.txt
```

The most recent recorded run and its interpretation are in
`mp2/mp2_validation.txt`.

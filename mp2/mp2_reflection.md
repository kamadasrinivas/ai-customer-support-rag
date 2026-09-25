# MP2 Reflection

## What worked

Paragraph-aware chunks capped at 500 characters, with 80 characters of overlap,
kept the story context small enough for focused retrieval while retaining
section metadata for citations. In the latest validation, all five questions
cited the expected story (2/2 predefined and 3/3 learner questions). The easy
Blue Carbuncle question matched its one expected fact, and the medium Engineer's
Thumb question matched all three.

## What didn't work

Correct source citations did not guarantee that answers included every expected
detail. The Red-Headed League answer matched only 1/5 expected fact phrases, and
the hard, multi-hop Scandal in Bohemia answer matched 2/4. The Speckled Band
answer matched 3/6 in the latest run. The validator uses case-insensitive
substring checks and does not save generated answer text, so I cannot tell from
these results alone whether a missed phrase was omitted or paraphrased; I also
cannot claim a hallucination or a retrieval failure based on these scores.

## What I'd change

With another five hours, I would add a per-question evaluation trace containing
the retrieved chunks, their section/source metadata, the generated answer, and
the expected-fact results. I would manually inspect the Red-Headed League and
Scandal in Bohemia cases first, then compare `k=3` with `k=5` on the same five
questions. That would help separate retrieval gaps from answer-generation or
substring-scoring issues.

## One surprise

The expected-source result stayed correct for the Speckled Band question, but
its literal fact score changed from 4/6 in a predefined-only run to 3/6 in the
latest full run. I did not expect that score to move while the citation remained
stable. It shows that this small evaluation is sensitive to answer wording (and
possibly generation variability), so a single literal-match score is a weak
stand-in for answer quality.

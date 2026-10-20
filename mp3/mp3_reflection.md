# MP3 Reflection

## Grounding & abstention

The assistant got all three unanswerable questions right. It abstained when
asked about Moriarty, the boiling point of water, and the Hound of the
Baskervilles. It did not try to answer using information from outside the
stories.

It also refused two questions that the stories do answer: one about Jabez
Wilson's assistant and one about Julia Stoner's death. The right story was
retrieved for both, but the assistant still abstained. The evaluation output
doesn't show the scores for those questions, Not sure whether the
threshold caused the refusals or whether the model chose to abstain after
seeing the retrieved passages.

The threshold was **0.28** which I modified from **0.30**, which is the default in the code;

## Citations

The answers counted as grounded cited the expected story, and the evaluation
didn't report any invalid citation numbers.

That check only catches citation numbers that don't match a provided source.
It doesn't check whether the cited passage actually supports the statement.
The evaluation also checks the story title, not whether every claim follows
from the cited passage.

## Reading eval table

The evaluation covered six answerable questions and three questions that
should be refused:

- **Retrieval hit rate: 1.0 (6/6).** The expected story was retrieved for every
  answerable question.
- **Grounded and cited rate: 0.67 (4/6).** Four answerable questions got an
  answer with a citation to the expected story.
- **Abstention accuracy: 1.0 (3/3).** All three unanswerable questions were
  refused.
- **Hallucination rate: 0.0 (0/3).** None of the unanswerable questions got an
  answer.

Grounded and cited rate was the weakest result. Retrieval found the right story
for every answerable question, but the assistant still refused two. I would
start by checking the scores and responses for those two questions. It would
also help to include that information in the evaluation output, so it's easier
to see why a question was refused.

## One surprise

I was surprised that retrieval hit rate was perfect while the grounded and
cited rate was only 0.67. Finding the right story didn't always mean the
assistant would answer. Both of my new answerable questions worked, including
the multi-part question about how Irene Adler hid the photograph and left with
her husband. That made the difference between retrieval quality and the
assistant's final response much clearer to me.

# eval table with questions added from learner_questions.jsonl
(.venv) PS C:\SRINI\IITM\CAPSTONEPROJECT\ai-customer-support-rag\mp3> python mp3_grounded_qa.py eval

  id                              type     hit   abstained  grounded  ok
  --------------------------------------------------------------------------
  q1_red_headed_league_assistant  answer   ✓     ✓          ✗         ✗
  q2_speckled_band_weapon         answer   ✓     ✓          ✗         ✗
  q3_scandal_bohemia_adler        answer   ✓     ✗          ✓         ✓
  q4_engineers_thumb_press        answer   ✓     ✗          ✓         ✓
  abstain_moriarty                abstain  None  ✓          None      ✓
  abstain_out_of_domain           abstain  None  ✓          None      ✓
  q5_blue_carbuncle_trail         answer   ✓     ✗          ✓         ✓
  q6_scandal_adler_escape         answer   ✓     ✗          ✓         ✓
  q7_abstain_baskerville          abstain  None  ✓          None      ✓
  --------------------------------------------------------------------------

  Retrieval hit rate    : 1.0   (6 answerable questions)
  Grounded & cited rate : 0.6666666666666666   (KPI: grounded response rate)
  Abstention accuracy   : 1.0   (3 should-abstain questions)
  Hallucination rate    : 0.0   (KPI: hallucination rate)

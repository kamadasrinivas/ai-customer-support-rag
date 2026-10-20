# MP3 Recorded Q&A Demo

This live command-line demo shows two answers grounded in the Sherlock corpus
and one question the assistant correctly abstains from answering.

## Command

```powershell
(.venv) PS C:\SRINI\IITM\CAPSTONEPROJECT\ai-customer-support-rag\mp3> python mp3_grounded_qa.py ask
```

## Captured output

```text
Grounded Q&A over the Sherlock corpus. Empty line to exit.

? In A Scandal in Bohemia, who is Irene Adler and what does the King of Bohemia want from her?

Irene Adler is a celebrated American opera contralto who had a brief romantic connection with the King of Bohemia when he was Crown Prince. The King wants a photograph that shows him and Irene Adler together, which she possesses. He is concerned that she will send this photograph to the bride's family as revenge for being cast aside, especially since it could jeopardize his upcoming marriage to Clotilde Lothman von Saxe-Meiningen [1][2].

  Sources:
    [1] A Scandal in Bohemia — The Photograph  (score 0.589)
    [2] A Scandal in Bohemia — The Photograph  (score 0.585)
  Latency: 6907ms

? What gemstone did Peterson find inside the goose?

Peterson found a brilliant blue gemstone, which Holmes recognized as the Blue Carbuncle of the Countess of Morcar [1].

  Sources:
    [1] The Adventure of the Blue Carbuncle — The Carbuncle  (score 0.711)
  Latency: 2240ms

? Who was Professor Moriarty, and how did he meet his end

I don't know based on the provided documents.

  (abstained — no supporting excerpt)
  Latency: 1015ms

?
```

## Demo narration

First, I asked about Irene Adler and the photograph the King wants back. The
assistant answers using two cited passages from *A Scandal in Bohemia*.

Next, I asked what gemstone Peterson's wife found in the goose. The assistant
identifies the Blue Carbuncle and cites *The Adventure of the Blue Carbuncle*.

Finally, I asked about Professor Moriarty, who is not covered by these stories.
The assistant responds, ‘I don't know based on the provided documents,’ rather
than guessing.”

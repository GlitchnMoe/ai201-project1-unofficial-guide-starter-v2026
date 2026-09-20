# The Unofficial Guide

<!-- Replace this line with your name and which corpus you picked. -->

> **This file is your submission.** Fill it in as you go — most sections get
> written during the milestone that produces them, not at the end.
>
> How the starter works, and every command you'll need, is in `RUNNING.md`.
> Leave that file alone.
>
> **Paste everything as text.** No screenshots, no video. A typed table gets
> full credit; a picture of the same table gets none.
>
> Delete these instruction blocks as you replace them. The `<!-- -->` comments
> are notes to you and don't show up when the page renders — you can leave them
> or remove them.

---

# Unit 1

## What This Does

<!-- Three or four sentences. Which corpus you picked, and the kinds of
     questions your system answers. Write it for someone who has never seen
     this repo.

     Milestone 5. -->

I chose to work with the campus life corpus. This corpus is comprised of 88 reviews of what this specific campus is like. My system can answer questions on details of that campus such as a few classes that were reviewed, housing costs, and daily life. The idea is that the information is grounded based on what is given to us so that the system is able to give more accurate answers more often than not. 

## Chunking Strategy

**Chunk size:**
0, the reviews were relatively short and if they were longer I would separate them into different chunks and keep the first line (which I called the "title") with the chunks in order to keep reference to some context.  

**Overlap:**

<!-- What about YOUR documents made you pick these numbers? Short posts and
     long sectioned guides don't want the same chunking, and "800 seemed
     reasonable" earns nothing. Point at something you noticed when you read
     the documents in Milestone 1.

     If you changed your mind partway through, say so and say why. That's worth
     more than pretending you got it right first time.

     Milestone 3. -->

## Sample Chunks

<!-- Five chunks, pasted as text. Label each one and name the file it came from
     AND the function that produced it — the grader checks your code against
     what you claim here.

     `python app.py chunks -n 5` prints all three for you. Copy them straight
     across.

     Milestone 3. -->

**Chunk 1** — source: `` — produced by: `chunker.py::split_documents`

```
On the add/drop deadline

You can add a course through the end of the second week. Dropping is a longer window — through the end of week six — but a drop after week two shows as a W on your transcript. Nothing anywhere on the registrar's site says this plainly, and students find out from each other.     
```

**Chunk 2** — source: `` — produced by: `chunker.py::split_documents`

```
Workload for BIOL 160 Cell Biology

People keep asking so: 9 to 11 hours a week, the heaviest first-year course by reputation. That's real time, not optimistic time.

It's front-loaded — the first month is heavier than the rest, partly because you're learning the format.
```

**Chunk 3** — source: `` — produced by: `chunker.py::split_documents`

```
PHYS 130 Mechanics

Just finished a year in this building. Format is lecture with a compulsory lab that meets fortnightly. Assessment: three midterms, no final, plus a lab practical. Not curved, but the lowest midterm is dropped.

Expect 7 hours a week, plus 3 on lab weeks.

The one piece of advice: the lab practical is worth 20% and almost nobody prepares for it.   
```

**Chunk 4** — source: `` — produced by: `chunker.py::split_documents`

```
Re: Verrill Street Grill

Adding to what people have said about Verrill Street Grill. The wait figure of up to 30 minutes on Friday evenings matches what I've seen. If you're trying to eat between classes, go before 11:45 and it's a different building entirely.

Also worth saying: one register, so the queue is a single line no matter how busy. Nobody tells you this at orientation.
```

**Chunk 5** — source: `` — produced by: `chunker.py::split_documents`

```
Morrow House — what it's actually like

The bad: known damp problem on the ground floor; two rooms were taken offline in 2024.       

Laundry costs $1.50 wash, $1.25 dry, coin or card. On noise: loud until about 1am on weekends, no enforced quiet hours.

For each one, ask: could someone answer a question using only this,
without reading what came before or after?
```

## Sample Answer

<!-- One complete question and answer, pasted as text, with the source line
     visible. Milestone 4. -->

**Question:**

"How often does the campus shuttle loop on weekdays?"

**Answer:**

```
======================================================================
System instruction sent with the prompt
======================================================================
You answer questions using only the documents provided to you.

Rules:
- Use only the information in the documents below. Do not use anything you know from elsewhere.
- If the documents don't cover the question, say you don't have enough information. Do not guess.
- Name the document your answer came from, using the filename given in each excerpt.
- Be brief. Two or three sentences is usually enough.

======================================================================
The assembled prompt, exactly as sent
======================================================================
Documents:

[from transit_shuttle.txt]
The campus shuttle

Runs a loop every 20 minutes from 7am to 11pm on weekdays and every 40 minutes on weekends. The published timetable is optimistic by about five minutes in the morning and accurate the rest of the day.

It's free with a student ID. The stop outside Fenwick Court is the one that gets skipped when the driver is behind, which is worth knowing if you live there.

[from dining_verrill_street_grill.txt]
Verrill Street Grill

I'm a junior and I've done this twice now. Wait times: up to 30 minutes on Friday evenings, otherwise under 10. The thing worth going for is the burger, which is the only late-night hot food on campus. The thing to know is that one register, so the queue is a single line no matter how busy.

Hours are 11:00am to 1:00am daily during term. Costs declining balance, or cash after 11:00pm.

[from transit_walking.txt]
Walking times across campus

Rough numbers, measured rather than guessed. Aldridge Hall to the science quad: 4 minutes. Fenwick Court to central campus: 18 minutes. Morrow House to Kestrel Commons: 7 minutes. Library to Ridgeway Café: 3 minutes.

Add four minutes in winter. The path past the pond genuinely ices over and people take the long way round.

[from dining_halden_hall_followup.txt]
Re: Halden Hall

Adding to what people have said about Halden Hall. The wait figure of rarely more than 8 minutes matches what I've seen. If you're trying to eat between classes, go before 11:45 and it's a different building entirely.

Also worth saying: closes at 7:00pm, which catches people out. Nobody tells you this at orientation.

[from dining_kestrel_commons_followup.txt]
Re: Kestrel Commons

Adding to what people have said about Kestrel Commons. The wait figure of 20 to 25 minutes between 12:15 and 1:00 matches what I've seen. If you're trying to eat between classes, go before 11:45 and it's a different building entirely.

Also worth saying: the salad bar wilts after 1:30. Nobody tells you this at orientation.

---

Question: How often does the campus shuttle loop on weekdays?

Answer using only the documents above, and name the file you used.
======================================================================

The campus shuttle runs a loop every 20 minutes on weekdays (transit_shuttle.txt).

Sources retrieved: dining_halden_hall_followup.txt, dining_kestrel_commons_followup.txt, dining_verrill_street_grill.txt, transit_shuttle.txt, transit_walking.txt

0 model calls this session, 1 served from cache
```

**My relevance cutoff:**

<!-- The number you set in config.py, and how you got there.

     You ran five questions your corpus covers and the five in OUT_OF_SCOPE
     that it clearly doesn't, and wrote down the best distance for each. What
     did those two groups look like? Where was the gap? Put the actual numbers
     here — the table below wants all ten rows.

     Milestone 4. -->

I chose to stick with 0.6 as my cutoff. The reason being some of the questions came back with a distance of roughly ~0.56 which would mean that if I lowered my cutoff I would have missed that answer. And going higher was not needed, as it seems that the distance of roughly 0.8 is when it begins to finally determine that it doesn't have the answer. So 0.6 seemed to be the sweet spot. 

| Question | In corpus? | Best distance |
|---|---|---|
|  "what is the maximum number of hours that can be worked in a week at the library?" | yes | 0.396 |
|"what is the cheapest housing option?" | yes | 0.564|
| "How long does the club fair go on for?" | yes | 0.457|
| "How often does the campus shuttle loop on weekdays?" | yes | 0.372 |
| "When do the paths get cleared on weekdays of snow?" | yes | 0.450 |
| "What is the capital of Mongolia?" | No | 0.825 |
| "How do I change the oil in a diesel engine?" | No | 0.934 |
| "Who won the 1994 World Cup?" | No | 0.886 |
| "What is the recommended dosage of ibuprofen for a headache?" | No | 0.844 |
| "How do I write a for loop in Rust?" | No | 0.896 |

## How I Used AI

<!-- Two specific moments. For each: what you asked for, what came back, and
     what you changed about it.

     "I asked Claude to write the chunking function from my notes. It ignored
     the overlap, so I added that myself" is the level of detail we're after.
     "I used AI to help me code" is not.

     Milestone 5. -->

**1.**

I asked AI on ways on how we should chunk the data. It originally suggested to sperate each chunk by sentence, but this was because I told it that the corpus was reviews, and that each review was relatively small. It was wrong in doing so and I told it that this is not the correct way to seperate this corpus. It then helped me to create a chunker based on similar paragraphs, it stayed nearly identical to the starter chunker, but a little better for longer reviews. 

**2.**

I asked AI to help me create good acceptance critera. It gave me ones that were too similar to the original 3 that were given to us. I explained that these were identical to what we had already and that it wouldn't be a viable option. It agreed and helped me brainstorm 2 more ideas. 

<!-- ── Stretch features ─────────────────────────────────────────────────────
     Doing one? Say so here BEFORE you start. A feature this README never
     claims earns nothing.
     ───────────────────────────────────────────────────────────────────────── -->

---

# Unit 2

<!-- These sections get ADDED to what's already above. Don't delete or rewrite
     unit 1 — the point is that someone can see what you said before you knew
     how it went. -->

## Run Log — Before

<!-- Your five criteria, three runs each. `python run_eval.py --label before`
     runs the questions, puts the OUT_OF_SCOPE ones through the gate, and
     writes it all into results/ for you. Targets come from criteria.md; the
     verdict column is your call.

     Criterion 3 is measured in one deterministic pass rather than three, so
     the same number goes in all three run columns. That's correct, not lazy.

     Milestone 1. -->

| Criterion | Target | Run 1 | Run 2 | Run 3 | Verdict |
|---|---|---|---|---|---|
| 1. Retrieved chunk contains the answer | 4 of 5 |  |  |  |  |
| 2. Every answer names a source | 5 of 5 |  |  |  |  |
| 3. Gate stops out-of-corpus questions | 4 of 5 |  |  |  |  |
| 4. | | | | | |
| 5. | | | | | |

<!-- Underneath, paste the REAL output for each criterion from one of your
     runs — the actual text your system produced, not a description of it.
     Name the file and function that produced it. -->

## Verdicts

<!-- MET or MISSED for each of the five, against the target you wrote last
     unit — not a new one. Plus a sentence on how you decided. That sentence
     matters most where it was close.

     If your target said 4 of 5 and your runs came out 4, 3, 4, that's a MISS.
     The target has to hold, not show up occasionally.

     Milestone 2. -->

| # | Criterion | Verdict | How I decided |
|---|---|---|---|
| 1 |  |  |  |
| 2 |  |  |  |
| 3 |  |  |  |
| 4 |  |  |  |
| 5 |  |  |  |

## Diagnoses

<!-- For each miss: which stage caused it, and how. The stage alone isn't
     enough — you need the mechanism.

     Not a diagnosis: "Question 3 didn't work."
     A diagnosis:     "Question 3 asks about laundry costs. The answer is in
                       one sentence that got split across two chunks, so
                       neither chunk on its own contains it."

     The five stages: loading → chunking → embedding → retrieval → generation.

     Look for a pattern. If three misses all ask about numbers, that's one
     problem, not three.

     Missed nothing? Say so, then say honestly whether your targets were set
     low, and which one you'd tighten and to what.

     Milestone 3. -->

## The Improvement

**What I changed:**

**Why I picked it:**

<!-- Connect it to a specific diagnosis above in one sentence. If you can't,
     you picked a fix because it sounded impressive. -->

### Run Log — After

<!-- Same format, same five criteria, three runs each.
     `python run_eval.py --label after` -->

| Criterion | Target | Run 1 | Run 2 | Run 3 | Verdict |
|---|---|---|---|---|---|
| 1. Retrieved chunk contains the answer | 4 of 5 |  |  |  |  |
| 2. Every answer names a source | 5 of 5 |  |  |  |  |
| 3. Gate stops out-of-corpus questions | 4 of 5 |  |  |  |  |
| 4. | | | | | |
| 5. | | | | | |

**Did it help?**

<!-- Say plainly whether it did, and how you know. If it made things worse,
     say that — a change that backfired, honestly reported, earns full credit
     and is more interesting than one that worked. What matters is that you can
     tell.

     Milestone 4. -->

## What's Still Broken

<!-- For each criterion still missed after your fix: what you'd do about it,
     and why you stopped where you did.

     "I ran out of time" is fine if it's true. Pretending nothing is left is
     not.

     Milestone 5. -->

## What I'd Do Differently

<!-- Knowing what you know now — which of your five criteria would you write
     differently, and why?

     Milestone 5. -->

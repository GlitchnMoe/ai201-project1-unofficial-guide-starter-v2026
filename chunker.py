"""
Stage 2 of the pipeline: splitting documents into chunks.

⚠️ THIS IS THE FILE YOU CHANGE IN MILESTONE 3.

`split_documents` below is deliberately plain. It cuts every document into
fixed-size pieces with a fixed overlap and pays no attention to where sentences
or paragraphs end. It works, and it is not good.

On a corpus of short posts it may not cut anything at all: `campus_life` comes
out as 88 documents and 88 chunks, because almost nothing in it reaches 800
characters. That is the baseline, not a bug — Milestone 3 is where you decide
whether one post should stay one chunk.

Your job in Milestone 3 is to replace the *body* of `split_documents` with a
strategy that fits the documents you actually read in Milestone 1. Keep the
name and the shape of what it returns — the rest of the pipeline calls it, and
your README has to name the function that produced your chunks.

If you get stuck for 30 minutes, `fallback_split` is the original. Switch back
to it, write down what you saw, and move on. That's a real observation about
your pipeline, not giving up.
"""

from dataclasses import dataclass

import config
from ingest import Document
import re

@dataclass
class Chunk:
    """One piece of one document."""

    text: str
    source: str        # which file it came from
    index: int         # which chunk within that file, starting at 0
    produced_by: str   # the function that made it — cite this in your README

    @property
    def label(self) -> str:
        return f"{self.source}#{self.index}"


def fallback_split(
    documents: list[Document],
    chunk_size: int | None = None,
    overlap: int | None = None,
) -> list[Chunk]:
    """
    The starter's original chunker. Fixed-size character windows with overlap.

    Keep this function. Milestone 3's stop rule points back at it, and having
    something to compare your own strategy against is useful in unit 2.
    """
    chunk_size = chunk_size or config.CHUNK_SIZE
    overlap = overlap or config.CHUNK_OVERLAP

    if overlap >= chunk_size:
        raise ValueError("overlap has to be smaller than chunk_size")

    chunks: list[Chunk] = []
    for doc in documents:
        start = 0
        index = 0
        while start < len(doc.text):
            piece = doc.text[start : start + chunk_size].strip()
            if piece:
                chunks.append(
                    Chunk(
                        text=piece,
                        source=doc.source,
                        index=index,
                        produced_by="chunker.py::fallback_split",
                    )
                )
                index += 1
            start += chunk_size - overlap

    return chunks




# def split_documents(documents: list[Document]) -> list[Chunk]:
#     """
#     Structure-aware chunker for short review-style documents.

#     - Preserves short reviews.
#     - Uses paragraph boundaries.
#     - Splits longer multi-paragraph reviews into groups of paragraphs.
#     - Carries the document title into every chunk.
#     - Avoids tiny leftover chunks.
#     """

#     MAX_PARAGRAPHS = 2
#     MIN_CHARS = 140

#     chunks: list[Chunk] = []

#     for doc in documents:
#         text = doc.text.strip()

#         if not text:
#             continue

#         paragraphs = [
#             p.strip()
#             for p in re.split(r"\n\s*\n", text)
#             if p.strip()
#         ]

#         if not paragraphs:
#             continue

#         # Detect a likely title/header.
#         first = paragraphs[0]

#         if (
#             len(first) <= 100
#             and len(first.split()) <= 15
#             and not first.endswith((".", "!", "?"))
#         ):
#             title = first
#             body = paragraphs[1:]
#         else:
#             title = ""
#             body = paragraphs

#         # Reviews with only one or two body paragraphs stay intact.
#         if len(body) <= MAX_PARAGRAPHS:
#             chunks.append(
#                 Chunk(
#                     text=text,
#                     source=doc.source,
#                     index=0,
#                     produced_by="chunker.py::split_documents",
#                 )
#             )
#             continue

#         # Group body paragraphs into pairs.
#         groups = []

#         for i in range(0, len(body), MAX_PARAGRAPHS):
#             group = body[i:i + MAX_PARAGRAPHS]
#             groups.append(group)

#         # If the final group is tiny, merge it into the previous one.
#         if len(groups) > 1:
#             final_text = "\n\n".join(groups[-1])

#             if len(final_text) < MIN_CHARS:
#                 groups[-2].extend(groups[-1])
#                 groups.pop()

#         # Create chunks, repeating the title for context.
#         for index, group in enumerate(groups):
#             body_text = "\n\n".join(group)

#             if title:
#                 chunk_text = f"{title}\n\n{body_text}"
#             else:
#                 chunk_text = body_text

#             chunks.append(
#                 Chunk(
#                     text=chunk_text,
#                     source=doc.source,
#                     index=index,
#                     produced_by="chunker.py::split_documents",
#                 )
#             )

#     return chunks

def split_documents(documents: list[Document]) -> list[Chunk]:
    """
    Second chunking strategy for short review-style documents.

    - Uses individual paragraphs as the preferred chunk boundary.
    - Preserves reviews that only have one body paragraph.
    - Carries the document title into every chunk.
    - Merges very small paragraphs with a neighboring paragraph
      so they do not become contextless fragments.
    """

    MIN_CHARS = 140

    chunks: list[Chunk] = []

    for doc in documents:
        text = doc.text.strip()

        if not text:
            continue

        paragraphs = [
            p.strip()
            for p in re.split(r"\n\s*\n", text)
            if p.strip()
        ]

        if not paragraphs:
            continue

        # Detect a likely title/header.
        first = paragraphs[0]

        if (
            len(first) <= 100
            and len(first.split()) <= 15
            and not first.endswith((".", "!", "?"))
        ):
            title = first
            body = paragraphs[1:]
        else:
            title = ""
            body = paragraphs

        # If there is only one body paragraph,
        # there is nothing useful to split.
        if len(body) <= 1:
            chunks.append(
                Chunk(
                    text=text,
                    source=doc.source,
                    index=0,
                    produced_by="chunker.py::split_documents",
                )
            )
            continue

        # New strategy:
        # begin with one body paragraph per chunk.
        groups = [[paragraph] for paragraph in body]

        # Merge any paragraph that is too small to stand alone.
        i = 0

        while i < len(groups):
            group_text = "\n\n".join(groups[i])

            if len(group_text) >= MIN_CHARS or len(groups) == 1:
                i += 1
                continue

            # Prefer merging a small chunk backward.
            if i > 0:
                groups[i - 1].extend(groups[i])
                groups.pop(i)

            # If it is the first chunk, merge it forward.
            else:
                groups[1] = groups[0] + groups[1]
                groups.pop(0)

        # Create final chunks.
        # Repeat the title so every split chunk retains document context.
        for index, group in enumerate(groups):
            body_text = "\n\n".join(group)

            if title:
                chunk_text = f"{title}\n\n{body_text}"
            else:
                chunk_text = body_text

            chunks.append(
                Chunk(
                    text=chunk_text,
                    source=doc.source,
                    index=index,
                    produced_by="chunker.py::split_documents",
                )
            )

    return chunks


def describe(chunks: list[Chunk]) -> str:
    """A one-line summary, printed after indexing."""
    if not chunks:
        return "0 chunks"
    lengths = [len(c.text) for c in chunks]
    return (
        f"{len(chunks)} chunks, "
        f"{sum(lengths) // len(lengths)} characters on average "
        f"(shortest {min(lengths)}, longest {max(lengths)}), "
        f"produced by {chunks[0].produced_by}"
    )


if __name__ == "__main__":
    from ingest import load_documents

    chunks = split_documents(load_documents())
    print(describe(chunks))

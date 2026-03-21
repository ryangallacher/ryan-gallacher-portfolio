# /case-study

Synthesise a portfolio case study from a project's session journals.

## Usage

```
/case-study path/to/project
```

Example: `/case-study C:/Users/Ryan/Documents/GitHub/sense-check`

## What this does

1. Reads all session journals from `[project]/project-story/*.md`
2. Reads `voice.md` and `case-study-template.md` from this repo
3. Produces a structured first-draft case study following the template schema and voice guidelines

## Instructions

When this command is run:

1. **Identify the project path** from the argument. If no argument is given, ask the user which project they want to write up.

2. **Read the journals** — read all `.md` files in `[project-path]/project-story/`. If the directory doesn't exist or is empty, tell the user and stop.

3. **Read the template and voice** — read both files from this repo:
   - `case-study-template.md`
   - `voice.md` (if it has content beyond the placeholder comments, use it; if empty, note that voice guidance isn't available yet and proceed with the template only)

4. **Synthesise** — produce a structured case study draft following the template story beats.

   > **Note for future extension:** this step is the synthesis layer. Currently handled by Claude reading the journals directly. Could be replaced with a NotebookLM pipeline, a RAG system, or any tool that accepts the journals as input and returns a structured summary — without changing the steps before or after.

 Prioritise:
   - Decisions and their rationale (from journal decision sentences)
   - Pivots and what caused them
   - Measurable outcomes (numbers, before/after)
   - Honest reflection on what didn't work

   Do not invent detail that isn't in the journals. If a section of the template has no supporting material, leave a `[no data — fill in manually]` note.

5. **Output** — write the draft to `[project-path]/case-study-draft.md`. Tell the user where it was saved and what sections need manual attention.

## Reminders

- This is a first draft only. Ryan will always rewrite before anything goes public.
- The output should feel like Ryan wrote it — check voice.md for guidance on tone and phrases.
- Big numbers deserve their own line. Don't bury metrics in prose.

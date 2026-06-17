# Block 3: Instructor Notes

## Per-slide notes

### 1. Title

- *"Blocks 1 and 2 were about how it works. This block is about how to use it on real research analysis without it blowing up."*

### 2. Where we left off ("workflows are reusable skills")

- Read the slide.

### 3. The research loop (skills)

- Acknowledge your HCI background.

### 4. Skills: invoke or auto-select

- The one genuinely new mechanic in this block. Land it clearly: a skill's `description` (the `Use when…` clause) is what the agent matches a generic ask against.
- *"You can name the skill, or you can just say what you want and let the agent route. Same file either way."*
- *"You don't use all seven every time. You pick the pattern that matches your work."* (We demo all seven because it's a full study.)

### 5. Demo intro

- In Copilot Chat (Agent mode), briefly show that there is no `blocks/03-research-loop/demo/docs/` directory yet, and that `blocks/03-research-loop/demo/AGENTS.md` + `blocks/03-research-loop/demo/starter/data.csv` are there in the Explorer.
- *"We're going to analyze this dataset and draft the write-up. Watch the artifacts appear in `docs/` as we go. And watch for the trap — the obvious test is the wrong test."*

### 6. Failure mode taxonomy

- Read the slide.

### 7. Mitigations

- Read the slide.

### 8. Reviewing the agent's work (git hygiene)

- Read the slide.

### 9. When the input is hostile (prompt injection)

- Read the slide


### 10. Bridge to Block 4

- Read the slide.


# Demo script: the seven skills

Run them one at a time, in order.

### 1. `profile-dataset` (target: 2 min)

```
Read blocks/03-research-loop/demo/AGENTS.md first, then use the profile-dataset skill on blocks/03-research-loop/demo/starter/data.csv.
```

(The first prompt names the full paths so the agent locks onto the demo folder and reads its `AGENTS.md`. After this, the agent knows the project root and the artifacts directory.)


### 2. `plan-analysis` (target: 2 min)

```
Use the plan-analysis skill to plan how to test whether the three interfaces differ in typing speed.
```

- The key beat: *"Watch whether it respects the within-subjects design. The right answer is a repeated-measures / Friedman family, not a one-way ANOVA."* Open `blocks/03-research-loop/demo/docs/analysis-plan-text-entry.md` and point at the **Automated vs Manual** success criteria — *"this is what makes validation possible."*

### 3. `explore-data` (target: 4 min — this is where the trap surfaces)

```
Use the explore-data skill to run the EDA and assumption checks the plan calls for.
```

- *"This is the phase that decides which test is valid."* When the Shapiro–Wilk results come back, point at `swipe` failing normality (p < .0001) — *"there's the outlier biting. This is why we'll go non-parametric."*
- Open the figures in `blocks/03-research-loop/demo/docs/figures/` (or the fallback `expected-artifacts/figures/`): the boxplot with the lone point near 10 wpm, and the paired-lines plot showing the within-subject structure.

### 4. `statistical-tests` (target: 4 min: narrate failure modes during)

```
Use the statistical-tests skill to run the test the assumptions support.
```

- Did it run Friedman (correct) or an independent one-way ANOVA (the trap)? If it reached for `f_oneway`, that's the 'scope creep / wrong test' failure mode live."
- Expect: Friedman χ²(2) ≈ 45.2, p ≈ 1.5e-10, Kendall's W ≈ 0.75; Wilcoxon post-hoc (Holm) all significant; ordering qwerty > swipe > predictive.

### 5. `draft-report` (target: 2 min)

```
Use the draft-report skill to write the Methods and Analysis sections.
```

- *"Watch the citations."* Open `blocks/03-research-loop/demo/docs/draft-text-entry.md` and point at the `[CITATION NEEDED]` markers — *"a draft full of visible placeholders is correct; a draft with confident fake citations is the failure mode."*

### 6. `validate-analysis` (target: 2 min)

```
Use the validate-analysis skill to check the analysis and the draft.
```

- *"This is the quality gate. It re-runs the numbers and checks the draft's claims against them."*
- When the report appears: read the pass/fail summary. 

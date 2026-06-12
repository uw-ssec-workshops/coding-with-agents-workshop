---
agent: agent
description: 'Draft a CITATION.cff and release notes from the repo metadata and git history.'
tools: ['read', 'search/codebase', 'execute/runInTerminal', 'vscode/askQuestions']
---

# Citation + release notes

Help a research project become citable and release-ready. This is the
**packaging / publication** phase of the research lifecycle — the step where
software becomes something other scientists can cite and reuse.

Scope for this run: `${input:scope:e.g. "v0.2.0 release" or "just the CITATION.cff"}`.
If the scope is blank or unclear, use `#tool:vscode/askQuestions` to confirm with
the user whether this is a full release or just the `CITATION.cff` before starting.
Repo root: `${workspaceFolder}` — read project metadata from there.

## Steps

1. Read `${workspaceFolder}/pyproject.toml`, `${workspaceFolder}/README.md`,
   `${workspaceFolder}/LICENSE`, and any existing `CITATION.cff`. Pull authors,
   project name, license, version, and repo URL.
2. **CITATION.cff**: draft or update a valid Citation File Format file
   (`cff-version: 1.2.0`). Include `title`, `authors` (name/affiliation/ORCID
   if discoverable — otherwise leave a clearly-marked TODO), `version`,
   `date-released`, `license`, `repository-code`, and a `preferred-citation`
   stub if the work has an associated paper.
3. **Release notes**: read recent history with `git log` (e.g.
   `git log --oneline -n 50` and tags via `git tag`). Group changes into
   **Added / Changed / Fixed / Removed** (Keep a Changelog style). Write for
   a scientist reader: lead with what changed for _users_, not internal refactors.
4. Suggest the version bump (semver: breaking -> major, feature -> minor,
   fix -> patch) and the next steps to archive for a DOI (e.g. tag the
   release, connect the repo to Zenodo).

## Constraints

- Use `git` commands read-only (`log`, `tag`, `show`). Do **not** create tags,
  commit, or push.
- Do not invent authors, ORCIDs, dates, or DOIs. Anything you cannot verify
  from the repo gets a `# TODO:` marker for the human to fill in.
- Produce valid CFF (it is YAML with a defined schema). If unsure about a
  field, omit it rather than emit something that fails validation.

## Output format

1. A fenced `CITATION.cff` block ready to save.
2. A `## Release notes — <version>` markdown section.
3. A short **"before you publish"** checklist (tag, archive for DOI, update
   version in `pyproject.toml`, fill remaining TODOs).

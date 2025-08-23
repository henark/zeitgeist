# Version Management Strategy for TimeChain Whitepaper

## 1. Semantic Versioning Scheme
| Version | Meaning | Typical Changes |
|---------|---------|-----------------|
| **v0.1** | First public draft | Initial content, informal review |
| **v0.2** | Feature‑complete draft | Incorporates reviewer feedback, adds diagrams |
| **v1.0** | Publication‑ready | Final polish, formal citations, legal review |
| **vX.Y+1** | Minor updates | Errata, formatting tweaks |
| **vX+1.0** | Major release | New sections, protocol revisions |

## 2. Branch Naming Convention (Git)
- `main` – always points to the latest released version (e.g., `v0.2`).
- `dev` – ongoing work for the next version.
- `feature/<short‑name>` – isolated work (e.g., `feature/consensus‑flow`).
- `review/<reviewer‑id>` – reviewer‑specific branches for comment resolution.

## 3. Tagging & Release Notes
```bash
git tag -a v0.2 -m "Release v0.2 – incorporated reviewer feedback"
git push origin v0.2
```
- Keep a `CHANGELOG.md` that follows **Keep a Changelog** conventions.

## 4. Quality Gates (Pre‑Release Checklist)
- [ ] All checklist items in `WHITEPAPER_REVIEW_CHECKLIST.md` marked ✅
- [ ] All diagrams exported in SVG + PNG (high‑res) and referenced in the markdown.
- [ ] Spell‑check & grammar (e.g., `cspell`, `write-good`).
- [ ] PDF build passes (Pandoc/Typst) without warnings.
- [ ] Legal disclaimer and licensing section added.

## 5. Change Management Process
1. **Open an Issue** → summarize the change (e.g., “Add PoT consensus flow diagram”).
2. **Create a Feature Branch** → `git checkout -b feature/consensus‑flow`.
3. **Implement & Commit** → reference the issue number.
4. **Open a Pull Request** → assign at least two reviewers.
5. **Merge** → after approvals, squash‑merge into `dev`.
6. **Release** → bump version, tag, and update `CHANGELOG.md`.

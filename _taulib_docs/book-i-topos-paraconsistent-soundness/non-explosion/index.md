---
{
  "projection_kind": "taulib_declaration",
  "title": "non_explosion",
  "permalink": "/verify/taulib/docs/book-i-topos-paraconsistent-soundness/non-explosion/",
  "summary_short": "`theorem` declaration in `TauLib.BookI.Topos.ParaconsistentSoundness`.",
  "declaration_id": "TauLib.BookI.Topos.ParaconsistentSoundness::non_explosion",
  "declaration_slug": "non-explosion",
  "kind": "theorem",
  "name": "non_explosion",
  "module_name": "TauLib.BookI.Topos.ParaconsistentSoundness",
  "module_url": "/verify/taulib/docs/book-i-topos-paraconsistent-soundness/",
  "source_line_start": 301,
  "source_line_end": 304,
  "registry_ids": [],
  "related_registry_items": [],
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookI/Topos/ParaconsistentSoundness.lean#L301-L304",
  "formal_status": "formalized",
  "right_rail": {
    "related": [
      {
        "title": "TauLib.BookI.Topos.ParaconsistentSoundness",
        "url": "/verify/taulib/docs/book-i-topos-paraconsistent-soundness/"
      },
      {
        "title": "TauLib Projection Index",
        "url": "/verify/taulib/docs/"
      },
      {
        "title": "Formalization Status",
        "url": "/verify/taulib/status/"
      }
    ],
    "artifacts": [
      {
        "title": "Source on GitHub",
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookI/Topos/ParaconsistentSoundness.lean#L301-L304",
        "external": true
      }
    ],
    "meta": {
      "type": "TauLib Declaration",
      "kind": "theorem",
      "status": "formalized"
    }
  },
  "layout": "taulib-doc",
  "lane": "verify",
  "v2_lane": "verify",
  "status": "Canonical",
  "generated_from": "corpus/taulib-projections",
  "projection_version": "v0.1",
  "canonical_source": "Panta-Rhei-Research/taulib",
  "do_not_edit": true,
  "type": "TauLib Declaration"
}
---

## Declaration Projection

This page is generated directly from the pinned TauLib Lean source snapshot. The source excerpt is public because the active TauLib repository is public.

## Source Provenance

- Module: [TauLib.BookI.Topos.ParaconsistentSoundness](/verify/taulib/docs/book-i-topos-paraconsistent-soundness/)
- Source path: [`TauLib/BookI/Topos/ParaconsistentSoundness.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookI/Topos/ParaconsistentSoundness.lean#L301-L304)
- Source range: L301-L304
- Kind: `theorem`
- Formal status hint: `formalized`

## Registry Links

- No Registry IDs were detected in this declaration block.

## Immediate Comment / Docstring

```lean
/-- **Failure of explosion** (paper Theorem 6.2 / paper ref
    `thm:non-explosion`).

    In `Cat_τ`'s internal logic, the classical rule
    `p ∧ ¬p ⊨ q` (*ex contradictione quodlibet*) **fails** under
    FDE designated-preservation: there exist closed propositions
    `p, q : Truth4` with `p ∧ σp` designated (so the premise is
    valid in `D`) while `q` is not designated (so the conclusion
    escapes `D`).

    Witness: `p = B` (the Liar's ω-germ stabilised value from
    Wave 9's `liar_stabilises_at_Both`), `q = N` (an unstabilised
    proposition, paper case (d) of `circularity-classification`).
    Then `p ∧ σp = B ∧ B = B ∈ D` but `q = N ∉ D`, so
    designated-preservation fails and hence `p ∧ ¬p ⊬ q`. -/
```

## Source Excerpt

```lean
theorem non_explosion :
    ∃ p q : Truth4, IsDesignated (Truth4.meet p (sigmaSwap p)) ∧
                    ¬ IsDesignated q :=
  ⟨B, N, meet_B_sigmaSwap_B_designated, not_isDesignated_N⟩
```

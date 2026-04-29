---
{
  "projection_kind": "taulib_declaration",
  "title": "four_sector_witness_liar",
  "permalink": "/verify/taulib/docs/book-i-topos-circularity-resolution/four-sector-witness-liar/",
  "summary_short": "`theorem` declaration in `TauLib.BookI.Topos.CircularityResolution`.",
  "declaration_id": "TauLib.BookI.Topos.CircularityResolution::four_sector_witness_liar",
  "declaration_slug": "four-sector-witness-liar",
  "kind": "theorem",
  "name": "four_sector_witness_liar",
  "module_name": "TauLib.BookI.Topos.CircularityResolution",
  "module_url": "/verify/taulib/docs/book-i-topos-circularity-resolution/",
  "source_line_start": 347,
  "source_line_end": 349,
  "registry_ids": [],
  "related_registry_items": [],
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookI/Topos/CircularityResolution.lean#L347-L349",
  "formal_status": "formalized",
  "right_rail": {
    "related": [
      {
        "title": "TauLib.BookI.Topos.CircularityResolution",
        "url": "/verify/taulib/docs/book-i-topos-circularity-resolution/"
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookI/Topos/CircularityResolution.lean#L347-L349",
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

- Module: [TauLib.BookI.Topos.CircularityResolution](/verify/taulib/docs/book-i-topos-circularity-resolution/)
- Source path: [`TauLib/BookI/Topos/CircularityResolution.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookI/Topos/CircularityResolution.lean#L347-L349)
- Source range: L347-L349
- Kind: `theorem`
- Formal status hint: `formalized`

## Registry Links

- No Registry IDs were detected in this declaration block.

## Immediate Comment / Docstring

```lean
/-- **Four-sector classification (existence form)**: for every
    template `Φ : Truth4 → Truth4` and seed `s`, the Cauchy
    iteration `cauchyIter Φ n s` exhibits at least one of the four
    asymptotic patterns — at the surface level this is the
    classical statement of paper Theorem
    `circularity-classification`, packaged here as a witness-
    existence claim using the `StabilisedValue` predicate.

    Concretely: for *any* finite-state dynamics on the 4-element
    state space `Truth4`, the orbit either stabilises at one of the
    four atoms or oscillates with finite period.  The Liar
    (`liar_stabilises_at_Both`) and the Truth-teller
    (`truth_teller_stabilises_T/F`) are the canonical witnesses;
    the general existence statement is established constructively
    by the case-analysis-over-orbit-pattern argument from the paper.

    This module establishes the *structural framework* and verifies
    the canonical witnesses; the full existence theorem (every
    `Φ, s` admits *some* `v` with `StabilisedValue Φ s v`) is a
    finite-state pigeonhole argument which we record here as
    a structural Prop and elaborate in a future wave once the
    pigeonhole infrastructure on `Truth4` is in place. -/
```

## Source Excerpt

```lean
theorem four_sector_witness_liar :
    ∃ v : Truth4, StabilisedValue liarTemplate F v :=
  ⟨B, liar_stabilises_at_Both⟩
```

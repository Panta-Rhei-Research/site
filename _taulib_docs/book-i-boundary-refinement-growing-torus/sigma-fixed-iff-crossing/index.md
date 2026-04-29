---
{
  "projection_kind": "taulib_declaration",
  "title": "RefinedTorusDefect.sigma_fixed_iff_crossing",
  "permalink": "/verify/taulib/docs/book-i-boundary-refinement-growing-torus/sigma-fixed-iff-crossing/",
  "summary_short": "`theorem` declaration in `TauLib.BookI.Boundary.RefinementGrowingTorus`.",
  "declaration_id": "TauLib.BookI.Boundary.RefinementGrowingTorus::RefinedTorusDefect.sigma_fixed_iff_crossing",
  "declaration_slug": "sigma-fixed-iff-crossing",
  "kind": "theorem",
  "name": "RefinedTorusDefect.sigma_fixed_iff_crossing",
  "module_name": "TauLib.BookI.Boundary.RefinementGrowingTorus",
  "module_url": "/verify/taulib/docs/book-i-boundary-refinement-growing-torus/",
  "source_line_start": 131,
  "source_line_end": 146,
  "registry_ids": [],
  "related_registry_items": [],
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookI/Boundary/RefinementGrowingTorus.lean#L131-L146",
  "formal_status": "formalized",
  "right_rail": {
    "related": [
      {
        "title": "TauLib.BookI.Boundary.RefinementGrowingTorus",
        "url": "/verify/taulib/docs/book-i-boundary-refinement-growing-torus/"
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookI/Boundary/RefinementGrowingTorus.lean#L131-L146",
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

- Module: [TauLib.BookI.Boundary.RefinementGrowingTorus](/verify/taulib/docs/book-i-boundary-refinement-growing-torus/)
- Source path: [`TauLib/BookI/Boundary/RefinementGrowingTorus.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookI/Boundary/RefinementGrowingTorus.lean#L131-L146)
- Source range: L131-L146
- Kind: `theorem`
- Formal status hint: `formalized`

## Registry Links

- No Registry IDs were detected in this declaration block.

## Immediate Comment / Docstring

```lean
/-- **σ-fixed iff crossing** (the singleton uniqueness key fact). -/
```

## Source Excerpt

```lean
theorem RefinedTorusDefect.sigma_fixed_iff_crossing {n : Nat}
    (x : RefinedTorusDefect n) :
    RefinedTorusDefect.sigmaSwap x = x ↔
    x = RefinedTorusDefect.crossing := by
  constructor
  · intro h
    cases x with
    | crossing => rfl
    | bSide k =>
      -- σ(bSide k) = cSide k = bSide k → contradiction
      exact absurd h (by intro heq; cases heq)
    | cSide k =>
      exact absurd h (by intro heq; cases heq)
  · intro h
    subst h
    rfl
```

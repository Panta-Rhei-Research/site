---
{
  "projection_kind": "taulib_declaration",
  "title": "alpha_orbit_strictly_monotone",
  "permalink": "/verify/taulib/docs/book-i-denotation-structural/alpha-orbit-strictly-monotone/",
  "summary_short": "`theorem` declaration in `TauLib.BookI.Denotation.Structural`.",
  "declaration_id": "TauLib.BookI.Denotation.Structural::alpha_orbit_strictly_monotone",
  "declaration_slug": "alpha-orbit-strictly-monotone",
  "kind": "theorem",
  "name": "alpha_orbit_strictly_monotone",
  "module_name": "TauLib.BookI.Denotation.Structural",
  "module_url": "/verify/taulib/docs/book-i-denotation-structural/",
  "source_line_start": 262,
  "source_line_end": 279,
  "registry_ids": [],
  "related_registry_items": [],
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookI/Denotation/Structural.lean#L262-L279",
  "formal_status": "formalized",
  "right_rail": {
    "related": [
      {
        "title": "TauLib.BookI.Denotation.Structural",
        "url": "/verify/taulib/docs/book-i-denotation-structural/"
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookI/Denotation/Structural.lean#L262-L279",
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

- Module: [TauLib.BookI.Denotation.Structural](/verify/taulib/docs/book-i-denotation-structural/)
- Source path: [`TauLib/BookI/Denotation/Structural.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookI/Denotation/Structural.lean#L262-L279)
- Source range: L262-L279
- Kind: `theorem`
- Formal status hint: `formalized`

## Registry Links

- No Registry IDs were detected in this declaration block.

## Immediate Comment / Docstring

```lean
/-- The alpha orbit is strictly monotone in depth: higher orbit index
    means strictly greater depth.  There is no "stalling" in the orbit. -/
```

## Source Excerpt

```lean
theorem alpha_orbit_strictly_monotone (n m : TauIdx) (h : n < m) :
    (toAlphaOrbit n).depth < (toAlphaOrbit m).depth := by
  simp [toAlphaOrbit]; exact h

-- ============================================================
-- SECTION 6: FINITE STABILIZATION & COMPACTNESS
-- ============================================================

/-! ## Section 6: Finite Stabilization & Compactness

The primorial ultrametric on omega-tails induces a profinite topology on
the completion space.  The key property is **finite stabilization**: at each
primorial level M_k, two omega-tails either agree or disagree — and agreement
propagates downward through the reduction maps.

This gives τ-Idx its *Cauchy-compact* character: every Compatible sequence
stabilizes at each finite level, making the completion (the space of all
compatible omega-tails) compact.  This is the τ-analog of Ẑ (profinite integers). -/
```

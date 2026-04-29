---
{
  "projection_kind": "taulib_declaration",
  "title": "polarity_swap_involutive",
  "permalink": "/verify/taulib/docs/book-iii-physics-hartogs-flow/polarity-swap-involutive/",
  "summary_short": "`theorem` declaration in `TauLib.BookIII.Physics.HartogsFlow`.",
  "declaration_id": "TauLib.BookIII.Physics.HartogsFlow::polarity_swap_involutive",
  "declaration_slug": "polarity-swap-involutive",
  "kind": "theorem",
  "name": "polarity_swap_involutive",
  "module_name": "TauLib.BookIII.Physics.HartogsFlow",
  "module_url": "/verify/taulib/docs/book-iii-physics-hartogs-flow/",
  "source_line_start": 160,
  "source_line_end": 162,
  "registry_ids": [
    "III.D41"
  ],
  "related_registry_items": [
    {
      "id": "III.D41",
      "title": "Operator Polarity Swap",
      "url": "/registry/object/III.D41/"
    }
  ],
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIII/Physics/HartogsFlow.lean#L160-L162",
  "formal_status": "formalized",
  "right_rail": {
    "related": [
      {
        "title": "TauLib.BookIII.Physics.HartogsFlow",
        "url": "/verify/taulib/docs/book-iii-physics-hartogs-flow/"
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIII/Physics/HartogsFlow.lean#L160-L162",
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

- Module: [TauLib.BookIII.Physics.HartogsFlow](/verify/taulib/docs/book-iii-physics-hartogs-flow/)
- Source path: [`TauLib/BookIII/Physics/HartogsFlow.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIII/Physics/HartogsFlow.lean#L160-L162)
- Source range: L160-L162
- Kind: `theorem`
- Formal status hint: `formalized`

## Registry Links

- `III.D41` — Operator Polarity Swap

## Immediate Comment / Docstring

```lean
/-- [III.D41] Polarity swap is involutive: σ² = id. -/
```

## Source Excerpt

```lean
theorem polarity_swap_involutive (nf : BoundaryNF) :
    polarity_swap (polarity_swap nf) = nf := by
  cases nf; rfl
```

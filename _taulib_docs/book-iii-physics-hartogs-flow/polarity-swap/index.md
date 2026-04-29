---
{
  "projection_kind": "taulib_declaration",
  "title": "polarity_swap",
  "permalink": "/verify/taulib/docs/book-iii-physics-hartogs-flow/polarity-swap/",
  "summary_short": "`def` declaration in `TauLib.BookIII.Physics.HartogsFlow`.",
  "declaration_id": "TauLib.BookIII.Physics.HartogsFlow::polarity_swap",
  "declaration_slug": "polarity-swap",
  "kind": "def",
  "name": "polarity_swap",
  "module_name": "TauLib.BookIII.Physics.HartogsFlow",
  "module_url": "/verify/taulib/docs/book-iii-physics-hartogs-flow/",
  "source_line_start": 156,
  "source_line_end": 157,
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
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIII/Physics/HartogsFlow.lean#L156-L157",
  "formal_status": "defined",
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIII/Physics/HartogsFlow.lean#L156-L157",
        "external": true
      }
    ],
    "meta": {
      "type": "TauLib Declaration",
      "kind": "def",
      "status": "defined"
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
- Source path: [`TauLib/BookIII/Physics/HartogsFlow.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIII/Physics/HartogsFlow.lean#L156-L157)
- Source range: L156-L157
- Kind: `def`
- Formal status hint: `defined`

## Registry Links

- `III.D41` — Operator Polarity Swap

## Immediate Comment / Docstring

```lean
/-- [III.D41] Polarity swap: exchange B-part and C-part of a BNF.
    This is the physics-level version of the functional equation
    involution J from Part IV. σ(b, c, x) = (c, b, x). -/
```

## Source Excerpt

```lean
def polarity_swap (nf : BoundaryNF) : BoundaryNF :=
  ⟨nf.c_part, nf.b_part, nf.x_part, nf.depth⟩
```

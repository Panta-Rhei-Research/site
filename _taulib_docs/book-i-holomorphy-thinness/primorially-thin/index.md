---
{
  "projection_kind": "taulib_declaration",
  "title": "PrimoriallyThin",
  "permalink": "/verify/taulib/docs/book-i-holomorphy-thinness/primorially-thin/",
  "summary_short": "`def` declaration in `TauLib.BookI.Holomorphy.Thinness`.",
  "declaration_id": "TauLib.BookI.Holomorphy.Thinness::PrimoriallyThin",
  "declaration_slug": "primorially-thin",
  "kind": "def",
  "name": "PrimoriallyThin",
  "module_name": "TauLib.BookI.Holomorphy.Thinness",
  "module_url": "/verify/taulib/docs/book-i-holomorphy-thinness/",
  "source_line_start": 40,
  "source_line_end": 41,
  "registry_ids": [
    "I.D67"
  ],
  "related_registry_items": [
    {
      "id": "I.D67",
      "title": "Primorial Thinness",
      "url": "/registry/object/I.D67/"
    }
  ],
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookI/Holomorphy/Thinness.lean#L40-L41",
  "formal_status": "defined",
  "right_rail": {
    "related": [
      {
        "title": "TauLib.BookI.Holomorphy.Thinness",
        "url": "/verify/taulib/docs/book-i-holomorphy-thinness/"
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookI/Holomorphy/Thinness.lean#L40-L41",
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

- Module: [TauLib.BookI.Holomorphy.Thinness](/verify/taulib/docs/book-i-holomorphy-thinness/)
- Source path: [`TauLib/BookI/Holomorphy/Thinness.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookI/Holomorphy/Thinness.lean#L40-L41)
- Source range: L40-L41
- Kind: `def`
- Formal status hint: `defined`

## Registry Links

- `I.D67` — Primorial Thinness

## Immediate Comment / Docstring

```lean
/-- [I.D67] A subset K is primordially thin at stage k if it
    occupies fewer than k - 1 of the first k positions.
    This leaves ≥ 2 "free" CRT directions. -/
```

## Source Excerpt

```lean
def PrimoriallyThin (inK : TauIdx → Bool) (k : TauIdx) : Prop :=
  k ≥ 2 ∧ count_in_K inK k + 2 ≤ k
```

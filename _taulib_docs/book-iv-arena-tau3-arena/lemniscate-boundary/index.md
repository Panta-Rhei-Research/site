---
{
  "projection_kind": "taulib_declaration",
  "title": "LemniscateBoundary",
  "permalink": "/corpus/taulib/docs/book-iv-arena-tau3-arena/lemniscate-boundary/",
  "summary_short": "`structure` declaration in `TauLib.BookIV.Arena.Tau3Arena`.",
  "declaration_id": "TauLib.BookIV.Arena.Tau3Arena::LemniscateBoundary",
  "declaration_slug": "lemniscate-boundary",
  "kind": "structure",
  "name": "LemniscateBoundary",
  "module_name": "TauLib.BookIV.Arena.Tau3Arena",
  "module_url": "/corpus/taulib/docs/book-iv-arena-tau3-arena/",
  "source_line_start": 186,
  "source_line_end": 193,
  "registry_ids": [
    "IV.D256"
  ],
  "related_registry_items": [
    {
      "id": "IV.D256",
      "title": "Lemniscate boundary --- physical reading",
      "url": "/registry/object/IV.D256/"
    }
  ],
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIV/Arena/Tau3Arena.lean#L186-L193",
  "formal_status": "defined",
  "declaration_role": "type/data schema",
  "formal_status_label": "type/data schema",
  "right_rail": {
    "related": [
      {
        "title": "TauLib.BookIV.Arena.Tau3Arena",
        "url": "/corpus/taulib/docs/book-iv-arena-tau3-arena/"
      },
      {
        "title": "TauLib Projection Index",
        "url": "/corpus/taulib/docs/"
      },
      {
        "title": "Formalization Status",
        "url": "/verify/taulib/status/"
      }
    ],
    "artifacts": [
      {
        "title": "Source on GitHub",
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIV/Arena/Tau3Arena.lean#L186-L193",
        "external": true
      }
    ],
    "meta": {
      "type": "TauLib Declaration",
      "kind": "structure",
      "role": "type/data schema",
      "status": "type/data schema"
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

- Module: [TauLib.BookIV.Arena.Tau3Arena](/corpus/taulib/docs/book-iv-arena-tau3-arena/)
- Source path: [`TauLib/BookIV/Arena/Tau3Arena.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIV/Arena/Tau3Arena.lean#L186-L193)
- Source range: L186-L193
- Kind: `structure`
- Public role: `type/data schema`
- Formal status hint: `type/data schema`

## Registry Links

- `IV.D256` — Lemniscate boundary --- physical reading

## Immediate Comment / Docstring

```lean
/-- [IV.D256] The lemniscate boundary L = S¹ ∨ S¹: algebraic lemniscate
    arising as the boundary of τ³. Two lobes (χ₊, χ₋) meeting at the
    crossing point ω. -/
```

## Source Excerpt

```lean
structure LemniscateBoundary where
  /-- Number of lobes. -/
  lobe_count : Nat
  lobe_count_eq : lobe_count = 2
  /-- Has a crossing point (ω). -/
  has_crossing : Bool
  crossing_true : has_crossing = true
  deriving Repr
```

---
{
  "projection_kind": "taulib_declaration",
  "title": "L2Inner",
  "permalink": "/verify/taulib/docs/book-ii-hartogs-l2-space/l2-inner/",
  "summary_short": "`structure` declaration in `TauLib.BookII.Hartogs.L2Space`.",
  "declaration_id": "TauLib.BookII.Hartogs.L2Space::L2Inner",
  "declaration_slug": "l2-inner",
  "kind": "structure",
  "name": "L2Inner",
  "module_name": "TauLib.BookII.Hartogs.L2Space",
  "module_url": "/verify/taulib/docs/book-ii-hartogs-l2-space/",
  "source_line_start": 54,
  "source_line_end": 56,
  "registry_ids": [
    "II.D82"
  ],
  "related_registry_items": [
    {
      "id": "II.D82",
      "title": "L² Inner Product",
      "url": "/registry/object/II.D82/"
    }
  ],
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookII/Hartogs/L2Space.lean#L54-L56",
  "formal_status": "defined",
  "right_rail": {
    "related": [
      {
        "title": "TauLib.BookII.Hartogs.L2Space",
        "url": "/verify/taulib/docs/book-ii-hartogs-l2-space/"
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookII/Hartogs/L2Space.lean#L54-L56",
        "external": true
      }
    ],
    "meta": {
      "type": "TauLib Declaration",
      "kind": "structure",
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

- Module: [TauLib.BookII.Hartogs.L2Space](/verify/taulib/docs/book-ii-hartogs-l2-space/)
- Source path: [`TauLib/BookII/Hartogs/L2Space.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookII/Hartogs/L2Space.lean#L54-L56)
- Source range: L54-L56
- Kind: `structure`
- Formal status hint: `defined`

## Registry Links

- `II.D82` — L² Inner Product

## Immediate Comment / Docstring

```lean
/-- [II.D82] L² inner product as rational pair: ⟨f,g⟩_k = (Σ f·g, M_k). -/
```

## Source Excerpt

```lean
structure L2Inner where
  numerator : Int
  denominator : Nat
```

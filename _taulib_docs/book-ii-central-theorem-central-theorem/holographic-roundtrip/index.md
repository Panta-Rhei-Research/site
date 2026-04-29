---
{
  "projection_kind": "taulib_declaration",
  "title": "holographic_roundtrip",
  "permalink": "/verify/taulib/docs/book-ii-central-theorem-central-theorem/holographic-roundtrip/",
  "summary_short": "`theorem` declaration in `TauLib.BookII.CentralTheorem.CentralTheorem`.",
  "declaration_id": "TauLib.BookII.CentralTheorem.CentralTheorem::holographic_roundtrip",
  "declaration_slug": "holographic-roundtrip",
  "kind": "theorem",
  "name": "holographic_roundtrip",
  "module_name": "TauLib.BookII.CentralTheorem.CentralTheorem",
  "module_url": "/verify/taulib/docs/book-ii-central-theorem-central-theorem/",
  "source_line_start": 449,
  "source_line_end": 454,
  "registry_ids": [
    "II.C01"
  ],
  "related_registry_items": [
    {
      "id": "II.C01",
      "title": "Holographic Principle",
      "url": "/registry/object/II.C01/"
    }
  ],
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookII/CentralTheorem/CentralTheorem.lean#L449-L454",
  "formal_status": "formalized",
  "right_rail": {
    "related": [
      {
        "title": "TauLib.BookII.CentralTheorem.CentralTheorem",
        "url": "/verify/taulib/docs/book-ii-central-theorem-central-theorem/"
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookII/CentralTheorem/CentralTheorem.lean#L449-L454",
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

- Module: [TauLib.BookII.CentralTheorem.CentralTheorem](/verify/taulib/docs/book-ii-central-theorem-central-theorem/)
- Source path: [`TauLib/BookII/CentralTheorem/CentralTheorem.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookII/CentralTheorem/CentralTheorem.lean#L449-L454)
- Source range: L449-L454
- Kind: `theorem`
- Formal status hint: `formalized`

## Registry Links

- `II.C01` — Holographic Principle

## Immediate Comment / Docstring

```lean
/-- [II.C01] Holographic principle: boundary reduction is involutive.
    reduce(bndlift(x, k), k) = reduce(x, k).
    The boundary completely determines the interior. -/
```

## Source Excerpt

```lean
theorem holographic_roundtrip (x k : TauIdx) :
    reduce (bndlift x k) k = reduce x k := by
  simp [bndlift]
  exact reduction_compat x (Nat.le_succ k)

end Tau.BookII.CentralTheorem
```

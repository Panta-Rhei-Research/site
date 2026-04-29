---
{
  "projection_kind": "taulib_declaration",
  "title": "e3_density_check",
  "permalink": "/verify/taulib/docs/book-iii-mirror-e3-witness/e3-density-check/",
  "summary_short": "`def` declaration in `TauLib.BookIII.Mirror.E3Witness`.",
  "declaration_id": "TauLib.BookIII.Mirror.E3Witness::e3_density_check",
  "declaration_slug": "e3-density-check",
  "kind": "def",
  "name": "e3_density_check",
  "module_name": "TauLib.BookIII.Mirror.E3Witness",
  "module_url": "/verify/taulib/docs/book-iii-mirror-e3-witness/",
  "source_line_start": 94,
  "source_line_end": 99,
  "registry_ids": [
    "III.D85"
  ],
  "related_registry_items": [
    {
      "id": "III.D85",
      "title": "Self-Referential Fixed Point",
      "url": "/registry/object/III.D85/"
    }
  ],
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIII/Mirror/E3Witness.lean#L94-L99",
  "formal_status": "defined",
  "right_rail": {
    "related": [
      {
        "title": "TauLib.BookIII.Mirror.E3Witness",
        "url": "/verify/taulib/docs/book-iii-mirror-e3-witness/"
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIII/Mirror/E3Witness.lean#L94-L99",
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

- Module: [TauLib.BookIII.Mirror.E3Witness](/verify/taulib/docs/book-iii-mirror-e3-witness/)
- Source path: [`TauLib/BookIII/Mirror/E3Witness.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIII/Mirror/E3Witness.lean#L94-L99)
- Source range: L94-L99
- Kind: `def`
- Formal status hint: `defined`

## Registry Links

- `III.D85` — Self-Referential Fixed Point

## Immediate Comment / Docstring

```lean
/-- [III.D85] Fixed point density: ratio of E₃ elements to total. -/
```

## Source Excerpt

```lean
def e3_density_check (k : Nat) : Bool :=
  let pk := primorial k
  let fp := count_e3_fixed_points k
  -- At each stage, ALL elements satisfy E₃ predicate
  -- (because reduce is idempotent on elements < M_k)
  fp == pk
```

---
{
  "projection_kind": "taulib_declaration",
  "title": "is_tau_admissible",
  "permalink": "/verify/taulib/docs/book-ii-interior-tau-admissible/is-tau-admissible/",
  "summary_short": "`def` declaration in `TauLib.BookII.Interior.TauAdmissible`.",
  "declaration_id": "TauLib.BookII.Interior.TauAdmissible::is_tau_admissible",
  "declaration_slug": "is-tau-admissible",
  "kind": "def",
  "name": "is_tau_admissible",
  "module_name": "TauLib.BookII.Interior.TauAdmissible",
  "module_url": "/verify/taulib/docs/book-ii-interior-tau-admissible/",
  "source_line_start": 76,
  "source_line_end": 77,
  "registry_ids": [
    "II.D03"
  ],
  "related_registry_items": [
    {
      "id": "II.D03",
      "title": "Constraint Lattice",
      "url": "/registry/object/II.D03/"
    }
  ],
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookII/Interior/TauAdmissible.lean#L76-L77",
  "formal_status": "defined",
  "right_rail": {
    "related": [
      {
        "title": "TauLib.BookII.Interior.TauAdmissible",
        "url": "/verify/taulib/docs/book-ii-interior-tau-admissible/"
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookII/Interior/TauAdmissible.lean#L76-L77",
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

- Module: [TauLib.BookII.Interior.TauAdmissible](/verify/taulib/docs/book-ii-interior-tau-admissible/)
- Source path: [`TauLib/BookII/Interior/TauAdmissible.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookII/Interior/TauAdmissible.lean#L76-L77)
- Source range: L76-L77
- Kind: `def`
- Formal status hint: `defined`

## Registry Links

- `II.D03` — Constraint Lattice

## Immediate Comment / Docstring

```lean
/-- [II.D03] Full constraint lattice check for a candidate (A, B, C, D). -/
```

## Source Excerpt

```lean
def is_tau_admissible (a b c d : TauIdx) : Bool :=
  constraint_C1 a && constraint_C3 d a && constraint_C4 a b c && constraint_C5 a b c d
```

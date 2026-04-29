---
{
  "projection_kind": "taulib_declaration",
  "title": "remark_noether_corollary",
  "permalink": "/verify/taulib/docs/book-iv-coda-laws-as-structure/remark-noether-corollary/",
  "summary_short": "`def` declaration in `TauLib.BookIV.Coda.LawsAsStructure`.",
  "declaration_id": "TauLib.BookIV.Coda.LawsAsStructure::remark_noether_corollary",
  "declaration_slug": "remark-noether-corollary",
  "kind": "def",
  "name": "remark_noether_corollary",
  "module_name": "TauLib.BookIV.Coda.LawsAsStructure",
  "module_url": "/verify/taulib/docs/book-iv-coda-laws-as-structure/",
  "source_line_start": 97,
  "source_line_end": 99,
  "registry_ids": [
    "IV.R180"
  ],
  "related_registry_items": [
    {
      "id": "IV.R180",
      "title": "Noether theorem as corollary",
      "url": "/registry/object/IV.R180/"
    }
  ],
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIV/Coda/LawsAsStructure.lean#L97-L99",
  "formal_status": "defined",
  "right_rail": {
    "related": [
      {
        "title": "TauLib.BookIV.Coda.LawsAsStructure",
        "url": "/verify/taulib/docs/book-iv-coda-laws-as-structure/"
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIV/Coda/LawsAsStructure.lean#L97-L99",
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

- Module: [TauLib.BookIV.Coda.LawsAsStructure](/verify/taulib/docs/book-iv-coda-laws-as-structure/)
- Source path: [`TauLib/BookIV/Coda/LawsAsStructure.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIV/Coda/LawsAsStructure.lean#L97-L99)
- Source range: L97-L99
- Kind: `def`
- Formal status hint: `defined`

## Registry Links

- `IV.R180` — Noether theorem as corollary

## Immediate Comment / Docstring

```lean
/-- [IV.R180] In Category tau, Noether's theorem is a corollary of the
    categorical structure:
    1. The structure determines which natural transformations exist.
    2. Each automatically satisfies naturality (commutation with tower).
    3. Naturality implies the conserved quantity.

    This inverts the orthodox logic: instead of "symmetry implies conservation",
    we have "structural architecture determines both symmetries and
    conservation laws simultaneously". -/
```

## Source Excerpt

```lean
def remark_noether_corollary : String :=
  "Noether's theorem is a corollary: tower-naturality implies both " ++
  "the symmetry and the conserved quantity simultaneously"
```

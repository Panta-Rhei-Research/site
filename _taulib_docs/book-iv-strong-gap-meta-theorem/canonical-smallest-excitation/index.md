---
{
  "projection_kind": "taulib_declaration",
  "title": "CanonicalSmallestExcitation",
  "permalink": "/verify/taulib/docs/book-iv-strong-gap-meta-theorem/canonical-smallest-excitation/",
  "summary_short": "`structure` declaration in `TauLib.BookIV.Strong.GapMetaTheorem`.",
  "declaration_id": "TauLib.BookIV.Strong.GapMetaTheorem::CanonicalSmallestExcitation",
  "declaration_slug": "canonical-smallest-excitation",
  "kind": "structure",
  "name": "CanonicalSmallestExcitation",
  "module_name": "TauLib.BookIV.Strong.GapMetaTheorem",
  "module_url": "/verify/taulib/docs/book-iv-strong-gap-meta-theorem/",
  "source_line_start": 158,
  "source_line_end": 165,
  "registry_ids": [
    "IV.D167"
  ],
  "related_registry_items": [
    {
      "id": "IV.D167",
      "title": "Canonical smallest excitation",
      "url": "/registry/object/IV.D167/"
    }
  ],
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIV/Strong/GapMetaTheorem.lean#L158-L165",
  "formal_status": "defined",
  "right_rail": {
    "related": [
      {
        "title": "TauLib.BookIV.Strong.GapMetaTheorem",
        "url": "/verify/taulib/docs/book-iv-strong-gap-meta-theorem/"
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIV/Strong/GapMetaTheorem.lean#L158-L165",
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

- Module: [TauLib.BookIV.Strong.GapMetaTheorem](/verify/taulib/docs/book-iv-strong-gap-meta-theorem/)
- Source path: [`TauLib/BookIV/Strong/GapMetaTheorem.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIV/Strong/GapMetaTheorem.lean#L158-L165)
- Source range: L158-L165
- Kind: `structure`
- Formal status hint: `defined`

## Registry Links

- `IV.D167` — Canonical smallest excitation

## Immediate Comment / Docstring

```lean
/-- [IV.D167] h_n := lexicographic argmin of (lambda_n(p), code_n(p))
    over P_n(U)\{0}. The lightest possible excitation above vacuum. -/
```

## Source Excerpt

```lean
structure CanonicalSmallestExcitation where
  /-- Stage n. -/
  stage : Nat
  /-- Argmin over nontrivial perturbations. -/
  is_argmin : Bool := true
  /-- With NF code tie-breaking. -/
  nf_tiebreak : Bool := true
  deriving Repr
```

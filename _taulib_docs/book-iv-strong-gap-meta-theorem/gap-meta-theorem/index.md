---
{
  "projection_kind": "taulib_declaration",
  "title": "GapMetaTheorem",
  "permalink": "/verify/taulib/docs/book-iv-strong-gap-meta-theorem/gap-meta-theorem/",
  "summary_short": "`structure` declaration in `TauLib.BookIV.Strong.GapMetaTheorem`.",
  "declaration_id": "TauLib.BookIV.Strong.GapMetaTheorem::GapMetaTheorem",
  "declaration_slug": "gap-meta-theorem",
  "kind": "structure",
  "name": "GapMetaTheorem",
  "module_name": "TauLib.BookIV.Strong.GapMetaTheorem",
  "module_url": "/verify/taulib/docs/book-iv-strong-gap-meta-theorem/",
  "source_line_start": 209,
  "source_line_end": 218,
  "registry_ids": [
    "IV.T73"
  ],
  "related_registry_items": [
    {
      "id": "IV.T73",
      "title": "τ-Gap Meta-Theorem (III.T26)",
      "url": "/registry/object/IV.T73/"
    }
  ],
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIV/Strong/GapMetaTheorem.lean#L209-L218",
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIV/Strong/GapMetaTheorem.lean#L209-L218",
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
- Source path: [`TauLib/BookIV/Strong/GapMetaTheorem.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIV/Strong/GapMetaTheorem.lean#L209-L218)
- Source range: L209-L218
- Kind: `structure`
- Formal status hint: `defined`

## Registry Links

- `IV.T73` — τ-Gap Meta-Theorem (III.T26)

## Immediate Comment / Docstring

```lean
/-- [IV.T73] tau-Gap Meta-Theorem: for any tau-holonomy sector satisfying
    (KH-1)-(KH-3):
    1. The omega-vacuum exists (by projective limit + KH-1)
    2. The omega-gap quantum exists (by projective limit + KH-2)
    3. The spectral gap delta_infinity > 0 (by KH-3 + monotonicity)

    This instantiates III.T26 from Book III at the E1 physics level. -/
```

## Source Excerpt

```lean
structure GapMetaTheorem where
  /-- Omega-vacuum exists. -/
  vacuum_exists : Bool := true
  /-- Omega-gap quantum exists. -/
  gap_quantum_exists : Bool := true
  /-- Spectral gap is strictly positive. -/
  gap_positive : Bool := true
  /-- Source: III.T26. -/
  source : String := "instantiation of III.T26"
  deriving Repr
```

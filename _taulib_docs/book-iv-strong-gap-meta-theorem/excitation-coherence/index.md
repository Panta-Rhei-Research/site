---
{
  "projection_kind": "taulib_declaration",
  "title": "ExcitationCoherence",
  "permalink": "/verify/taulib/docs/book-iv-strong-gap-meta-theorem/excitation-coherence/",
  "summary_short": "`structure` declaration in `TauLib.BookIV.Strong.GapMetaTheorem`.",
  "declaration_id": "TauLib.BookIV.Strong.GapMetaTheorem::ExcitationCoherence",
  "declaration_slug": "excitation-coherence",
  "kind": "structure",
  "name": "ExcitationCoherence",
  "module_name": "TauLib.BookIV.Strong.GapMetaTheorem",
  "module_url": "/verify/taulib/docs/book-iv-strong-gap-meta-theorem/",
  "source_line_start": 260,
  "source_line_end": 265,
  "registry_ids": [
    "IV.L12"
  ],
  "related_registry_items": [
    {
      "id": "IV.L12",
      "title": "Excitation coherence",
      "url": "/registry/object/IV.L12/"
    }
  ],
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIV/Strong/GapMetaTheorem.lean#L260-L265",
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIV/Strong/GapMetaTheorem.lean#L260-L265",
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
- Source path: [`TauLib/BookIV/Strong/GapMetaTheorem.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIV/Strong/GapMetaTheorem.lean#L260-L265)
- Source range: L260-L265
- Kind: `structure`
- Formal status hint: `defined`

## Registry Links

- `IV.L12` — Excitation coherence

## Immediate Comment / Docstring

```lean
/-- [IV.L12] Excitation coherence: rho(h_{n+1}) = h_n for n >= n_*. -/
```

## Source Excerpt

```lean
structure ExcitationCoherence where
  /-- Restriction preserves excitation. -/
  restriction_preserves : Bool := true
  /-- Follows from KH-2 (monotonicity) + surjectivity. -/
  mechanism : String := "KH-2 monotonicity + surjectivity of restriction"
  deriving Repr
```

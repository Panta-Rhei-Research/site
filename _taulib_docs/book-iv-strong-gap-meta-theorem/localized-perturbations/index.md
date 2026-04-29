---
{
  "projection_kind": "taulib_declaration",
  "title": "LocalizedPerturbations",
  "permalink": "/verify/taulib/docs/book-iv-strong-gap-meta-theorem/localized-perturbations/",
  "summary_short": "`structure` declaration in `TauLib.BookIV.Strong.GapMetaTheorem`.",
  "declaration_id": "TauLib.BookIV.Strong.GapMetaTheorem::LocalizedPerturbations",
  "declaration_slug": "localized-perturbations",
  "kind": "structure",
  "name": "LocalizedPerturbations",
  "module_name": "TauLib.BookIV.Strong.GapMetaTheorem",
  "module_url": "/verify/taulib/docs/book-iv-strong-gap-meta-theorem/",
  "source_line_start": 112,
  "source_line_end": 119,
  "registry_ids": [
    "IV.D164"
  ],
  "related_registry_items": [
    {
      "id": "IV.D164",
      "title": "Localized perturbations",
      "url": "/registry/object/IV.D164/"
    }
  ],
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIV/Strong/GapMetaTheorem.lean#L112-L119",
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIV/Strong/GapMetaTheorem.lean#L112-L119",
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
- Source path: [`TauLib/BookIV/Strong/GapMetaTheorem.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIV/Strong/GapMetaTheorem.lean#L112-L119)
- Source range: L112-L119
- Kind: `structure`
- Formal status hint: `defined`

## Registry Links

- `IV.D164` — Localized perturbations

## Immediate Comment / Docstring

```lean
/-- [IV.D164] Localized perturbation set P_n(U): admissible perturbations
    supported within a region U subset T^2, such that Omega_n^* + p
    remains admissible. -/
```

## Source Excerpt

```lean
structure LocalizedPerturbations where
  /-- Stage n. -/
  stage : Nat
  /-- Perturbations are localized in a region U. -/
  localized : Bool := true
  /-- Superposition with vacuum remains admissible. -/
  admissible_superposition : Bool := true
  deriving Repr
```

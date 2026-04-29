---
{
  "projection_kind": "taulib_declaration",
  "title": "refine_spectral_check",
  "permalink": "/verify/taulib/docs/book-ii-hartogs-mutual-determination/refine-spectral-check/",
  "summary_short": "`def` declaration in `TauLib.BookII.Hartogs.MutualDetermination`.",
  "declaration_id": "TauLib.BookII.Hartogs.MutualDetermination::refine_spectral_check",
  "declaration_slug": "refine-spectral-check",
  "kind": "def",
  "name": "refine_spectral_check",
  "module_name": "TauLib.BookII.Hartogs.MutualDetermination",
  "module_url": "/verify/taulib/docs/book-ii-hartogs-mutual-determination/",
  "source_line_start": 210,
  "source_line_end": 211,
  "registry_ids": [
    "II.L02"
  ],
  "related_registry_items": [
    {
      "id": "II.L02",
      "title": "Refinement-Spectral Equivalence",
      "url": "/registry/object/II.L02/"
    }
  ],
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookII/Hartogs/MutualDetermination.lean#L210-L211",
  "formal_status": "defined",
  "right_rail": {
    "related": [
      {
        "title": "TauLib.BookII.Hartogs.MutualDetermination",
        "url": "/verify/taulib/docs/book-ii-hartogs-mutual-determination/"
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookII/Hartogs/MutualDetermination.lean#L210-L211",
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

- Module: [TauLib.BookII.Hartogs.MutualDetermination](/verify/taulib/docs/book-ii-hartogs-mutual-determination/)
- Source path: [`TauLib/BookII/Hartogs/MutualDetermination.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookII/Hartogs/MutualDetermination.lean#L210-L211)
- Source range: L210-L211
- Kind: `def`
- Formal status hint: `defined`

## Registry Links

- `II.L02` — Refinement-Spectral Equivalence

## Immediate Comment / Docstring

```lean
/-- [II.L02] Refinement <-> Spectral:
    Refinement coherence implies spectral stability and vice versa.
    The tower coherence condition reduce(f_{k+1}, k) = f_k ensures
    that the spectral (B, C) components at stage k are determined by
    those at stage k+1. -/
```

## Source Excerpt

```lean
def refine_spectral_check (bound db : TauIdx) : Bool :=
  refinement_tail_check bound db && spectral_tail_check bound db
```

---
{
  "projection_kind": "taulib_declaration",
  "title": "SpectralTightening",
  "permalink": "/verify/taulib/docs/book-iv-strong-strong-vacuum/spectral-tightening/",
  "summary_short": "`structure` declaration in `TauLib.BookIV.Strong.StrongVacuum`.",
  "declaration_id": "TauLib.BookIV.Strong.StrongVacuum::SpectralTightening",
  "declaration_slug": "spectral-tightening",
  "kind": "structure",
  "name": "SpectralTightening",
  "module_name": "TauLib.BookIV.Strong.StrongVacuum",
  "module_url": "/verify/taulib/docs/book-iv-strong-strong-vacuum/",
  "source_line_start": 95,
  "source_line_end": 102,
  "registry_ids": [
    "IV.P80"
  ],
  "related_registry_items": [
    {
      "id": "IV.P80",
      "title": "Spectral tightening in the C-sector",
      "url": "/registry/object/IV.P80/"
    }
  ],
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIV/Strong/StrongVacuum.lean#L95-L102",
  "formal_status": "defined",
  "right_rail": {
    "related": [
      {
        "title": "TauLib.BookIV.Strong.StrongVacuum",
        "url": "/verify/taulib/docs/book-iv-strong-strong-vacuum/"
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIV/Strong/StrongVacuum.lean#L95-L102",
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

- Module: [TauLib.BookIV.Strong.StrongVacuum](/verify/taulib/docs/book-iv-strong-strong-vacuum/)
- Source path: [`TauLib/BookIV/Strong/StrongVacuum.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIV/Strong/StrongVacuum.lean#L95-L102)
- Source range: L95-L102
- Kind: `structure`
- Formal status hint: `defined`

## Registry Links

- `IV.P80` — Spectral tightening in the C-sector

## Immediate Comment / Docstring

```lean
/-- [IV.P80] Spectral tightening in the C-sector: under refinement rho,
    the support of chi_minus-dominant characters shrinks strictly
    Supp_{n+1}(chi_minus) subset Supp_n(chi_minus) beyond depth d=3.

    This is the structural mechanism that drives confinement:
    as refinement proceeds, fewer modes survive chi_minus dominance. -/
```

## Source Excerpt

```lean
structure SpectralTightening where
  /-- Activation depth beyond which tightening occurs. -/
  activation_depth : Nat := 3
  /-- Support is strictly decreasing. -/
  strict_decrease : Bool := true
  /-- Tightening is inherited from chi_minus dominance. -/
  mechanism : String := "chi_minus-dominant character support shrinks under rho"
  deriving Repr
```

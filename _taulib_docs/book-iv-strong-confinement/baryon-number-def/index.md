---
{
  "projection_kind": "taulib_declaration",
  "title": "BaryonNumberDef",
  "permalink": "/verify/taulib/docs/book-iv-strong-confinement/baryon-number-def/",
  "summary_short": "`structure` declaration in `TauLib.BookIV.Strong.Confinement`.",
  "declaration_id": "TauLib.BookIV.Strong.Confinement::BaryonNumberDef",
  "declaration_slug": "baryon-number-def",
  "kind": "structure",
  "name": "BaryonNumberDef",
  "module_name": "TauLib.BookIV.Strong.Confinement",
  "module_url": "/verify/taulib/docs/book-iv-strong-confinement/",
  "source_line_start": 215,
  "source_line_end": 220,
  "registry_ids": [
    "IV.D161"
  ],
  "related_registry_items": [
    {
      "id": "IV.D161",
      "title": "Baryon number",
      "url": "/registry/object/IV.D161/"
    }
  ],
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIV/Strong/Confinement.lean#L215-L220",
  "formal_status": "defined",
  "right_rail": {
    "related": [
      {
        "title": "TauLib.BookIV.Strong.Confinement",
        "url": "/verify/taulib/docs/book-iv-strong-confinement/"
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIV/Strong/Confinement.lean#L215-L220",
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

- Module: [TauLib.BookIV.Strong.Confinement](/verify/taulib/docs/book-iv-strong-confinement/)
- Source path: [`TauLib/BookIV/Strong/Confinement.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIV/Strong/Confinement.lean#L215-L220)
- Source range: L215-L220
- Kind: `structure`
- Formal status hint: `defined`

## Registry Links

- `IV.D161` — Baryon number

## Immediate Comment / Docstring

```lean
/-- [IV.D161] Baryon number B(Psi) := (1/3) * sum_j n_j,
    where n_j is the eta-winding of constituent psi_j.
    For a baryon with {c1,c2,c3} = {0,1,2}: B = (0+1+2)/3 = 1. -/
```

## Source Excerpt

```lean
structure BaryonNumberDef where
  /-- Sum of windings. -/
  winding_sum : Nat
  /-- Baryon number = winding_sum / 3 (integer for singlets). -/
  baryon_number : Nat
  deriving Repr
```

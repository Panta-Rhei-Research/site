---
{
  "projection_kind": "taulib_declaration",
  "title": "full_laurent_residue_check",
  "permalink": "/verify/taulib/docs/book-ii-hartogs-laurent-residue/full-laurent-residue-check/",
  "summary_short": "`def` declaration in `TauLib.BookII.Hartogs.LaurentResidue`.",
  "declaration_id": "TauLib.BookII.Hartogs.LaurentResidue::full_laurent_residue_check",
  "declaration_slug": "full-laurent-residue-check",
  "kind": "def",
  "name": "full_laurent_residue_check",
  "module_name": "TauLib.BookII.Hartogs.LaurentResidue",
  "module_url": "/verify/taulib/docs/book-ii-hartogs-laurent-residue/",
  "source_line_start": 394,
  "source_line_end": 402,
  "registry_ids": [],
  "related_registry_items": [],
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookII/Hartogs/LaurentResidue.lean#L394-L402",
  "formal_status": "defined",
  "right_rail": {
    "related": [
      {
        "title": "TauLib.BookII.Hartogs.LaurentResidue",
        "url": "/verify/taulib/docs/book-ii-hartogs-laurent-residue/"
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookII/Hartogs/LaurentResidue.lean#L394-L402",
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

- Module: [TauLib.BookII.Hartogs.LaurentResidue](/verify/taulib/docs/book-ii-hartogs-laurent-residue/)
- Source path: [`TauLib/BookII/Hartogs/LaurentResidue.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookII/Hartogs/LaurentResidue.lean#L394-L402)
- Source range: L394-L402
- Kind: `def`
- Formal status hint: `defined`

## Registry Links

- No Registry IDs were detected in this declaration block.

## Immediate Comment / Docstring

```lean
/-- Complete Laurent-Residue verification:
    1. Laurent expansion well-defined and stable
    2. Residues determine points (CRT uniqueness)
    3. CRT reconstruction round-trip
    4. Residue theorem (reconstruction = original)
    5. Meromorphic structure
    6. Residue-evolution compatibility -/
```

## Source Excerpt

```lean
def full_laurent_residue_check (bound db : TauIdx) : Bool :=
  laurent_range_check bound db &&
  laurent_stability_check bound db &&
  residue_stage_independence_check bound db &&
  residue_determines_check bound db &&
  crt_roundtrip_check db &&
  residue_reconstruction_check bound db &&
  hol_is_mero_check bound db &&
  residue_evolution_check bound db
```

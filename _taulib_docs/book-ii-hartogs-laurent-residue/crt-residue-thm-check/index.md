---
{
  "projection_kind": "taulib_declaration",
  "title": "crt_residue_thm_check",
  "permalink": "/verify/taulib/docs/book-ii-hartogs-laurent-residue/crt-residue-thm-check/",
  "summary_short": "`def` declaration in `TauLib.BookII.Hartogs.LaurentResidue`.",
  "declaration_id": "TauLib.BookII.Hartogs.LaurentResidue::crt_residue_thm_check",
  "declaration_slug": "crt-residue-thm-check",
  "kind": "def",
  "name": "crt_residue_thm_check",
  "module_name": "TauLib.BookII.Hartogs.LaurentResidue",
  "module_url": "/verify/taulib/docs/book-ii-hartogs-laurent-residue/",
  "source_line_start": 260,
  "source_line_end": 262,
  "registry_ids": [
    "II.T30"
  ],
  "related_registry_items": [
    {
      "id": "II.T30",
      "title": "Residue Theorem",
      "url": "/registry/object/II.T30/"
    }
  ],
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookII/Hartogs/LaurentResidue.lean#L260-L262",
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookII/Hartogs/LaurentResidue.lean#L260-L262",
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
- Source path: [`TauLib/BookII/Hartogs/LaurentResidue.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookII/Hartogs/LaurentResidue.lean#L260-L262)
- Source range: L260-L262
- Kind: `def`
- Formal status hint: `defined`

## Registry Links

- `II.T30` — Residue Theorem

## Immediate Comment / Docstring

```lean
/-- [II.T30] Formal residue theorem for a specific stage:
    CRT reconstruction from Laurent coefficients at stage k
    is the identity on [0, M_k).

    Verified computationally for stages 1-3 (M_1=2, M_2=6, M_3=30). -/
```

## Source Excerpt

```lean
def crt_residue_thm_check (db : TauIdx) : Bool :=
  crt_roundtrip_check db &&
  residue_reconstruction_check (primorial db) db
```

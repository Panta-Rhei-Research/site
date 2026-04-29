---
{
  "projection_kind": "taulib_declaration",
  "title": "WindingPreservation",
  "permalink": "/verify/taulib/docs/book-iv-strong-confinement/winding-preservation/",
  "summary_short": "`structure` declaration in `TauLib.BookIV.Strong.Confinement`.",
  "declaration_id": "TauLib.BookIV.Strong.Confinement::WindingPreservation",
  "declaration_slug": "winding-preservation",
  "kind": "structure",
  "name": "WindingPreservation",
  "module_name": "TauLib.BookIV.Strong.Confinement",
  "module_url": "/verify/taulib/docs/book-iv-strong-confinement/",
  "source_line_start": 241,
  "source_line_end": 248,
  "registry_ids": [
    "IV.L8"
  ],
  "related_registry_items": [
    {
      "id": "IV.L8",
      "title": "Winding Preservation",
      "url": "/registry/object/IV.L8/"
    }
  ],
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIV/Strong/Confinement.lean#L241-L248",
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIV/Strong/Confinement.lean#L241-L248",
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
- Source path: [`TauLib/BookIV/Strong/Confinement.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIV/Strong/Confinement.lean#L241-L248)
- Source range: L241-L248
- Kind: `structure`
- Formal status hint: `defined`

## Registry Links

- `IV.L8` — Winding Preservation

## Immediate Comment / Docstring

```lean
/-- [IV.L8] Winding Preservation: any admissible endomorphism phi
    compatible with the C-sector preserves total eta-winding mod 3,
    ensuring baryon number conservation under all physical processes. -/
```

## Source Excerpt

```lean
structure WindingPreservation where
  /-- Admissible endomorphisms preserve winding mod 3. -/
  preserves_mod3 : Bool := true
  /-- Consequence: baryon number is conserved. -/
  baryon_conserved : Bool := true
  /-- Mechanism: admissibility condition (SA-i) forces eta-sector preservation. -/
  mechanism : String := "SA-i forces eta-sector chi_minus preservation"
  deriving Repr
```

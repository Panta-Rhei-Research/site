---
{
  "projection_kind": "taulib_declaration",
  "title": "SingletStability",
  "permalink": "/verify/taulib/docs/book-iv-strong-confinement/singlet-stability/",
  "summary_short": "`structure` declaration in `TauLib.BookIV.Strong.Confinement`.",
  "declaration_id": "TauLib.BookIV.Strong.Confinement::SingletStability",
  "declaration_slug": "singlet-stability",
  "kind": "structure",
  "name": "SingletStability",
  "module_name": "TauLib.BookIV.Strong.Confinement",
  "module_url": "/verify/taulib/docs/book-iv-strong-confinement/",
  "source_line_start": 134,
  "source_line_end": 141,
  "registry_ids": [
    "IV.P94"
  ],
  "related_registry_items": [
    {
      "id": "IV.P94",
      "title": "Singlet Stability",
      "url": "/registry/object/IV.P94/"
    }
  ],
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIV/Strong/Confinement.lean#L134-L141",
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIV/Strong/Confinement.lean#L134-L141",
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
- Source path: [`TauLib/BookIV/Strong/Confinement.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIV/Strong/Confinement.lean#L134-L141)
- Source range: L134-L141
- Kind: `structure`
- Formal status hint: `defined`

## Registry Links

- `IV.P94` — Singlet Stability

## Immediate Comment / Docstring

```lean
/-- [IV.P94] A color singlet resolves to a stable boundary character:
    the fractional eta-phases cancel exactly, so the composite boundary
    character sequence converges in H_partial[omega]. -/
```

## Source Excerpt

```lean
structure SingletStability where
  /-- Fractional phases cancel. -/
  phases_cancel : Bool := true
  /-- Converges in profinite limit. -/
  converges : Bool := true
  /-- Stable boundary character on L. -/
  stable_on_L : Bool := true
  deriving Repr
```

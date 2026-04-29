---
{
  "projection_kind": "taulib_declaration",
  "title": "SingletClassification",
  "permalink": "/verify/taulib/docs/book-iv-strong-confinement/singlet-classification/",
  "summary_short": "`structure` declaration in `TauLib.BookIV.Strong.Confinement`.",
  "declaration_id": "TauLib.BookIV.Strong.Confinement::SingletClassification",
  "declaration_slug": "singlet-classification",
  "kind": "structure",
  "name": "SingletClassification",
  "module_name": "TauLib.BookIV.Strong.Confinement",
  "module_url": "/verify/taulib/docs/book-iv-strong-confinement/",
  "source_line_start": 164,
  "source_line_end": 171,
  "registry_ids": [
    "IV.P95"
  ],
  "related_registry_items": [
    {
      "id": "IV.P95",
      "title": "Singlet Classification",
      "url": "/registry/object/IV.P95/"
    }
  ],
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIV/Strong/Confinement.lean#L164-L171",
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIV/Strong/Confinement.lean#L164-L171",
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
- Source path: [`TauLib/BookIV/Strong/Confinement.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIV/Strong/Confinement.lean#L164-L171)
- Source range: L164-L171
- Kind: `structure`
- Formal status hint: `defined`

## Registry Links

- `IV.P95` — Singlet Classification

## Immediate Comment / Docstring

```lean
/-- [IV.P95] Every persistent hadronic state is a color singlet.
    Minimal singlet structures:
    - Baryon: {0,1,2} (three quarks, one per color)
    - Meson: {c, bar{c}} (quark-antiquark)
    - Exotic: {c1,c2,bar{c3},bar{c4}} etc. with total 0 mod 3 -/
```

## Source Excerpt

```lean
structure SingletClassification where
  /-- All hadrons are singlets. -/
  all_hadrons_singlets : Bool := true
  /-- Minimal baryonic singlet size. -/
  min_baryon_size : Nat := 3
  /-- Minimal mesonic singlet size. -/
  min_meson_size : Nat := 2
  deriving Repr
```

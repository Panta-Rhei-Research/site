---
{
  "projection_kind": "taulib_declaration",
  "title": "ColorSingletDef",
  "permalink": "/verify/taulib/docs/book-iv-strong-confinement/color-singlet-def/",
  "summary_short": "`structure` declaration in `TauLib.BookIV.Strong.Confinement`.",
  "declaration_id": "TauLib.BookIV.Strong.Confinement::ColorSingletDef",
  "declaration_slug": "color-singlet-def",
  "kind": "structure",
  "name": "ColorSingletDef",
  "module_name": "TauLib.BookIV.Strong.Confinement",
  "module_url": "/verify/taulib/docs/book-iv-strong-confinement/",
  "source_line_start": 120,
  "source_line_end": 125,
  "registry_ids": [
    "IV.D160"
  ],
  "related_registry_items": [
    {
      "id": "IV.D160",
      "title": "Color singlet",
      "url": "/registry/object/IV.D160/"
    }
  ],
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIV/Strong/Confinement.lean#L120-L125",
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIV/Strong/Confinement.lean#L120-L125",
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
- Source path: [`TauLib/BookIV/Strong/Confinement.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIV/Strong/Confinement.lean#L120-L125)
- Source range: L120-L125
- Kind: `structure`
- Formal status hint: `defined`

## Registry Links

- `IV.D160` — Color singlet

## Immediate Comment / Docstring

```lean
/-- [IV.D160] Color singlet: composite state with trivial total
    eta-holonomy, hol_eta(Psi) = 1, i.e., sum c_j equiv 0 mod 3. -/
```

## Source Excerpt

```lean
structure ColorSingletDef where
  /-- Total winding sum mod 3 = 0. -/
  total_mod3 : Nat := 0
  /-- Trivial total holonomy. -/
  trivial_holonomy : Bool := true
  deriving Repr
```

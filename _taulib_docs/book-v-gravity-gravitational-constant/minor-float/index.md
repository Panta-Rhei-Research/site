---
{
  "projection_kind": "taulib_declaration",
  "title": "TorusVacuum.minorFloat",
  "permalink": "/verify/taulib/docs/book-v-gravity-gravitational-constant/minor-float/",
  "summary_short": "`def` declaration in `TauLib.BookV.Gravity.GravitationalConstant`.",
  "declaration_id": "TauLib.BookV.Gravity.GravitationalConstant::TorusVacuum.minorFloat",
  "declaration_slug": "minor-float",
  "kind": "def",
  "name": "TorusVacuum.minorFloat",
  "module_name": "TauLib.BookV.Gravity.GravitationalConstant",
  "module_url": "/verify/taulib/docs/book-v-gravity-gravitational-constant/",
  "source_line_start": 94,
  "source_line_end": 95,
  "registry_ids": [],
  "related_registry_items": [],
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookV/Gravity/GravitationalConstant.lean#L94-L95",
  "formal_status": "defined",
  "right_rail": {
    "related": [
      {
        "title": "TauLib.BookV.Gravity.GravitationalConstant",
        "url": "/verify/taulib/docs/book-v-gravity-gravitational-constant/"
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookV/Gravity/GravitationalConstant.lean#L94-L95",
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

- Module: [TauLib.BookV.Gravity.GravitationalConstant](/verify/taulib/docs/book-v-gravity-gravitational-constant/)
- Source path: [`TauLib/BookV/Gravity/GravitationalConstant.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookV/Gravity/GravitationalConstant.lean#L94-L95)
- Source range: L94-L95
- Kind: `def`
- Formal status hint: `defined`

## Registry Links

- No Registry IDs were detected in this declaration block.

## Immediate Comment / Docstring

```lean
/-- Minor radius as Float. -/
```

## Source Excerpt

```lean
def TorusVacuum.minorFloat (v : TorusVacuum) : Float :=
  Float.ofNat v.minor_numer / Float.ofNat v.minor_denom
```

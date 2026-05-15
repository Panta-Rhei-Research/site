---
{
  "projection_kind": "taulib_declaration",
  "title": "TauMHDSystem.magReynolds",
  "permalink": "/corpus/taulib/docs/book-v-fluid-macro-tau-mhd/mag-reynolds/",
  "summary_short": "`def` declaration in `TauLib.BookV.FluidMacro.TauMHD`.",
  "declaration_id": "TauLib.BookV.FluidMacro.TauMHD::TauMHDSystem.magReynolds",
  "declaration_slug": "mag-reynolds",
  "kind": "def",
  "name": "TauMHDSystem.magReynolds",
  "module_name": "TauLib.BookV.FluidMacro.TauMHD",
  "module_url": "/corpus/taulib/docs/book-v-fluid-macro-tau-mhd/",
  "source_line_start": 101,
  "source_line_end": 102,
  "registry_ids": [],
  "related_registry_items": [],
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookV/FluidMacro/TauMHD.lean#L101-L102",
  "formal_status": "defined",
  "declaration_role": "data/computed value",
  "formal_status_label": "data/computed value",
  "right_rail": {
    "related": [
      {
        "title": "TauLib.BookV.FluidMacro.TauMHD",
        "url": "/corpus/taulib/docs/book-v-fluid-macro-tau-mhd/"
      },
      {
        "title": "TauLib Projection Index",
        "url": "/corpus/taulib/docs/"
      },
      {
        "title": "Formalization Status",
        "url": "/verify/taulib/status/"
      }
    ],
    "artifacts": [
      {
        "title": "Source on GitHub",
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookV/FluidMacro/TauMHD.lean#L101-L102",
        "external": true
      }
    ],
    "meta": {
      "type": "TauLib Declaration",
      "kind": "def",
      "role": "data/computed value",
      "status": "data/computed value"
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

- Module: [TauLib.BookV.FluidMacro.TauMHD](/corpus/taulib/docs/book-v-fluid-macro-tau-mhd/)
- Source path: [`TauLib/BookV/FluidMacro/TauMHD.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookV/FluidMacro/TauMHD.lean#L101-L102)
- Source range: L101-L102
- Kind: `def`
- Public role: `data/computed value`
- Formal status hint: `data/computed value`

## Registry Links

- No Registry IDs were detected in this declaration block.

## Immediate Comment / Docstring

```lean
/-- Magnetic Reynolds number ratio. -/
```

## Source Excerpt

```lean
def TauMHDSystem.magReynolds (s : TauMHDSystem) : Nat :=
  s.mag_reynolds_numer / s.mag_reynolds_denom
```

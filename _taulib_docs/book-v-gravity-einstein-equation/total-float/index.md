---
{
  "projection_kind": "taulib_declaration",
  "title": "MatterCharacter.totalFloat",
  "permalink": "/verify/taulib/docs/book-v-gravity-einstein-equation/total-float/",
  "summary_short": "`def` declaration in `TauLib.BookV.Gravity.EinsteinEquation`.",
  "declaration_id": "TauLib.BookV.Gravity.EinsteinEquation::MatterCharacter.totalFloat",
  "declaration_slug": "total-float",
  "kind": "def",
  "name": "MatterCharacter.totalFloat",
  "module_name": "TauLib.BookV.Gravity.EinsteinEquation",
  "module_url": "/verify/taulib/docs/book-v-gravity-einstein-equation/",
  "source_line_start": 104,
  "source_line_end": 105,
  "registry_ids": [],
  "related_registry_items": [],
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookV/Gravity/EinsteinEquation.lean#L104-L105",
  "formal_status": "defined",
  "right_rail": {
    "related": [
      {
        "title": "TauLib.BookV.Gravity.EinsteinEquation",
        "url": "/verify/taulib/docs/book-v-gravity-einstein-equation/"
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookV/Gravity/EinsteinEquation.lean#L104-L105",
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

- Module: [TauLib.BookV.Gravity.EinsteinEquation](/verify/taulib/docs/book-v-gravity-einstein-equation/)
- Source path: [`TauLib/BookV/Gravity/EinsteinEquation.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookV/Gravity/EinsteinEquation.lean#L104-L105)
- Source range: L104-L105
- Kind: `def`
- Formal status hint: `defined`

## Registry Links

- No Registry IDs were detected in this declaration block.

## Immediate Comment / Docstring

```lean
/-- Matter character total as Float. -/
```

## Source Excerpt

```lean
def MatterCharacter.totalFloat (m : MatterCharacter) : Float :=
  Float.ofNat m.total_numer / Float.ofNat m.denom
```

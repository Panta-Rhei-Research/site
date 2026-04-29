---
{
  "projection_kind": "taulib_declaration",
  "title": "j_squared_check",
  "permalink": "/verify/taulib/docs/book-ii-transcendentals-jreplaces-i/j-squared-check/",
  "summary_short": "`def` declaration in `TauLib.BookII.Transcendentals.JReplacesI`.",
  "declaration_id": "TauLib.BookII.Transcendentals.JReplacesI::j_squared_check",
  "declaration_slug": "j-squared-check",
  "kind": "def",
  "name": "j_squared_check",
  "module_name": "TauLib.BookII.Transcendentals.JReplacesI",
  "module_url": "/verify/taulib/docs/book-ii-transcendentals-jreplaces-i/",
  "source_line_start": 44,
  "source_line_end": 45,
  "registry_ids": [],
  "related_registry_items": [],
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookII/Transcendentals/JReplacesI.lean#L44-L45",
  "formal_status": "defined",
  "right_rail": {
    "related": [
      {
        "title": "TauLib.BookII.Transcendentals.JReplacesI",
        "url": "/verify/taulib/docs/book-ii-transcendentals-jreplaces-i/"
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookII/Transcendentals/JReplacesI.lean#L44-L45",
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

- Module: [TauLib.BookII.Transcendentals.JReplacesI](/verify/taulib/docs/book-ii-transcendentals-jreplaces-i/)
- Source path: [`TauLib/BookII/Transcendentals/JReplacesI.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookII/Transcendentals/JReplacesI.lean#L44-L45)
- Source range: L44-L45
- Kind: `def`
- Formal status hint: `defined`

## Registry Links

- No Registry IDs were detected in this declaration block.

## Immediate Comment / Docstring

```lean
/-- j^2 = 1: the defining property. (0,1)*(0,1) = (0*0+1*1, 0*1+1*0) = (1,0). -/
```

## Source Excerpt

```lean
def j_squared_check : Bool :=
  SplitComplex.mul j_unit j_unit == ⟨1, 0⟩
```

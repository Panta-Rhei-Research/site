---
{
  "projection_kind": "taulib_declaration",
  "title": "iota_tau_float",
  "permalink": "/verify/taulib/docs/book-i-boundary-iota/iota-tau-float/",
  "summary_short": "`def` declaration in `TauLib.BookI.Boundary.Iota`.",
  "declaration_id": "TauLib.BookI.Boundary.Iota::iota_tau_float",
  "declaration_slug": "iota-tau-float",
  "kind": "def",
  "name": "iota_tau_float",
  "module_name": "TauLib.BookI.Boundary.Iota",
  "module_url": "/verify/taulib/docs/book-i-boundary-iota/",
  "source_line_start": 53,
  "source_line_end": 53,
  "registry_ids": [],
  "related_registry_items": [],
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookI/Boundary/Iota.lean#L53-L53",
  "formal_status": "defined",
  "right_rail": {
    "related": [
      {
        "title": "TauLib.BookI.Boundary.Iota",
        "url": "/verify/taulib/docs/book-i-boundary-iota/"
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookI/Boundary/Iota.lean#L53-L53",
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

- Module: [TauLib.BookI.Boundary.Iota](/verify/taulib/docs/book-i-boundary-iota/)
- Source path: [`TauLib/BookI/Boundary/Iota.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookI/Boundary/Iota.lean#L53-L53)
- Source range: L53-L53
- Kind: `def`
- Formal status hint: `defined`

## Registry Links

- No Registry IDs were detected in this declaration block.

## Immediate Comment / Docstring

```lean
/-- Float approximation of iota_tau = 2/(pi + e) ~ 0.341304.
    Since Lean 4 Float does not have a built-in pi constant,
    we use the known decimal approximation. -/
```

## Source Excerpt

```lean
def iota_tau_float : Float := 0.341304
```

---
{
  "projection_kind": "taulib_declaration",
  "title": "TauReal.pi",
  "permalink": "/verify/taulib/docs/book-i-boundary-tau-real-pi/pi/",
  "summary_short": "`def` declaration in `TauLib.BookI.Boundary.TauRealPi`.",
  "declaration_id": "TauLib.BookI.Boundary.TauRealPi::TauReal.pi",
  "declaration_slug": "pi",
  "kind": "def",
  "name": "TauReal.pi",
  "module_name": "TauLib.BookI.Boundary.TauRealPi",
  "module_url": "/verify/taulib/docs/book-i-boundary-tau-real-pi/",
  "source_line_start": 93,
  "source_line_end": 93,
  "registry_ids": [],
  "related_registry_items": [],
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookI/Boundary/TauRealPi.lean#L93-L93",
  "formal_status": "defined",
  "right_rail": {
    "related": [
      {
        "title": "TauLib.BookI.Boundary.TauRealPi",
        "url": "/verify/taulib/docs/book-i-boundary-tau-real-pi/"
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookI/Boundary/TauRealPi.lean#L93-L93",
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

- Module: [TauLib.BookI.Boundary.TauRealPi](/verify/taulib/docs/book-i-boundary-tau-real-pi/)
- Source path: [`TauLib/BookI/Boundary/TauRealPi.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookI/Boundary/TauRealPi.lean#L93-L93)
- Source range: L93-L93
- Kind: `def`
- Formal status hint: `defined`

## Registry Links

- No Registry IDs were detected in this declaration block.

## Immediate Comment / Docstring

```lean
/-- The constructive real `π`. -/
```

## Source Excerpt

```lean
def TauReal.pi : TauReal := ⟨TauRat.pi_partial⟩
```

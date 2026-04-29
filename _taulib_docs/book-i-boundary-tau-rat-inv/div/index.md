---
{
  "projection_kind": "taulib_declaration",
  "title": "TauRat.div",
  "permalink": "/verify/taulib/docs/book-i-boundary-tau-rat-inv/div/",
  "summary_short": "`def` declaration in `TauLib.BookI.Boundary.TauRatInv`.",
  "declaration_id": "TauLib.BookI.Boundary.TauRatInv::TauRat.div",
  "declaration_slug": "div",
  "kind": "def",
  "name": "TauRat.div",
  "module_name": "TauLib.BookI.Boundary.TauRatInv",
  "module_url": "/verify/taulib/docs/book-i-boundary-tau-rat-inv/",
  "source_line_start": 69,
  "source_line_end": 70,
  "registry_ids": [],
  "related_registry_items": [],
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookI/Boundary/TauRatInv.lean#L69-L70",
  "formal_status": "defined",
  "right_rail": {
    "related": [
      {
        "title": "TauLib.BookI.Boundary.TauRatInv",
        "url": "/verify/taulib/docs/book-i-boundary-tau-rat-inv/"
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookI/Boundary/TauRatInv.lean#L69-L70",
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

- Module: [TauLib.BookI.Boundary.TauRatInv](/verify/taulib/docs/book-i-boundary-tau-rat-inv/)
- Source path: [`TauLib/BookI/Boundary/TauRatInv.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookI/Boundary/TauRatInv.lean#L69-L70)
- Source range: L69-L70
- Kind: `def`
- Formal status hint: `defined`

## Registry Links

- No Registry IDs were detected in this declaration block.

## Immediate Comment / Docstring

```lean
/-- Division on `TauRat`: `a / b = a · b⁻¹`, with a nonzero hypothesis
    on `b`. -/
```

## Source Excerpt

```lean
def TauRat.div (a b : TauRat) (hb : b.is_nonzero) : TauRat :=
  a.mul (b.inv hb)
```

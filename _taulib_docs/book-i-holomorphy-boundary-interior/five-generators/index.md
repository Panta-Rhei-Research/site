---
{
  "projection_kind": "taulib_declaration",
  "title": "five_generators",
  "permalink": "/verify/taulib/docs/book-i-holomorphy-boundary-interior/five-generators/",
  "summary_short": "`theorem` declaration in `TauLib.BookI.Holomorphy.BoundaryInterior`.",
  "declaration_id": "TauLib.BookI.Holomorphy.BoundaryInterior::five_generators",
  "declaration_slug": "five-generators",
  "kind": "theorem",
  "name": "five_generators",
  "module_name": "TauLib.BookI.Holomorphy.BoundaryInterior",
  "module_url": "/verify/taulib/docs/book-i-holomorphy-boundary-interior/",
  "source_line_start": 132,
  "source_line_end": 133,
  "registry_ids": [],
  "related_registry_items": [],
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookI/Holomorphy/BoundaryInterior.lean#L132-L133",
  "formal_status": "formalized",
  "right_rail": {
    "related": [
      {
        "title": "TauLib.BookI.Holomorphy.BoundaryInterior",
        "url": "/verify/taulib/docs/book-i-holomorphy-boundary-interior/"
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookI/Holomorphy/BoundaryInterior.lean#L132-L133",
        "external": true
      }
    ],
    "meta": {
      "type": "TauLib Declaration",
      "kind": "theorem",
      "status": "formalized"
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

- Module: [TauLib.BookI.Holomorphy.BoundaryInterior](/verify/taulib/docs/book-i-holomorphy-boundary-interior/)
- Source path: [`TauLib/BookI/Holomorphy/BoundaryInterior.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookI/Holomorphy/BoundaryInterior.lean#L132-L133)
- Source range: L132-L133
- Kind: `theorem`
- Formal status hint: `formalized`

## Registry Links

- No Registry IDs were detected in this declaration block.

## Immediate Comment / Docstring

```lean
/-- Book I summary: 5 generators (α, π, γ, η, ω). -/
```

## Source Excerpt

```lean
theorem five_generators :
    [Tau.Kernel.Generator.alpha, .pi, .gamma, .eta, .omega].length = 5 := rfl
```

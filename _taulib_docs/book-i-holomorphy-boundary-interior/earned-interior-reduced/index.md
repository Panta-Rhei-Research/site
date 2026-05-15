---
{
  "projection_kind": "taulib_declaration",
  "title": "earned_interior_reduced",
  "permalink": "/corpus/taulib/docs/book-i-holomorphy-boundary-interior/earned-interior-reduced/",
  "summary_short": "`theorem` declaration in `TauLib.BookI.Holomorphy.BoundaryInterior`.",
  "declaration_id": "TauLib.BookI.Holomorphy.BoundaryInterior::earned_interior_reduced",
  "declaration_slug": "earned-interior-reduced",
  "kind": "theorem",
  "name": "earned_interior_reduced",
  "module_name": "TauLib.BookI.Holomorphy.BoundaryInterior",
  "module_url": "/corpus/taulib/docs/book-i-holomorphy-boundary-interior/",
  "source_line_start": 71,
  "source_line_end": 73,
  "registry_ids": [],
  "related_registry_items": [],
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookI/Holomorphy/BoundaryInterior.lean#L71-L73",
  "formal_status": "formalized",
  "declaration_role": "proof obligation",
  "formal_status_label": "formal proof obligation checked",
  "right_rail": {
    "related": [
      {
        "title": "TauLib.BookI.Holomorphy.BoundaryInterior",
        "url": "/corpus/taulib/docs/book-i-holomorphy-boundary-interior/"
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookI/Holomorphy/BoundaryInterior.lean#L71-L73",
        "external": true
      }
    ],
    "meta": {
      "type": "TauLib Declaration",
      "kind": "theorem",
      "role": "proof obligation",
      "status": "formal proof obligation checked"
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

- Module: [TauLib.BookI.Holomorphy.BoundaryInterior](/corpus/taulib/docs/book-i-holomorphy-boundary-interior/)
- Source path: [`TauLib/BookI/Holomorphy/BoundaryInterior.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookI/Holomorphy/BoundaryInterior.lean#L71-L73)
- Source range: L71-L73
- Kind: `theorem`
- Public role: `proof obligation`
- Formal status hint: `formal proof obligation checked`

## Registry Links

- No Registry IDs were detected in this declaration block.

## Immediate Comment / Docstring

```lean
/-- Interior values are self-consistent: output at stage k is reduced. -/
```

## Source Excerpt

```lean
theorem earned_interior_reduced (p : EarnedInteriorPoint) (n k : TauIdx) :
    reduce (p.boundary_fun.b_fun n k) k = p.boundary_fun.b_fun n k :=
  output_reduced p.boundary_fun p.coherent n k
```

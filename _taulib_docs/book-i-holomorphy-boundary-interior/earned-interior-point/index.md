---
{
  "projection_kind": "taulib_declaration",
  "title": "EarnedInteriorPoint",
  "permalink": "/verify/taulib/docs/book-i-holomorphy-boundary-interior/earned-interior-point/",
  "summary_short": "`structure` declaration in `TauLib.BookI.Holomorphy.BoundaryInterior`.",
  "declaration_id": "TauLib.BookI.Holomorphy.BoundaryInterior::EarnedInteriorPoint",
  "declaration_slug": "earned-interior-point",
  "kind": "structure",
  "name": "EarnedInteriorPoint",
  "module_name": "TauLib.BookI.Holomorphy.BoundaryInterior",
  "module_url": "/verify/taulib/docs/book-i-holomorphy-boundary-interior/",
  "source_line_start": 57,
  "source_line_end": 63,
  "registry_ids": [
    "I.D68"
  ],
  "related_registry_items": [
    {
      "id": "I.D68",
      "title": "Earned Stage-Determined Point",
      "url": "/registry/object/I.D68/"
    }
  ],
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookI/Holomorphy/BoundaryInterior.lean#L57-L63",
  "formal_status": "defined",
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookI/Holomorphy/BoundaryInterior.lean#L57-L63",
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

- Module: [TauLib.BookI.Holomorphy.BoundaryInterior](/verify/taulib/docs/book-i-holomorphy-boundary-interior/)
- Source path: [`TauLib/BookI/Holomorphy/BoundaryInterior.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookI/Holomorphy/BoundaryInterior.lean#L57-L63)
- Source range: L57-L63
- Kind: `structure`
- Formal status hint: `defined`

## Registry Links

- `I.D68` — Earned Stage-Determined Point

## Immediate Comment / Docstring

```lean
/-- [I.D68] An earned interior point: a value obtained by
    extending boundary data via the Hartogs extension.
    The extension is uniquely determined by tower coherence
    and the Identity Theorem. -/
```

## Source Excerpt

```lean
structure EarnedInteriorPoint where
  -- The boundary function (tower-coherent StageFun)
  boundary_fun : StageFun
  -- Tower coherence
  coherent : TowerCoherent boundary_fun
  -- The interior value at input n, stage k
  value_at : TauIdx → TauIdx → TauIdx := boundary_fun.b_fun
```

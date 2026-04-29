---
{
  "projection_kind": "taulib_declaration",
  "title": "no_simul_projection_c",
  "permalink": "/verify/taulib/docs/book-i-holomorphy-diagonal-protection/no-simul-projection-c/",
  "summary_short": "`theorem` declaration in `TauLib.BookI.Holomorphy.DiagonalProtection`.",
  "declaration_id": "TauLib.BookI.Holomorphy.DiagonalProtection::no_simul_projection_c",
  "declaration_slug": "no-simul-projection-c",
  "kind": "theorem",
  "name": "no_simul_projection_c",
  "module_name": "TauLib.BookI.Holomorphy.DiagonalProtection",
  "module_url": "/verify/taulib/docs/book-i-holomorphy-diagonal-protection/",
  "source_line_start": 62,
  "source_line_end": 65,
  "registry_ids": [],
  "related_registry_items": [],
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookI/Holomorphy/DiagonalProtection.lean#L62-L65",
  "formal_status": "formalized",
  "right_rail": {
    "related": [
      {
        "title": "TauLib.BookI.Holomorphy.DiagonalProtection",
        "url": "/verify/taulib/docs/book-i-holomorphy-diagonal-protection/"
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookI/Holomorphy/DiagonalProtection.lean#L62-L65",
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

- Module: [TauLib.BookI.Holomorphy.DiagonalProtection](/verify/taulib/docs/book-i-holomorphy-diagonal-protection/)
- Source path: [`TauLib/BookI/Holomorphy/DiagonalProtection.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookI/Holomorphy/DiagonalProtection.lean#L62-L65)
- Source range: L62-L65
- Kind: `theorem`
- Formal status hint: `formalized`

## Registry Links

- No Registry IDs were detected in this declaration block.

## Immediate Comment / Docstring

```lean
No immediate Lean doc/comment block was detected for this declaration.
```

## Source Excerpt

```lean
theorem no_simul_projection_c (f : StageFun) (n k : TauIdx)
    (hc : f.c_fun n k = 0) :
    SectorPair.mul ⟨f.b_fun n k, 0⟩ ⟨0, f.c_fun n k⟩ = ⟨0, 0⟩ := by
  simp [SectorPair.mul, hc]
```

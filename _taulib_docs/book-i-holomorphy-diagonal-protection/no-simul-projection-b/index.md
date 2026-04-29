---
{
  "projection_kind": "taulib_declaration",
  "title": "no_simul_projection_b",
  "permalink": "/verify/taulib/docs/book-i-holomorphy-diagonal-protection/no-simul-projection-b/",
  "summary_short": "`theorem` declaration in `TauLib.BookI.Holomorphy.DiagonalProtection`.",
  "declaration_id": "TauLib.BookI.Holomorphy.DiagonalProtection::no_simul_projection_b",
  "declaration_slug": "no-simul-projection-b",
  "kind": "theorem",
  "name": "no_simul_projection_b",
  "module_name": "TauLib.BookI.Holomorphy.DiagonalProtection",
  "module_url": "/verify/taulib/docs/book-i-holomorphy-diagonal-protection/",
  "source_line_start": 57,
  "source_line_end": 60,
  "registry_ids": [
    "I.P23"
  ],
  "related_registry_items": [
    {
      "id": "I.P23",
      "title": "No Simultaneous Projection",
      "url": "/registry/object/I.P23/"
    }
  ],
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookI/Holomorphy/DiagonalProtection.lean#L57-L60",
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookI/Holomorphy/DiagonalProtection.lean#L57-L60",
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
- Source path: [`TauLib/BookI/Holomorphy/DiagonalProtection.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookI/Holomorphy/DiagonalProtection.lean#L57-L60)
- Source range: L57-L60
- Kind: `theorem`
- Formal status hint: `formalized`

## Registry Links

- `I.P23` — No Simultaneous Projection

## Immediate Comment / Docstring

```lean
/-- [I.P23] No Simultaneous Projection (sector purity):
    For a tower-coherent function where one sector is constantly zero,
    the other sector carries all the information.

    Concretely: if f.b_fun = 0 everywhere, then f.c_fun is the sole
    carrier; and vice versa. The sectors cannot BOTH be nontrivial
    for a well-behaved (tower-coherent) omega-germ transformer.

    This is formalized as: the product of a B-only and C-only
    stagewise function outputs zero. -/
```

## Source Excerpt

```lean
theorem no_simul_projection_b (f : StageFun) (n k : TauIdx)
    (hb : f.b_fun n k = 0) :
    SectorPair.mul ⟨f.b_fun n k, 0⟩ ⟨0, f.c_fun n k⟩ = ⟨0, 0⟩ := by
  simp [SectorPair.mul, hb]
```

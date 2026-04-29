---
{
  "projection_kind": "taulib_declaration",
  "title": "chi_minus_coherent",
  "permalink": "/verify/taulib/docs/book-i-holomorphy-tau-holomorphic/chi-minus-coherent/",
  "summary_short": "`theorem` declaration in `TauLib.BookI.Holomorphy.TauHolomorphic`.",
  "declaration_id": "TauLib.BookI.Holomorphy.TauHolomorphic::chi_minus_coherent",
  "declaration_slug": "chi-minus-coherent",
  "kind": "theorem",
  "name": "chi_minus_coherent",
  "module_name": "TauLib.BookI.Holomorphy.TauHolomorphic",
  "module_url": "/verify/taulib/docs/book-i-holomorphy-tau-holomorphic/",
  "source_line_start": 184,
  "source_line_end": 191,
  "registry_ids": [],
  "related_registry_items": [],
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookI/Holomorphy/TauHolomorphic.lean#L184-L191",
  "formal_status": "formalized",
  "right_rail": {
    "related": [
      {
        "title": "TauLib.BookI.Holomorphy.TauHolomorphic",
        "url": "/verify/taulib/docs/book-i-holomorphy-tau-holomorphic/"
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookI/Holomorphy/TauHolomorphic.lean#L184-L191",
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

- Module: [TauLib.BookI.Holomorphy.TauHolomorphic](/verify/taulib/docs/book-i-holomorphy-tau-holomorphic/)
- Source path: [`TauLib/BookI/Holomorphy/TauHolomorphic.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookI/Holomorphy/TauHolomorphic.lean#L184-L191)
- Source range: L184-L191
- Kind: `theorem`
- Formal status hint: `formalized`

## Registry Links

- No Registry IDs were detected in this declaration block.

## Immediate Comment / Docstring

```lean
/-- χ₋ is tower-coherent. -/
```

## Source Excerpt

```lean
theorem chi_minus_coherent : TowerCoherent chi_minus_stage := by
  constructor
  · -- B-sector: reduce(0, k) = 0
    intro _ k _ _
    exact reduce_zero k
  · -- C-sector: reduce(reduce(n, l), k) = reduce(n, k)
    intro n k l hkl
    exact reduce_compat n hkl
```

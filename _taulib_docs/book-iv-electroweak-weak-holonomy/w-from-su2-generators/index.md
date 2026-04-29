---
{
  "projection_kind": "taulib_declaration",
  "title": "w_from_su2_generators",
  "permalink": "/verify/taulib/docs/book-iv-electroweak-weak-holonomy/w-from-su2-generators/",
  "summary_short": "`theorem` declaration in `TauLib.BookIV.Electroweak.WeakHolonomy`.",
  "declaration_id": "TauLib.BookIV.Electroweak.WeakHolonomy::w_from_su2_generators",
  "declaration_slug": "w-from-su2-generators",
  "kind": "theorem",
  "name": "w_from_su2_generators",
  "module_name": "TauLib.BookIV.Electroweak.WeakHolonomy",
  "module_url": "/verify/taulib/docs/book-iv-electroweak-weak-holonomy/",
  "source_line_start": 253,
  "source_line_end": 256,
  "registry_ids": [
    "IV.P56"
  ],
  "related_registry_items": [
    {
      "id": "IV.P56",
      "title": "Charged and Neutral Combinations",
      "url": "/registry/object/IV.P56/"
    }
  ],
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIV/Electroweak/WeakHolonomy.lean#L253-L256",
  "formal_status": "formalized",
  "right_rail": {
    "related": [
      {
        "title": "TauLib.BookIV.Electroweak.WeakHolonomy",
        "url": "/verify/taulib/docs/book-iv-electroweak-weak-holonomy/"
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIV/Electroweak/WeakHolonomy.lean#L253-L256",
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

- Module: [TauLib.BookIV.Electroweak.WeakHolonomy](/verify/taulib/docs/book-iv-electroweak-weak-holonomy/)
- Source path: [`TauLib/BookIV/Electroweak/WeakHolonomy.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIV/Electroweak/WeakHolonomy.lean#L253-L256)
- Source range: L253-L256
- Kind: `theorem`
- Formal status hint: `formalized`

## Registry Links

- `IV.P56` — Charged and Neutral Combinations

## Immediate Comment / Docstring

```lean
/-- [IV.P56] The physical W+, W-, W3 bosons arise from the 3 SU(2)
    generators: W± from (sigma_1 ± i·sigma_2)/√2,
    W3 = sigma_3. There are exactly 3 gauge bosons. -/
```

## Source Excerpt

```lean
theorem w_from_su2_generators :
    su2_generators.length = 3 ∧
    adjoint_su2.num_bosons = 3 := by
  exact ⟨rfl, rfl⟩
```

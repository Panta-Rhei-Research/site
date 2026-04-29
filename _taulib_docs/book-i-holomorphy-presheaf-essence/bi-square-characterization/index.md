---
{
  "projection_kind": "taulib_declaration",
  "title": "bi_square_characterization",
  "permalink": "/verify/taulib/docs/book-i-holomorphy-presheaf-essence/bi-square-characterization/",
  "summary_short": "`theorem` declaration in `TauLib.BookI.Holomorphy.PresheafEssence`.",
  "declaration_id": "TauLib.BookI.Holomorphy.PresheafEssence::bi_square_characterization",
  "declaration_slug": "bi-square-characterization",
  "kind": "theorem",
  "name": "bi_square_characterization",
  "module_name": "TauLib.BookI.Holomorphy.PresheafEssence",
  "module_url": "/verify/taulib/docs/book-i-holomorphy-presheaf-essence/",
  "source_line_start": 125,
  "source_line_end": 129,
  "registry_ids": [
    "I.T41"
  ],
  "related_registry_items": [
    {
      "id": "I.T41",
      "title": "Bi-Square Characterization",
      "url": "/registry/object/I.T41/"
    }
  ],
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookI/Holomorphy/PresheafEssence.lean#L125-L129",
  "formal_status": "formalized",
  "right_rail": {
    "related": [
      {
        "title": "TauLib.BookI.Holomorphy.PresheafEssence",
        "url": "/verify/taulib/docs/book-i-holomorphy-presheaf-essence/"
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookI/Holomorphy/PresheafEssence.lean#L125-L129",
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

- Module: [TauLib.BookI.Holomorphy.PresheafEssence](/verify/taulib/docs/book-i-holomorphy-presheaf-essence/)
- Source path: [`TauLib/BookI/Holomorphy/PresheafEssence.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookI/Holomorphy/PresheafEssence.lean#L125-L129)
- Source range: L125-L129
- Kind: `theorem`
- Formal status hint: `formalized`

## Registry Links

- `I.T41` — Bi-Square Characterization

## Immediate Comment / Docstring

```lean
/-- [I.T41] The bi-square characterizes τ-holomorphy completely:
    TowerCoherent f ↔ both sectors of the left square commute. -/
```

## Source Excerpt

```lean
theorem bi_square_characterization (f : StageFun) :
    TowerCoherent f ↔
    (∀ n k l : TauIdx, k ≤ l → reduce (f.b_fun n l) k = f.b_fun n k) ∧
    (∀ n k l : TauIdx, k ≤ l → reduce (f.c_fun n l) k = f.c_fun n k) :=
  Iff.rfl
```

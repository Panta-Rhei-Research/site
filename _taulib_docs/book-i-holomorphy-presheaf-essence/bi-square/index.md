---
{
  "projection_kind": "taulib_declaration",
  "title": "BiSquare",
  "permalink": "/verify/taulib/docs/book-i-holomorphy-presheaf-essence/bi-square/",
  "summary_short": "`structure` declaration in `TauLib.BookI.Holomorphy.PresheafEssence`.",
  "declaration_id": "TauLib.BookI.Holomorphy.PresheafEssence::BiSquare",
  "declaration_slug": "bi-square",
  "kind": "structure",
  "name": "BiSquare",
  "module_name": "TauLib.BookI.Holomorphy.PresheafEssence",
  "module_url": "/verify/taulib/docs/book-i-holomorphy-presheaf-essence/",
  "source_line_start": 102,
  "source_line_end": 109,
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
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookI/Holomorphy/PresheafEssence.lean#L102-L109",
  "formal_status": "defined",
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookI/Holomorphy/PresheafEssence.lean#L102-L109",
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

- Module: [TauLib.BookI.Holomorphy.PresheafEssence](/verify/taulib/docs/book-i-holomorphy-presheaf-essence/)
- Source path: [`TauLib/BookI/Holomorphy/PresheafEssence.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookI/Holomorphy/PresheafEssence.lean#L102-L109)
- Source range: L102-L109
- Kind: `structure`
- Formal status hint: `defined`

## Registry Links

- `I.T41` — Bi-Square Characterization

## Immediate Comment / Docstring

```lean
/-- [I.T41] The holomorphy bi-square: the minimal complete
    characterization of τ-holomorphic functions.

    Left square: tower coherence for each sector.
    The right square (spectral naturality) follows automatically
    from left_b and left_c — see `right_from_left`. -/
```

## Source Excerpt

```lean
structure BiSquare where
  stage_fun : StageFun
  /-- LEFT SQUARE, B-sector: reduce(B_ℓ(n), k) = B_k(n). -/
  left_b : ∀ n k l : TauIdx, k ≤ l →
    reduce (stage_fun.b_fun n l) k = stage_fun.b_fun n k
  /-- LEFT SQUARE, C-sector: reduce(C_ℓ(n), k) = C_k(n). -/
  left_c : ∀ n k l : TauIdx, k ≤ l →
    reduce (stage_fun.c_fun n l) k = stage_fun.c_fun n k
```

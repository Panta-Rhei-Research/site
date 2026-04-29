---
{
  "projection_kind": "taulib_declaration",
  "title": "PrimorialPresheaf",
  "permalink": "/verify/taulib/docs/book-i-holomorphy-presheaf-essence/primorial-presheaf/",
  "summary_short": "`structure` declaration in `TauLib.BookI.Holomorphy.PresheafEssence`.",
  "declaration_id": "TauLib.BookI.Holomorphy.PresheafEssence::PrimorialPresheaf",
  "declaration_slug": "primorial-presheaf",
  "kind": "structure",
  "name": "PrimorialPresheaf",
  "module_name": "TauLib.BookI.Holomorphy.PresheafEssence",
  "module_url": "/verify/taulib/docs/book-i-holomorphy-presheaf-essence/",
  "source_line_start": 49,
  "source_line_end": 51,
  "registry_ids": [
    "I.D83"
  ],
  "related_registry_items": [
    {
      "id": "I.D83",
      "title": "Primorial Presheaf",
      "url": "/registry/object/I.D83/"
    }
  ],
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookI/Holomorphy/PresheafEssence.lean#L49-L51",
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookI/Holomorphy/PresheafEssence.lean#L49-L51",
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
- Source path: [`TauLib/BookI/Holomorphy/PresheafEssence.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookI/Holomorphy/PresheafEssence.lean#L49-L51)
- Source range: L49-L51
- Kind: `structure`
- Formal status hint: `defined`

## Registry Links

- `I.D83` — Primorial Presheaf

## Immediate Comment / Docstring

```lean
/-- [I.D83] An element of the primorial presheaf lim← ℤ/M_dℤ:
    a compatible family of values at each primorial depth.
    Compatibility: reduce(value_at ℓ, k) = value_at k for k ≤ ℓ. -/
```

## Source Excerpt

```lean
structure PrimorialPresheaf where
  value_at : TauIdx → TauIdx
  compatible : ∀ k l : TauIdx, k ≤ l → reduce (value_at l) k = value_at k
```

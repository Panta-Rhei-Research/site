---
{
  "projection_kind": "taulib_declaration",
  "title": "BlueprintMonoid",
  "permalink": "/corpus/taulib/docs/book-v-cosmology-bhbipolar-fusion/blueprint-monoid/",
  "summary_short": "`structure` declaration in `TauLib.BookV.Cosmology.BHBipolarFusion`.",
  "declaration_id": "TauLib.BookV.Cosmology.BHBipolarFusion::BlueprintMonoid",
  "declaration_slug": "blueprint-monoid",
  "kind": "structure",
  "name": "BlueprintMonoid",
  "module_name": "TauLib.BookV.Cosmology.BHBipolarFusion",
  "module_url": "/corpus/taulib/docs/book-v-cosmology-bhbipolar-fusion/",
  "source_line_start": 194,
  "source_line_end": 201,
  "registry_ids": [
    "V.D172"
  ],
  "related_registry_items": [
    {
      "id": "V.D172",
      "title": "Blueprint Monoid",
      "url": "/registry/object/V.D172/"
    }
  ],
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookV/Cosmology/BHBipolarFusion.lean#L194-L201",
  "formal_status": "defined",
  "declaration_role": "type/data schema",
  "formal_status_label": "type/data schema",
  "right_rail": {
    "related": [
      {
        "title": "TauLib.BookV.Cosmology.BHBipolarFusion",
        "url": "/corpus/taulib/docs/book-v-cosmology-bhbipolar-fusion/"
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookV/Cosmology/BHBipolarFusion.lean#L194-L201",
        "external": true
      }
    ],
    "meta": {
      "type": "TauLib Declaration",
      "kind": "structure",
      "role": "type/data schema",
      "status": "type/data schema"
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

- Module: [TauLib.BookV.Cosmology.BHBipolarFusion](/corpus/taulib/docs/book-v-cosmology-bhbipolar-fusion/)
- Source path: [`TauLib/BookV/Cosmology/BHBipolarFusion.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookV/Cosmology/BHBipolarFusion.lean#L194-L201)
- Source range: L194-L201
- Kind: `structure`
- Public role: `type/data schema`
- Formal status hint: `type/data schema`

## Registry Links

- `V.D172` — Blueprint Monoid

## Immediate Comment / Docstring

```lean
/-- [V.D172] Blueprint monoid M_BH: blueprints with fusion and
    vacuum identity.

    - Carrier: BH blueprints
    - Operation: Fuse_ω (pointwise lobe multiplication)
    - Identity: vacuum blueprint (χ⁺ = χ⁻ = 1, m = 0)
    - Non-invertible: mergers are irreversible -/
```

## Source Excerpt

```lean
structure BlueprintMonoid where
  /-- Whether fusion is associative. -/
  is_associative : Bool := true
  /-- Whether identity exists. -/
  has_identity : Bool := true
  /-- Whether the monoid is non-invertible (not a group). -/
  non_invertible : Bool := true
  deriving Repr
```

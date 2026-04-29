---
{
  "projection_kind": "taulib_declaration",
  "title": "BlueprintFusion",
  "permalink": "/verify/taulib/docs/book-v-cosmology-bhbipolar-fusion/blueprint-fusion/",
  "summary_short": "`def` declaration in `TauLib.BookV.Cosmology.BHBipolarFusion`.",
  "declaration_id": "TauLib.BookV.Cosmology.BHBipolarFusion::BlueprintFusion",
  "declaration_slug": "blueprint-fusion",
  "kind": "def",
  "name": "BlueprintFusion",
  "module_name": "TauLib.BookV.Cosmology.BHBipolarFusion",
  "module_url": "/verify/taulib/docs/book-v-cosmology-bhbipolar-fusion/",
  "source_line_start": 173,
  "source_line_end": 181,
  "registry_ids": [
    "V.D171"
  ],
  "related_registry_items": [
    {
      "id": "V.D171",
      "title": "Blueprint fusion mathrmFuse",
      "url": "/registry/object/V.D171/"
    }
  ],
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookV/Cosmology/BHBipolarFusion.lean#L173-L181",
  "formal_status": "defined",
  "right_rail": {
    "related": [
      {
        "title": "TauLib.BookV.Cosmology.BHBipolarFusion",
        "url": "/verify/taulib/docs/book-v-cosmology-bhbipolar-fusion/"
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookV/Cosmology/BHBipolarFusion.lean#L173-L181",
        "external": true
      }
    ],
    "meta": {
      "type": "TauLib Declaration",
      "kind": "def",
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

- Module: [TauLib.BookV.Cosmology.BHBipolarFusion](/verify/taulib/docs/book-v-cosmology-bhbipolar-fusion/)
- Source path: [`TauLib/BookV/Cosmology/BHBipolarFusion.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookV/Cosmology/BHBipolarFusion.lean#L173-L181)
- Source range: L173-L181
- Kind: `def`
- Formal status hint: `defined`

## Registry Links

- `V.D171` — Blueprint fusion mathrmFuse

## Immediate Comment / Docstring

```lean
/-- [V.D171] Blueprint fusion Fuse_ω: combines two blueprints by
    pointwise multiplication of lobe characters.

    Fuse_ω(b₁, b₂) = (χ₁⁺ · χ₂⁺, χ₁⁻ · χ₂⁻)

    Product on the ω (crossing) sector. -/
```

## Source Excerpt

```lean
def BlueprintFusion (b1 b2 : BHBlueprint) : BHBlueprint where
  bipolarity := {
    chi_plus := b1.bipolarity.chi_plus * b2.bipolarity.chi_plus
    chi_minus := b1.bipolarity.chi_minus * b2.bipolarity.chi_minus
    plus_pos := Nat.mul_pos b1.bipolarity.plus_pos b2.bipolarity.plus_pos
    minus_pos := Nat.mul_pos b1.bipolarity.minus_pos b2.bipolarity.minus_pos
  }
  mass_index := b1.mass_index + b2.mass_index
  mass_pos := Nat.add_pos_left b1.mass_pos _
```

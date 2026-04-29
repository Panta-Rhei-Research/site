---
{
  "projection_kind": "taulib_declaration",
  "title": "CapacityIdentity",
  "permalink": "/verify/taulib/docs/book-iv-physics-lemniscate-capacity/capacity-identity/",
  "summary_short": "`structure` declaration in `TauLib.BookIV.Physics.LemniscateCapacity`.",
  "declaration_id": "TauLib.BookIV.Physics.LemniscateCapacity::CapacityIdentity",
  "declaration_slug": "capacity-identity",
  "kind": "structure",
  "name": "CapacityIdentity",
  "module_name": "TauLib.BookIV.Physics.LemniscateCapacity",
  "module_url": "/verify/taulib/docs/book-iv-physics-lemniscate-capacity/",
  "source_line_start": 220,
  "source_line_end": 228,
  "registry_ids": [],
  "related_registry_items": [],
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIV/Physics/LemniscateCapacity.lean#L220-L228",
  "formal_status": "defined",
  "right_rail": {
    "related": [
      {
        "title": "TauLib.BookIV.Physics.LemniscateCapacity",
        "url": "/verify/taulib/docs/book-iv-physics-lemniscate-capacity/"
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIV/Physics/LemniscateCapacity.lean#L220-L228",
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

- Module: [TauLib.BookIV.Physics.LemniscateCapacity](/verify/taulib/docs/book-iv-physics-lemniscate-capacity/)
- Source path: [`TauLib/BookIV/Physics/LemniscateCapacity.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIV/Physics/LemniscateCapacity.lean#L220-L228)
- Source range: L220-L228
- Kind: `structure`
- Formal status hint: `defined`

## Registry Links

- No Registry IDs were detected in this declaration block.

## Immediate Comment / Docstring

```lean
/-- The capacity identity: √3·ι_τ^(-2) = 4π√3 × X_E^(nat)
    where X_E^(nat) = 1/(4π·ι_τ²) is the natural electrostatic capacity
    of the torus T² with shape ι_τ.

    This gives the correction term a clean physical interpretation:
    it is the lemniscate-corrected universal capacity of T². -/
```

## Source Excerpt

```lean
structure CapacityIdentity where
  /-- The correction coefficient. -/
  coeff_numer : Nat := sqrt3_numer      -- √3
  coeff_denom : Nat := sqrt3_denom
  /-- The ι_τ power in the denominator. -/
  iota_power : Nat := 2
  /-- Physical interpretation. -/
  interpretation : String := "lemniscate-corrected T² capacity"
  deriving Repr
```

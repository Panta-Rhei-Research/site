---
{
  "projection_kind": "taulib_declaration",
  "title": "eval at L93",
  "permalink": "/verify/taulib/docs/tour-central-theorem/eval-l93/",
  "summary_short": "`eval` declaration in `TauLib.Tour.CentralTheorem`.",
  "declaration_id": "TauLib.Tour.CentralTheorem::#eval:93",
  "declaration_slug": "eval-l93",
  "kind": "eval",
  "name": null,
  "module_name": "TauLib.Tour.CentralTheorem",
  "module_url": "/verify/taulib/docs/tour-central-theorem/",
  "source_line_start": 93,
  "source_line_end": 119,
  "registry_ids": [],
  "related_registry_items": [],
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/Tour/CentralTheorem.lean#L93-L119",
  "formal_status": "computed",
  "right_rail": {
    "related": [
      {
        "title": "TauLib.Tour.CentralTheorem",
        "url": "/verify/taulib/docs/tour-central-theorem/"
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/Tour/CentralTheorem.lean#L93-L119",
        "external": true
      }
    ],
    "meta": {
      "type": "TauLib Declaration",
      "kind": "eval",
      "status": "computed"
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

- Module: [TauLib.Tour.CentralTheorem](/verify/taulib/docs/tour-central-theorem/)
- Source path: [`TauLib/Tour/CentralTheorem.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/Tour/CentralTheorem.lean#L93-L119)
- Source range: L93-L119
- Kind: `eval`
- Formal status hint: `computed`

## Registry Links

- No Registry IDs were detected in this declaration block.

## Immediate Comment / Docstring

```lean
No immediate Lean doc/comment block was detected for this declaration.
```

## Source Excerpt

```lean
#eval SectorPair.mul ⟨2, 3⟩ ⟨4, 5⟩              -- (8, 15)

-- ================================================================
-- PART 3: THE TAU^3 FIBERED PRODUCT
-- ================================================================

-- tau^3 = tau^1 x_f T^2 is NOT a Cartesian product.
-- It is a fibered product where the fiber depends on the base.

-- Base tau^1: the (D, A) coordinate space
--   D = radial depth (alpha-channel)
--   A = prime direction (pi-channel)
#check BaseTau1               -- structure with fields `d` and `a`

-- Fiber T^2: the (B, C) coordinate space
--   B = exponent (gamma-channel)
--   C = tetration height (eta-channel)
#check FiberT2                -- structure with fields `b` and `c`

-- The fibered product tau^3:
#check Tau3                   -- structure with `base : BaseTau1` and `fiber : FiberT2`

-- Conversion from the ABCD chart to fibered product form and back:
#check to_tau3                -- TauAdmissiblePoint -> Tau3
#check from_tau3              -- Tau3 -> TauAdmissiblePoint
#check tau3_round_trip        -- from_tau3(to_tau3(p)) = p
#check tau3_round_trip'       -- to_tau3(from_tau3(t)) = t
```

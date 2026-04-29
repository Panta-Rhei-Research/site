---
{
  "projection_kind": "taulib_declaration",
  "title": "CoRotorCoupling",
  "permalink": "/verify/taulib/docs/book-v-gravity-co-rotor-coupling/co-rotor-coupling/",
  "summary_short": "`structure` declaration in `TauLib.BookV.Gravity.CoRotorCoupling`.",
  "declaration_id": "TauLib.BookV.Gravity.CoRotorCoupling::CoRotorCoupling",
  "declaration_slug": "co-rotor-coupling",
  "kind": "structure",
  "name": "CoRotorCoupling",
  "module_name": "TauLib.BookV.Gravity.CoRotorCoupling",
  "module_url": "/verify/taulib/docs/book-v-gravity-co-rotor-coupling/",
  "source_line_start": 90,
  "source_line_end": 103,
  "registry_ids": [
    "V.D10"
  ],
  "related_registry_items": [],
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookV/Gravity/CoRotorCoupling.lean#L90-L103",
  "formal_status": "defined",
  "right_rail": {
    "related": [
      {
        "title": "TauLib.BookV.Gravity.CoRotorCoupling",
        "url": "/verify/taulib/docs/book-v-gravity-co-rotor-coupling/"
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookV/Gravity/CoRotorCoupling.lean#L90-L103",
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

- Module: [TauLib.BookV.Gravity.CoRotorCoupling](/verify/taulib/docs/book-v-gravity-co-rotor-coupling/)
- Source path: [`TauLib/BookV/Gravity/CoRotorCoupling.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookV/Gravity/CoRotorCoupling.lean#L90-L103)
- Source range: L90-L103
- Kind: `structure`
- Formal status hint: `defined`

## Registry Links

- No Registry IDs were detected in this declaration block.

## Immediate Comment / Docstring

```lean
/-- [V.D10] Co-rotor coupling structure on T².

    Encodes the tree-level coupling distance κ_n^{tree} = 2√3
    and the α-order correction coefficient c₁.

    The physical κ_n = κ_n^{tree} × (1 - c₁·α):
    - tree_factor = 2 (from b₁(T²) = 2, two rotation axes)
    - spectral_distance_sq = 3 (from |1-ω|² = 3, three-fold lemniscate)
    - correction_c1_numer/denom ≈ 3/π ≈ 0.95493

    With these values and CODATA α:
    κ_n ≈ 2√3 × (1 - (3/π)·α) ≈ 3.4400 (0.0003% from CODATA G). -/
```

## Source Excerpt

```lean
structure CoRotorCoupling where
  /-- Tree-level factor (number of rotation axes on T²). -/
  tree_factor : Nat
  /-- Spectral distance squared |1-ω|² at the crossing. -/
  spectral_distance_sq : Nat
  /-- c₁ numerator (rational approximation of 3/π). -/
  correction_c1_numer : Nat
  /-- c₁ denominator. -/
  correction_c1_denom : Nat
  /-- Denominator positive. -/
  denom_pos : correction_c1_denom > 0
  /-- Scope label. -/
  scope : String := "conjectural"
  deriving Repr
```

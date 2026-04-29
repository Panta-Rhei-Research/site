---
{
  "projection_kind": "taulib_declaration",
  "title": "BHMassIndex",
  "permalink": "/verify/taulib/docs/book-v-gravity-schwarzschild/bhmass-index/",
  "summary_short": "`structure` declaration in `TauLib.BookV.Gravity.Schwarzschild`.",
  "declaration_id": "TauLib.BookV.Gravity.Schwarzschild::BHMassIndex",
  "declaration_slug": "bhmass-index",
  "kind": "structure",
  "name": "BHMassIndex",
  "module_name": "TauLib.BookV.Gravity.Schwarzschild",
  "module_url": "/verify/taulib/docs/book-v-gravity-schwarzschild/",
  "source_line_start": 81,
  "source_line_end": 92,
  "registry_ids": [
    "V.D07"
  ],
  "related_registry_items": [],
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookV/Gravity/Schwarzschild.lean#L81-L92",
  "formal_status": "defined",
  "right_rail": {
    "related": [
      {
        "title": "TauLib.BookV.Gravity.Schwarzschild",
        "url": "/verify/taulib/docs/book-v-gravity-schwarzschild/"
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookV/Gravity/Schwarzschild.lean#L81-L92",
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

- Module: [TauLib.BookV.Gravity.Schwarzschild](/verify/taulib/docs/book-v-gravity-schwarzschild/)
- Source path: [`TauLib/BookV/Gravity/Schwarzschild.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookV/Gravity/Schwarzschild.lean#L81-L92)
- Source range: L81-L92
- Kind: `structure`
- Formal status hint: `defined`

## Registry Links

- No Registry IDs were detected in this declaration block.

## Immediate Comment / Docstring

```lean
/-- [V.D07] Black hole mass index: the α-Idx readout from a
    normal-form stabilized torus vacuum.

    M_n(x) := MassIdx(NF_ω(x))

    Properties:
    - Resistance/scale index of stabilized torus (not primitive scalar)
    - Comes with minimal carrier that can host it
    - Monotone under admissible evolution (No-Shrink) -/
```

## Source Excerpt

```lean
structure BHMassIndex where
  /-- Mass index numerator (scaled). -/
  mass_numer : Nat
  /-- Mass index denominator. -/
  mass_denom : Nat
  /-- Denominator positive. -/
  denom_pos : mass_denom > 0
  /-- Mass is positive for any physical BH. -/
  mass_positive : mass_numer > 0
  /-- Whether this state is beyond the maturity horizon n*. -/
  is_mature : Bool
  deriving Repr
```

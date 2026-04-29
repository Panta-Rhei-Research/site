---
{
  "projection_kind": "taulib_declaration",
  "title": "iota_float",
  "permalink": "/verify/taulib/docs/book-v-astrophysics-ehtreread/iota-float/",
  "summary_short": "`def` declaration in `TauLib.BookV.Astrophysics.EHTReread`.",
  "declaration_id": "TauLib.BookV.Astrophysics.EHTReread::iota_float",
  "declaration_slug": "iota-float",
  "kind": "def",
  "name": "iota_float",
  "module_name": "TauLib.BookV.Astrophysics.EHTReread",
  "module_url": "/verify/taulib/docs/book-v-astrophysics-ehtreread/",
  "source_line_start": 255,
  "source_line_end": 255,
  "registry_ids": [
    "V.R196",
    "V.R197",
    "V.R198",
    "V.R199"
  ],
  "related_registry_items": [
    {
      "id": "V.R196",
      "title": "Observational accessibility",
      "url": "/registry/object/V.R196/"
    },
    {
      "id": "V.R197",
      "title": "M87* Shadow Re-Read",
      "url": "/registry/object/V.R197/"
    },
    {
      "id": "V.R198",
      "title": "Sgr A* Shadow Re-Read",
      "url": "/registry/object/V.R198/"
    },
    {
      "id": "V.R199",
      "title": "The strongest single test",
      "url": "/registry/object/V.R199/"
    }
  ],
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookV/Astrophysics/EHTReread.lean#L255-L255",
  "formal_status": "defined",
  "right_rail": {
    "related": [
      {
        "title": "TauLib.BookV.Astrophysics.EHTReread",
        "url": "/verify/taulib/docs/book-v-astrophysics-ehtreread/"
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookV/Astrophysics/EHTReread.lean#L255-L255",
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

- Module: [TauLib.BookV.Astrophysics.EHTReread](/verify/taulib/docs/book-v-astrophysics-ehtreread/)
- Source path: [`TauLib/BookV/Astrophysics/EHTReread.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookV/Astrophysics/EHTReread.lean#L255-L255)
- Source range: L255-L255
- Kind: `def`
- Formal status hint: `defined`

## Registry Links

- `V.R196` — Observational accessibility
- `V.R197` — M87* Shadow Re-Read
- `V.R198` — Sgr A* Shadow Re-Read
- `V.R199` — The strongest single test

## Immediate Comment / Docstring

```lean
-- ============================================================
-- REMARKS (comment-only)
-- ============================================================

-- [V.R196] M87* Shadow Consistent: the M87* shadow imaged by EHT
-- (2019) has angular diameter 42 ± 3 μas, consistent with both GR
-- and the τ-framework prediction for M = 6.5 × 10⁹ M_☉ at D = 16.8 Mpc.

-- [V.R197] Firewall Paradox Dissolved: the AMPS firewall paradox
-- (2012) argued that complementarity, unitarity, and equivalence
-- principle cannot all hold at the horizon. In the τ-framework,
-- the paradox is dissolved because there is no event horizon —
-- only a topology crossing with continuous boundary characters.

-- [V.R198] Sgr A* as Milky Way Test: Sgr A* (the Milky Way's
-- central BH, 4 × 10⁶ M_☉, D = 8.3 kpc) provides the largest
-- angular shadow of any BH (~52 μas). EHT 2022 confirmed the
-- shadow is consistent with the predicted size and morphology.

-- [V.R199] Future EHT Precision Tests: next-generation EHT
-- (ngEHT, space VLBI) will resolve the photon ring sub-structure,
-- enabling direct tests of the near-horizon geometry. The τ and GR
-- predictions diverge only at the n ≥ 2 sub-ring level.

-- ============================================================
-- Sprint 7E: EHT Shadow T² Correction (Wave 7)
-- ============================================================
```

## Source Excerpt

```lean
private def iota_float : Float := 0.341304238875
```

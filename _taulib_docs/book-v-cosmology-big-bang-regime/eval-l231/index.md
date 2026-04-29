---
{
  "projection_kind": "taulib_declaration",
  "title": "eval at L231",
  "permalink": "/verify/taulib/docs/book-v-cosmology-big-bang-regime/eval-l231/",
  "summary_short": "`eval` declaration in `TauLib.BookV.Cosmology.BigBangRegime`.",
  "declaration_id": "TauLib.BookV.Cosmology.BigBangRegime::#eval:231",
  "declaration_slug": "eval-l231",
  "kind": "eval",
  "name": null,
  "module_name": "TauLib.BookV.Cosmology.BigBangRegime",
  "module_url": "/verify/taulib/docs/book-v-cosmology-big-bang-regime/",
  "source_line_start": 231,
  "source_line_end": 231,
  "registry_ids": [
    "V.R209",
    "V.R210",
    "V.R211",
    "V.R212",
    "V.R213"
  ],
  "related_registry_items": [
    {
      "id": "V.R209",
      "title": "No manifold Rightarrow no singularity",
      "url": "/registry/object/V.R209/"
    },
    {
      "id": "V.R210",
      "title": "Planck Epoch Reinterpretation",
      "url": "/registry/object/V.R210/"
    },
    {
      "id": "V.R211",
      "title": "The Penrose--Hawking theorems are not wrong",
      "url": "/registry/object/V.R211/"
    },
    {
      "id": "V.R212",
      "title": "No ``hot'' or ``cold''",
      "url": "/registry/object/V.R212/"
    },
    {
      "id": "V.R213",
      "title": "Falsifiability",
      "url": "/registry/object/V.R213/"
    }
  ],
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookV/Cosmology/BigBangRegime.lean#L231-L231",
  "formal_status": "computed",
  "right_rail": {
    "related": [
      {
        "title": "TauLib.BookV.Cosmology.BigBangRegime",
        "url": "/verify/taulib/docs/book-v-cosmology-big-bang-regime/"
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookV/Cosmology/BigBangRegime.lean#L231-L231",
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

- Module: [TauLib.BookV.Cosmology.BigBangRegime](/verify/taulib/docs/book-v-cosmology-big-bang-regime/)
- Source path: [`TauLib/BookV/Cosmology/BigBangRegime.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookV/Cosmology/BigBangRegime.lean#L231-L231)
- Source range: L231-L231
- Kind: `eval`
- Formal status hint: `computed`

## Registry Links

- `V.R209` — No manifold Rightarrow no singularity
- `V.R210` — Planck Epoch Reinterpretation
- `V.R211` — The Penrose--Hawking theorems are not wrong
- `V.R212` — No ``hot'' or ``cold''
- `V.R213` — Falsifiability

## Immediate Comment / Docstring

```lean
-- ============================================================
-- REMARKS (comment-only)
-- ============================================================

-- [V.R209] No manifold ⇒ no singularity: GR singularities require
-- smooth manifolds with no minimum scale; τ³ is profinite with
-- first element α₁, so a → 0 is structurally inaccessible.
-- The Penrose-Hawking premises simply do not apply.

-- [V.R210] Planck Epoch Reinterpretation: the Planck epoch (t < t_P)
-- is reinterpreted as the first few α-ticks α₁, α₂, ... governed
-- by the SAME τ-Einstein equation. No new physics at Planck scale.

-- [V.R211] The Penrose-Hawking theorems are not wrong — they are
-- mathematically correct within smooth Lorentzian manifolds satisfying
-- standard energy conditions. τ³ is simply not a smooth manifold.

-- [V.R212] No "hot" or "cold": temperature is a chart-level readout
-- requiring thermal equilibrium. At very early α-ticks, no meaningful
-- thermometer exists. The first ticks are "maximally coupled," not
-- "infinitely hot."

-- [V.R213] Falsifiability: the τ-framework makes falsifiable early-
-- universe predictions that differ from orthodox cosmology:
-- no primordial singularity, no trans-Planckian modes.

-- ============================================================
-- SMOKE TESTS
-- ============================================================
```

## Source Excerpt

```lean
#eval canonical_opening.first_tick        -- 1
```

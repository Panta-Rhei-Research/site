---
{
  "projection_kind": "taulib_declaration",
  "title": "defect_step0",
  "permalink": "/verify/taulib/docs/book-v-gravity-field-nonlinear-einstein/defect-step0/",
  "summary_short": "`def` declaration in `TauLib.BookV.GravityField.NonlinearEinstein`.",
  "declaration_id": "TauLib.BookV.GravityField.NonlinearEinstein::defect_step0",
  "declaration_slug": "defect-step0",
  "kind": "def",
  "name": "defect_step0",
  "module_name": "TauLib.BookV.GravityField.NonlinearEinstein",
  "module_url": "/verify/taulib/docs/book-v-gravity-field-nonlinear-einstein/",
  "source_line_start": 398,
  "source_line_end": 402,
  "registry_ids": [
    "V.R77",
    "V.R80"
  ],
  "related_registry_items": [
    {
      "id": "V.R77",
      "title": "Why ``address''?",
      "url": "/registry/object/V.R77/"
    },
    {
      "id": "V.R80",
      "title": "Extremal black holes",
      "url": "/registry/object/V.R80/"
    }
  ],
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookV/GravityField/NonlinearEinstein.lean#L398-L402",
  "formal_status": "defined",
  "right_rail": {
    "related": [
      {
        "title": "TauLib.BookV.GravityField.NonlinearEinstein",
        "url": "/verify/taulib/docs/book-v-gravity-field-nonlinear-einstein/"
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookV/GravityField/NonlinearEinstein.lean#L398-L402",
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

- Module: [TauLib.BookV.GravityField.NonlinearEinstein](/verify/taulib/docs/book-v-gravity-field-nonlinear-einstein/)
- Source path: [`TauLib/BookV/GravityField/NonlinearEinstein.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookV/GravityField/NonlinearEinstein.lean#L398-L402)
- Source range: L398-L402
- Kind: `def`
- Formal status hint: `defined`

## Registry Links

- `V.R77` — Why ``address''?
- `V.R80` — Extremal black holes

## Immediate Comment / Docstring

```lean
-- ============================================================
-- [V.R77] ADDRESS RESOLUTION ANALOGY
-- ============================================================

-- [V.R77] The NF Einstein iteration is analogous to address
-- resolution in a network: each step resolves finer details
-- of the gravitational field, converging to the exact solution.
-- The cocycle defect is the "routing error" at each step.

-- ============================================================
-- [V.R80] EXTREMAL BLACK HOLES
-- ============================================================

-- [V.R80] Extremal black holes (maximal spin/charge for given mass)
-- in the τ-framework correspond to configurations where the
-- NF iteration depth exactly saturates the density bound.
-- No naked singularities exist: cosmic censorship is automatic
-- from density saturation.

-- ============================================================
-- SMOKE TESTS
-- ============================================================

-- Cocycle defect examples
```

## Source Excerpt

```lean
def defect_step0 : CocycleDefect where
  defect_numer := 100
  defect_denom := 1000
  denom_pos := by omega
  step := 0
```

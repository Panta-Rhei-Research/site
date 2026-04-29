---
{
  "projection_kind": "taulib_declaration",
  "title": "eval at L305",
  "permalink": "/verify/taulib/docs/book-v-coda-constants-ledger/eval-l305/",
  "summary_short": "`eval` declaration in `TauLib.BookV.Coda.ConstantsLedger`.",
  "declaration_id": "TauLib.BookV.Coda.ConstantsLedger::#eval:305",
  "declaration_slug": "eval-l305",
  "kind": "eval",
  "name": null,
  "module_name": "TauLib.BookV.Coda.ConstantsLedger",
  "module_url": "/verify/taulib/docs/book-v-coda-constants-ledger/",
  "source_line_start": 305,
  "source_line_end": 305,
  "registry_ids": [
    "V.R296",
    "V.R299",
    "V.R304",
    "V.R307"
  ],
  "related_registry_items": [
    {
      "id": "V.R296",
      "title": "The honest status of galaxy fits",
      "url": "/registry/object/V.R296/"
    },
    {
      "id": "V.R299",
      "title": "Scope of the delta_A prediction",
      "url": "/registry/object/V.R299/"
    },
    {
      "id": "V.R304",
      "title": "Falsifiability as strength",
      "url": "/registry/object/V.R304/"
    },
    {
      "id": "V.R307",
      "title": "The neutrino exponent",
      "url": "/registry/object/V.R307/"
    }
  ],
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookV/Coda/ConstantsLedger.lean#L305-L305",
  "formal_status": "computed",
  "right_rail": {
    "related": [
      {
        "title": "TauLib.BookV.Coda.ConstantsLedger",
        "url": "/verify/taulib/docs/book-v-coda-constants-ledger/"
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookV/Coda/ConstantsLedger.lean#L305-L305",
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

- Module: [TauLib.BookV.Coda.ConstantsLedger](/verify/taulib/docs/book-v-coda-constants-ledger/)
- Source path: [`TauLib/BookV/Coda/ConstantsLedger.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookV/Coda/ConstantsLedger.lean#L305-L305)
- Source range: L305-L305
- Kind: `eval`
- Formal status hint: `computed`

## Registry Links

- `V.R296` — The honest status of galaxy fits
- `V.R299` — Scope of the delta_A prediction
- `V.R304` — Falsifiability as strength
- `V.R307` — The neutrino exponent

## Immediate Comment / Docstring

```lean
-- [V.R296] The honest status of galaxy fits: tau predicts rotation
-- curves from sector-exhaustion (no dark matter), but detailed fits
-- require computation beyond current scope.

-- [V.R299] Scope of the delta_A prediction: delta_A/m_n ~ (sqrt3/2)
-- * iota_tau^6 (0.55%). Accurate but the Level 1 correction needs
-- weak-sector computation.

-- [V.R304] Falsifiability as strength: a framework that cannot be
-- falsified cannot be tested. tau's willingness to make specific
-- predictions (Lambda = 0, no DM, no evaporation) is a strength.

-- [V.R307] The neutrino exponent: m_3(nu) ~ m_e * iota_tau^15.
-- The exponent 15 = 7 + 2*4 comes from the spectral gap between
-- the fiber-charged (electron) and fiber-neutral (neutrino) modes.

-- ============================================================
-- SMOKE TESTS
-- ============================================================
```

## Source Excerpt

```lean
#eval constants_ledger.length  -- 10
```

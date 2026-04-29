---
{
  "projection_kind": "taulib_declaration",
  "title": "constants_ledger",
  "permalink": "/verify/taulib/docs/book-v-coda-constants-ledger/constants-ledger/",
  "summary_short": "`def` declaration in `TauLib.BookV.Coda.ConstantsLedger`.",
  "declaration_id": "TauLib.BookV.Coda.ConstantsLedger::constants_ledger",
  "declaration_slug": "constants-ledger",
  "kind": "def",
  "name": "constants_ledger",
  "module_name": "TauLib.BookV.Coda.ConstantsLedger",
  "module_url": "/verify/taulib/docs/book-v-coda-constants-ledger/",
  "source_line_start": 92,
  "source_line_end": 132,
  "registry_ids": [],
  "related_registry_items": [],
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookV/Coda/ConstantsLedger.lean#L92-L132",
  "formal_status": "defined",
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookV/Coda/ConstantsLedger.lean#L92-L132",
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

- Module: [TauLib.BookV.Coda.ConstantsLedger](/verify/taulib/docs/book-v-coda-constants-ledger/)
- Source path: [`TauLib/BookV/Coda/ConstantsLedger.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookV/Coda/ConstantsLedger.lean#L92-L132)
- Source range: L92-L132
- Kind: `def`
- Formal status hint: `defined`

## Registry Links

- No Registry IDs were detected in this declaration block.

## Immediate Comment / Docstring

```lean
/-- The complete Book V constants ledger. -/
```

## Source Excerpt

```lean
def constants_ledger : List LedgerEntry :=
  [ { name := "Electron mass (m_e)"
      prediction := "m_n / R, R = iota^(-7) - (sqrt3 + pi^3*alpha^2)*iota^(-2)"
      precision := "0.025 ppm"
      scope := .TauEffective }
  , { name := "Gravitational constant (G)"
      prediction := "Closing identity: alpha_G = alpha^18 * (chi*kn/2)"
      precision := "3 ppm"
      scope := .Conjectural }
  , { name := "Cosmological constant (Lambda)"
      prediction := "Lambda = 0 exactly"
      precision := "exact"
      scope := .TauEffective }
  , { name := "Dark matter"
      prediction := "absent (5 sectors exhaust budget)"
      precision := "N/A"
      scope := .TauEffective }
  , { name := "Dark energy"
      prediction := "absent (S_def -> S_ref artifact)"
      precision := "N/A"
      scope := .TauEffective }
  , { name := "Neutrino mass (heaviest)"
      prediction := "m_e * iota_tau^15 ~ 50.7 meV"
      precision := "~3%"
      scope := .Conjectural }
  , { name := "Equation of state w(z)"
      prediction := "varies with z, not exactly -1"
      precision := "TBD"
      scope := .TauEffective }
  , { name := "BH evaporation"
      prediction := "absent (No Shrink)"
      precision := "N/A"
      scope := .TauEffective }
  , { name := "Singularities"
      prediction := "absent (profinite tower finite)"
      precision := "N/A"
      scope := .TauEffective }
  , { name := "UV divergences"
      prediction := "absent (spectral sums converge)"
      precision := "N/A"
      scope := .TauEffective } ]
```

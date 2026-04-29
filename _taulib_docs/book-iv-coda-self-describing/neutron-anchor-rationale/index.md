---
{
  "projection_kind": "taulib_declaration",
  "title": "NeutronAnchorRationale",
  "permalink": "/verify/taulib/docs/book-iv-coda-self-describing/neutron-anchor-rationale/",
  "summary_short": "`structure` declaration in `TauLib.BookIV.Coda.SelfDescribing`.",
  "declaration_id": "TauLib.BookIV.Coda.SelfDescribing::NeutronAnchorRationale",
  "declaration_slug": "neutron-anchor-rationale",
  "kind": "structure",
  "name": "NeutronAnchorRationale",
  "module_name": "TauLib.BookIV.Coda.SelfDescribing",
  "module_url": "/verify/taulib/docs/book-iv-coda-self-describing/",
  "source_line_start": 67,
  "source_line_end": 78,
  "registry_ids": [
    "IV.R190"
  ],
  "related_registry_items": [
    {
      "id": "IV.R190",
      "title": "Why neutron not electron as anchor",
      "url": "/registry/object/IV.R190/"
    }
  ],
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIV/Coda/SelfDescribing.lean#L67-L78",
  "formal_status": "defined",
  "right_rail": {
    "related": [
      {
        "title": "TauLib.BookIV.Coda.SelfDescribing",
        "url": "/verify/taulib/docs/book-iv-coda-self-describing/"
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIV/Coda/SelfDescribing.lean#L67-L78",
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

- Module: [TauLib.BookIV.Coda.SelfDescribing](/verify/taulib/docs/book-iv-coda-self-describing/)
- Source path: [`TauLib/BookIV/Coda/SelfDescribing.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIV/Coda/SelfDescribing.lean#L67-L78)
- Source range: L67-L78
- Kind: `structure`
- Formal status hint: `defined`

## Registry Links

- `IV.R190` — Why neutron not electron as anchor

## Immediate Comment / Docstring

```lean
/-- [IV.R190] The neutron is chosen as calibration anchor because it is
    ontologically prior: a composite defect bundle whose existence is
    guaranteed by the strong-sector structure (C-sector confinement
    with coupling kappa(C;3) = iota_tau^3 / (1 - iota_tau)).

    The ontological priority chain is:
    neutron -> proton -> electron -> Planck mass

    Each subsequent quantity is derived from the previous one:
    - m_p = m_n - delta_A (proton-neutron mass difference)
    - m_e = m_n / R (mass ratio R = iota_tau^(-7) - correction)
    - m_P = m_n / (alpha^9 * sqrt(chi*kappa_n/2)) (closing identity)

    Choosing the electron as anchor would require deriving m_n from m_e,
    inverting the natural derivation direction. -/
```

## Source Excerpt

```lean
structure NeutronAnchorRationale where
  /-- Neutron is ontologically prior. -/
  ontologically_prior : Bool := true
  /-- Guaranteed by C-sector confinement. -/
  confinement_guarantees : Bool := true
  /-- Priority chain length. -/
  chain_length : Nat := 4
  /-- Priority chain. -/
  chain : List String := ["neutron", "proton", "electron", "Planck mass"]
  /-- Inverting would be unnatural. -/
  inversion_unnatural : Bool := true
  deriving Repr
```

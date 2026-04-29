---
{
  "projection_kind": "taulib_declaration",
  "title": "AsymptoticFreedomSpectral",
  "permalink": "/verify/taulib/docs/book-iv-strong-strong-coupling/asymptotic-freedom-spectral/",
  "summary_short": "`structure` declaration in `TauLib.BookIV.Strong.StrongCoupling`.",
  "declaration_id": "TauLib.BookIV.Strong.StrongCoupling::AsymptoticFreedomSpectral",
  "declaration_slug": "asymptotic-freedom-spectral",
  "kind": "structure",
  "name": "AsymptoticFreedomSpectral",
  "module_name": "TauLib.BookIV.Strong.StrongCoupling",
  "module_url": "/verify/taulib/docs/book-iv-strong-strong-coupling/",
  "source_line_start": 297,
  "source_line_end": 310,
  "registry_ids": [
    "IV.P112"
  ],
  "related_registry_items": [
    {
      "id": "IV.P112",
      "title": "Asymptotic freedom as spectral tightening",
      "url": "/registry/object/IV.P112/"
    }
  ],
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIV/Strong/StrongCoupling.lean#L297-L310",
  "formal_status": "defined",
  "right_rail": {
    "related": [
      {
        "title": "TauLib.BookIV.Strong.StrongCoupling",
        "url": "/verify/taulib/docs/book-iv-strong-strong-coupling/"
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIV/Strong/StrongCoupling.lean#L297-L310",
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

- Module: [TauLib.BookIV.Strong.StrongCoupling](/verify/taulib/docs/book-iv-strong-strong-coupling/)
- Source path: [`TauLib/BookIV/Strong/StrongCoupling.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIV/Strong/StrongCoupling.lean#L297-L310)
- Source range: L297-L310
- Kind: `structure`
- Formal status hint: `defined`

## Registry Links

- `IV.P112` — Asymptotic freedom as spectral tightening

## Immediate Comment / Docstring

```lean
/-- [IV.P112] Asymptotic freedom as spectral tightening:
    at high energy (mu >> Lambda_QCD), the C-sector readout
    R_C(mu^2) < 1 and decreases with increasing mu.
    Chi_minus-dominant character modes become increasingly
    tightly concentrated under spectral tightening.

    The orthodox beta function coefficient b_0 = (11*N_c - 2*N_f)/(12*pi)
    with N_c = 3, N_f = 6 gives b_0 = (33-12)/(12*pi) > 0. -/
```

## Source Excerpt

```lean
structure AsymptoticFreedomSpectral where
  /-- Readout decreases at high energy. -/
  decreasing_at_high_E : Bool := true
  /-- Mechanism: spectral tightening. -/
  mechanism : String := "chi_minus spectral tightening"
  /-- Beta function coefficient b_0 > 0 (from N_c = 3, N_f = 6). -/
  beta_positive : Bool := true
  /-- N_c = 3. -/
  num_colors : Nat := 3
  /-- N_f = 6. -/
  num_flavors : Nat := 6
  /-- 11*N_c - 2*N_f = 21 > 0. -/
  beta_numerator : Nat := 21
  deriving Repr
```

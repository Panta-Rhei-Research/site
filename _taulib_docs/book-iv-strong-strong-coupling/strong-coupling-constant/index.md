---
{
  "projection_kind": "taulib_declaration",
  "title": "StrongCouplingConstant",
  "permalink": "/verify/taulib/docs/book-iv-strong-strong-coupling/strong-coupling-constant/",
  "summary_short": "`structure` declaration in `TauLib.BookIV.Strong.StrongCoupling`.",
  "declaration_id": "TauLib.BookIV.Strong.StrongCoupling::StrongCouplingConstant",
  "declaration_slug": "strong-coupling-constant",
  "kind": "structure",
  "name": "StrongCouplingConstant",
  "module_name": "TauLib.BookIV.Strong.StrongCoupling",
  "module_url": "/verify/taulib/docs/book-iv-strong-strong-coupling/",
  "source_line_start": 92,
  "source_line_end": 103,
  "registry_ids": [
    "IV.D182"
  ],
  "related_registry_items": [
    {
      "id": "IV.D182",
      "title": "The τ-strong coupling constant",
      "url": "/registry/object/IV.D182/"
    }
  ],
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIV/Strong/StrongCoupling.lean#L92-L103",
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIV/Strong/StrongCoupling.lean#L92-L103",
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
- Source path: [`TauLib/BookIV/Strong/StrongCoupling.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIV/Strong/StrongCoupling.lean#L92-L103)
- Source range: L92-L103
- Kind: `structure`
- Formal status hint: `defined`

## Registry Links

- `IV.D182` — The τ-strong coupling constant

## Immediate Comment / Docstring

```lean
/-- [IV.D182] The tau-strong coupling constant:
    alpha_s^* := NF(Lift_pi^omega) in Fix(s).
    Normal-form selector applied to the pi-lift omega-limit.
    Determined entirely by iota_tau and the boundary holonomy structure.

    Numerical value: kappa(C;3) = iota_tau^3/(1-iota_tau) approx 0.0604. -/
```

## Source Excerpt

```lean
structure StrongCouplingConstant where
  /-- NF selector applied to lift limit. -/
  construction : String := "NF(Lift_pi^omega)"
  /-- Lives in Fix(s). -/
  lives_in : String := "Fix(s)"
  /-- Equals kappa(C;3). -/
  equals_kappa_C : Bool := true
  /-- Coupling numerator (same as strong_sector). -/
  coupling_numer : Nat := iota_cu_numer * iotaD
  /-- Coupling denominator (same as strong_sector). -/
  coupling_denom : Nat := iota_cu_denom * (iotaD - iota)
  deriving Repr
```

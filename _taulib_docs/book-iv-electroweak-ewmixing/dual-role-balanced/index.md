---
{
  "projection_kind": "taulib_declaration",
  "title": "DualRoleBalanced",
  "permalink": "/verify/taulib/docs/book-iv-electroweak-ewmixing/dual-role-balanced/",
  "summary_short": "`structure` declaration in `TauLib.BookIV.Electroweak.EWMixing`.",
  "declaration_id": "TauLib.BookIV.Electroweak.EWMixing::DualRoleBalanced",
  "declaration_slug": "dual-role-balanced",
  "kind": "structure",
  "name": "DualRoleBalanced",
  "module_name": "TauLib.BookIV.Electroweak.EWMixing",
  "module_url": "/verify/taulib/docs/book-iv-electroweak-ewmixing/",
  "source_line_start": 416,
  "source_line_end": 425,
  "registry_ids": [
    "IV.P71"
  ],
  "related_registry_items": [
    {
      "id": "IV.P71",
      "title": "Parity Bridge and Mixing",
      "url": "/registry/object/IV.P71/"
    }
  ],
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIV/Electroweak/EWMixing.lean#L416-L425",
  "formal_status": "defined",
  "right_rail": {
    "related": [
      {
        "title": "TauLib.BookIV.Electroweak.EWMixing",
        "url": "/verify/taulib/docs/book-iv-electroweak-ewmixing/"
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIV/Electroweak/EWMixing.lean#L416-L425",
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

- Module: [TauLib.BookIV.Electroweak.EWMixing](/verify/taulib/docs/book-iv-electroweak-ewmixing/)
- Source path: [`TauLib/BookIV/Electroweak/EWMixing.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIV/Electroweak/EWMixing.lean#L416-L425)
- Source range: L416-L425
- Kind: `structure`
- Formal status hint: `defined`

## Registry Links

- `IV.P71` — Parity Bridge and Mixing

## Immediate Comment / Docstring

```lean
/-- [IV.P71] The weak sector A plays a dual role:
    1. As the temporal arrow (κ_A = ι_τ, the master constant itself).
    2. As the unique balanced-polarity sector enabling EW mixing.

    This duality is not a coincidence — it is forced by the structure:
    balanced polarity (pol = 1) means equal χ₊/χ₋ content, which
    is exactly the condition for a sector to serve as the "pivot"
    in the temporal complement κ_A + κ_D = 1. The same balance
    that makes A the temporal arrow also makes it the unique
    EW mixing partner. -/
```

## Source Excerpt

```lean
structure DualRoleBalanced where
  /-- Sector A. -/
  sector : Sector := .A
  /-- Role 1: temporal arrow. -/
  role_temporal : String := "kappa_A = iota_tau (master constant)"
  /-- Role 2: EW mixing pivot. -/
  role_mixing : String := "unique balanced polarity for EW mixing"
  /-- Both roles forced by pol = 1. -/
  forced_by_balance : Bool := true
  deriving Repr
```

---
{
  "projection_kind": "taulib_declaration",
  "title": "MatterCharacter",
  "permalink": "/verify/taulib/docs/book-v-gravity-einstein-equation/matter-character/",
  "summary_short": "`structure` declaration in `TauLib.BookV.Gravity.EinsteinEquation`.",
  "declaration_id": "TauLib.BookV.Gravity.EinsteinEquation::MatterCharacter",
  "declaration_slug": "matter-character",
  "kind": "structure",
  "name": "MatterCharacter",
  "module_name": "TauLib.BookV.Gravity.EinsteinEquation",
  "module_url": "/verify/taulib/docs/book-v-gravity-einstein-equation/",
  "source_line_start": 86,
  "source_line_end": 97,
  "registry_ids": [
    "V.D03"
  ],
  "related_registry_items": [],
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookV/Gravity/EinsteinEquation.lean#L86-L97",
  "formal_status": "defined",
  "right_rail": {
    "related": [
      {
        "title": "TauLib.BookV.Gravity.EinsteinEquation",
        "url": "/verify/taulib/docs/book-v-gravity-einstein-equation/"
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookV/Gravity/EinsteinEquation.lean#L86-L97",
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

- Module: [TauLib.BookV.Gravity.EinsteinEquation](/verify/taulib/docs/book-v-gravity-einstein-equation/)
- Source path: [`TauLib/BookV/Gravity/EinsteinEquation.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookV/Gravity/EinsteinEquation.lean#L86-L97)
- Source range: L86-L97
- Kind: `structure`
- Formal status hint: `defined`

## Registry Links

- No Registry IDs were detected in this declaration block.

## Immediate Comment / Docstring

```lean
/-- [V.D03] Matter character T^mat: the direct sum of EM, Weak, and
    Strong sector boundary projections.

    T^mat_n(x) = η_n(T^EM_n(x) ⊕ T^wk_n(x) ⊕ T^s_n(x))

    The matter character includes exactly the three spatial sectors
    (B, A, C) but NOT gravity (D). Gravity appears on the LHS
    of the Einstein equation as curvature. -/
```

## Source Excerpt

```lean
structure MatterCharacter where
  /-- EM sector contribution T^EM (B-sector). -/
  em_numer : Nat
  /-- Weak sector contribution T^wk (A-sector). -/
  weak_numer : Nat
  /-- Strong sector contribution T^s (C-sector). -/
  strong_numer : Nat
  /-- Common denominator for all three. -/
  denom : Nat
  /-- Denominator positive. -/
  denom_pos : denom > 0
  deriving Repr
```

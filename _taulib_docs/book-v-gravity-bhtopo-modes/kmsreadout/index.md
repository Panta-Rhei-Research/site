---
{
  "projection_kind": "taulib_declaration",
  "title": "KMSReadout",
  "permalink": "/verify/taulib/docs/book-v-gravity-bhtopo-modes/kmsreadout/",
  "summary_short": "`structure` declaration in `TauLib.BookV.Gravity.BHTopoModes`.",
  "declaration_id": "TauLib.BookV.Gravity.BHTopoModes::KMSReadout",
  "declaration_slug": "kmsreadout",
  "kind": "structure",
  "name": "KMSReadout",
  "module_name": "TauLib.BookV.Gravity.BHTopoModes",
  "module_url": "/verify/taulib/docs/book-v-gravity-bhtopo-modes/",
  "source_line_start": 587,
  "source_line_end": 598,
  "registry_ids": [],
  "related_registry_items": [],
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookV/Gravity/BHTopoModes.lean#L587-L598",
  "formal_status": "defined",
  "right_rail": {
    "related": [
      {
        "title": "TauLib.BookV.Gravity.BHTopoModes",
        "url": "/verify/taulib/docs/book-v-gravity-bhtopo-modes/"
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookV/Gravity/BHTopoModes.lean#L587-L598",
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

- Module: [TauLib.BookV.Gravity.BHTopoModes](/verify/taulib/docs/book-v-gravity-bhtopo-modes/)
- Source path: [`TauLib/BookV/Gravity/BHTopoModes.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookV/Gravity/BHTopoModes.lean#L587-L598)
- Source range: L587-L598
- Kind: `structure`
- Formal status hint: `defined`

## Registry Links

- No Registry IDs were detected in this declaration block.

## Immediate Comment / Docstring

```lean
/-- [Sprint 22C] KMS readout derivation. The Planckian spectrum follows from the
    KMS condition on the boundary algebra without Bogoliubov transformations.

    1. H_∂[ω] restricted to L = S¹∨S¹ is a bosonic algebra (Book IV, K5+K6)
    2. The readout Gibbs state (V.D276, τ-effective) is max-entropy at T_H
    3. KMS condition (Haag-Hugenholtz-Winnink 1967): thermal equilibrium on
       a bosonic algebra has unique spectral distribution = Bose-Einstein
    4. Therefore B(ν,T_H) = (2hν³/c²)/(exp(hν/k_BT_H)−1) — Planckian. QED. -/
```

## Source Excerpt

```lean
structure KMSReadout where
  /-- Boundary algebra is bosonic (from Book IV K5+K6). -/
  boundary_algebra_bosonic : Nat := 1
  /-- Readout state satisfies KMS condition at T_H. -/
  kms_condition_satisfied : Nat := 1
  /-- Spectral distribution is unique (Haag-Hugenholtz-Winnink). -/
  spectral_uniqueness : Nat := 1
  /-- Resulting spectrum is Planckian. -/
  is_planckian : Nat := 1
  /-- No Bogoliubov transformation needed. -/
  no_bogoliubov : Nat := 1
  deriving Repr
```

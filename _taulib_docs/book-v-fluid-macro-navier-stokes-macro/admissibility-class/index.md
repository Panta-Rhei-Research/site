---
{
  "projection_kind": "taulib_declaration",
  "title": "AdmissibilityClass",
  "permalink": "/verify/taulib/docs/book-v-fluid-macro-navier-stokes-macro/admissibility-class/",
  "summary_short": "`structure` declaration in `TauLib.BookV.FluidMacro.NavierStokesMacro`.",
  "declaration_id": "TauLib.BookV.FluidMacro.NavierStokesMacro::AdmissibilityClass",
  "declaration_slug": "admissibility-class",
  "kind": "structure",
  "name": "AdmissibilityClass",
  "module_name": "TauLib.BookV.FluidMacro.NavierStokesMacro",
  "module_url": "/verify/taulib/docs/book-v-fluid-macro-navier-stokes-macro/",
  "source_line_start": 340,
  "source_line_end": 349,
  "registry_ids": [
    "V.D315"
  ],
  "related_registry_items": [
    {
      "id": "V.D315",
      "title": "Admissibility Class",
      "url": "/registry/object/V.D315/"
    }
  ],
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookV/FluidMacro/NavierStokesMacro.lean#L340-L349",
  "formal_status": "defined",
  "right_rail": {
    "related": [
      {
        "title": "TauLib.BookV.FluidMacro.NavierStokesMacro",
        "url": "/verify/taulib/docs/book-v-fluid-macro-navier-stokes-macro/"
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookV/FluidMacro/NavierStokesMacro.lean#L340-L349",
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

- Module: [TauLib.BookV.FluidMacro.NavierStokesMacro](/verify/taulib/docs/book-v-fluid-macro-navier-stokes-macro/)
- Source path: [`TauLib/BookV/FluidMacro/NavierStokesMacro.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookV/FluidMacro/NavierStokesMacro.lean#L340-L349)
- Source range: L340-L349
- Kind: `structure`
- Formal status hint: `defined`

## Registry Links

- `V.D315` — Admissibility Class

## Immediate Comment / Docstring

```lean
/-- [V.D315] Admissibility class comparison.

    τ-admissible: ABCD bound + sector decomposition + NF confluence on τ³
    Schwartz: C^∞ with rapid decay on ℝ³
    The two classes overlap but neither contains the other. -/
```

## Source Excerpt

```lean
structure AdmissibilityClass where
  /-- Number of τ-admissibility conditions. -/
  tau_conditions : Nat := 3
  /-- Conditions: ABCD(1), sector(2), NF(3). -/
  abcd : Nat := 1
  sector : Nat := 1
  nf : Nat := 1
  /-- Sum check. -/
  sum_check : abcd + sector + nf = tau_conditions := by omega
  deriving Repr
```

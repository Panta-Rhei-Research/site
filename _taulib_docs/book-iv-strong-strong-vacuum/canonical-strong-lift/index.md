---
{
  "projection_kind": "taulib_declaration",
  "title": "CanonicalStrongLift",
  "permalink": "/verify/taulib/docs/book-iv-strong-strong-vacuum/canonical-strong-lift/",
  "summary_short": "`structure` declaration in `TauLib.BookIV.Strong.StrongVacuum`.",
  "declaration_id": "TauLib.BookIV.Strong.StrongVacuum::CanonicalStrongLift",
  "declaration_slug": "canonical-strong-lift",
  "kind": "structure",
  "name": "CanonicalStrongLift",
  "module_name": "TauLib.BookIV.Strong.StrongVacuum",
  "module_url": "/verify/taulib/docs/book-iv-strong-strong-vacuum/",
  "source_line_start": 358,
  "source_line_end": 367,
  "registry_ids": [
    "IV.D153"
  ],
  "related_registry_items": [
    {
      "id": "IV.D153",
      "title": "Canonical strong lift",
      "url": "/registry/object/IV.D153/"
    }
  ],
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIV/Strong/StrongVacuum.lean#L358-L367",
  "formal_status": "defined",
  "right_rail": {
    "related": [
      {
        "title": "TauLib.BookIV.Strong.StrongVacuum",
        "url": "/verify/taulib/docs/book-iv-strong-strong-vacuum/"
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIV/Strong/StrongVacuum.lean#L358-L367",
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

- Module: [TauLib.BookIV.Strong.StrongVacuum](/verify/taulib/docs/book-iv-strong-strong-vacuum/)
- Source path: [`TauLib/BookIV/Strong/StrongVacuum.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIV/Strong/StrongVacuum.lean#L358-L367)
- Source range: L358-L367
- Kind: `structure`
- Formal status hint: `defined`

## Registry Links

- `IV.D153` — Canonical strong lift

## Immediate Comment / Docstring

```lean
/-- [IV.D153] Canonical strong lift Lift_{s,n}: NFMin-minimal element
    of HolEnd_tau(s)[n] achieving the same defect as the vacuum.
    Omega-limit Lift_s = varprojlim Lift_{s,n} is the simplest
    endomorphism preserving the strong vacuum. -/
```

## Source Excerpt

```lean
structure CanonicalStrongLift where
  /-- Stage n. -/
  stage : Nat
  /-- Achieves vacuum defect value. -/
  achieves_vacuum_defect : Bool := true
  /-- NFMin-minimal among candidates. -/
  nfmin_minimal : Bool := true
  /-- Truncation coherent. -/
  truncation_coherent : Bool := true
  deriving Repr
```

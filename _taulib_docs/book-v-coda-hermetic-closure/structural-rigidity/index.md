---
{
  "projection_kind": "taulib_declaration",
  "title": "StructuralRigidity",
  "permalink": "/verify/taulib/docs/book-v-coda-hermetic-closure/structural-rigidity/",
  "summary_short": "`structure` declaration in `TauLib.BookV.Coda.HermeticClosure`.",
  "declaration_id": "TauLib.BookV.Coda.HermeticClosure::StructuralRigidity",
  "declaration_slug": "structural-rigidity",
  "kind": "structure",
  "name": "StructuralRigidity",
  "module_name": "TauLib.BookV.Coda.HermeticClosure",
  "module_url": "/verify/taulib/docs/book-v-coda-hermetic-closure/",
  "source_line_start": 283,
  "source_line_end": 298,
  "registry_ids": [
    "V.P120"
  ],
  "related_registry_items": [
    {
      "id": "V.P120",
      "title": "Structural rigidity",
      "url": "/registry/object/V.P120/"
    }
  ],
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookV/Coda/HermeticClosure.lean#L283-L298",
  "formal_status": "defined",
  "right_rail": {
    "related": [
      {
        "title": "TauLib.BookV.Coda.HermeticClosure",
        "url": "/verify/taulib/docs/book-v-coda-hermetic-closure/"
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookV/Coda/HermeticClosure.lean#L283-L298",
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

- Module: [TauLib.BookV.Coda.HermeticClosure](/verify/taulib/docs/book-v-coda-hermetic-closure/)
- Source path: [`TauLib/BookV/Coda/HermeticClosure.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookV/Coda/HermeticClosure.lean#L283-L298)
- Source range: L283-L298
- Kind: `structure`
- Formal status hint: `defined`

## Registry Links

- `V.P120` — Structural rigidity

## Immediate Comment / Docstring

```lean
/-- [V.P120] Structural rigidity: the axiom system K0-K6 admits a
    unique coherence kernel. Every dimensionless constant is derived.
    No continuous variation is possible.

    - K0-K6 → unique boundary algebra on L
    - Unique boundary → unique ι_τ = 2/(π+e)
    - Unique ι_τ → unique coupling budget
    - No free parameters → no continuous deformation -/
```

## Source Excerpt

```lean
structure StructuralRigidity where
  /-- Number of axioms in the kernel. -/
  n_axioms : Nat
  /-- Seven axioms K0-K6. -/
  axioms_eq : n_axioms = 7
  /-- Coherence kernel is unique. -/
  kernel_unique : Bool := true
  /-- All constants derived. -/
  all_derived : Bool := true
  /-- No continuous variation. -/
  no_variation : Bool := true
  /-- Number of derived constants (all from ι_τ). -/
  n_derived_constants : Nat := 0
  /-- Number of free parameters. -/
  n_free : Nat := 0
  deriving Repr
```

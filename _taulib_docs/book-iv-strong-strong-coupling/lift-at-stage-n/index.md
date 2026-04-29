---
{
  "projection_kind": "taulib_declaration",
  "title": "LiftAtStageN",
  "permalink": "/verify/taulib/docs/book-iv-strong-strong-coupling/lift-at-stage-n/",
  "summary_short": "`structure` declaration in `TauLib.BookIV.Strong.StrongCoupling`.",
  "declaration_id": "TauLib.BookIV.Strong.StrongCoupling::LiftAtStageN",
  "declaration_slug": "lift-at-stage-n",
  "kind": "structure",
  "name": "LiftAtStageN",
  "module_name": "TauLib.BookIV.Strong.StrongCoupling",
  "module_url": "/verify/taulib/docs/book-iv-strong-strong-coupling/",
  "source_line_start": 52,
  "source_line_end": 61,
  "registry_ids": [
    "IV.D180"
  ],
  "related_registry_items": [
    {
      "id": "IV.D180",
      "title": "π-lift at stage n",
      "url": "/registry/object/IV.D180/"
    }
  ],
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIV/Strong/StrongCoupling.lean#L52-L61",
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIV/Strong/StrongCoupling.lean#L52-L61",
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
- Source path: [`TauLib/BookIV/Strong/StrongCoupling.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIV/Strong/StrongCoupling.lean#L52-L61)
- Source range: L52-L61
- Kind: `structure`
- Formal status hint: `defined`

## Registry Links

- `IV.D180` — π-lift at stage n

## Immediate Comment / Docstring

```lean
/-- [IV.D180] The pi-lift at stage n: restriction of the canonical
    strong lift Lift_{s,n} to pi-supported endomorphisms, selecting
    the NF-minimal element. Deep inelastic scattering analogue. -/
```

## Source Excerpt

```lean
structure LiftAtStageN where
  /-- Stage n. -/
  stage : Nat
  /-- Restricted to pi-supported endomorphisms. -/
  pi_supported : Bool := true
  /-- NF-minimal among candidates. -/
  nf_minimal : Bool := true
  /-- Active from depth 3. -/
  activation_depth : Nat := 3
  deriving Repr
```

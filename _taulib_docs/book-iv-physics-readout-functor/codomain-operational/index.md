---
{
  "projection_kind": "taulib_declaration",
  "title": "codomain_operational",
  "permalink": "/verify/taulib/docs/book-iv-physics-readout-functor/codomain-operational/",
  "summary_short": "`theorem` declaration in `TauLib.BookIV.Physics.ReadoutFunctor`.",
  "declaration_id": "TauLib.BookIV.Physics.ReadoutFunctor::codomain_operational",
  "declaration_slug": "codomain-operational",
  "kind": "theorem",
  "name": "codomain_operational",
  "module_name": "TauLib.BookIV.Physics.ReadoutFunctor",
  "module_url": "/verify/taulib/docs/book-iv-physics-readout-functor/",
  "source_line_start": 230,
  "source_line_end": 235,
  "registry_ids": [
    "IV.P177"
  ],
  "related_registry_items": [
    {
      "id": "IV.P177",
      "title": "Codomain Is Operational",
      "url": "/registry/object/IV.P177/"
    }
  ],
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIV/Physics/ReadoutFunctor.lean#L230-L235",
  "formal_status": "formalized",
  "right_rail": {
    "related": [
      {
        "title": "TauLib.BookIV.Physics.ReadoutFunctor",
        "url": "/verify/taulib/docs/book-iv-physics-readout-functor/"
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIV/Physics/ReadoutFunctor.lean#L230-L235",
        "external": true
      }
    ],
    "meta": {
      "type": "TauLib Declaration",
      "kind": "theorem",
      "status": "formalized"
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

- Module: [TauLib.BookIV.Physics.ReadoutFunctor](/verify/taulib/docs/book-iv-physics-readout-functor/)
- Source path: [`TauLib/BookIV/Physics/ReadoutFunctor.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIV/Physics/ReadoutFunctor.lean#L230-L235)
- Source range: L230-L235
- Kind: `theorem`
- Formal status hint: `formalized`

## Registry Links

- `IV.P177` — Codomain Is Operational

## Immediate Comment / Docstring

```lean
/-- [IV.P177] The codomain of R_μ is operational: each measurement
    procedure specifies a protocol, not just a number. -/
```

## Source Excerpt

```lean
theorem codomain_operational :
    neutron_procedure.protocol ≠ "" ∧
    electron_procedure.protocol ≠ "" ∧
    alpha_procedure.protocol ≠ "" ∧
    gravity_procedure.protocol ≠ "" := by
  simp [neutron_procedure, electron_procedure, alpha_procedure, gravity_procedure]
```

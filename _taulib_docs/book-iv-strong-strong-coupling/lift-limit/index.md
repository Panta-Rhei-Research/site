---
{
  "projection_kind": "taulib_declaration",
  "title": "LiftLimit",
  "permalink": "/verify/taulib/docs/book-iv-strong-strong-coupling/lift-limit/",
  "summary_short": "`structure` declaration in `TauLib.BookIV.Strong.StrongCoupling`.",
  "declaration_id": "TauLib.BookIV.Strong.StrongCoupling::LiftLimit",
  "declaration_slug": "lift-limit",
  "kind": "structure",
  "name": "LiftLimit",
  "module_name": "TauLib.BookIV.Strong.StrongCoupling",
  "module_url": "/verify/taulib/docs/book-iv-strong-strong-coupling/",
  "source_line_start": 71,
  "source_line_end": 78,
  "registry_ids": [
    "IV.D181"
  ],
  "related_registry_items": [
    {
      "id": "IV.D181",
      "title": "π-lift ω-limit",
      "url": "/registry/object/IV.D181/"
    }
  ],
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIV/Strong/StrongCoupling.lean#L71-L78",
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIV/Strong/StrongCoupling.lean#L71-L78",
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
- Source path: [`TauLib/BookIV/Strong/StrongCoupling.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIV/Strong/StrongCoupling.lean#L71-L78)
- Source range: L71-L78
- Kind: `structure`
- Formal status hint: `defined`

## Registry Links

- `IV.D181` — π-lift ω-limit

## Immediate Comment / Docstring

```lean
/-- [IV.D181] Pi-lift omega-limit:
    Lift_pi^omega := [(Lift_pi(n))_{n>=3}]_{~omega}
    The tail equivalence class in H_partial representing the
    profinite strong coupling as a well-defined boundary element. -/
```

## Source Excerpt

```lean
structure LiftLimit where
  /-- Construction: tail equivalence class. -/
  construction : String := "[(Lift_pi(n))_{n>=3}]_{~omega}"
  /-- Lives in H_partial. -/
  lives_in : String := "H_partial (boundary algebra)"
  /-- Well-defined by truncation coherence. -/
  well_defined : Bool := true
  deriving Repr
```

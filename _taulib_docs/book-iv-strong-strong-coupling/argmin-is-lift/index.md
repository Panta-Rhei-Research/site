---
{
  "projection_kind": "taulib_declaration",
  "title": "ArgminIsLift",
  "permalink": "/verify/taulib/docs/book-iv-strong-strong-coupling/argmin-is-lift/",
  "summary_short": "`structure` declaration in `TauLib.BookIV.Strong.StrongCoupling`.",
  "declaration_id": "TauLib.BookIV.Strong.StrongCoupling::ArgminIsLift",
  "declaration_slug": "argmin-is-lift",
  "kind": "structure",
  "name": "ArgminIsLift",
  "module_name": "TauLib.BookIV.Strong.StrongCoupling",
  "module_url": "/verify/taulib/docs/book-iv-strong-strong-coupling/",
  "source_line_start": 179,
  "source_line_end": 184,
  "registry_ids": [
    "IV.P110"
  ],
  "related_registry_items": [
    {
      "id": "IV.P110",
      "title": "The argmin is the π-lift",
      "url": "/registry/object/IV.P110/"
    }
  ],
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIV/Strong/StrongCoupling.lean#L179-L184",
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIV/Strong/StrongCoupling.lean#L179-L184",
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
- Source path: [`TauLib/BookIV/Strong/StrongCoupling.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIV/Strong/StrongCoupling.lean#L179-L184)
- Source range: L179-L184
- Kind: `structure`
- Formal status hint: `defined`

## Registry Links

- `IV.P110` — The argmin is the π-lift

## Immediate Comment / Docstring

```lean
/-- [IV.P110] The argmin of combined defect over A_pi[n]
    equals the pi-lift Lift_pi(n). -/
```

## Source Excerpt

```lean
structure ArgminIsLift where
  /-- Argmin equals lift. -/
  argmin_equals_lift : Bool := true
  /-- Canonical construction coincides with variational. -/
  canonical_equals_variational : Bool := true
  deriving Repr
```

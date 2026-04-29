---
{
  "projection_kind": "taulib_declaration",
  "title": "OnticCoupling",
  "permalink": "/verify/taulib/docs/book-iv-strong-strong-coupling/ontic-coupling/",
  "summary_short": "`structure` declaration in `TauLib.BookIV.Strong.StrongCoupling`.",
  "declaration_id": "TauLib.BookIV.Strong.StrongCoupling::OnticCoupling",
  "declaration_slug": "ontic-coupling",
  "kind": "structure",
  "name": "OnticCoupling",
  "module_name": "TauLib.BookIV.Strong.StrongCoupling",
  "module_url": "/verify/taulib/docs/book-iv-strong-strong-coupling/",
  "source_line_start": 215,
  "source_line_end": 226,
  "registry_ids": [
    "IV.D184"
  ],
  "related_registry_items": [
    {
      "id": "IV.D184",
      "title": "Ontic coupling",
      "url": "/registry/object/IV.D184/"
    }
  ],
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIV/Strong/StrongCoupling.lean#L215-L226",
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIV/Strong/StrongCoupling.lean#L215-L226",
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
- Source path: [`TauLib/BookIV/Strong/StrongCoupling.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIV/Strong/StrongCoupling.lean#L215-L226)
- Source range: L215-L226
- Kind: `structure`
- Formal status hint: `defined`

## Registry Links

- `IV.D184` — Ontic coupling

## Immediate Comment / Docstring

```lean
/-- [IV.D184] An ontic coupling: element of H_partial obtained by
    finite-stage minimization, omega-tail stabilization, and
    NF normalization. Belongs to Fix(S) for some sector S.
    Scale-independent, unique, parameter-free. -/
```

## Source Excerpt

```lean
structure OnticCoupling where
  /-- Construction: minimize, stabilize, normalize. -/
  construction : String := "finite-stage minimize -> omega-tail -> NF normalize"
  /-- Lives in Fix(S) for some sector S. -/
  lives_in_fix : Bool := true
  /-- Scale-independent. -/
  scale_independent : Bool := true
  /-- Unique. -/
  unique : Bool := true
  /-- Parameter-free. -/
  parameter_free : Bool := true
  deriving Repr
```

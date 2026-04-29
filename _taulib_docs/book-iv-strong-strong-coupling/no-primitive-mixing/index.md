---
{
  "projection_kind": "taulib_declaration",
  "title": "NoPrimitiveMixing",
  "permalink": "/verify/taulib/docs/book-iv-strong-strong-coupling/no-primitive-mixing/",
  "summary_short": "`structure` declaration in `TauLib.BookIV.Strong.StrongCoupling`.",
  "declaration_id": "TauLib.BookIV.Strong.StrongCoupling::NoPrimitiveMixing",
  "declaration_slug": "no-primitive-mixing",
  "kind": "structure",
  "name": "NoPrimitiveMixing",
  "module_name": "TauLib.BookIV.Strong.StrongCoupling",
  "module_url": "/verify/taulib/docs/book-iv-strong-strong-coupling/",
  "source_line_start": 146,
  "source_line_end": 155,
  "registry_ids": [
    "IV.P109"
  ],
  "related_registry_items": [
    {
      "id": "IV.P109",
      "title": "No primitive mixing",
      "url": "/registry/object/IV.P109/"
    }
  ],
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIV/Strong/StrongCoupling.lean#L146-L155",
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIV/Strong/StrongCoupling.lean#L146-L155",
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
- Source path: [`TauLib/BookIV/Strong/StrongCoupling.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIV/Strong/StrongCoupling.lean#L146-L155)
- Source range: L146-L155
- Kind: `structure`
- Formal status hint: `defined`

## Registry Links

- `IV.P109` — No primitive mixing

## Immediate Comment / Docstring

```lean
/-- [IV.P109] No primitive mixing: alpha_s^* is distinct from
    alpha_em^* and alpha_wk^*. The fixed-point subalgebras
    Fix(s), Fix(EM), Fix(wk) intersect only trivially. -/
```

## Source Excerpt

```lean
structure NoPrimitiveMixing where
  /-- Strong distinct from EM. -/
  distinct_from_em : Bool := true
  /-- Strong distinct from weak. -/
  distinct_from_weak : Bool := true
  /-- Intersection is trivial. -/
  trivial_intersection : Bool := true
  /-- Mechanism: different generators, different sectors. -/
  mechanism : String := "Fix(s) cap Fix(EM) cap Fix(wk) = {id}"
  deriving Repr
```

---
{
  "projection_kind": "taulib_declaration",
  "title": "e1_md_instance_check",
  "permalink": "/verify/taulib/docs/book-iii-arithmetic-enr-functor01/e1-md-instance-check/",
  "summary_short": "`def` declaration in `TauLib.BookIII.Arithmetic.EnrFunctor01`.",
  "declaration_id": "TauLib.BookIII.Arithmetic.EnrFunctor01::e1_md_instance_check",
  "declaration_slug": "e1-md-instance-check",
  "kind": "def",
  "name": "e1_md_instance_check",
  "module_name": "TauLib.BookIII.Arithmetic.EnrFunctor01",
  "module_url": "/verify/taulib/docs/book-iii-arithmetic-enr-functor01/",
  "source_line_start": 96,
  "source_line_end": 104,
  "registry_ids": [
    "III.D58"
  ],
  "related_registry_items": [
    {
      "id": "III.D58",
      "title": "E₁ Mutual Determination Instance",
      "url": "/registry/object/III.D58/"
    }
  ],
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIII/Arithmetic/EnrFunctor01.lean#L96-L104",
  "formal_status": "defined",
  "right_rail": {
    "related": [
      {
        "title": "TauLib.BookIII.Arithmetic.EnrFunctor01",
        "url": "/verify/taulib/docs/book-iii-arithmetic-enr-functor01/"
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIII/Arithmetic/EnrFunctor01.lean#L96-L104",
        "external": true
      }
    ],
    "meta": {
      "type": "TauLib Declaration",
      "kind": "def",
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

- Module: [TauLib.BookIII.Arithmetic.EnrFunctor01](/verify/taulib/docs/book-iii-arithmetic-enr-functor01/)
- Source path: [`TauLib/BookIII/Arithmetic/EnrFunctor01.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIII/Arithmetic/EnrFunctor01.lean#L96-L104)
- Source range: L96-L104
- Kind: `def`
- Formal status hint: `defined`

## Registry Links

- `III.D58` — E₁ Mutual Determination Instance

## Immediate Comment / Docstring

```lean
/-- [III.D58] E₁ MD instance: the triple (B₁, S₁, I₁) at E₁ level.
    B₁ = boundary (flow data), S₁ = spectral (gap data),
    I₁ = interior (addressability data). All three determine each other. -/
```

## Source Excerpt

```lean
def e1_md_instance_check (bound db : TauIdx) : Bool :=
  -- B₁: flow stabilization (NS)
  let b1 := flow_stabilization_check bound db
  -- S₁: gap existence (YM)
  let s1 := yang_mills_gap_check db
  -- I₁: NF-addressability (Hodge)
  let i1 := nf_addressability_check bound db
  -- Mutual determination: all three hold simultaneously
  b1 && s1 && i1
```

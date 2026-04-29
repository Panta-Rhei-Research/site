---
{
  "projection_kind": "taulib_declaration",
  "title": "FiberBaseFactorization",
  "permalink": "/verify/taulib/docs/book-iv-many-body-condensed-matter/fiber-base-factorization/",
  "summary_short": "`structure` declaration in `TauLib.BookIV.ManyBody.CondensedMatter`.",
  "declaration_id": "TauLib.BookIV.ManyBody.CondensedMatter::FiberBaseFactorization",
  "declaration_slug": "fiber-base-factorization",
  "kind": "structure",
  "name": "FiberBaseFactorization",
  "module_name": "TauLib.BookIV.ManyBody.CondensedMatter",
  "module_url": "/verify/taulib/docs/book-iv-many-body-condensed-matter/",
  "source_line_start": 149,
  "source_line_end": 162,
  "registry_ids": [
    "IV.T94"
  ],
  "related_registry_items": [
    {
      "id": "IV.T94",
      "title": "Fiber-base factorization",
      "url": "/registry/object/IV.T94/"
    }
  ],
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIV/ManyBody/CondensedMatter.lean#L149-L162",
  "formal_status": "defined",
  "right_rail": {
    "related": [
      {
        "title": "TauLib.BookIV.ManyBody.CondensedMatter",
        "url": "/verify/taulib/docs/book-iv-many-body-condensed-matter/"
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIV/ManyBody/CondensedMatter.lean#L149-L162",
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

- Module: [TauLib.BookIV.ManyBody.CondensedMatter](/verify/taulib/docs/book-iv-many-body-condensed-matter/)
- Source path: [`TauLib/BookIV/ManyBody/CondensedMatter.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIV/ManyBody/CondensedMatter.lean#L149-L162)
- Source range: L149-L162
- Kind: `structure`
- Formal status hint: `defined`

## Registry Links

- `IV.T94` — Fiber-base factorization

## Immediate Comment / Docstring

```lean
/-- [IV.T94] The universal defect functional on tau^3 = tau^1 x_f T^2
    factorizes exactly:

    delta[omega]_{tau^3} = delta[omega]_{T^2} tensor delta[omega]_{tau^1}

    The fiber component delta[omega]_{T^2} contains all of:
    - Quantum mechanics (Part III)
    - Particle spectrum (Part VI)
    - Electroweak and strong forces (Parts IV-V)
    - Many-body and condensed matter (Part VII)

    The base component delta[omega]_{tau^1} contains:
    - Gravity (D-sector)
    - Temporal structure
    - Cosmological evolution

    The factorization is exact by axiom K5 (fibered-product structure)
    and the lemniscate L. The only fiber-base coupling passes through
    the omega-sector (Kirchhoff junction). -/
```

## Source Excerpt

```lean
structure FiberBaseFactorization where
  /-- Factorizes as tensor product. -/
  tensor_product : Bool := true
  /-- Fiber: T^2 (spatial physics). -/
  fiber : String := "T^2 (spatial)"
  /-- Base: tau^1 (temporal physics). -/
  base : String := "tau^1 (temporal)"
  /-- Exact by K5 + lemniscate. -/
  exact : Bool := true
  /-- Only coupling: omega-sector. -/
  coupling_omega_only : Bool := true
  /-- Number of fiber parts covered. -/
  fiber_parts : Nat := 5
  deriving Repr
```

---
{
  "projection_kind": "taulib_declaration",
  "title": "orthodox_property",
  "permalink": "/verify/taulib/docs/book-ii-mirror-sign-classification/orthodox-property/",
  "summary_short": "`def` declaration in `TauLib.BookII.Mirror.SignClassification`.",
  "declaration_id": "TauLib.BookII.Mirror.SignClassification::orthodox_property",
  "declaration_slug": "orthodox-property",
  "kind": "def",
  "name": "orthodox_property",
  "module_name": "TauLib.BookII.Mirror.SignClassification",
  "module_url": "/verify/taulib/docs/book-ii-mirror-sign-classification/",
  "source_line_start": 69,
  "source_line_end": 81,
  "registry_ids": [
    "II.D68"
  ],
  "related_registry_items": [
    {
      "id": "II.D68",
      "title": "Structural Sign Classification",
      "url": "/registry/object/II.D68/"
    }
  ],
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookII/Mirror/SignClassification.lean#L69-L81",
  "formal_status": "defined",
  "right_rail": {
    "related": [
      {
        "title": "TauLib.BookII.Mirror.SignClassification",
        "url": "/verify/taulib/docs/book-ii-mirror-sign-classification/"
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookII/Mirror/SignClassification.lean#L69-L81",
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

- Module: [TauLib.BookII.Mirror.SignClassification](/verify/taulib/docs/book-ii-mirror-sign-classification/)
- Source path: [`TauLib/BookII/Mirror/SignClassification.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookII/Mirror/SignClassification.lean#L69-L81)
- Source range: L69-L81
- Kind: `def`
- Formal status hint: `defined`

## Registry Links

- `II.D68` — Structural Sign Classification

## Immediate Comment / Docstring

```lean
/-- [II.D68] The orthodox property at each sign level. -/
```

## Source Excerpt

```lean
def orthodox_property : SignLevel → String
  | .ScalarAlgebra   => "i^2 = -1 (Gaussian integers, complex numbers)"
  | .HolomorphyPDE   => "elliptic Cauchy-Riemann PDE (Laplacian)"
  | .BoundaryInterior => "interior determines boundary (maximum principle)"
  | .Infinity         => "Cantor cardinal hierarchy (aleph_0, aleph_1, ...)"
  | .Cardinality      => "uncountable real line (2^aleph_0 elements)"
  | .Topology         => "Hausdorff, second countable, locally Euclidean"
  | .Geometry         => "Riemannian metric (inner product on tangent bundle)"
  | .Compactness      => "locally compact Hausdorff (Alexandrov extension)"
  | .Idempotents      => "no nontrivial idempotents (C is a field)"
  | .Liouville        => "bounded entire function is constant (Liouville)"
  | .Gluing           => "sheaf on open covers (Leray, Cech)"
  | .Spectrum         => "Gelfand spectrum (maximal ideals of C*-algebra)"
```

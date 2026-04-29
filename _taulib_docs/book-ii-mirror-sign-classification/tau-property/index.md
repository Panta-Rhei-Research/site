---
{
  "projection_kind": "taulib_declaration",
  "title": "tau_property",
  "permalink": "/verify/taulib/docs/book-ii-mirror-sign-classification/tau-property/",
  "summary_short": "`def` declaration in `TauLib.BookII.Mirror.SignClassification`.",
  "declaration_id": "TauLib.BookII.Mirror.SignClassification::tau_property",
  "declaration_slug": "tau-property",
  "kind": "def",
  "name": "tau_property",
  "module_name": "TauLib.BookII.Mirror.SignClassification",
  "module_url": "/verify/taulib/docs/book-ii-mirror-sign-classification/",
  "source_line_start": 84,
  "source_line_end": 96,
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
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookII/Mirror/SignClassification.lean#L84-L96",
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookII/Mirror/SignClassification.lean#L84-L96",
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
- Source path: [`TauLib/BookII/Mirror/SignClassification.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookII/Mirror/SignClassification.lean#L84-L96)
- Source range: L84-L96
- Kind: `def`
- Formal status hint: `defined`

## Registry Links

- `II.D68` — Structural Sign Classification

## Immediate Comment / Docstring

```lean
/-- [II.D68] The tau property at each sign level. -/
```

## Source Excerpt

```lean
def tau_property : SignLevel → String
  | .ScalarAlgebra   => "j^2 = +1 (split-complex, bipolar scalars)"
  | .HolomorphyPDE   => "hyperbolic split-CR PDE (wave equation)"
  | .BoundaryInterior => "boundary determines interior (Hartogs extension)"
  | .Infinity         => "unique omega (omega-germs, no cardinal hierarchy)"
  | .Cardinality      => "countable tau-reals (primorial tower limit)"
  | .Topology         => "Stone space (profinite, totally disconnected)"
  | .Geometry         => "betweenness-first (earned from divisibility order)"
  | .Compactness      => "profinitely compact (inverse limit of finite stages)"
  | .Idempotents      => "nontrivial idempotents e+, e- (bipolar decomposition)"
  | .Liouville        => "bounded hol implies sector-balanced (bipolar Liouville)"
  | .Gluing           => "sheaf on clopen covers (Stone topology gluing)"
  | .Spectrum         => "primorial spectrum (tower of Z/M_kZ spectra)"
```

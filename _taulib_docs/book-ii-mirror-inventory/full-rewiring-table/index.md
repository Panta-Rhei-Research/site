---
{
  "projection_kind": "taulib_declaration",
  "title": "full_rewiring_table",
  "permalink": "/verify/taulib/docs/book-ii-mirror-inventory/full-rewiring-table/",
  "summary_short": "`def` declaration in `TauLib.BookII.Mirror.Inventory`.",
  "declaration_id": "TauLib.BookII.Mirror.Inventory::full_rewiring_table",
  "declaration_slug": "full-rewiring-table",
  "kind": "def",
  "name": "full_rewiring_table",
  "module_name": "TauLib.BookII.Mirror.Inventory",
  "module_url": "/verify/taulib/docs/book-ii-mirror-inventory/",
  "source_line_start": 48,
  "source_line_end": 96,
  "registry_ids": [
    "II.D72"
  ],
  "related_registry_items": [
    {
      "id": "II.D72",
      "title": "The Rewiring Table",
      "url": "/registry/object/II.D72/"
    }
  ],
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookII/Mirror/Inventory.lean#L48-L96",
  "formal_status": "defined",
  "right_rail": {
    "related": [
      {
        "title": "TauLib.BookII.Mirror.Inventory",
        "url": "/verify/taulib/docs/book-ii-mirror-inventory/"
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookII/Mirror/Inventory.lean#L48-L96",
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

- Module: [TauLib.BookII.Mirror.Inventory](/verify/taulib/docs/book-ii-mirror-inventory/)
- Source path: [`TauLib/BookII/Mirror/Inventory.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookII/Mirror/Inventory.lean#L48-L96)
- Source range: L48-L96
- Kind: `def`
- Formal status hint: `defined`

## Registry Links

- `II.D72` — The Rewiring Table

## Immediate Comment / Docstring

```lean
/-- [II.D72] The full rewiring table: all 12 rows. -/
```

## Source Excerpt

```lean
def full_rewiring_table : List RewiringRow :=
  [ { level := .ScalarAlgebra
    , orthodox := "i^2 = -1 (complex numbers)"
    , tau_equiv := "j^2 = +1 (split-complex)"
    , tradeoff := "lose field property, gain bipolar decomposition" }
  , { level := .HolomorphyPDE
    , orthodox := "elliptic CR equations"
    , tau_equiv := "hyperbolic split-CR equations"
    , tradeoff := "lose maximum principle, gain wave propagation" }
  , { level := .BoundaryInterior
    , orthodox := "interior determines boundary"
    , tau_equiv := "boundary determines interior"
    , tradeoff := "lose interior-first analysis, gain Hartogs extension" }
  , { level := .Infinity
    , orthodox := "Cantor cardinal hierarchy"
    , tau_equiv := "unique omega (omega-germs)"
    , tradeoff := "lose uncountable sets, gain constructive infinity" }
  , { level := .Cardinality
    , orthodox := "uncountable reals (2^aleph_0)"
    , tau_equiv := "countable tau-reals (primorial limit)"
    , tradeoff := "lose Archimedean density, gain finite witnesses" }
  , { level := .Topology
    , orthodox := "Hausdorff, second countable"
    , tau_equiv := "Stone space (profinite)"
    , tradeoff := "lose connected open sets, gain clopen basis" }
  , { level := .Geometry
    , orthodox := "Riemannian metric"
    , tau_equiv := "betweenness-first (earned from order)"
    , tradeoff := "lose smooth manifold, gain algebraic geometry" }
  , { level := .Compactness
    , orthodox := "locally compact Hausdorff"
    , tau_equiv := "profinitely compact"
    , tradeoff := "lose local compactness, gain global compactness" }
  , { level := .Idempotents
    , orthodox := "no nontrivial idempotents (C is field)"
    , tau_equiv := "nontrivial e+, e- (bipolar)"
    , tradeoff := "lose integral domain, gain sector decomposition" }
  , { level := .Liouville
    , orthodox := "bounded entire => constant"
    , tau_equiv := "bounded hol => sector-balanced"
    , tradeoff := "lose Liouville rigidity, gain bipolar balance" }
  , { level := .Gluing
    , orthodox := "sheaf on open covers"
    , tau_equiv := "sheaf on clopen covers"
    , tradeoff := "lose arbitrary open gluing, gain finite-stage gluing" }
  , { level := .Spectrum
    , orthodox := "Gelfand spectrum (maximal ideals)"
    , tau_equiv := "primorial spectrum (tower of Z/M_kZ)"
    , tradeoff := "lose C*-algebra framework, gain tower structure" } ]
```

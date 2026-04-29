---
{
  "projection_kind": "taulib_declaration",
  "title": "TopologicalBranch",
  "permalink": "/verify/taulib/docs/book-iv-many-body-condensed-matter/topological-branch/",
  "summary_short": "`structure` declaration in `TauLib.BookIV.ManyBody.CondensedMatter`.",
  "declaration_id": "TauLib.BookIV.ManyBody.CondensedMatter::TopologicalBranch",
  "declaration_slug": "topological-branch",
  "kind": "structure",
  "name": "TopologicalBranch",
  "module_name": "TauLib.BookIV.ManyBody.CondensedMatter",
  "module_url": "/verify/taulib/docs/book-iv-many-body-condensed-matter/",
  "source_line_start": 101,
  "source_line_end": 116,
  "registry_ids": [
    "IV.D240"
  ],
  "related_registry_items": [
    {
      "id": "IV.D240",
      "title": "Topological branch",
      "url": "/registry/object/IV.D240/"
    }
  ],
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIV/ManyBody/CondensedMatter.lean#L101-L116",
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIV/ManyBody/CondensedMatter.lean#L101-L116",
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
- Source path: [`TauLib/BookIV/ManyBody/CondensedMatter.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIV/ManyBody/CondensedMatter.lean#L101-L116)
- Source range: L101-L116
- Kind: `structure`
- Formal status hint: `defined`

## Registry Links

- `IV.D240` — Topological branch

## Immediate Comment / Docstring

```lean
/-- [IV.D240] A topological branch of the defect spectrum is a regime with:
    1. Nonzero maximal mobility (free base-direction translation)
    2. Zero bulk vorticity nu_bulk = 0 (except at quantized cores)
    3. Quantized topological charge theta in Z

    The two topological regimes are:
    - Superfluid: theta quantized on fluid vortex cores
    - Superconductor: theta quantized on magnetic flux tubes

    They are distinguished by whether the B-sector (EM) is coupled. -/
```

## Source Excerpt

```lean
structure TopologicalBranch where
  /-- Number of topological regimes. -/
  num_regimes : Nat := 2
  /-- Common: maximal mobility. -/
  maximal_mobility : Bool := true
  /-- Common: zero bulk vorticity. -/
  zero_bulk_vorticity : Bool := true
  /-- Common: quantized theta. -/
  quantized_theta : Bool := true
  /-- Superfluid: no EM coupling. -/
  superfluid_no_em : Bool := true
  /-- Superconductor: EM coupled. -/
  superconductor_em : Bool := true
  /-- Distinguished by B-sector coupling. -/
  distinguished_by_em : Bool := true
  deriving Repr
```

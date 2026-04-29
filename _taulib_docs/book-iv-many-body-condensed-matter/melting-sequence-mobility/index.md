---
{
  "projection_kind": "taulib_declaration",
  "title": "MeltingSequenceMobility",
  "permalink": "/verify/taulib/docs/book-iv-many-body-condensed-matter/melting-sequence-mobility/",
  "summary_short": "`structure` declaration in `TauLib.BookIV.ManyBody.CondensedMatter`.",
  "declaration_id": "TauLib.BookIV.ManyBody.CondensedMatter::MeltingSequenceMobility",
  "declaration_slug": "melting-sequence-mobility",
  "kind": "structure",
  "name": "MeltingSequenceMobility",
  "module_name": "TauLib.BookIV.ManyBody.CondensedMatter",
  "module_url": "/verify/taulib/docs/book-iv-many-body-condensed-matter/",
  "source_line_start": 64,
  "source_line_end": 74,
  "registry_ids": [
    "IV.P143"
  ],
  "related_registry_items": [
    {
      "id": "IV.P143",
      "title": "Melting sequence monotone mobility",
      "url": "/registry/object/IV.P143/"
    }
  ],
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIV/ManyBody/CondensedMatter.lean#L64-L74",
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIV/ManyBody/CondensedMatter.lean#L64-L74",
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
- Source path: [`TauLib/BookIV/ManyBody/CondensedMatter.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIV/ManyBody/CondensedMatter.lean#L64-L74)
- Source range: L64-L74
- Kind: `structure`
- Formal status hint: `defined`

## Registry Links

- `IV.P143` — Melting sequence monotone mobility

## Immediate Comment / Docstring

```lean
/-- [IV.P143] The six non-topological regimes are ordered by monotonically
    increasing macroscopic mobility:

    mu_crystal <= mu_quasi <= mu_glass < mu_Euler <= mu_NS < mu_MHD <= mu_plasma

    This defines the **melting sequence**: each step increases the
    degrees of freedom available to the many-body system.

    The two topological regimes (superfluid, superconductor) lie on a
    separate branch with maximal mobility but constrained theta. -/
```

## Source Excerpt

```lean
structure MeltingSequenceMobility where
  /-- Number of non-topological regimes. -/
  num_regimes : Nat := 6
  /-- Ordering is monotone in mobility. -/
  monotone : Bool := true
  /-- Regime labels in order. -/
  sequence : List String :=
    ["Crystal", "Quasicrystal", "Glass", "Euler", "Navier-Stokes", "Plasma"]
  /-- Topological branch separate. -/
  topological_separate : Bool := true
  deriving Repr
```

---
{
  "projection_kind": "taulib_declaration",
  "title": "full_evolution_check",
  "permalink": "/verify/taulib/docs/book-ii-hartogs-evolution-operator/full-evolution-check/",
  "summary_short": "`def` declaration in `TauLib.BookII.Hartogs.EvolutionOperator`.",
  "declaration_id": "TauLib.BookII.Hartogs.EvolutionOperator::full_evolution_check",
  "declaration_slug": "full-evolution-check",
  "kind": "def",
  "name": "full_evolution_check",
  "module_name": "TauLib.BookII.Hartogs.EvolutionOperator",
  "module_url": "/verify/taulib/docs/book-ii-hartogs-evolution-operator/",
  "source_line_start": 263,
  "source_line_end": 268,
  "registry_ids": [],
  "related_registry_items": [],
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookII/Hartogs/EvolutionOperator.lean#L263-L268",
  "formal_status": "defined",
  "right_rail": {
    "related": [
      {
        "title": "TauLib.BookII.Hartogs.EvolutionOperator",
        "url": "/verify/taulib/docs/book-ii-hartogs-evolution-operator/"
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookII/Hartogs/EvolutionOperator.lean#L263-L268",
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

- Module: [TauLib.BookII.Hartogs.EvolutionOperator](/verify/taulib/docs/book-ii-hartogs-evolution-operator/)
- Source path: [`TauLib/BookII/Hartogs/EvolutionOperator.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookII/Hartogs/EvolutionOperator.lean#L263-L268)
- Source range: L263-L268
- Kind: `def`
- Formal status hint: `defined`

## Registry Links

- No Registry IDs were detected in this declaration block.

## Immediate Comment / Docstring

```lean
/-- Combined check: evolution semigroup + causal arrow.
    The evolution semigroup provides the dynamics; the causal arrow
    provides the direction. Together they give the full Hartogs
    evolution structure. -/
```

## Source Excerpt

```lean
def full_evolution_check (bound db : TauIdx) : Bool :=
  evolution_semigroup_check bound db &&
  evolution_identity_check bound db &&
  bc_asymmetry_witness &&
  causal_arrow_check bound &&
  causal_nontrivial_check bound
```

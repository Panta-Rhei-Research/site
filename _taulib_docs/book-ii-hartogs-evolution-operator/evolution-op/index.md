---
{
  "projection_kind": "taulib_declaration",
  "title": "evolution_op",
  "permalink": "/verify/taulib/docs/book-ii-hartogs-evolution-operator/evolution-op/",
  "summary_short": "`def` declaration in `TauLib.BookII.Hartogs.EvolutionOperator`.",
  "declaration_id": "TauLib.BookII.Hartogs.EvolutionOperator::evolution_op",
  "declaration_slug": "evolution-op",
  "kind": "def",
  "name": "evolution_op",
  "module_name": "TauLib.BookII.Hartogs.EvolutionOperator",
  "module_url": "/verify/taulib/docs/book-ii-hartogs-evolution-operator/",
  "source_line_start": 65,
  "source_line_end": 66,
  "registry_ids": [
    "II.D37"
  ],
  "related_registry_items": [
    {
      "id": "II.D37",
      "title": "Evolution Operator",
      "url": "/registry/object/II.D37/"
    }
  ],
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookII/Hartogs/EvolutionOperator.lean#L65-L66",
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookII/Hartogs/EvolutionOperator.lean#L65-L66",
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
- Source path: [`TauLib/BookII/Hartogs/EvolutionOperator.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookII/Hartogs/EvolutionOperator.lean#L65-L66)
- Source range: L65-L66
- Kind: `def`
- Formal status hint: `defined`

## Registry Links

- `II.D37` — Evolution Operator

## Immediate Comment / Docstring

```lean
/-- [II.D37] The evolution operator E_{n->m}:
    maps a point x from stage n context to stage m.
    Defined as reduce(x, m), the canonical projection to Z/M_m Z.

    When n <= m, this is "refinement" (going to a coarser stage).
    When n >= m, this is "extension" (compatible with bndlift).

    The key insight: the entire tower of BndLifts telescopes to
    a single reduce. -/
```

## Source Excerpt

```lean
def evolution_op (x _n m : TauIdx) : TauIdx :=
  reduce x m
```

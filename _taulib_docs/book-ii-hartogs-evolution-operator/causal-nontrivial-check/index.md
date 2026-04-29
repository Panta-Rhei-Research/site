---
{
  "projection_kind": "taulib_declaration",
  "title": "causal_nontrivial_check",
  "permalink": "/verify/taulib/docs/book-ii-hartogs-evolution-operator/causal-nontrivial-check/",
  "summary_short": "`def` declaration in `TauLib.BookII.Hartogs.EvolutionOperator`.",
  "declaration_id": "TauLib.BookII.Hartogs.EvolutionOperator::causal_nontrivial_check",
  "declaration_slug": "causal-nontrivial-check",
  "kind": "def",
  "name": "causal_nontrivial_check",
  "module_name": "TauLib.BookII.Hartogs.EvolutionOperator",
  "module_url": "/verify/taulib/docs/book-ii-hartogs-evolution-operator/",
  "source_line_start": 239,
  "source_line_end": 253,
  "registry_ids": [
    "II.D38"
  ],
  "related_registry_items": [
    {
      "id": "II.D38",
      "title": "Causal Arrow",
      "url": "/registry/object/II.D38/"
    }
  ],
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookII/Hartogs/EvolutionOperator.lean#L239-L253",
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookII/Hartogs/EvolutionOperator.lean#L239-L253",
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
- Source path: [`TauLib/BookII/Hartogs/EvolutionOperator.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookII/Hartogs/EvolutionOperator.lean#L239-L253)
- Source range: L239-L253
- Kind: `def`
- Formal status hint: `defined`

## Registry Links

- `II.D38` — Causal Arrow

## Immediate Comment / Docstring

```lean
/-- [II.D38] B/C asymmetry is non-trivial: not all points are balanced.
    There exist both B-dominant and C-dominant points in [2, bound].
    This is the categorical origin of the arrow of time. -/
```

## Source Excerpt

```lean
def causal_nontrivial_check (bound : TauIdx) : Bool :=
  has_b_dom 2 (bound + 1) && has_c_dom 2 (bound + 1)
where
  has_b_dom (x fuel : Nat) : Bool :=
    if fuel = 0 then false
    else if x > bound then false
    else if causal_arrow x == 1 then true
    else has_b_dom (x + 1) (fuel - 1)
  termination_by fuel
  has_c_dom (x fuel : Nat) : Bool :=
    if fuel = 0 then false
    else if x > bound then false
    else if causal_arrow x == 2 then true
    else has_c_dom (x + 1) (fuel - 1)
  termination_by fuel
```

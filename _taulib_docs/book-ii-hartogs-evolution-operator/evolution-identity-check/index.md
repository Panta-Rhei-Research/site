---
{
  "projection_kind": "taulib_declaration",
  "title": "evolution_identity_check",
  "permalink": "/verify/taulib/docs/book-ii-hartogs-evolution-operator/evolution-identity-check/",
  "summary_short": "`def` declaration in `TauLib.BookII.Hartogs.EvolutionOperator`.",
  "declaration_id": "TauLib.BookII.Hartogs.EvolutionOperator::evolution_identity_check",
  "declaration_slug": "evolution-identity-check",
  "kind": "def",
  "name": "evolution_identity_check",
  "module_name": "TauLib.BookII.Hartogs.EvolutionOperator",
  "module_url": "/verify/taulib/docs/book-ii-hartogs-evolution-operator/",
  "source_line_start": 101,
  "source_line_end": 112,
  "registry_ids": [
    "II.T28"
  ],
  "related_registry_items": [
    {
      "id": "II.T28",
      "title": "B/C Asymmetry Implies Time Arrow",
      "url": "/registry/object/II.T28/"
    }
  ],
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookII/Hartogs/EvolutionOperator.lean#L101-L112",
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookII/Hartogs/EvolutionOperator.lean#L101-L112",
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
- Source path: [`TauLib/BookII/Hartogs/EvolutionOperator.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookII/Hartogs/EvolutionOperator.lean#L101-L112)
- Source range: L101-L112
- Kind: `def`
- Formal status hint: `defined`

## Registry Links

- `II.T28` — B/C Asymmetry Implies Time Arrow

## Immediate Comment / Docstring

```lean
/-- [II.T28] Evolution identity check:
    E_{n->n} is idempotent: reduce(reduce(x, n), n) = reduce(x, n).
    Double reduction at the same stage does not change the value. -/
```

## Source Excerpt

```lean
def evolution_identity_check (bound db : TauIdx) : Bool :=
  go 2 1 ((bound + 1) * (db + 1))
where
  go (x n fuel : Nat) : Bool :=
    if fuel = 0 then true
    else if x > bound then true
    else if n > db then go (x + 1) 1 (fuel - 1)
    else
      let red := reduce x n
      let ok := reduce red n == red
      ok && go x (n + 1) (fuel - 1)
  termination_by fuel
```

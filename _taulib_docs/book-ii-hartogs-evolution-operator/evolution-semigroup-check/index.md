---
{
  "projection_kind": "taulib_declaration",
  "title": "evolution_semigroup_check",
  "permalink": "/verify/taulib/docs/book-ii-hartogs-evolution-operator/evolution-semigroup-check/",
  "summary_short": "`def` declaration in `TauLib.BookII.Hartogs.EvolutionOperator`.",
  "declaration_id": "TauLib.BookII.Hartogs.EvolutionOperator::evolution_semigroup_check",
  "declaration_slug": "evolution-semigroup-check",
  "kind": "def",
  "name": "evolution_semigroup_check",
  "module_name": "TauLib.BookII.Hartogs.EvolutionOperator",
  "module_url": "/verify/taulib/docs/book-ii-hartogs-evolution-operator/",
  "source_line_start": 83,
  "source_line_end": 96,
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
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookII/Hartogs/EvolutionOperator.lean#L83-L96",
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookII/Hartogs/EvolutionOperator.lean#L83-L96",
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
- Source path: [`TauLib/BookII/Hartogs/EvolutionOperator.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookII/Hartogs/EvolutionOperator.lean#L83-L96)
- Source range: L83-L96
- Kind: `def`
- Formal status hint: `defined`

## Registry Links

- `II.T28` — B/C Asymmetry Implies Time Arrow

## Immediate Comment / Docstring

```lean
/-- [II.T28] Evolution semigroup check:
    E_{m->l} . E_{n->m} = E_{n->l}
    i.e., reduce(reduce(x, m), n) = reduce(x, n)  for n <= m.

    This is the tower coherence condition expressed as a semigroup law.
    The evolution operators form a semigroup under composition,
    indexed by the primorial stage numbers. -/
```

## Source Excerpt

```lean
def evolution_semigroup_check (bound db : TauIdx) : Bool :=
  go 2 1 1 ((bound + 1) * (db + 1) * (db + 1))
where
  go (x n m fuel : Nat) : Bool :=
    if fuel = 0 then true
    else if x > bound then true
    else if n > db then go (x + 1) 1 1 (fuel - 1)
    else if m > db then go x (n + 1) 1 (fuel - 1)
    else
      -- For n <= m: reduce(reduce(x, m), n) = reduce(x, n)
      let ok := !(n ≤ m) ||
        (reduce (reduce x m) n == reduce x n)
      ok && go x n (m + 1) (fuel - 1)
  termination_by fuel
```

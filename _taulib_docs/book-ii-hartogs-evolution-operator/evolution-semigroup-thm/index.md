---
{
  "projection_kind": "taulib_declaration",
  "title": "evolution_semigroup_thm",
  "permalink": "/verify/taulib/docs/book-ii-hartogs-evolution-operator/evolution-semigroup-thm/",
  "summary_short": "`theorem` declaration in `TauLib.BookII.Hartogs.EvolutionOperator`.",
  "declaration_id": "TauLib.BookII.Hartogs.EvolutionOperator::evolution_semigroup_thm",
  "declaration_slug": "evolution-semigroup-thm",
  "kind": "theorem",
  "name": "evolution_semigroup_thm",
  "module_name": "TauLib.BookII.Hartogs.EvolutionOperator",
  "module_url": "/verify/taulib/docs/book-ii-hartogs-evolution-operator/",
  "source_line_start": 142,
  "source_line_end": 145,
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
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookII/Hartogs/EvolutionOperator.lean#L142-L145",
  "formal_status": "formalized",
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookII/Hartogs/EvolutionOperator.lean#L142-L145",
        "external": true
      }
    ],
    "meta": {
      "type": "TauLib Declaration",
      "kind": "theorem",
      "status": "formalized"
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
- Source path: [`TauLib/BookII/Hartogs/EvolutionOperator.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookII/Hartogs/EvolutionOperator.lean#L142-L145)
- Source range: L142-L145
- Kind: `theorem`
- Formal status hint: `formalized`

## Registry Links

- `II.T28` — B/C Asymmetry Implies Time Arrow

## Immediate Comment / Docstring

```lean
/-- [II.T28] Evolution semigroup theorem (formal):
    reduce(reduce(x, m), n) = reduce(x, n)  for n <= m.
    This is a direct corollary of reduction_compat from ModArith. -/
```

## Source Excerpt

```lean
theorem evolution_semigroup_thm (x : TauIdx) {n m : TauIdx} (h : n ≤ m) :
    evolution_op (evolution_op x m m) m n = evolution_op x m n := by
  simp only [evolution_op]
  exact reduction_compat x h
```

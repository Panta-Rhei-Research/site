---
{
  "projection_kind": "taulib_declaration",
  "title": "bc_asymmetry_witness",
  "permalink": "/verify/taulib/docs/book-ii-hartogs-evolution-operator/bc-asymmetry-witness/",
  "summary_short": "`def` declaration in `TauLib.BookII.Hartogs.EvolutionOperator`.",
  "declaration_id": "TauLib.BookII.Hartogs.EvolutionOperator::bc_asymmetry_witness",
  "declaration_slug": "bc-asymmetry-witness",
  "kind": "def",
  "name": "bc_asymmetry_witness",
  "module_name": "TauLib.BookII.Hartogs.EvolutionOperator",
  "module_url": "/verify/taulib/docs/book-ii-hartogs-evolution-operator/",
  "source_line_start": 213,
  "source_line_end": 219,
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
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookII/Hartogs/EvolutionOperator.lean#L213-L219",
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookII/Hartogs/EvolutionOperator.lean#L213-L219",
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
- Source path: [`TauLib/BookII/Hartogs/EvolutionOperator.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookII/Hartogs/EvolutionOperator.lean#L213-L219)
- Source range: L213-L219
- Kind: `def`
- Formal status hint: `defined`

## Registry Links

- `II.D38` — Causal Arrow

## Immediate Comment / Docstring

```lean
/-- [II.D38] B/C asymmetry witness: exhibit specific points where B != C.
    Greedy peel prefers tetration, so from_tau_idx 4 = (2,1,2,1):
    A=2, B=1, C=2, D=1 → C-dominant.
    from_tau_idx 64 = (2,3,2,1): A=2, B=3, C=2, D=1 → B-dominant.
    This demonstrates that both directions (B-dominant and C-dominant) exist. -/
```

## Source Excerpt

```lean
def bc_asymmetry_witness : Bool :=
  let p4 := from_tau_idx 4      -- (2, 1, 2, 1): B=1, C=2 (greedy peel: tetration first)
  let p64 := from_tau_idx 64    -- (2, 3, 2, 1): B=3, C=2
  -- 4 is C-dominant (C > B): tetration dominates at small values
  p4.c > p4.b &&
  -- 64 is B-dominant (B > C): exponent dominates at larger values
  p64.b > p64.c
```

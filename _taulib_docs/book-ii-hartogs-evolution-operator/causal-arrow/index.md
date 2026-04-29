---
{
  "projection_kind": "taulib_declaration",
  "title": "causal_arrow",
  "permalink": "/verify/taulib/docs/book-ii-hartogs-evolution-operator/causal-arrow/",
  "summary_short": "`def` declaration in `TauLib.BookII.Hartogs.EvolutionOperator`.",
  "declaration_id": "TauLib.BookII.Hartogs.EvolutionOperator::causal_arrow",
  "declaration_slug": "causal-arrow",
  "kind": "def",
  "name": "causal_arrow",
  "module_name": "TauLib.BookII.Hartogs.EvolutionOperator",
  "module_url": "/verify/taulib/docs/book-ii-hartogs-evolution-operator/",
  "source_line_start": 176,
  "source_line_end": 180,
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
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookII/Hartogs/EvolutionOperator.lean#L176-L180",
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookII/Hartogs/EvolutionOperator.lean#L176-L180",
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
- Source path: [`TauLib/BookII/Hartogs/EvolutionOperator.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookII/Hartogs/EvolutionOperator.lean#L176-L180)
- Source range: L176-L180
- Kind: `def`
- Formal status hint: `defined`

## Registry Links

- `II.D38` — Causal Arrow

## Immediate Comment / Docstring

```lean
/-- [II.D38] The causal arrow: a direction determined by B/C asymmetry.

    For a point x, we compare how the B-coordinate and C-coordinate
    change across stages. The B-coordinate (exponent, gamma-orbit)
    grows polynomially, while the C-coordinate (tetration, eta-orbit)
    grows hyper-exponentially. This asymmetry selects a preferred
    direction: forward = increasing stage number.

    Returns:
    - 1  if B grows faster at this sample (B-dominant direction)
    - 2  if C grows faster at this sample (C-dominant direction)
    - 0  if they grow at the same rate (balanced) -/
```

## Source Excerpt

```lean
def causal_arrow (x : TauIdx) : TauIdx :=
  let p := from_tau_idx x
  if p.b > p.c then 1       -- B-dominant: exponent leads
  else if p.c > p.b then 2  -- C-dominant: tetration leads
  else 0                     -- balanced
```

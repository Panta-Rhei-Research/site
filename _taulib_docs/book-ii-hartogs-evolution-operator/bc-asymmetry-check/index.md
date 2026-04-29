---
{
  "projection_kind": "taulib_declaration",
  "title": "bc_asymmetry_check",
  "permalink": "/verify/taulib/docs/book-ii-hartogs-evolution-operator/bc-asymmetry-check/",
  "summary_short": "`def` declaration in `TauLib.BookII.Hartogs.EvolutionOperator`.",
  "declaration_id": "TauLib.BookII.Hartogs.EvolutionOperator::bc_asymmetry_check",
  "declaration_slug": "bc-asymmetry-check",
  "kind": "def",
  "name": "bc_asymmetry_check",
  "module_name": "TauLib.BookII.Hartogs.EvolutionOperator",
  "module_url": "/verify/taulib/docs/book-ii-hartogs-evolution-operator/",
  "source_line_start": 194,
  "source_line_end": 206,
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
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookII/Hartogs/EvolutionOperator.lean#L194-L206",
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookII/Hartogs/EvolutionOperator.lean#L194-L206",
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
- Source path: [`TauLib/BookII/Hartogs/EvolutionOperator.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookII/Hartogs/EvolutionOperator.lean#L194-L206)
- Source range: L194-L206
- Kind: `def`
- Formal status hint: `defined`

## Registry Links

- `II.D38` — Causal Arrow

## Immediate Comment / Docstring

```lean
/-- [II.D38] B/C growth rate comparison at powers of 2.
    For the canonical base a=2, compare B and C coordinates of 2^n.
    As n increases, B (exponent) grows linearly while C (tetration)
    stays bounded. For powers of prime: x = p^n has B = n, C = 1.

    This shows: in the "exponential direction," B dominates.
    The complementary "tetration direction" (a ↑↑ n) has C dominating.
    The asymmetry between the two rates is fundamental. -/
```

## Source Excerpt

```lean
def bc_asymmetry_check (bound : TauIdx) : Bool :=
  go 2 (bound + 1)
where
  go (x fuel : Nat) : Bool :=
    if fuel = 0 then true
    else if x > bound then true
    else
      let p := from_tau_idx x
      -- For x >= 2, at least one of B, C is >= 1 (tower atom is nontrivial)
      -- The asymmetry manifests: not all points have B = C
      let ok := p.b >= 1 || p.c >= 1 || x <= 1
      ok && go (x + 1) (fuel - 1)
  termination_by fuel
```

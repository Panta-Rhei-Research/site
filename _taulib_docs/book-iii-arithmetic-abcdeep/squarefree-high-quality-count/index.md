---
{
  "projection_kind": "taulib_declaration",
  "title": "squarefree_high_quality_count",
  "permalink": "/verify/taulib/docs/book-iii-arithmetic-abcdeep/squarefree-high-quality-count/",
  "summary_short": "`def` declaration in `TauLib.BookIII.Arithmetic.ABCDeep`.",
  "declaration_id": "TauLib.BookIII.Arithmetic.ABCDeep::squarefree_high_quality_count",
  "declaration_slug": "squarefree-high-quality-count",
  "kind": "def",
  "name": "squarefree_high_quality_count",
  "module_name": "TauLib.BookIII.Arithmetic.ABCDeep",
  "module_url": "/verify/taulib/docs/book-iii-arithmetic-abcdeep/",
  "source_line_start": 173,
  "source_line_end": 188,
  "registry_ids": [
    "III.P47"
  ],
  "related_registry_items": [
    {
      "id": "III.P47",
      "title": "Squarefree Dominance Theorem",
      "url": "/registry/object/III.P47/"
    }
  ],
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIII/Arithmetic/ABCDeep.lean#L173-L188",
  "formal_status": "defined",
  "right_rail": {
    "related": [
      {
        "title": "TauLib.BookIII.Arithmetic.ABCDeep",
        "url": "/verify/taulib/docs/book-iii-arithmetic-abcdeep/"
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIII/Arithmetic/ABCDeep.lean#L173-L188",
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

- Module: [TauLib.BookIII.Arithmetic.ABCDeep](/verify/taulib/docs/book-iii-arithmetic-abcdeep/)
- Source path: [`TauLib/BookIII/Arithmetic/ABCDeep.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIII/Arithmetic/ABCDeep.lean#L173-L188)
- Source range: L173-L188
- Kind: `def`
- Formal status hint: `defined`

## Registry Links

- `III.P47` — Squarefree Dominance Theorem

## Immediate Comment / Docstring

```lean
/-- [III.P47] Squarefree dominance: for ALL squarefree coprime pairs
    (a,b) with a,b ≤ bound, count how many have c ≥ rad(abc).
    The theorem states this count is 0. -/
```

## Source Excerpt

```lean
def squarefree_high_quality_count (bound : Nat) : Nat :=
  go 2 2 0 ((bound + 1) * (bound + 1))
where
  go (a b acc fuel : Nat) : Nat :=
    if fuel = 0 then acc
    else if a > bound then acc
    else if b > bound then go (a + 1) 2 acc (fuel - 1)
    else
      let g := Nat.gcd a b
      let acc' := if g == 1 && is_squarefree a && is_squarefree b then
        let c := a + b
        let r := radical (a * b * c)
        if r > 0 && c >= r then acc + 1 else acc
      else acc
      go a (b + 1) acc' (fuel - 1)
  termination_by fuel
```

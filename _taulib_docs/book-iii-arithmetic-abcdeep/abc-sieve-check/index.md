---
{
  "projection_kind": "taulib_declaration",
  "title": "abc_sieve_check",
  "permalink": "/verify/taulib/docs/book-iii-arithmetic-abcdeep/abc-sieve-check/",
  "summary_short": "`def` declaration in `TauLib.BookIII.Arithmetic.ABCDeep`.",
  "declaration_id": "TauLib.BookIII.Arithmetic.ABCDeep::abc_sieve_check",
  "declaration_slug": "abc-sieve-check",
  "kind": "def",
  "name": "abc_sieve_check",
  "module_name": "TauLib.BookIII.Arithmetic.ABCDeep",
  "module_url": "/verify/taulib/docs/book-iii-arithmetic-abcdeep/",
  "source_line_start": 88,
  "source_line_end": 98,
  "registry_ids": [
    "III.D108"
  ],
  "related_registry_items": [
    {
      "id": "III.D108",
      "title": "Sieve-Accelerated ABC",
      "url": "/registry/object/III.D108/"
    }
  ],
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIII/Arithmetic/ABCDeep.lean#L88-L98",
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIII/Arithmetic/ABCDeep.lean#L88-L98",
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
- Source path: [`TauLib/BookIII/Arithmetic/ABCDeep.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIII/Arithmetic/ABCDeep.lean#L88-L98)
- Source range: L88-L98
- Kind: `def`
- Formal status hint: `defined`

## Registry Links

- `III.D108` — Sieve-Accelerated ABC

## Immediate Comment / Docstring

```lean
/-- [III.D108] ABC quality check for coprime pairs up to bound.
    Same as abc_quality_bound_check but with clearer structure. -/
```

## Source Excerpt

```lean
def abc_sieve_check (bound : Nat) : Bool :=
  go 1 1 ((bound + 1) * (bound + 1))
where
  go (a b fuel : Nat) : Bool :=
    if fuel = 0 then true
    else if a > bound then true
    else if b > bound then go (a + 1) 1 (fuel - 1)
    else
      let ok := abc_triple_check a b
      ok && go a (b + 1) (fuel - 1)
  termination_by fuel
```

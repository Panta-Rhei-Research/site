---
{
  "projection_kind": "taulib_declaration",
  "title": "radical",
  "permalink": "/verify/taulib/docs/book-iii-arithmetic-abcconjecture/radical/",
  "summary_short": "`def` declaration in `TauLib.BookIII.Arithmetic.ABCConjecture`.",
  "declaration_id": "TauLib.BookIII.Arithmetic.ABCConjecture::radical",
  "declaration_slug": "radical",
  "kind": "def",
  "name": "radical",
  "module_name": "TauLib.BookIII.Arithmetic.ABCConjecture",
  "module_url": "/verify/taulib/docs/book-iii-arithmetic-abcconjecture/",
  "source_line_start": 65,
  "source_line_end": 85,
  "registry_ids": [
    "III.D97"
  ],
  "related_registry_items": [
    {
      "id": "III.D97",
      "title": "Radical Function",
      "url": "/registry/object/III.D97/"
    }
  ],
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIII/Arithmetic/ABCConjecture.lean#L65-L85",
  "formal_status": "defined",
  "right_rail": {
    "related": [
      {
        "title": "TauLib.BookIII.Arithmetic.ABCConjecture",
        "url": "/verify/taulib/docs/book-iii-arithmetic-abcconjecture/"
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIII/Arithmetic/ABCConjecture.lean#L65-L85",
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

- Module: [TauLib.BookIII.Arithmetic.ABCConjecture](/verify/taulib/docs/book-iii-arithmetic-abcconjecture/)
- Source path: [`TauLib/BookIII/Arithmetic/ABCConjecture.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIII/Arithmetic/ABCConjecture.lean#L65-L85)
- Source range: L65-L85
- Kind: `def`
- Formal status hint: `defined`

## Registry Links

- `III.D97` — Radical Function

## Immediate Comment / Docstring

```lean
/-- [III.D97] Radical of n: product of distinct prime divisors.
    rad(1) = 1, rad(p^k) = p, rad(p·q) = p·q. -/
```

## Source Excerpt

```lean
def radical (n : Nat) : Nat :=
  if n <= 1 then 1
  else go 2 n 1 (n + 1)
where
  go (d n acc fuel : Nat) : Nat :=
    if fuel = 0 then acc
    else if d > n then acc
    else if n % d == 0 then
      -- d is a prime factor; include it once and divide out all copies
      let n' := strip d n
      go (d + 1) n' (acc * d) (fuel - 1)
    else go (d + 1) n acc (fuel - 1)
  termination_by fuel
  strip (d n : Nat) : Nat :=
    if d <= 1 || n == 0 then n
    else go_strip d n (n + 1)
  go_strip (d n fuel : Nat) : Nat :=
    if fuel = 0 then n
    else if n % d == 0 then go_strip d (n / d) (fuel - 1)
    else n
  termination_by fuel
```

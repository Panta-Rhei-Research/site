---
{
  "projection_kind": "taulib_declaration",
  "title": "prime_count_mod",
  "permalink": "/verify/taulib/docs/book-i-coordinates-chebyshev-bias/prime-count-mod/",
  "summary_short": "`def` declaration in `TauLib.BookI.Coordinates.ChebyshevBias`.",
  "declaration_id": "TauLib.BookI.Coordinates.ChebyshevBias::prime_count_mod",
  "declaration_slug": "prime-count-mod",
  "kind": "def",
  "name": "prime_count_mod",
  "module_name": "TauLib.BookI.Coordinates.ChebyshevBias",
  "module_url": "/verify/taulib/docs/book-i-coordinates-chebyshev-bias/",
  "source_line_start": 56,
  "source_line_end": 66,
  "registry_ids": [
    "I.D97"
  ],
  "related_registry_items": [
    {
      "id": "I.D97",
      "title": "Galois Automorphism",
      "url": "/registry/object/I.D97/"
    }
  ],
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookI/Coordinates/ChebyshevBias.lean#L56-L66",
  "formal_status": "defined",
  "right_rail": {
    "related": [
      {
        "title": "TauLib.BookI.Coordinates.ChebyshevBias",
        "url": "/verify/taulib/docs/book-i-coordinates-chebyshev-bias/"
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookI/Coordinates/ChebyshevBias.lean#L56-L66",
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

- Module: [TauLib.BookI.Coordinates.ChebyshevBias](/verify/taulib/docs/book-i-coordinates-chebyshev-bias/)
- Source path: [`TauLib/BookI/Coordinates/ChebyshevBias.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookI/Coordinates/ChebyshevBias.lean#L56-L66)
- Source range: L56-L66
- Kind: `def`
- Formal status hint: `defined`

## Registry Links

- `I.D97` — Galois Automorphism

## Immediate Comment / Docstring

```lean
/-- [I.D97] Count primes p ≤ x with p ≡ a (mod q). -/
```

## Source Excerpt

```lean
def prime_count_mod (x q a : Nat) : Nat :=
  if q == 0 then 0
  else go 2 0 (x + 1)
where
  go (p acc fuel : Nat) : Nat :=
    if fuel = 0 then acc
    else if p > x then acc
    else
      let hit := if is_prime_cb p && p % q == a % q then 1 else 0
      go (p + 1) (acc + hit) (fuel - 1)
  termination_by fuel
```

---
{
  "projection_kind": "taulib_declaration",
  "title": "chebyshev_bias",
  "permalink": "/verify/taulib/docs/book-i-coordinates-chebyshev-bias/chebyshev-bias/",
  "summary_short": "`def` declaration in `TauLib.BookI.Coordinates.ChebyshevBias`.",
  "declaration_id": "TauLib.BookI.Coordinates.ChebyshevBias::chebyshev_bias",
  "declaration_slug": "chebyshev-bias",
  "kind": "def",
  "name": "chebyshev_bias",
  "module_name": "TauLib.BookI.Coordinates.ChebyshevBias",
  "module_url": "/verify/taulib/docs/book-i-coordinates-chebyshev-bias/",
  "source_line_start": 89,
  "source_line_end": 101,
  "registry_ids": [
    "I.D98"
  ],
  "related_registry_items": [
    {
      "id": "I.D98",
      "title": "Galois Group of Primorial Stage",
      "url": "/registry/object/I.D98/"
    }
  ],
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookI/Coordinates/ChebyshevBias.lean#L89-L101",
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookI/Coordinates/ChebyshevBias.lean#L89-L101",
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
- Source path: [`TauLib/BookI/Coordinates/ChebyshevBias.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookI/Coordinates/ChebyshevBias.lean#L89-L101)
- Source range: L89-L101
- Kind: `def`
- Formal status hint: `defined`

## Registry Links

- `I.D98` — Galois Group of Primorial Stage

## Immediate Comment / Docstring

```lean
/-- [I.D98] Chebyshev bias: count how often π(n;q,a₁) > π(n;q,a₂)
    for n from 2 to x. Returns the count of "winning" values. -/
```

## Source Excerpt

```lean
def chebyshev_bias (x q a1 a2 : Nat) : Nat :=
  if q == 0 then 0
  else go 2 0 (x + 1) q a1 a2
where
  go (n acc fuel q a1 a2 : Nat) : Nat :=
    if fuel = 0 then acc
    else if n > x then acc
    else
      let c1 := prime_count_mod n q a1
      let c2 := prime_count_mod n q a2
      let win := if c1 > c2 then 1 else 0
      go (n + 1) (acc + win) (fuel - 1) q a1 a2
  termination_by fuel
```

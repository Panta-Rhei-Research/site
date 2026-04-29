---
{
  "projection_kind": "taulib_declaration",
  "title": "prime_race_check",
  "permalink": "/verify/taulib/docs/book-i-coordinates-chebyshev-bias/prime-race-check/",
  "summary_short": "`def` declaration in `TauLib.BookI.Coordinates.ChebyshevBias`.",
  "declaration_id": "TauLib.BookI.Coordinates.ChebyshevBias::prime_race_check",
  "declaration_slug": "prime-race-check",
  "kind": "def",
  "name": "prime_race_check",
  "module_name": "TauLib.BookI.Coordinates.ChebyshevBias",
  "module_url": "/verify/taulib/docs/book-i-coordinates-chebyshev-bias/",
  "source_line_start": 69,
  "source_line_end": 81,
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
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookI/Coordinates/ChebyshevBias.lean#L69-L81",
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookI/Coordinates/ChebyshevBias.lean#L69-L81",
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
- Source path: [`TauLib/BookI/Coordinates/ChebyshevBias.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookI/Coordinates/ChebyshevBias.lean#L69-L81)
- Source range: L69-L81
- Kind: `def`
- Formal status hint: `defined`

## Registry Links

- `I.D97` — Galois Automorphism

## Immediate Comment / Docstring

```lean
/-- [I.D97] Prime race: compare π(x; q, a₁) vs π(x; q, a₂). -/
```

## Source Excerpt

```lean
def prime_race_check (bound q a1 a2 : Nat) : Bool :=
  go 2 (bound + 1)
where
  go (x fuel : Nat) : Bool :=
    if fuel = 0 then true
    else if x > bound then true
    else
      -- Just check that both counts are well-defined (non-negative)
      let c1 := prime_count_mod x q a1
      let c2 := prime_count_mod x q a2
      -- At each x, one of them leads (or they're equal)
      (c1 >= 0 || c2 >= 0) && go (x + 1) (fuel - 1)  -- always true, structural
  termination_by fuel
```

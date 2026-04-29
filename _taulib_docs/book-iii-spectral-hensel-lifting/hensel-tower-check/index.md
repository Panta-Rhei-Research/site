---
{
  "projection_kind": "taulib_declaration",
  "title": "hensel_tower_check",
  "permalink": "/verify/taulib/docs/book-iii-spectral-hensel-lifting/hensel-tower-check/",
  "summary_short": "`def` declaration in `TauLib.BookIII.Spectral.HenselLifting`.",
  "declaration_id": "TauLib.BookIII.Spectral.HenselLifting::hensel_tower_check",
  "declaration_slug": "hensel-tower-check",
  "kind": "def",
  "name": "hensel_tower_check",
  "module_name": "TauLib.BookIII.Spectral.HenselLifting",
  "module_url": "/verify/taulib/docs/book-iii-spectral-hensel-lifting/",
  "source_line_start": 127,
  "source_line_end": 142,
  "registry_ids": [
    "III.T11"
  ],
  "related_registry_items": [
    {
      "id": "III.T11",
      "title": "Constructive Hensel Lifting",
      "url": "/registry/object/III.T11/"
    }
  ],
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIII/Spectral/HenselLifting.lean#L127-L142",
  "formal_status": "defined",
  "right_rail": {
    "related": [
      {
        "title": "TauLib.BookIII.Spectral.HenselLifting",
        "url": "/verify/taulib/docs/book-iii-spectral-hensel-lifting/"
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIII/Spectral/HenselLifting.lean#L127-L142",
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

- Module: [TauLib.BookIII.Spectral.HenselLifting](/verify/taulib/docs/book-iii-spectral-hensel-lifting/)
- Source path: [`TauLib/BookIII/Spectral/HenselLifting.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIII/Spectral/HenselLifting.lean#L127-L142)
- Source range: L127-L142
- Kind: `def`
- Formal status hint: `defined`

## Registry Links

- `III.T11` — Constructive Hensel Lifting

## Immediate Comment / Docstring

```lean
/-- [III.T11] Tower coherence of Hensel lifting:
    lift_n(r) mod p^k = lift_k(r) for k < n. -/
```

## Source Excerpt

```lean
def hensel_tower_check (bound : TauIdx) : Bool :=
  go 3 (bound + 1)
where
  go (p fuel : Nat) : Bool :=
    if fuel = 0 then true
    else if p > bound then true
    else
      if !is_prime_naive p then go (p + 1) (fuel - 1)
      else
        let a := 1
        let lift2 := hensel_lift a 1 p 2
        let lift3 := hensel_lift a 1 p 3
        let p2 := p * p
        let ok := if p2 > 0 then lift3 % p2 == lift2 % p2 else true
        ok && go (p + 1) (fuel - 1)
  termination_by fuel
```

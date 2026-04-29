---
{
  "projection_kind": "taulib_declaration",
  "title": "hensel_uniqueness_check",
  "permalink": "/verify/taulib/docs/book-iii-spectral-hensel-lifting/hensel-uniqueness-check/",
  "summary_short": "`def` declaration in `TauLib.BookIII.Spectral.HenselLifting`.",
  "declaration_id": "TauLib.BookIII.Spectral.HenselLifting::hensel_uniqueness_check",
  "declaration_slug": "hensel-uniqueness-check",
  "kind": "def",
  "name": "hensel_uniqueness_check",
  "module_name": "TauLib.BookIII.Spectral.HenselLifting",
  "module_url": "/verify/taulib/docs/book-iii-spectral-hensel-lifting/",
  "source_line_start": 107,
  "source_line_end": 123,
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
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIII/Spectral/HenselLifting.lean#L107-L123",
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIII/Spectral/HenselLifting.lean#L107-L123",
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
- Source path: [`TauLib/BookIII/Spectral/HenselLifting.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIII/Spectral/HenselLifting.lean#L107-L123)
- Source range: L107-L123
- Kind: `def`
- Formal status hint: `defined`

## Registry Links

- `III.T11` — Constructive Hensel Lifting

## Immediate Comment / Docstring

```lean
/-- [III.T11] Hensel uniqueness: the lifted root is unique mod p^n.
    Starting from any root r with r ≡ 1 mod p, the lift produces
    the same result as starting from 1. -/
```

## Source Excerpt

```lean
def hensel_uniqueness_check (bound : TauIdx) : Bool :=
  go 3 (bound + 1)
where
  go (p fuel : Nat) : Bool :=
    if fuel = 0 then true
    else if p > bound then true
    else
      if !is_prime_naive p then go (p + 1) (fuel - 1)
      else
        let a := 1
        -- Both start as 1 mod p (since hensel_lift reduces root mod p)
        let r1 := hensel_lift a 1 p 3
        let r2 := hensel_lift a (p + 1) p 3  -- p+1 ≡ 1 mod p
        let pn := p * p * p
        let ok := if pn > 0 then r1 % pn == r2 % pn else true
        ok && go (p + 1) (fuel - 1)
  termination_by fuel
```

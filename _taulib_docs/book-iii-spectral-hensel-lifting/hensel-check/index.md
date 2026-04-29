---
{
  "projection_kind": "taulib_declaration",
  "title": "hensel_check",
  "permalink": "/verify/taulib/docs/book-iii-spectral-hensel-lifting/hensel-check/",
  "summary_short": "`def` declaration in `TauLib.BookIII.Spectral.HenselLifting`.",
  "declaration_id": "TauLib.BookIII.Spectral.HenselLifting::hensel_check",
  "declaration_slug": "hensel-check",
  "kind": "def",
  "name": "hensel_check",
  "module_name": "TauLib.BookIII.Spectral.HenselLifting",
  "module_url": "/verify/taulib/docs/book-iii-spectral-hensel-lifting/",
  "source_line_start": 86,
  "source_line_end": 102,
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
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIII/Spectral/HenselLifting.lean#L86-L102",
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIII/Spectral/HenselLifting.lean#L86-L102",
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
- Source path: [`TauLib/BookIII/Spectral/HenselLifting.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIII/Spectral/HenselLifting.lean#L86-L102)
- Source range: L86-L102
- Kind: `def`
- Formal status hint: `defined`

## Registry Links

- `III.T11` — Constructive Hensel Lifting

## Immediate Comment / Docstring

```lean
/-- [III.T11] Hensel lifting check: verify that lifted root satisfies
    f(x) ≡ 0 mod p^n for test cases. -/
```

## Source Excerpt

```lean
def hensel_check (bound : TauIdx) : Bool :=
  go 3 (bound + 1)
where
  go (p fuel : Nat) : Bool :=
    if fuel = 0 then true
    else if p > bound then true
    else
      if !is_prime_naive p then go (p + 1) (fuel - 1)
      else
        let a := 1  -- f(x) = x² - 1
        let root := 1  -- 1 is always a root of x²-1 mod p
        let lifted2 := hensel_lift a root p 2
        let lifted3 := hensel_lift a root p 3
        let ok2 := poly_eval a lifted2 (p * p) == 0
        let ok3 := poly_eval a lifted3 (p * p * p) == 0
        ok2 && ok3 && go (p + 1) (fuel - 1)
  termination_by fuel
```

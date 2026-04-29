---
{
  "projection_kind": "taulib_declaration",
  "title": "additive_multiplicative_check",
  "permalink": "/verify/taulib/docs/book-iii-spectral-additive-conjectures/additive-multiplicative-check/",
  "summary_short": "`def` declaration in `TauLib.BookIII.Spectral.AdditiveConjectures`.",
  "declaration_id": "TauLib.BookIII.Spectral.AdditiveConjectures::additive_multiplicative_check",
  "declaration_slug": "additive-multiplicative-check",
  "kind": "def",
  "name": "additive_multiplicative_check",
  "module_name": "TauLib.BookIII.Spectral.AdditiveConjectures",
  "module_url": "/verify/taulib/docs/book-iii-spectral-additive-conjectures/",
  "source_line_start": 167,
  "source_line_end": 184,
  "registry_ids": [
    "III.P40"
  ],
  "related_registry_items": [
    {
      "id": "III.P40",
      "title": "Additive-Multiplicative Duality",
      "url": "/registry/object/III.P40/"
    }
  ],
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIII/Spectral/AdditiveConjectures.lean#L167-L184",
  "formal_status": "defined",
  "right_rail": {
    "related": [
      {
        "title": "TauLib.BookIII.Spectral.AdditiveConjectures",
        "url": "/verify/taulib/docs/book-iii-spectral-additive-conjectures/"
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIII/Spectral/AdditiveConjectures.lean#L167-L184",
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

- Module: [TauLib.BookIII.Spectral.AdditiveConjectures](/verify/taulib/docs/book-iii-spectral-additive-conjectures/)
- Source path: [`TauLib/BookIII/Spectral/AdditiveConjectures.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIII/Spectral/AdditiveConjectures.lean#L167-L184)
- Source range: L167-L184
- Kind: `def`
- Formal status hint: `defined`

## Registry Links

- `III.P40` — Additive-Multiplicative Duality

## Immediate Comment / Docstring

```lean
/-- [III.P40] Additive-multiplicative duality: at each primorial level,
    the Goldbach partition count and twin prime count are both positive.
    Both additive and multiplicative structures are nontrivial. -/
```

## Source Excerpt

```lean
def additive_multiplicative_check (db : Nat) : Bool :=
  go 2 (db + 1)
where
  go (k fuel : Nat) : Bool :=
    if fuel = 0 then true
    else if k > db then true
    else
      let pk := primorial k
      -- Pick an even number near M_k (at least 4)
      let test_n := if pk >= 4 then (if pk % 2 == 0 then pk else pk - 1) else 4
      -- Goldbach partition count positive
      let gp := goldbach_partition_count test_n > 0
      -- Twin primes exist up to M_k (capped)
      let tp := twin_prime_count (min pk 100) > 0
      -- CRT dimension = k (multiplicative structure)
      let crt := k > 0
      gp && tp && crt && go (k + 1) (fuel - 1)
  termination_by fuel
```

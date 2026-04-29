---
{
  "projection_kind": "taulib_declaration",
  "title": "goldbach_pair",
  "permalink": "/verify/taulib/docs/book-iii-spectral-additive-conjectures/goldbach-pair/",
  "summary_short": "`def` declaration in `TauLib.BookIII.Spectral.AdditiveConjectures`.",
  "declaration_id": "TauLib.BookIII.Spectral.AdditiveConjectures::goldbach_pair",
  "declaration_slug": "goldbach-pair",
  "kind": "def",
  "name": "goldbach_pair",
  "module_name": "TauLib.BookIII.Spectral.AdditiveConjectures",
  "module_url": "/verify/taulib/docs/book-iii-spectral-additive-conjectures/",
  "source_line_start": 69,
  "source_line_end": 78,
  "registry_ids": [
    "III.D95"
  ],
  "related_registry_items": [
    {
      "id": "III.D95",
      "title": "Goldbach Representation",
      "url": "/registry/object/III.D95/"
    }
  ],
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIII/Spectral/AdditiveConjectures.lean#L69-L78",
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIII/Spectral/AdditiveConjectures.lean#L69-L78",
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
- Source path: [`TauLib/BookIII/Spectral/AdditiveConjectures.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIII/Spectral/AdditiveConjectures.lean#L69-L78)
- Source range: L69-L78
- Kind: `def`
- Formal status hint: `defined`

## Registry Links

- `III.D95` — Goldbach Representation

## Immediate Comment / Docstring

```lean
/-- [III.D95] Check if even n ≥ 4 has a Goldbach representation p + q = n. -/
```

## Source Excerpt

```lean
def goldbach_pair (n : Nat) : Bool :=
  if n < 4 || n % 2 != 0 then false
  else go 2 (n / 2 + 1)
where
  go (p fuel : Nat) : Bool :=
    if fuel = 0 then false
    else if p > n / 2 then false
    else if is_prime_nat p && is_prime_nat (n - p) then true
    else go (p + 1) (fuel - 1)
  termination_by fuel
```

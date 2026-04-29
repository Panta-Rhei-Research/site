---
{
  "projection_kind": "taulib_declaration",
  "title": "twin_prime_density_check",
  "permalink": "/verify/taulib/docs/book-iii-spectral-additive-conjectures/twin-prime-density-check/",
  "summary_short": "`def` declaration in `TauLib.BookIII.Spectral.AdditiveConjectures`.",
  "declaration_id": "TauLib.BookIII.Spectral.AdditiveConjectures::twin_prime_density_check",
  "declaration_slug": "twin-prime-density-check",
  "kind": "def",
  "name": "twin_prime_density_check",
  "module_name": "TauLib.BookIII.Spectral.AdditiveConjectures",
  "module_url": "/verify/taulib/docs/book-iii-spectral-additive-conjectures/",
  "source_line_start": 129,
  "source_line_end": 140,
  "registry_ids": [
    "III.D96"
  ],
  "related_registry_items": [
    {
      "id": "III.D96",
      "title": "Twin Prime Distribution",
      "url": "/registry/object/III.D96/"
    }
  ],
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIII/Spectral/AdditiveConjectures.lean#L129-L140",
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIII/Spectral/AdditiveConjectures.lean#L129-L140",
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
- Source path: [`TauLib/BookIII/Spectral/AdditiveConjectures.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIII/Spectral/AdditiveConjectures.lean#L129-L140)
- Source range: L129-L140
- Kind: `def`
- Formal status hint: `defined`

## Registry Links

- `III.D96` — Twin Prime Distribution

## Immediate Comment / Docstring

```lean
/-- [III.D96] Twin prime density check: at least one twin pair exists
    up to each primorial level. -/
```

## Source Excerpt

```lean
def twin_prime_density_check (db : Nat) : Bool :=
  go 2 (db + 1)
where
  go (k fuel : Nat) : Bool :=
    if fuel = 0 then true
    else if k > db then true
    else
      let pk := primorial k
      let bound := min pk 100
      let count := twin_prime_count bound
      count > 0 && go (k + 1) (fuel - 1)
  termination_by fuel
```

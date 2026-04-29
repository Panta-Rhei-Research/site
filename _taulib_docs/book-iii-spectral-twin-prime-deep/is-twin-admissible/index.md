---
{
  "projection_kind": "taulib_declaration",
  "title": "is_twin_admissible",
  "permalink": "/verify/taulib/docs/book-iii-spectral-twin-prime-deep/is-twin-admissible/",
  "summary_short": "`def` declaration in `TauLib.BookIII.Spectral.TwinPrimeDeep`.",
  "declaration_id": "TauLib.BookIII.Spectral.TwinPrimeDeep::is_twin_admissible",
  "declaration_slug": "is-twin-admissible",
  "kind": "def",
  "name": "is_twin_admissible",
  "module_name": "TauLib.BookIII.Spectral.TwinPrimeDeep",
  "module_url": "/verify/taulib/docs/book-iii-spectral-twin-prime-deep/",
  "source_line_start": 103,
  "source_line_end": 117,
  "registry_ids": [],
  "related_registry_items": [],
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIII/Spectral/TwinPrimeDeep.lean#L103-L117",
  "formal_status": "defined",
  "right_rail": {
    "related": [
      {
        "title": "TauLib.BookIII.Spectral.TwinPrimeDeep",
        "url": "/verify/taulib/docs/book-iii-spectral-twin-prime-deep/"
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIII/Spectral/TwinPrimeDeep.lean#L103-L117",
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

- Module: [TauLib.BookIII.Spectral.TwinPrimeDeep](/verify/taulib/docs/book-iii-spectral-twin-prime-deep/)
- Source path: [`TauLib/BookIII/Spectral/TwinPrimeDeep.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIII/Spectral/TwinPrimeDeep.lean#L103-L117)
- Source range: L103-L117
- Kind: `def`
- Formal status hint: `defined`

## Registry Links

- No Registry IDs were detected in this declaration block.

## Immediate Comment / Docstring

```lean
/-- Helper: check if residue r is twin-admissible at all primes up to depth d.
    For each p_i (i=1..d): r mod p_i ≠ 0 AND (r+2) mod p_i ≠ 0.
    This includes p=2: r must be odd. -/
```

## Source Excerpt

```lean
def is_twin_admissible (r d : Nat) : Bool :=
  go 1 (d + 1)
where
  go (i fuel : Nat) : Bool :=
    if fuel = 0 then true
    else if i > d then true
    else
      let p := nth_prime i
      if p == 0 then go (i + 1) (fuel - 1)
      else
        let r_mod := r % p
        let r2_mod := (r + 2) % p
        if r_mod == 0 || r2_mod == 0 then false
        else go (i + 1) (fuel - 1)
  termination_by fuel
```

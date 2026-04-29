---
{
  "projection_kind": "taulib_declaration",
  "title": "finite_spectral_support_check",
  "permalink": "/verify/taulib/docs/book-ii-hartogs-canonical-basis/finite-spectral-support-check/",
  "summary_short": "`def` declaration in `TauLib.BookII.Hartogs.CanonicalBasis`.",
  "declaration_id": "TauLib.BookII.Hartogs.CanonicalBasis::finite_spectral_support_check",
  "declaration_slug": "finite-spectral-support-check",
  "kind": "def",
  "name": "finite_spectral_support_check",
  "module_name": "TauLib.BookII.Hartogs.CanonicalBasis",
  "module_url": "/verify/taulib/docs/book-ii-hartogs-canonical-basis/",
  "source_line_start": 211,
  "source_line_end": 222,
  "registry_ids": [
    "II.T31"
  ],
  "related_registry_items": [
    {
      "id": "II.T31",
      "title": "Finite Spectral Support",
      "url": "/registry/object/II.T31/"
    }
  ],
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookII/Hartogs/CanonicalBasis.lean#L211-L222",
  "formal_status": "defined",
  "right_rail": {
    "related": [
      {
        "title": "TauLib.BookII.Hartogs.CanonicalBasis",
        "url": "/verify/taulib/docs/book-ii-hartogs-canonical-basis/"
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookII/Hartogs/CanonicalBasis.lean#L211-L222",
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

- Module: [TauLib.BookII.Hartogs.CanonicalBasis](/verify/taulib/docs/book-ii-hartogs-canonical-basis/)
- Source path: [`TauLib/BookII/Hartogs/CanonicalBasis.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookII/Hartogs/CanonicalBasis.lean#L211-L222)
- Source range: L211-L222
- Kind: `def`
- Formal status hint: `defined`

## Registry Links

- `II.T31` — Finite Spectral Support

## Immediate Comment / Docstring

```lean
/-- [II.T31] Finite spectral support check:
    at each stage k, the count of active generators equals k,
    which is <= sum of p_i. -/
```

## Source Excerpt

```lean
def finite_spectral_support_check (k_max bound : TauIdx) : Bool :=
  go 1 0 ((k_max + 1) * (bound + 1))
where
  go (k x fuel : Nat) : Bool :=
    if fuel = 0 then true
    else if k > k_max then true
    else if x >= primorial k then go (k + 1) 0 (fuel - 1)
    else
      let cnt := count_nonzero_generators k x
      let bnd := prime_sum k
      (cnt == k && cnt <= bnd) && go k (x + 1) (fuel - 1)
  termination_by fuel
```

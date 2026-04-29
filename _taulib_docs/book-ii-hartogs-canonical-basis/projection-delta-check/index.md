---
{
  "projection_kind": "taulib_declaration",
  "title": "projection_delta_check",
  "permalink": "/verify/taulib/docs/book-ii-hartogs-canonical-basis/projection-delta-check/",
  "summary_short": "`def` declaration in `TauLib.BookII.Hartogs.CanonicalBasis`.",
  "declaration_id": "TauLib.BookII.Hartogs.CanonicalBasis::projection_delta_check",
  "declaration_slug": "projection-delta-check",
  "kind": "def",
  "name": "projection_delta_check",
  "module_name": "TauLib.BookII.Hartogs.CanonicalBasis",
  "module_url": "/verify/taulib/docs/book-ii-hartogs-canonical-basis/",
  "source_line_start": 243,
  "source_line_end": 259,
  "registry_ids": [
    "II.P09"
  ],
  "related_registry_items": [
    {
      "id": "II.P09",
      "title": "Decomposition Functoriality",
      "url": "/registry/object/II.P09/"
    }
  ],
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookII/Hartogs/CanonicalBasis.lean#L243-L259",
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookII/Hartogs/CanonicalBasis.lean#L243-L259",
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
- Source path: [`TauLib/BookII/Hartogs/CanonicalBasis.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookII/Hartogs/CanonicalBasis.lean#L243-L259)
- Source range: L243-L259
- Kind: `def`
- Formal status hint: `defined`

## Registry Links

- `II.P09` — Decomposition Functoriality

## Immediate Comment / Docstring

```lean
/-- [II.P09] Projection delta check: for delta_a(x) = (x == a ? 1 : 0),
    proj_coeff(delta_a, k, pi, a mod p) = 1 for all a in [0, P_k). -/
```

## Source Excerpt

```lean
def projection_delta_check (k_max : TauIdx) : Bool :=
  go 1 1 0 (k_max * k_max * 100 + 1)
where
  go (k pi_idx a fuel : Nat) : Bool :=
    if fuel = 0 then true
    else if k > k_max then true
    else if pi_idx > k then go (k + 1) 1 0 (fuel - 1)
    else if a >= primorial k then go k (pi_idx + 1) 0 (fuel - 1)
    else
      let p := nth_prime pi_idx
      if p == 0 then go k (pi_idx + 1) 0 (fuel - 1)
      else
        let v := a % p
        let delta_a : TauIdx → Int := fun x => if x == a then 1 else 0
        let coeff := proj_coeff delta_a k pi_idx v
        (coeff == 1) && go k pi_idx (a + 1) (fuel - 1)
  termination_by fuel
```

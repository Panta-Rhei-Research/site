---
{
  "projection_kind": "taulib_declaration",
  "title": "projection_recovery_check",
  "permalink": "/verify/taulib/docs/book-ii-hartogs-canonical-basis/projection-recovery-check/",
  "summary_short": "`def` declaration in `TauLib.BookII.Hartogs.CanonicalBasis`.",
  "declaration_id": "TauLib.BookII.Hartogs.CanonicalBasis::projection_recovery_check",
  "declaration_slug": "projection-recovery-check",
  "kind": "def",
  "name": "projection_recovery_check",
  "module_name": "TauLib.BookII.Hartogs.CanonicalBasis",
  "module_url": "/verify/taulib/docs/book-ii-hartogs-canonical-basis/",
  "source_line_start": 263,
  "source_line_end": 279,
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
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookII/Hartogs/CanonicalBasis.lean#L263-L279",
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookII/Hartogs/CanonicalBasis.lean#L263-L279",
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
- Source path: [`TauLib/BookII/Hartogs/CanonicalBasis.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookII/Hartogs/CanonicalBasis.lean#L263-L279)
- Source range: L263-L279
- Kind: `def`
- Formal status hint: `defined`

## Registry Links

- `II.P09` — Decomposition Functoriality

## Immediate Comment / Docstring

```lean
/-- [II.P09] Projection recovery check: for f(x) = 1,
    proj_coeff(1, k, pi, v) = P_k / p for each v. -/
```

## Source Excerpt

```lean
def projection_recovery_check (k_max : TauIdx) : Bool :=
  go 1 1 0 (k_max * k_max * 20 + 1)
where
  go (k pi_idx v fuel : Nat) : Bool :=
    if fuel = 0 then true
    else if k > k_max then true
    else if pi_idx > k then go (k + 1) 1 0 (fuel - 1)
    else
      let p := nth_prime pi_idx
      if p == 0 then go k (pi_idx + 1) 0 (fuel - 1)
      else if v >= p then go k (pi_idx + 1) 0 (fuel - 1)
      else
        let one_fn : TauIdx → Int := fun _ => 1
        let coeff := proj_coeff one_fn k pi_idx v
        let expected : Int := (primorial k / p : Nat)
        (coeff == expected) && go k pi_idx (v + 1) (fuel - 1)
  termination_by fuel
```

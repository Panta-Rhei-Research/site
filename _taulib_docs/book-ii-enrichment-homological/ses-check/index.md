---
{
  "projection_kind": "taulib_declaration",
  "title": "ses_check",
  "permalink": "/verify/taulib/docs/book-ii-enrichment-homological/ses-check/",
  "summary_short": "`def` declaration in `TauLib.BookII.Enrichment.Homological`.",
  "declaration_id": "TauLib.BookII.Enrichment.Homological::ses_check",
  "declaration_slug": "ses-check",
  "kind": "def",
  "name": "ses_check",
  "module_name": "TauLib.BookII.Enrichment.Homological",
  "module_url": "/verify/taulib/docs/book-ii-enrichment-homological/",
  "source_line_start": 128,
  "source_line_end": 155,
  "registry_ids": [
    "II.P19"
  ],
  "related_registry_items": [
    {
      "id": "II.P19",
      "title": "Long Exact Sequence",
      "url": "/registry/object/II.P19/"
    }
  ],
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookII/Enrichment/Homological.lean#L128-L155",
  "formal_status": "defined",
  "right_rail": {
    "related": [
      {
        "title": "TauLib.BookII.Enrichment.Homological",
        "url": "/verify/taulib/docs/book-ii-enrichment-homological/"
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookII/Enrichment/Homological.lean#L128-L155",
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

- Module: [TauLib.BookII.Enrichment.Homological](/verify/taulib/docs/book-ii-enrichment-homological/)
- Source path: [`TauLib/BookII/Enrichment/Homological.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookII/Enrichment/Homological.lean#L128-L155)
- Source range: L128-L155
- Kind: `def`
- Formal status hint: `defined`

## Registry Links

- `II.P19` — Long Exact Sequence

## Immediate Comment / Docstring

```lean
/-- [II.P19] Short exact sequence check: 0 → A →f B →g C → 0.
    For primorial tower: A = Z/M_{k-1} Z, B = Z/M_k Z, C = Z/p_k Z.
    f = inclusion (x ↦ x · p_k), g = reduction (x ↦ x mod p_k). -/
```

## Source Excerpt

```lean
def ses_check (k : Nat) : Bool :=
  if k == 0 then true
  else
    let pk := primorial k
    let p := nth_prime k
    if p == 0 then true
    else
      -- Check g ∘ f = 0: (x · p_k) mod p_k = 0
      let gf_zero := go_gf 0 (primorial (k - 1)) p pk
      -- Check f injective: x · p_k ≠ y · p_k mod M_k for x ≠ y
      let f_inj := go_inj 0 (primorial (k - 1)) p pk
      gf_zero && f_inj
where
  go_gf (x bound p pk : Nat) : Bool :=
    if x >= bound then true
    else
      let fx := (x * p) % pk
      let gfx := fx % p
      gfx == 0 && go_gf (x + 1) bound p pk
  termination_by bound - x
  go_inj (x bound p pk : Nat) : Bool :=
    if x >= bound then true
    else
      let fx := (x * p) % pk
      -- fx uniquely determines x (since p | M_k and gcd(p, M_{k-1}) = 1)
      let recovered := fx / p
      recovered == x && go_inj (x + 1) bound p pk
  termination_by bound - x
```

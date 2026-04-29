---
{
  "projection_kind": "taulib_declaration",
  "title": "ses_exactness_check",
  "permalink": "/verify/taulib/docs/book-ii-enrichment-homological/ses-exactness-check/",
  "summary_short": "`def` declaration in `TauLib.BookII.Enrichment.Homological`.",
  "declaration_id": "TauLib.BookII.Enrichment.Homological::ses_exactness_check",
  "declaration_slug": "ses-exactness-check",
  "kind": "def",
  "name": "ses_exactness_check",
  "module_name": "TauLib.BookII.Enrichment.Homological",
  "module_url": "/verify/taulib/docs/book-ii-enrichment-homological/",
  "source_line_start": 86,
  "source_line_end": 102,
  "registry_ids": [
    "II.D85"
  ],
  "related_registry_items": [
    {
      "id": "II.D85",
      "title": "Homology via SES",
      "url": "/registry/object/II.D85/"
    }
  ],
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookII/Enrichment/Homological.lean#L86-L102",
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookII/Enrichment/Homological.lean#L86-L102",
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
- Source path: [`TauLib/BookII/Enrichment/Homological.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookII/Enrichment/Homological.lean#L86-L102)
- Source range: L86-L102
- Kind: `def`
- Formal status hint: `defined`

## Registry Links

- `II.D85` — Homology via SES

## Immediate Comment / Docstring

```lean
/-- [II.D85] For the SES 0 → Z/M_{k-1} →f Z/M_k →g Z/p_k → 0:
    ker(g) = {x ∈ Z/M_k : x mod p_k = 0} and im(f) = {x·p_k : x ∈ Z/M_{k-1}}.
    Exactness means ker(g) = im(f), so H = ker/im is trivial.
    This check verifies ker(g) ⊆ im(f): every x with x mod p = 0 equals y·p
    for some y. -/
```

## Source Excerpt

```lean
def ses_exactness_check (k : Nat) : Bool :=
  if k == 0 then true
  else
    let pk := primorial k
    let p := nth_prime k
    if p == 0 then true
    else go 0 pk p pk
where
  go (x pk p fuel : Nat) : Bool :=
    if fuel = 0 then true
    else if x >= pk then true
    else
      let in_ker_g := x % p == 0
      -- If x ∈ ker(g), check x = y · p for some y < M_{k-1}
      let in_im_f := if in_ker_g then x / p < pk / p else true
      in_im_f && go (x + 1) pk p (fuel - 1)
  termination_by fuel
```

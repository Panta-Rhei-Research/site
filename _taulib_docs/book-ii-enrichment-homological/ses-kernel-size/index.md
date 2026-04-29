---
{
  "projection_kind": "taulib_declaration",
  "title": "ses_kernel_size",
  "permalink": "/verify/taulib/docs/book-ii-enrichment-homological/ses-kernel-size/",
  "summary_short": "`def` declaration in `TauLib.BookII.Enrichment.Homological`.",
  "declaration_id": "TauLib.BookII.Enrichment.Homological::ses_kernel_size",
  "declaration_slug": "ses-kernel-size",
  "kind": "def",
  "name": "ses_kernel_size",
  "module_name": "TauLib.BookII.Enrichment.Homological",
  "module_url": "/verify/taulib/docs/book-ii-enrichment-homological/",
  "source_line_start": 106,
  "source_line_end": 112,
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
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookII/Enrichment/Homological.lean#L106-L112",
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookII/Enrichment/Homological.lean#L106-L112",
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
- Source path: [`TauLib/BookII/Enrichment/Homological.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookII/Enrichment/Homological.lean#L106-L112)
- Source range: L106-L112
- Kind: `def`
- Formal status hint: `defined`

## Registry Links

- `II.D85` — Homology via SES

## Immediate Comment / Docstring

```lean
/-- [II.D85] Count the size of ker(g) = |{x ∈ Z/M_k : x mod p_k = 0}|.
    Should equal M_{k-1} = M_k / p_k. -/
```

## Source Excerpt

```lean
def ses_kernel_size (k : Nat) : Nat :=
  if k == 0 then 1
  else
    let pk := primorial k
    let p := nth_prime k
    if p == 0 then 0
    else pk / p
```

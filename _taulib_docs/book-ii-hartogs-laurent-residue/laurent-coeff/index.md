---
{
  "projection_kind": "taulib_declaration",
  "title": "laurent_coeff",
  "permalink": "/verify/taulib/docs/book-ii-hartogs-laurent-residue/laurent-coeff/",
  "summary_short": "`def` declaration in `TauLib.BookII.Hartogs.LaurentResidue`.",
  "declaration_id": "TauLib.BookII.Hartogs.LaurentResidue::laurent_coeff",
  "declaration_slug": "laurent-coeff",
  "kind": "def",
  "name": "laurent_coeff",
  "module_name": "TauLib.BookII.Hartogs.LaurentResidue",
  "module_url": "/verify/taulib/docs/book-ii-hartogs-laurent-residue/",
  "source_line_start": 63,
  "source_line_end": 65,
  "registry_ids": [
    "II.D42"
  ],
  "related_registry_items": [
    {
      "id": "II.D42",
      "title": "Laurent Expansion",
      "url": "/registry/object/II.D42/"
    }
  ],
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookII/Hartogs/LaurentResidue.lean#L63-L65",
  "formal_status": "defined",
  "right_rail": {
    "related": [
      {
        "title": "TauLib.BookII.Hartogs.LaurentResidue",
        "url": "/verify/taulib/docs/book-ii-hartogs-laurent-residue/"
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookII/Hartogs/LaurentResidue.lean#L63-L65",
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

- Module: [TauLib.BookII.Hartogs.LaurentResidue](/verify/taulib/docs/book-ii-hartogs-laurent-residue/)
- Source path: [`TauLib/BookII/Hartogs/LaurentResidue.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookII/Hartogs/LaurentResidue.lean#L63-L65)
- Source range: L63-L65
- Kind: `def`
- Formal status hint: `defined`

## Registry Links

- `II.D42` — Laurent Expansion

## Immediate Comment / Docstring

```lean
/-- [II.D42] The i-th Laurent coefficient of x at stage k:
    the residue of x modulo the i-th prime p_i.

    In the CRT decomposition of Z/M_k Z = Z/p_1 Z x ... x Z/p_k Z,
    the i-th component is x mod p_i. This is the tau-analog of the
    i-th Laurent coefficient in the expansion around the i-th prime.

    Returns 0 if prime_idx = 0 or prime_idx > k (out of range). -/
```

## Source Excerpt

```lean
def laurent_coeff (x k prime_idx : TauIdx) : TauIdx :=
  if prime_idx == 0 || prime_idx > k then 0
  else x % nth_prime prime_idx
```

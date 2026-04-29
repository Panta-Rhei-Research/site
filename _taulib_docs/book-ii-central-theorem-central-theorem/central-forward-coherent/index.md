---
{
  "projection_kind": "taulib_declaration",
  "title": "central_forward_coherent",
  "permalink": "/verify/taulib/docs/book-ii-central-theorem-central-theorem/central-forward-coherent/",
  "summary_short": "`theorem` declaration in `TauLib.BookII.CentralTheorem.CentralTheorem`.",
  "declaration_id": "TauLib.BookII.CentralTheorem.CentralTheorem::central_forward_coherent",
  "declaration_slug": "central-forward-coherent",
  "kind": "theorem",
  "name": "central_forward_coherent",
  "module_name": "TauLib.BookII.CentralTheorem.CentralTheorem",
  "module_url": "/verify/taulib/docs/book-ii-central-theorem-central-theorem/",
  "source_line_start": 425,
  "source_line_end": 427,
  "registry_ids": [
    "II.T40"
  ],
  "related_registry_items": [
    {
      "id": "II.T40",
      "title": "Central Theorem",
      "url": "/registry/object/II.T40/"
    }
  ],
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookII/CentralTheorem/CentralTheorem.lean#L425-L427",
  "formal_status": "formalized",
  "right_rail": {
    "related": [
      {
        "title": "TauLib.BookII.CentralTheorem.CentralTheorem",
        "url": "/verify/taulib/docs/book-ii-central-theorem-central-theorem/"
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookII/CentralTheorem/CentralTheorem.lean#L425-L427",
        "external": true
      }
    ],
    "meta": {
      "type": "TauLib Declaration",
      "kind": "theorem",
      "status": "formalized"
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

- Module: [TauLib.BookII.CentralTheorem.CentralTheorem](/verify/taulib/docs/book-ii-central-theorem-central-theorem/)
- Source path: [`TauLib/BookII/CentralTheorem/CentralTheorem.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookII/CentralTheorem/CentralTheorem.lean#L425-L427)
- Source range: L425-L427
- Kind: `theorem`
- Formal status hint: `formalized`

## Registry Links

- `II.T40` — Central Theorem

## Immediate Comment / Docstring

```lean
/-- [II.T40] Central Theorem forward: spectral data produces tower-coherent output.
    spectral_to_hol(b_fn, c_fn, x, k) uses reduce(x, k), so
    reduce(spectral_to_hol(_, _, x, l), k) = spectral_to_hol(_, _, x, k)
    when b_fn and c_fn are the identity (both sides reduce to reduce(x, k)). -/
```

## Source Excerpt

```lean
theorem central_forward_coherent (x : TauIdx) {k l : TauIdx} (h : k ≤ l) :
    reduce (reduce x l) k = reduce x k :=
  reduction_compat x h
```

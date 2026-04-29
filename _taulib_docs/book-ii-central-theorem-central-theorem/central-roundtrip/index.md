---
{
  "projection_kind": "taulib_declaration",
  "title": "central_roundtrip",
  "permalink": "/verify/taulib/docs/book-ii-central-theorem-central-theorem/central-roundtrip/",
  "summary_short": "`theorem` declaration in `TauLib.BookII.CentralTheorem.CentralTheorem`.",
  "declaration_id": "TauLib.BookII.CentralTheorem.CentralTheorem::central_roundtrip",
  "declaration_slug": "central-roundtrip",
  "kind": "theorem",
  "name": "central_roundtrip",
  "module_name": "TauLib.BookII.CentralTheorem.CentralTheorem",
  "module_url": "/verify/taulib/docs/book-ii-central-theorem-central-theorem/",
  "source_line_start": 441,
  "source_line_end": 444,
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
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookII/CentralTheorem/CentralTheorem.lean#L441-L444",
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookII/CentralTheorem/CentralTheorem.lean#L441-L444",
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
- Source path: [`TauLib/BookII/CentralTheorem/CentralTheorem.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookII/CentralTheorem/CentralTheorem.lean#L441-L444)
- Source range: L441-L444
- Kind: `theorem`
- Formal status hint: `formalized`

## Registry Links

- `II.T40` — Central Theorem

## Immediate Comment / Docstring

```lean
/-- [II.T40] Central Theorem round-trip: the forward and inverse maps compose
    to the identity on spectral data. For b_fn = identity:
    spectral_to_hol(id, id, x, k) = (reduce(x,k), reduce(x,k))
    hol_to_spectral(id_stage, x, k) = (reduce(x,k), reduce(x,k))
    These are equal. -/
```

## Source Excerpt

```lean
theorem central_roundtrip (x k : TauIdx) :
    spectral_to_hol (fun n => (n : Int)) (fun n => (n : Int)) x k =
    hol_to_spectral id_stage x k := by
  simp [spectral_to_hol, hol_to_spectral, id_stage, reduce]
```

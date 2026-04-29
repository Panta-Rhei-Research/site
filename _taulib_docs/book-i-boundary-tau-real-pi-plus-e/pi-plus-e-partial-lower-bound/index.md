---
{
  "projection_kind": "taulib_declaration",
  "title": "TauReal.pi_plus_e_partial_lower_bound",
  "permalink": "/verify/taulib/docs/book-i-boundary-tau-real-pi-plus-e/pi-plus-e-partial-lower-bound/",
  "summary_short": "`theorem` declaration in `TauLib.BookI.Boundary.TauRealPiPlusE`.",
  "declaration_id": "TauLib.BookI.Boundary.TauRealPiPlusE::TauReal.pi_plus_e_partial_lower_bound",
  "declaration_slug": "pi-plus-e-partial-lower-bound",
  "kind": "theorem",
  "name": "TauReal.pi_plus_e_partial_lower_bound",
  "module_name": "TauLib.BookI.Boundary.TauRealPiPlusE",
  "module_url": "/verify/taulib/docs/book-i-boundary-tau-real-pi-plus-e/",
  "source_line_start": 126,
  "source_line_end": 134,
  "registry_ids": [],
  "related_registry_items": [],
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookI/Boundary/TauRealPiPlusE.lean#L126-L134",
  "formal_status": "formalized",
  "right_rail": {
    "related": [
      {
        "title": "TauLib.BookI.Boundary.TauRealPiPlusE",
        "url": "/verify/taulib/docs/book-i-boundary-tau-real-pi-plus-e/"
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookI/Boundary/TauRealPiPlusE.lean#L126-L134",
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

- Module: [TauLib.BookI.Boundary.TauRealPiPlusE](/verify/taulib/docs/book-i-boundary-tau-real-pi-plus-e/)
- Source path: [`TauLib/BookI/Boundary/TauRealPiPlusE.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookI/Boundary/TauRealPiPlusE.lean#L126-L134)
- Source range: L126-L134
- Kind: `theorem`
- Formal status hint: `formalized`

## Registry Links

- No Registry IDs were detected in this declaration block.

## Immediate Comment / Docstring

```lean
-- ============================================================
-- PART 3: LOWER BOUND  pi_partial n + e_partial n ≥ 11/3  for n ≥ 1
-- ============================================================
```

## Source Excerpt

```lean
theorem TauReal.pi_plus_e_partial_lower_bound (n : Nat) (hn : 1 ≤ n) :
    (TauRat.pi_partial n).toRat + (TauRat.e_partial n).toRat ≥ 11 / 3 := by
  have h_pi_mono : (TauRat.pi_partial 1).toRat ≤ (TauRat.pi_partial n).toRat :=
    TauRat.pi_partial_monotone hn
  have h_e_mono : (TauRat.e_partial 1).toRat ≤ (TauRat.e_partial n).toRat :=
    TauRat.e_partial_monotone hn
  have h_pi_1 := TauRat.pi_partial_one_toRat
  have h_e_1 := TauRat.e_partial_one_toRat
  linarith
```

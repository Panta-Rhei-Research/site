---
{
  "projection_kind": "taulib_declaration",
  "title": "teich_orthogonality_formal",
  "permalink": "/verify/taulib/docs/book-i-polarity-teichmueller-lift/teich-orthogonality-formal/",
  "summary_short": "`theorem` declaration in `TauLib.BookI.Polarity.TeichmuellerLift`.",
  "declaration_id": "TauLib.BookI.Polarity.TeichmuellerLift::teich_orthogonality_formal",
  "declaration_slug": "teich-orthogonality-formal",
  "kind": "theorem",
  "name": "teich_orthogonality_formal",
  "module_name": "TauLib.BookI.Polarity.TeichmuellerLift",
  "module_url": "/verify/taulib/docs/book-i-polarity-teichmueller-lift/",
  "source_line_start": 223,
  "source_line_end": 230,
  "registry_ids": [],
  "related_registry_items": [],
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookI/Polarity/TeichmuellerLift.lean#L223-L230",
  "formal_status": "formalized",
  "right_rail": {
    "related": [
      {
        "title": "TauLib.BookI.Polarity.TeichmuellerLift",
        "url": "/verify/taulib/docs/book-i-polarity-teichmueller-lift/"
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookI/Polarity/TeichmuellerLift.lean#L223-L230",
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

- Module: [TauLib.BookI.Polarity.TeichmuellerLift](/verify/taulib/docs/book-i-polarity-teichmueller-lift/)
- Source path: [`TauLib/BookI/Polarity/TeichmuellerLift.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookI/Polarity/TeichmuellerLift.lean#L223-L230)
- Source range: L223-L230
- Kind: `theorem`
- Formal status hint: `formalized`

## Registry Links

- No Registry IDs were detected in this declaration block.

## Immediate Comment / Docstring

```lean
/-- Teichmüller orthogonality (formal):
    teich_component r i d ≡ 0 (mod p_{j+1}) for j ≠ i, both < d. -/
```

## Source Excerpt

```lean
theorem teich_orthogonality_formal {r i j d : TauIdx}
    (hi : i < d) (hj : j < d) (hne : i ≠ j)
    (hyp : CRTHyp d) :
    teich_component r i d % nth_prime (j + 1) = 0 := by
  simp only [teich_component, show ¬(d ≤ i) from by simp only [TauIdx] at *; omega,
    ↓reduceIte]
  rw [crt_reconstruct_mod_prime _ hj hyp, teich_residues_getD_off hj (Ne.symm hne)]
  simp
```

---
{
  "projection_kind": "taulib_declaration",
  "title": "id_eq_chi_sum",
  "permalink": "/verify/taulib/docs/book-i-holomorphy-identity-theorem/id-eq-chi-sum/",
  "summary_short": "`theorem` declaration in `TauLib.BookI.Holomorphy.IdentityTheorem`.",
  "declaration_id": "TauLib.BookI.Holomorphy.IdentityTheorem::id_eq_chi_sum",
  "declaration_slug": "id-eq-chi-sum",
  "kind": "theorem",
  "name": "id_eq_chi_sum",
  "module_name": "TauLib.BookI.Holomorphy.IdentityTheorem",
  "module_url": "/verify/taulib/docs/book-i-holomorphy-identity-theorem/",
  "source_line_start": 224,
  "source_line_end": 226,
  "registry_ids": [],
  "related_registry_items": [],
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookI/Holomorphy/IdentityTheorem.lean#L224-L226",
  "formal_status": "formalized",
  "right_rail": {
    "related": [
      {
        "title": "TauLib.BookI.Holomorphy.IdentityTheorem",
        "url": "/verify/taulib/docs/book-i-holomorphy-identity-theorem/"
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookI/Holomorphy/IdentityTheorem.lean#L224-L226",
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

- Module: [TauLib.BookI.Holomorphy.IdentityTheorem](/verify/taulib/docs/book-i-holomorphy-identity-theorem/)
- Source path: [`TauLib/BookI/Holomorphy/IdentityTheorem.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookI/Holomorphy/IdentityTheorem.lean#L224-L226)
- Source range: L224-L226
- Kind: `theorem`
- Formal status hint: `formalized`

## Registry Links

- No Registry IDs were detected in this declaration block.

## Immediate Comment / Docstring

```lean
/-- Verification: the identity agrees with χ₊ + χ₋ in sector sums.
    id_stage gives (reduce n k, reduce n k) while
    chi_plus + chi_minus gives (reduce n k, 0) + (0, reduce n k) = (reduce n k, reduce n k). -/
```

## Source Excerpt

```lean
theorem id_eq_chi_sum (n k : TauIdx) :
    id_stage.b_fun n k = chi_plus_stage.b_fun n k + chi_minus_stage.b_fun n k := by
  simp [id_stage, chi_plus_stage, chi_minus_stage]
```

---
{
  "projection_kind": "taulib_declaration",
  "title": "e_minus_idem",
  "permalink": "/corpus/taulib/docs/book-i-polarity-bipolar-algebra/e-minus-idem/",
  "summary_short": "`theorem` declaration in `TauLib.BookI.Polarity.BipolarAlgebra`.",
  "declaration_id": "TauLib.BookI.Polarity.BipolarAlgebra::e_minus_idem",
  "declaration_slug": "e-minus-idem",
  "kind": "theorem",
  "name": "e_minus_idem",
  "module_name": "TauLib.BookI.Polarity.BipolarAlgebra",
  "module_url": "/corpus/taulib/docs/book-i-polarity-bipolar-algebra/",
  "source_line_start": 147,
  "source_line_end": 148,
  "registry_ids": [],
  "related_registry_items": [],
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookI/Polarity/BipolarAlgebra.lean#L147-L148",
  "formal_status": "formalized",
  "declaration_role": "proof obligation",
  "formal_status_label": "formal proof obligation checked",
  "right_rail": {
    "related": [
      {
        "title": "TauLib.BookI.Polarity.BipolarAlgebra",
        "url": "/corpus/taulib/docs/book-i-polarity-bipolar-algebra/"
      },
      {
        "title": "TauLib Projection Index",
        "url": "/corpus/taulib/docs/"
      },
      {
        "title": "Formalization Status",
        "url": "/verify/taulib/status/"
      }
    ],
    "artifacts": [
      {
        "title": "Source on GitHub",
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookI/Polarity/BipolarAlgebra.lean#L147-L148",
        "external": true
      }
    ],
    "meta": {
      "type": "TauLib Declaration",
      "kind": "theorem",
      "role": "proof obligation",
      "status": "formal proof obligation checked"
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

- Module: [TauLib.BookI.Polarity.BipolarAlgebra](/corpus/taulib/docs/book-i-polarity-bipolar-algebra/)
- Source path: [`TauLib/BookI/Polarity/BipolarAlgebra.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookI/Polarity/BipolarAlgebra.lean#L147-L148)
- Source range: L147-L148
- Kind: `theorem`
- Public role: `proof obligation`
- Formal status hint: `formal proof obligation checked`

## Registry Links

- No Registry IDs were detected in this declaration block.

## Immediate Comment / Docstring

```lean
/-- e-² = e- (idempotent). -/
```

## Source Excerpt

```lean
theorem e_minus_idem : SectorPair.mul e_minus_sector e_minus_sector = e_minus_sector := by
  simp [e_minus_sector, SectorPair.mul]
```

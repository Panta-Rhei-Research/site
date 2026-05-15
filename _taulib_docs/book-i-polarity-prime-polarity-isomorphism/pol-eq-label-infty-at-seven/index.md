---
{
  "projection_kind": "taulib_declaration",
  "title": "Pol_eq_labelInfty_at_seven",
  "permalink": "/corpus/taulib/docs/book-i-polarity-prime-polarity-isomorphism/pol-eq-label-infty-at-seven/",
  "summary_short": "`theorem` declaration in `TauLib.BookI.Polarity.PrimePolarityIsomorphism`.",
  "declaration_id": "TauLib.BookI.Polarity.PrimePolarityIsomorphism::Pol_eq_labelInfty_at_seven",
  "declaration_slug": "pol-eq-label-infty-at-seven",
  "kind": "theorem",
  "name": "Pol_eq_labelInfty_at_seven",
  "module_name": "TauLib.BookI.Polarity.PrimePolarityIsomorphism",
  "module_url": "/corpus/taulib/docs/book-i-polarity-prime-polarity-isomorphism/",
  "source_line_start": 168,
  "source_line_end": 171,
  "registry_ids": [],
  "related_registry_items": [],
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookI/Polarity/PrimePolarityIsomorphism.lean#L168-L171",
  "formal_status": "formalized",
  "declaration_role": "proof obligation",
  "formal_status_label": "formal proof obligation checked",
  "right_rail": {
    "related": [
      {
        "title": "TauLib.BookI.Polarity.PrimePolarityIsomorphism",
        "url": "/corpus/taulib/docs/book-i-polarity-prime-polarity-isomorphism/"
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookI/Polarity/PrimePolarityIsomorphism.lean#L168-L171",
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

- Module: [TauLib.BookI.Polarity.PrimePolarityIsomorphism](/corpus/taulib/docs/book-i-polarity-prime-polarity-isomorphism/)
- Source path: [`TauLib/BookI/Polarity/PrimePolarityIsomorphism.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookI/Polarity/PrimePolarityIsomorphism.lean#L168-L171)
- Source range: L168-L171
- Kind: `theorem`
- Public role: `proof obligation`
- Formal status hint: `formal proof obligation checked`

## Registry Links

- No Registry IDs were detected in this declaration block.

## Immediate Comment / Docstring

```lean
/-- Concrete isomorphism at p = 7 (the first B-class prime). -/
```

## Source Excerpt

```lean
theorem Pol_eq_labelInfty_at_seven :
    Pol 7 = labelInfty 3 := by
  unfold Pol labelInfty
  native_decide
```

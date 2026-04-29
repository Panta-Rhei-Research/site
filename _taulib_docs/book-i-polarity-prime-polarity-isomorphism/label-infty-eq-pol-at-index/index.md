---
{
  "projection_kind": "taulib_declaration",
  "title": "labelInfty_eq_Pol_at_index",
  "permalink": "/verify/taulib/docs/book-i-polarity-prime-polarity-isomorphism/label-infty-eq-pol-at-index/",
  "summary_short": "`theorem` declaration in `TauLib.BookI.Polarity.PrimePolarityIsomorphism`.",
  "declaration_id": "TauLib.BookI.Polarity.PrimePolarityIsomorphism::labelInfty_eq_Pol_at_index",
  "declaration_slug": "label-infty-eq-pol-at-index",
  "kind": "theorem",
  "name": "labelInfty_eq_Pol_at_index",
  "module_name": "TauLib.BookI.Polarity.PrimePolarityIsomorphism",
  "module_url": "/verify/taulib/docs/book-i-polarity-prime-polarity-isomorphism/",
  "source_line_start": 139,
  "source_line_end": 141,
  "registry_ids": [],
  "related_registry_items": [],
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookI/Polarity/PrimePolarityIsomorphism.lean#L139-L141",
  "formal_status": "formalized",
  "right_rail": {
    "related": [
      {
        "title": "TauLib.BookI.Polarity.PrimePolarityIsomorphism",
        "url": "/verify/taulib/docs/book-i-polarity-prime-polarity-isomorphism/"
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookI/Polarity/PrimePolarityIsomorphism.lean#L139-L141",
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

- Module: [TauLib.BookI.Polarity.PrimePolarityIsomorphism](/verify/taulib/docs/book-i-polarity-prime-polarity-isomorphism/)
- Source path: [`TauLib/BookI/Polarity/PrimePolarityIsomorphism.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookI/Polarity/PrimePolarityIsomorphism.lean#L139-L141)
- Source range: L139-L141
- Kind: `theorem`
- Formal status hint: `formalized`

## Registry Links

- No Registry IDs were detected in this declaration block.

## Immediate Comment / Docstring

```lean
/-- **Symmetric form**: `labelInfty i = Pol (nth_prime (i+1))`. -/
```

## Source Excerpt

```lean
theorem labelInfty_eq_Pol_at_index (i : TauIdx) :
    labelInfty i = Pol (nth_prime (i + 1)) :=
  (Pol_eq_labelInfty_at_index i).symm
```

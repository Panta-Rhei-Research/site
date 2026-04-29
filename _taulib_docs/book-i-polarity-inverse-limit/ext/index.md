---
{
  "projection_kind": "taulib_declaration",
  "title": "OmegaInverseLimit.ext",
  "permalink": "/verify/taulib/docs/book-i-polarity-inverse-limit/ext/",
  "summary_short": "`theorem` declaration in `TauLib.BookI.Polarity.InverseLimit`.",
  "declaration_id": "TauLib.BookI.Polarity.InverseLimit::OmegaInverseLimit.ext",
  "declaration_slug": "ext",
  "kind": "theorem",
  "name": "OmegaInverseLimit.ext",
  "module_name": "TauLib.BookI.Polarity.InverseLimit",
  "module_url": "/verify/taulib/docs/book-i-polarity-inverse-limit/",
  "source_line_start": 208,
  "source_line_end": 215,
  "registry_ids": [],
  "related_registry_items": [],
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookI/Polarity/InverseLimit.lean#L208-L215",
  "formal_status": "formalized",
  "right_rail": {
    "related": [
      {
        "title": "TauLib.BookI.Polarity.InverseLimit",
        "url": "/verify/taulib/docs/book-i-polarity-inverse-limit/"
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookI/Polarity/InverseLimit.lean#L208-L215",
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

- Module: [TauLib.BookI.Polarity.InverseLimit](/verify/taulib/docs/book-i-polarity-inverse-limit/)
- Source path: [`TauLib/BookI/Polarity/InverseLimit.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookI/Polarity/InverseLimit.lean#L208-L215)
- Source range: L208-L215
- Kind: `theorem`
- Formal status hint: `formalized`

## Registry Links

- No Registry IDs were detected in this declaration block.

## Immediate Comment / Docstring

```lean
/-- Two inverse-limit elements are equal iff their coefficient
    functions agree pointwise.  Standard extensionality at the
    structural level. -/
```

## Source Excerpt

```lean
theorem OmegaInverseLimit.ext (t₁ t₂ : OmegaInverseLimit)
    (h : ∀ k, t₁.coeff k = t₂.coeff k) :
    t₁ = t₂ := by
  cases t₁
  cases t₂
  congr 1
  funext k
  exact h k
```

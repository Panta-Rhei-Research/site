---
{
  "projection_kind": "taulib_declaration",
  "title": "idx_zero_add",
  "permalink": "/corpus/taulib/docs/book-i-denotation-arithmetic/idx-zero-add/",
  "summary_short": "`theorem` declaration in `TauLib.BookI.Denotation.Arithmetic`.",
  "declaration_id": "TauLib.BookI.Denotation.Arithmetic::idx_zero_add",
  "declaration_slug": "idx-zero-add",
  "kind": "theorem",
  "name": "idx_zero_add",
  "module_name": "TauLib.BookI.Denotation.Arithmetic",
  "module_url": "/corpus/taulib/docs/book-i-denotation-arithmetic/",
  "source_line_start": 162,
  "source_line_end": 163,
  "registry_ids": [],
  "related_registry_items": [],
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookI/Denotation/Arithmetic.lean#L162-L163",
  "formal_status": "formalized",
  "declaration_role": "proof obligation",
  "formal_status_label": "formal proof obligation checked",
  "right_rail": {
    "related": [
      {
        "title": "TauLib.BookI.Denotation.Arithmetic",
        "url": "/corpus/taulib/docs/book-i-denotation-arithmetic/"
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookI/Denotation/Arithmetic.lean#L162-L163",
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

- Module: [TauLib.BookI.Denotation.Arithmetic](/corpus/taulib/docs/book-i-denotation-arithmetic/)
- Source path: [`TauLib/BookI/Denotation/Arithmetic.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookI/Denotation/Arithmetic.lean#L162-L163)
- Source range: L162-L163
- Kind: `theorem`
- Public role: `proof obligation`
- Formal status hint: `formal proof obligation checked`

## Registry Links

- No Registry IDs were detected in this declaration block.

## Immediate Comment / Docstring

```lean
/-- Zero is a left identity for addition. -/
```

## Source Excerpt

```lean
theorem idx_zero_add (n : TauIdx) : idx_add 0 n = n := by
  simp [idx_add_eq_nat_add]
```

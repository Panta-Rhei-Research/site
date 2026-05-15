---
{
  "projection_kind": "taulib_declaration",
  "title": "sc_left_distrib",
  "permalink": "/corpus/taulib/docs/book-i-boundary-split-complex/sc-left-distrib/",
  "summary_short": "`theorem` declaration in `TauLib.BookI.Boundary.SplitComplex`.",
  "declaration_id": "TauLib.BookI.Boundary.SplitComplex::sc_left_distrib",
  "declaration_slug": "sc-left-distrib",
  "kind": "theorem",
  "name": "sc_left_distrib",
  "module_name": "TauLib.BookI.Boundary.SplitComplex",
  "module_url": "/corpus/taulib/docs/book-i-boundary-split-complex/",
  "source_line_start": 83,
  "source_line_end": 86,
  "registry_ids": [],
  "related_registry_items": [],
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookI/Boundary/SplitComplex.lean#L83-L86",
  "formal_status": "formalized",
  "declaration_role": "proof obligation",
  "formal_status_label": "formal proof obligation checked",
  "right_rail": {
    "related": [
      {
        "title": "TauLib.BookI.Boundary.SplitComplex",
        "url": "/corpus/taulib/docs/book-i-boundary-split-complex/"
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookI/Boundary/SplitComplex.lean#L83-L86",
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

- Module: [TauLib.BookI.Boundary.SplitComplex](/corpus/taulib/docs/book-i-boundary-split-complex/)
- Source path: [`TauLib/BookI/Boundary/SplitComplex.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookI/Boundary/SplitComplex.lean#L83-L86)
- Source range: L83-L86
- Kind: `theorem`
- Public role: `proof obligation`
- Formal status hint: `formal proof obligation checked`

## Registry Links

- No Registry IDs were detected in this declaration block.

## Immediate Comment / Docstring

```lean
/-- Left distributivity: a * (b + c) = a*b + a*c. -/
```

## Source Excerpt

```lean
theorem sc_left_distrib (a b c : SplitComplex) :
    SplitComplex.mul a (SplitComplex.add b c) =
    SplitComplex.add (SplitComplex.mul a b) (SplitComplex.mul a c) := by
  ext <;> simp [SplitComplex.mul, SplitComplex.add] <;> ring
```

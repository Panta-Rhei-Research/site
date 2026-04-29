---
{
  "projection_kind": "taulib_declaration",
  "title": "TauObj.ofGen",
  "permalink": "/verify/taulib/docs/book-i-kernel-axioms/of-gen/",
  "summary_short": "`def` declaration in `TauLib.BookI.Kernel.Axioms`.",
  "declaration_id": "TauLib.BookI.Kernel.Axioms::TauObj.ofGen",
  "declaration_slug": "of-gen",
  "kind": "def",
  "name": "TauObj.ofGen",
  "module_name": "TauLib.BookI.Kernel.Axioms",
  "module_url": "/verify/taulib/docs/book-i-kernel-axioms/",
  "source_line_start": 57,
  "source_line_end": 57,
  "registry_ids": [],
  "related_registry_items": [],
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookI/Kernel/Axioms.lean#L57-L57",
  "formal_status": "defined",
  "right_rail": {
    "related": [
      {
        "title": "TauLib.BookI.Kernel.Axioms",
        "url": "/verify/taulib/docs/book-i-kernel-axioms/"
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookI/Kernel/Axioms.lean#L57-L57",
        "external": true
      }
    ],
    "meta": {
      "type": "TauLib Declaration",
      "kind": "def",
      "status": "defined"
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

- Module: [TauLib.BookI.Kernel.Axioms](/verify/taulib/docs/book-i-kernel-axioms/)
- Source path: [`TauLib/BookI/Kernel/Axioms.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookI/Kernel/Axioms.lean#L57-L57)
- Source range: L57-L57
- Kind: `def`
- Formal status hint: `defined`

## Registry Links

- No Registry IDs were detected in this declaration block.

## Immediate Comment / Docstring

```lean
/-- Construct a TauObj from a generator (depth 0). -/
```

## Source Excerpt

```lean
def TauObj.ofGen (g : Generator) : TauObj := ⟨g, 0⟩
```

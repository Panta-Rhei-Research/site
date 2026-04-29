---
{
  "projection_kind": "taulib_declaration",
  "title": "nonOmegaGenerators",
  "permalink": "/verify/taulib/docs/book-i-kernel-signature/non-omega-generators/",
  "summary_short": "`def` declaration in `TauLib.BookI.Kernel.Signature`.",
  "declaration_id": "TauLib.BookI.Kernel.Signature::nonOmegaGenerators",
  "declaration_slug": "non-omega-generators",
  "kind": "def",
  "name": "nonOmegaGenerators",
  "module_name": "TauLib.BookI.Kernel.Signature",
  "module_url": "/verify/taulib/docs/book-i-kernel-signature/",
  "source_line_start": 94,
  "source_line_end": 94,
  "registry_ids": [
    "I.D01"
  ],
  "related_registry_items": [
    {
      "id": "I.D01",
      "title": "Five Generators",
      "url": "/registry/object/I.D01/"
    }
  ],
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookI/Kernel/Signature.lean#L94-L94",
  "formal_status": "defined",
  "right_rail": {
    "related": [
      {
        "title": "TauLib.BookI.Kernel.Signature",
        "url": "/verify/taulib/docs/book-i-kernel-signature/"
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookI/Kernel/Signature.lean#L94-L94",
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

- Module: [TauLib.BookI.Kernel.Signature](/verify/taulib/docs/book-i-kernel-signature/)
- Source path: [`TauLib/BookI/Kernel/Signature.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookI/Kernel/Signature.lean#L94-L94)
- Source range: L94-L94
- Kind: `def`
- Formal status hint: `defined`

## Registry Links

- `I.D01` — Five Generators

## Immediate Comment / Docstring

```lean
/-- [I.D01] The four non-omega generators that seed orbit rays. -/
```

## Source Excerpt

```lean
def nonOmegaGenerators : List Generator := [alpha, pi, gamma, eta]
```

---
{
  "projection_kind": "taulib_declaration",
  "title": "solenoidalGenerators",
  "permalink": "/verify/taulib/docs/book-i-kernel-diagonal/solenoidal-generators/",
  "summary_short": "`def` declaration in `TauLib.BookI.Kernel.Diagonal`.",
  "declaration_id": "TauLib.BookI.Kernel.Diagonal::solenoidalGenerators",
  "declaration_slug": "solenoidal-generators",
  "kind": "def",
  "name": "solenoidalGenerators",
  "module_name": "TauLib.BookI.Kernel.Diagonal",
  "module_url": "/verify/taulib/docs/book-i-kernel-diagonal/",
  "source_line_start": 52,
  "source_line_end": 52,
  "registry_ids": [],
  "related_registry_items": [],
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookI/Kernel/Diagonal.lean#L52-L52",
  "formal_status": "defined",
  "right_rail": {
    "related": [
      {
        "title": "TauLib.BookI.Kernel.Diagonal",
        "url": "/verify/taulib/docs/book-i-kernel-diagonal/"
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookI/Kernel/Diagonal.lean#L52-L52",
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

- Module: [TauLib.BookI.Kernel.Diagonal](/verify/taulib/docs/book-i-kernel-diagonal/)
- Source path: [`TauLib/BookI/Kernel/Diagonal.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookI/Kernel/Diagonal.lean#L52-L52)
- Source range: L52-L52
- Kind: `def`
- Formal status hint: `defined`

## Registry Links

- No Registry IDs were detected in this declaration block.

## Immediate Comment / Docstring

```lean
/-- The 3 solenoidal generators that serve as rewiring targets.
    α is the counting scaffold and is NOT a rewiring target. -/
```

## Source Excerpt

```lean
def solenoidalGenerators : List Generator := [pi, gamma, eta]
```

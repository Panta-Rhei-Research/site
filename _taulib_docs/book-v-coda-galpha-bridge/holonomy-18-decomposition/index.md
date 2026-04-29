---
{
  "projection_kind": "taulib_declaration",
  "title": "holonomy_18_decomposition",
  "permalink": "/verify/taulib/docs/book-v-coda-galpha-bridge/holonomy-18-decomposition/",
  "summary_short": "`theorem` declaration in `TauLib.BookV.Coda.GAlphaBridge`.",
  "declaration_id": "TauLib.BookV.Coda.GAlphaBridge::holonomy_18_decomposition",
  "declaration_slug": "holonomy-18-decomposition",
  "kind": "theorem",
  "name": "holonomy_18_decomposition",
  "module_name": "TauLib.BookV.Coda.GAlphaBridge",
  "module_url": "/verify/taulib/docs/book-v-coda-galpha-bridge/",
  "source_line_start": 88,
  "source_line_end": 89,
  "registry_ids": [],
  "related_registry_items": [],
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookV/Coda/GAlphaBridge.lean#L88-L89",
  "formal_status": "formalized",
  "right_rail": {
    "related": [
      {
        "title": "TauLib.BookV.Coda.GAlphaBridge",
        "url": "/verify/taulib/docs/book-v-coda-galpha-bridge/"
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookV/Coda/GAlphaBridge.lean#L88-L89",
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

- Module: [TauLib.BookV.Coda.GAlphaBridge](/verify/taulib/docs/book-v-coda-galpha-bridge/)
- Source path: [`TauLib/BookV/Coda/GAlphaBridge.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookV/Coda/GAlphaBridge.lean#L88-L89)
- Source range: L88-L89
- Kind: `theorem`
- Formal status hint: `formalized`

## Registry Links

- No Registry IDs were detected in this declaration block.

## Immediate Comment / Docstring

```lean
/-- Holonomy exponent 18 = 2 × 9 = 2 × 3². -/
```

## Source Excerpt

```lean
theorem holonomy_18_decomposition :
    18 = 2 * 9 ∧ (9 : Nat) = 3 * 3 := ⟨rfl, rfl⟩
```

---
{
  "projection_kind": "taulib_declaration",
  "title": "BHEvolutionMode.is_internal",
  "permalink": "/verify/taulib/docs/book-v-gravity-schwarzschild/is-internal/",
  "summary_short": "`def` declaration in `TauLib.BookV.Gravity.Schwarzschild`.",
  "declaration_id": "TauLib.BookV.Gravity.Schwarzschild::BHEvolutionMode.is_internal",
  "declaration_slug": "is-internal",
  "kind": "def",
  "name": "BHEvolutionMode.is_internal",
  "module_name": "TauLib.BookV.Gravity.Schwarzschild",
  "module_url": "/verify/taulib/docs/book-v-gravity-schwarzschild/",
  "source_line_start": 190,
  "source_line_end": 193,
  "registry_ids": [],
  "related_registry_items": [],
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookV/Gravity/Schwarzschild.lean#L190-L193",
  "formal_status": "defined",
  "right_rail": {
    "related": [
      {
        "title": "TauLib.BookV.Gravity.Schwarzschild",
        "url": "/verify/taulib/docs/book-v-gravity-schwarzschild/"
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookV/Gravity/Schwarzschild.lean#L190-L193",
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

- Module: [TauLib.BookV.Gravity.Schwarzschild](/verify/taulib/docs/book-v-gravity-schwarzschild/)
- Source path: [`TauLib/BookV/Gravity/Schwarzschild.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookV/Gravity/Schwarzschild.lean#L190-L193)
- Source range: L190-L193
- Kind: `def`
- Formal status hint: `defined`

## Registry Links

- No Registry IDs were detected in this declaration block.

## Immediate Comment / Docstring

```lean
/-- Whether an evolution mode is internal (vs. requires external input). -/
```

## Source Excerpt

```lean
def BHEvolutionMode.is_internal : BHEvolutionMode → Bool
  | .Ringdown  => true    -- internal normalization
  | .Transport => false   -- boundary-induced
  | .Fusion    => false   -- requires second BH
```

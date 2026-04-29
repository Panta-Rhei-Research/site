---
{
  "projection_kind": "taulib_declaration",
  "title": "blocking_targets",
  "permalink": "/verify/taulib/docs/book-i-meta-logic-ontic-invariance/blocking-targets/",
  "summary_short": "`def` declaration in `TauLib.BookI.MetaLogic.OnticInvariance`.",
  "declaration_id": "TauLib.BookI.MetaLogic.OnticInvariance::blocking_targets",
  "declaration_slug": "blocking-targets",
  "kind": "def",
  "name": "blocking_targets",
  "module_name": "TauLib.BookI.MetaLogic.OnticInvariance",
  "module_url": "/verify/taulib/docs/book-i-meta-logic-ontic-invariance/",
  "source_line_start": 37,
  "source_line_end": 40,
  "registry_ids": [],
  "related_registry_items": [],
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookI/MetaLogic/OnticInvariance.lean#L37-L40",
  "formal_status": "defined",
  "right_rail": {
    "related": [
      {
        "title": "TauLib.BookI.MetaLogic.OnticInvariance",
        "url": "/verify/taulib/docs/book-i-meta-logic-ontic-invariance/"
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookI/MetaLogic/OnticInvariance.lean#L37-L40",
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

- Module: [TauLib.BookI.MetaLogic.OnticInvariance](/verify/taulib/docs/book-i-meta-logic-ontic-invariance/)
- Source path: [`TauLib/BookI/MetaLogic/OnticInvariance.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookI/MetaLogic/OnticInvariance.lean#L37-L40)
- Source range: L37-L40
- Kind: `def`
- Formal status hint: `defined`

## Registry Links

- No Registry IDs were detected in this declaration block.

## Immediate Comment / Docstring

```lean
/-- Each blocking mechanism targets a specific resonance component. -/
```

## Source Excerpt

```lean
def blocking_targets : BlockingMechanism → ResonanceComponent
  | .k5_diagonal_discipline    => .L
  | .nf_confluence             => .E
  | .star_autonomous_structure => .P
```

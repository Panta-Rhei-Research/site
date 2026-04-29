---
{
  "projection_kind": "taulib_declaration",
  "title": "translation_failure_boundary_check",
  "permalink": "/verify/taulib/docs/book-iii-bridge-translation-obstruction/translation-failure-boundary-check/",
  "summary_short": "`def` declaration in `TauLib.BookIII.Bridge.TranslationObstruction`.",
  "declaration_id": "TauLib.BookIII.Bridge.TranslationObstruction::translation_failure_boundary_check",
  "declaration_slug": "translation-failure-boundary-check",
  "kind": "def",
  "name": "translation_failure_boundary_check",
  "module_name": "TauLib.BookIII.Bridge.TranslationObstruction",
  "module_url": "/verify/taulib/docs/book-iii-bridge-translation-obstruction/",
  "source_line_start": 187,
  "source_line_end": 193,
  "registry_ids": [
    "III.T61"
  ],
  "related_registry_items": [
    {
      "id": "III.T61",
      "title": "Translation Failure Boundary",
      "url": "/registry/object/III.T61/"
    }
  ],
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIII/Bridge/TranslationObstruction.lean#L187-L193",
  "formal_status": "defined",
  "right_rail": {
    "related": [
      {
        "title": "TauLib.BookIII.Bridge.TranslationObstruction",
        "url": "/verify/taulib/docs/book-iii-bridge-translation-obstruction/"
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIII/Bridge/TranslationObstruction.lean#L187-L193",
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

- Module: [TauLib.BookIII.Bridge.TranslationObstruction](/verify/taulib/docs/book-iii-bridge-translation-obstruction/)
- Source path: [`TauLib/BookIII/Bridge/TranslationObstruction.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIII/Bridge/TranslationObstruction.lean#L187-L193)
- Source range: L187-L193
- Kind: `def`
- Formal status hint: `defined`

## Registry Links

- `III.T61` — Translation Failure Boundary

## Immediate Comment / Docstring

```lean
/-- [III.T61] Full translation failure boundary. -/
```

## Source Excerpt

```lean
def translation_failure_boundary_check (bound db : Nat) : Bool :=
  safe_region_check bound db &&
  obstruction_check db &&
  -- Arithmetic: 3 of 5 moves obstruct
  arith_obstruction_count == 3 &&
  -- Topology: 4 of 5 moves obstruct (but 2 are mild)
  topo_obstruction_count == 4
```

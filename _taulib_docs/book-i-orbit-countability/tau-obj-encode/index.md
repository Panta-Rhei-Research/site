---
{
  "projection_kind": "taulib_declaration",
  "title": "tauObj_encode",
  "permalink": "/verify/taulib/docs/book-i-orbit-countability/tau-obj-encode/",
  "summary_short": "`def` declaration in `TauLib.BookI.Orbit.Countability`.",
  "declaration_id": "TauLib.BookI.Orbit.Countability::tauObj_encode",
  "declaration_slug": "tau-obj-encode",
  "kind": "def",
  "name": "tauObj_encode",
  "module_name": "TauLib.BookI.Orbit.Countability",
  "module_url": "/verify/taulib/docs/book-i-orbit-countability/",
  "source_line_start": 56,
  "source_line_end": 57,
  "registry_ids": [],
  "related_registry_items": [],
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookI/Orbit/Countability.lean#L56-L57",
  "formal_status": "defined",
  "right_rail": {
    "related": [
      {
        "title": "TauLib.BookI.Orbit.Countability",
        "url": "/verify/taulib/docs/book-i-orbit-countability/"
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookI/Orbit/Countability.lean#L56-L57",
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

- Module: [TauLib.BookI.Orbit.Countability](/verify/taulib/docs/book-i-orbit-countability/)
- Source path: [`TauLib/BookI/Orbit/Countability.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookI/Orbit/Countability.lean#L56-L57)
- Source range: L56-L57
- Kind: `def`
- Formal status hint: `defined`

## Registry Links

- No Registry IDs were detected in this declaration block.

## Immediate Comment / Docstring

```lean
/-- Encode a TauObj as a natural number: 5 * depth + seed_index.
    This gives a computable injection TauObj → Nat. -/
```

## Source Excerpt

```lean
def tauObj_encode (x : TauObj) : Nat :=
  5 * x.depth + x.seed.toNat
```

---
{
  "projection_kind": "taulib_declaration",
  "title": "bridge_necessary_insufficient",
  "permalink": "/verify/taulib/docs/book-iii-bridge-conjecture-gaps/bridge-necessary-insufficient/",
  "summary_short": "`theorem` declaration in `TauLib.BookIII.Bridge.ConjectureGaps`.",
  "declaration_id": "TauLib.BookIII.Bridge.ConjectureGaps::bridge_necessary_insufficient",
  "declaration_slug": "bridge-necessary-insufficient",
  "kind": "theorem",
  "name": "bridge_necessary_insufficient",
  "module_name": "TauLib.BookIII.Bridge.ConjectureGaps",
  "module_url": "/verify/taulib/docs/book-iii-bridge-conjecture-gaps/",
  "source_line_start": 217,
  "source_line_end": 218,
  "registry_ids": [
    "III.T80"
  ],
  "related_registry_items": [
    {
      "id": "III.T80",
      "title": "Bridge Necessary Insufficient",
      "url": "/registry/object/III.T80/"
    }
  ],
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIII/Bridge/ConjectureGaps.lean#L217-L218",
  "formal_status": "formalized",
  "right_rail": {
    "related": [
      {
        "title": "TauLib.BookIII.Bridge.ConjectureGaps",
        "url": "/verify/taulib/docs/book-iii-bridge-conjecture-gaps/"
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIII/Bridge/ConjectureGaps.lean#L217-L218",
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

- Module: [TauLib.BookIII.Bridge.ConjectureGaps](/verify/taulib/docs/book-iii-bridge-conjecture-gaps/)
- Source path: [`TauLib/BookIII/Bridge/ConjectureGaps.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIII/Bridge/ConjectureGaps.lean#L217-L218)
- Source range: L217-L218
- Kind: `theorem`
- Formal status hint: `formalized`

## Registry Links

- `III.T80` — Bridge Necessary Insufficient

## Immediate Comment / Docstring

```lean
/-- [III.T80] Bridge is necessary but insufficient for full conjectures. -/
```

## Source Excerpt

```lean
theorem bridge_necessary_insufficient :
    bridge_necessary_check = true := by native_decide
```

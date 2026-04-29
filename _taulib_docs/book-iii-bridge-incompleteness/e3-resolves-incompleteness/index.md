---
{
  "projection_kind": "taulib_declaration",
  "title": "e3_resolves_incompleteness",
  "permalink": "/verify/taulib/docs/book-iii-bridge-incompleteness/e3-resolves-incompleteness/",
  "summary_short": "`theorem` declaration in `TauLib.BookIII.Bridge.Incompleteness`.",
  "declaration_id": "TauLib.BookIII.Bridge.Incompleteness::e3_resolves_incompleteness",
  "declaration_slug": "e3-resolves-incompleteness",
  "kind": "theorem",
  "name": "e3_resolves_incompleteness",
  "module_name": "TauLib.BookIII.Bridge.Incompleteness",
  "module_url": "/verify/taulib/docs/book-iii-bridge-incompleteness/",
  "source_line_start": 284,
  "source_line_end": 287,
  "registry_ids": [
    "III.T44"
  ],
  "related_registry_items": [
    {
      "id": "III.T44",
      "title": "Incompleteness as VM Boundary",
      "url": "/registry/object/III.T44/"
    }
  ],
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIII/Bridge/Incompleteness.lean#L284-L287",
  "formal_status": "formalized",
  "right_rail": {
    "related": [
      {
        "title": "TauLib.BookIII.Bridge.Incompleteness",
        "url": "/verify/taulib/docs/book-iii-bridge-incompleteness/"
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIII/Bridge/Incompleteness.lean#L284-L287",
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

- Module: [TauLib.BookIII.Bridge.Incompleteness](/verify/taulib/docs/book-iii-bridge-incompleteness/)
- Source path: [`TauLib/BookIII/Bridge/Incompleteness.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIII/Bridge/Incompleteness.lean#L284-L287)
- Source range: L284-L287
- Kind: `theorem`
- Formal status hint: `formalized`

## Registry Links

- `III.T44` — Incompleteness as VM Boundary

## Immediate Comment / Docstring

```lean
/-- [III.T44] Structural: E3 is the resolution level for incompleteness. -/
```

## Source Excerpt

```lean
theorem e3_resolves_incompleteness :
    EnrLevel.E3.toNat = 3 := rfl

end Tau.BookIII.Bridge
```

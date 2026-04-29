---
{
  "projection_kind": "taulib_declaration",
  "title": "fusion_increases_mass",
  "permalink": "/verify/taulib/docs/book-v-gravity-schwarzschild/fusion-increases-mass/",
  "summary_short": "`theorem` declaration in `TauLib.BookV.Gravity.Schwarzschild`.",
  "declaration_id": "TauLib.BookV.Gravity.Schwarzschild::fusion_increases_mass",
  "declaration_slug": "fusion-increases-mass",
  "kind": "theorem",
  "name": "fusion_increases_mass",
  "module_name": "TauLib.BookV.Gravity.Schwarzschild",
  "module_url": "/verify/taulib/docs/book-v-gravity-schwarzschild/",
  "source_line_start": 229,
  "source_line_end": 230,
  "registry_ids": [],
  "related_registry_items": [],
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookV/Gravity/Schwarzschild.lean#L229-L230",
  "formal_status": "formalized",
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookV/Gravity/Schwarzschild.lean#L229-L230",
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

- Module: [TauLib.BookV.Gravity.Schwarzschild](/verify/taulib/docs/book-v-gravity-schwarzschild/)
- Source path: [`TauLib/BookV/Gravity/Schwarzschild.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookV/Gravity/Schwarzschild.lean#L229-L230)
- Source range: L229-L230
- Kind: `theorem`
- Formal status hint: `formalized`

## Registry Links

- No Registry IDs were detected in this declaration block.

## Immediate Comment / Docstring

```lean
/-- Fusion increases mass (does not preserve). -/
```

## Source Excerpt

```lean
theorem fusion_increases_mass :
    BHEvolutionMode.Fusion.preserves_mass = false := by rfl
```

---
{
  "projection_kind": "taulib_declaration",
  "title": "alfven_damping",
  "permalink": "/corpus/taulib/docs/book-v-fluid-macro-tau-alfven/alfven-damping-l211/",
  "summary_short": "`theorem` declaration in `TauLib.BookV.FluidMacro.TauAlfven`.",
  "declaration_id": "TauLib.BookV.FluidMacro.TauAlfven::alfven_damping",
  "declaration_slug": "alfven-damping-l211",
  "kind": "theorem",
  "name": "alfven_damping",
  "module_name": "TauLib.BookV.FluidMacro.TauAlfven",
  "module_url": "/corpus/taulib/docs/book-v-fluid-macro-tau-alfven/",
  "source_line_start": 211,
  "source_line_end": 212,
  "registry_ids": [],
  "related_registry_items": [],
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookV/FluidMacro/TauAlfven.lean#L211-L212",
  "formal_status": "formalized",
  "declaration_role": "proof obligation",
  "formal_status_label": "formal proof obligation checked",
  "right_rail": {
    "related": [
      {
        "title": "TauLib.BookV.FluidMacro.TauAlfven",
        "url": "/corpus/taulib/docs/book-v-fluid-macro-tau-alfven/"
      },
      {
        "title": "TauLib Projection Index",
        "url": "/corpus/taulib/docs/"
      },
      {
        "title": "Formalization Status",
        "url": "/verify/taulib/status/"
      }
    ],
    "artifacts": [
      {
        "title": "Source on GitHub",
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookV/FluidMacro/TauAlfven.lean#L211-L212",
        "external": true
      }
    ],
    "meta": {
      "type": "TauLib Declaration",
      "kind": "theorem",
      "role": "proof obligation",
      "status": "formal proof obligation checked"
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

- Module: [TauLib.BookV.FluidMacro.TauAlfven](/corpus/taulib/docs/book-v-fluid-macro-tau-alfven/)
- Source path: [`TauLib/BookV/FluidMacro/TauAlfven.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookV/FluidMacro/TauAlfven.lean#L211-L212)
- Source range: L211-L212
- Kind: `theorem`
- Public role: `proof obligation`
- Formal status hint: `formal proof obligation checked`

## Registry Links

- No Registry IDs were detected in this declaration block.

## Immediate Comment / Docstring

```lean
/-- Damping is always bounded. -/
```

## Source Excerpt

```lean
theorem alfven_damping (d : AlfvenDamping) :
    d.rate ≤ d.max_rate := d.rate_bounded
```

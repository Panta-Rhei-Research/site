---
{
  "projection_kind": "taulib_declaration",
  "title": "chi_plus_admissible",
  "permalink": "/verify/taulib/docs/book-iii-spectrum-interface-width/chi-plus-admissible/",
  "summary_short": "`theorem` declaration in `TauLib.BookIII.Spectrum.InterfaceWidth`.",
  "declaration_id": "TauLib.BookIII.Spectrum.InterfaceWidth::chi_plus_admissible",
  "declaration_slug": "chi-plus-admissible",
  "kind": "theorem",
  "name": "chi_plus_admissible",
  "module_name": "TauLib.BookIII.Spectrum.InterfaceWidth",
  "module_url": "/verify/taulib/docs/book-iii-spectrum-interface-width/",
  "source_line_start": 107,
  "source_line_end": 108,
  "registry_ids": [
    "I.P30"
  ],
  "related_registry_items": [],
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIII/Spectrum/InterfaceWidth.lean#L107-L108",
  "formal_status": "formalized",
  "right_rail": {
    "related": [
      {
        "title": "TauLib.BookIII.Spectrum.InterfaceWidth",
        "url": "/verify/taulib/docs/book-iii-spectrum-interface-width/"
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIII/Spectrum/InterfaceWidth.lean#L107-L108",
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

- Module: [TauLib.BookIII.Spectrum.InterfaceWidth](/verify/taulib/docs/book-iii-spectrum-interface-width/)
- Source path: [`TauLib/BookIII/Spectrum/InterfaceWidth.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIII/Spectrum/InterfaceWidth.lean#L107-L108)
- Source range: L107-L108
- Kind: `theorem`
- Formal status hint: `formalized`

## Registry Links

- No Registry IDs were detected in this declaration block.

## Immediate Comment / Docstring

```lean
/-- [I.P30] χ₊ is τ-admissible: at any depth D, it stabilizes
    because χ₊ is tower-coherent. -/
```

## Source Excerpt

```lean
theorem chi_plus_admissible : TauAdmissible chi_plus_stage :=
  coherent_admissible chi_plus_stage chi_plus_coherent
```

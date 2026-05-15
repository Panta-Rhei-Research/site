---
{
  "projection_kind": "taulib_declaration",
  "title": "width_principle_c",
  "permalink": "/corpus/taulib/docs/book-iii-spectrum-interface-width/width-principle-c/",
  "summary_short": "`theorem` declaration in `TauLib.BookIII.Spectrum.InterfaceWidth`.",
  "declaration_id": "TauLib.BookIII.Spectrum.InterfaceWidth::width_principle_c",
  "declaration_slug": "width-principle-c",
  "kind": "theorem",
  "name": "width_principle_c",
  "module_name": "TauLib.BookIII.Spectrum.InterfaceWidth",
  "module_url": "/corpus/taulib/docs/book-iii-spectrum-interface-width/",
  "source_line_start": 92,
  "source_line_end": 94,
  "registry_ids": [],
  "related_registry_items": [],
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIII/Spectrum/InterfaceWidth.lean#L92-L94",
  "formal_status": "formalized",
  "declaration_role": "proof obligation",
  "formal_status_label": "formal proof obligation checked",
  "right_rail": {
    "related": [
      {
        "title": "TauLib.BookIII.Spectrum.InterfaceWidth",
        "url": "/corpus/taulib/docs/book-iii-spectrum-interface-width/"
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIII/Spectrum/InterfaceWidth.lean#L92-L94",
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

- Module: [TauLib.BookIII.Spectrum.InterfaceWidth](/corpus/taulib/docs/book-iii-spectrum-interface-width/)
- Source path: [`TauLib/BookIII/Spectrum/InterfaceWidth.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIII/Spectrum/InterfaceWidth.lean#L92-L94)
- Source range: L92-L94
- Kind: `theorem`
- Public role: `proof obligation`
- Formal status hint: `formal proof obligation checked`

## Registry Links

- No Registry IDs were detected in this declaration block.

## Immediate Comment / Docstring

```lean
/-- Width principle for C-sector. -/
```

## Source Excerpt

```lean
theorem width_principle_c (f : StageFun) (hcoh : TowerCoherent f)
    (D : TauIdx) : ∀ n k, k ≤ D → reduce (f.c_fun n D) k = f.c_fun n k :=
  fun n k hk => hcoh.2 n k D hk
```

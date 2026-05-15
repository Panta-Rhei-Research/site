---
{
  "projection_kind": "taulib_declaration",
  "title": "five_field_modes",
  "permalink": "/corpus/taulib/docs/book-v-gravity-field-tau-schwarzschild/five-field-modes/",
  "summary_short": "`theorem` declaration in `TauLib.BookV.GravityField.TauSchwarzschild`.",
  "declaration_id": "TauLib.BookV.GravityField.TauSchwarzschild::five_field_modes",
  "declaration_slug": "five-field-modes",
  "kind": "theorem",
  "name": "five_field_modes",
  "module_name": "TauLib.BookV.GravityField.TauSchwarzschild",
  "module_url": "/corpus/taulib/docs/book-v-gravity-field-tau-schwarzschild/",
  "source_line_start": 170,
  "source_line_end": 175,
  "registry_ids": [],
  "related_registry_items": [],
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookV/GravityField/TauSchwarzschild.lean#L170-L175",
  "formal_status": "formalized",
  "declaration_role": "proof obligation",
  "formal_status_label": "formal proof obligation checked",
  "right_rail": {
    "related": [
      {
        "title": "TauLib.BookV.GravityField.TauSchwarzschild",
        "url": "/corpus/taulib/docs/book-v-gravity-field-tau-schwarzschild/"
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookV/GravityField/TauSchwarzschild.lean#L170-L175",
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

- Module: [TauLib.BookV.GravityField.TauSchwarzschild](/corpus/taulib/docs/book-v-gravity-field-tau-schwarzschild/)
- Source path: [`TauLib/BookV/GravityField/TauSchwarzschild.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookV/GravityField/TauSchwarzschild.lean#L170-L175)
- Source range: L170-L175
- Kind: `theorem`
- Public role: `proof obligation`
- Formal status hint: `formal proof obligation checked`

## Registry Links

- No Registry IDs were detected in this declaration block.

## Immediate Comment / Docstring

```lean
/-- Exactly 5 total field evolution modes (2 pre-maturity + 3 mature). -/
```

## Source Excerpt

```lean
theorem five_field_modes :
    [FieldEvolutionMode.GeometricRelax,
     FieldEvolutionMode.TopologicalRelax,
     FieldEvolutionMode.MatureEvolution .Ringdown,
     FieldEvolutionMode.MatureEvolution .Transport,
     FieldEvolutionMode.MatureEvolution .Fusion].length = 5 := by rfl
```

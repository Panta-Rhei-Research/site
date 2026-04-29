---
{
  "projection_kind": "taulib_declaration",
  "title": "code_is_data",
  "permalink": "/verify/taulib/docs/book-iii-computation-tower-machine/code-is-data/",
  "summary_short": "`theorem` declaration in `TauLib.BookIII.Computation.TowerMachine`.",
  "declaration_id": "TauLib.BookIII.Computation.TowerMachine::code_is_data",
  "declaration_slug": "code-is-data",
  "kind": "theorem",
  "name": "code_is_data",
  "module_name": "TauLib.BookIII.Computation.TowerMachine",
  "module_url": "/verify/taulib/docs/book-iii-computation-tower-machine/",
  "source_line_start": 205,
  "source_line_end": 206,
  "registry_ids": [
    "III.T30"
  ],
  "related_registry_items": [
    {
      "id": "III.T30",
      "title": "TTM τ-Nativity",
      "url": "/registry/object/III.T30/"
    }
  ],
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIII/Computation/TowerMachine.lean#L205-L206",
  "formal_status": "formalized",
  "right_rail": {
    "related": [
      {
        "title": "TauLib.BookIII.Computation.TowerMachine",
        "url": "/verify/taulib/docs/book-iii-computation-tower-machine/"
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIII/Computation/TowerMachine.lean#L205-L206",
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

- Module: [TauLib.BookIII.Computation.TowerMachine](/verify/taulib/docs/book-iii-computation-tower-machine/)
- Source path: [`TauLib/BookIII/Computation/TowerMachine.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIII/Computation/TowerMachine.lean#L205-L206)
- Source range: L205-L206
- Kind: `theorem`
- Formal status hint: `formalized`

## Registry Links

- `III.T30` — TTM τ-Nativity

## Immediate Comment / Docstring

```lean
/-- [III.T30] Structural: code=data (self-application). -/
```

## Source Excerpt

```lean
theorem code_is_data :
    (ttm_step ⟨0, 7, 7, 3⟩).reg_a = (7 + 7) % 30 := by native_decide
```

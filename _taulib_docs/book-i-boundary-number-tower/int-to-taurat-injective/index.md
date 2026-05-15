---
{
  "projection_kind": "taulib_declaration",
  "title": "int_to_taurat_injective",
  "permalink": "/corpus/taulib/docs/book-i-boundary-number-tower/int-to-taurat-injective/",
  "summary_short": "`theorem` declaration in `TauLib.BookI.Boundary.NumberTower`.",
  "declaration_id": "TauLib.BookI.Boundary.NumberTower::int_to_taurat_injective",
  "declaration_slug": "int-to-taurat-injective",
  "kind": "theorem",
  "name": "int_to_taurat_injective",
  "module_name": "TauLib.BookI.Boundary.NumberTower",
  "module_url": "/corpus/taulib/docs/book-i-boundary-number-tower/",
  "source_line_start": 381,
  "source_line_end": 384,
  "registry_ids": [],
  "related_registry_items": [],
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookI/Boundary/NumberTower.lean#L381-L384",
  "formal_status": "formalized",
  "declaration_role": "proof obligation",
  "formal_status_label": "formal proof obligation checked",
  "right_rail": {
    "related": [
      {
        "title": "TauLib.BookI.Boundary.NumberTower",
        "url": "/corpus/taulib/docs/book-i-boundary-number-tower/"
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookI/Boundary/NumberTower.lean#L381-L384",
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

- Module: [TauLib.BookI.Boundary.NumberTower](/corpus/taulib/docs/book-i-boundary-number-tower/)
- Source path: [`TauLib/BookI/Boundary/NumberTower.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookI/Boundary/NumberTower.lean#L381-L384)
- Source range: L381-L384
- Kind: `theorem`
- Public role: `proof obligation`
- Formal status hint: `formal proof obligation checked`

## Registry Links

- No Registry IDs were detected in this declaration block.

## Immediate Comment / Docstring

```lean
/-- The embedding is injective (on TauInt structures). -/
```

## Source Excerpt

```lean
theorem int_to_taurat_injective {a b : TauInt}
    (h : int_to_taurat a = int_to_taurat b) : a = b := by
  simp only [int_to_taurat, TauRat.mk.injEq] at h
  exact h.1
```

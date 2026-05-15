---
{
  "projection_kind": "taulib_declaration",
  "title": "ee_monotone_convergence",
  "permalink": "/corpus/taulib/docs/book-vi-persistence-temporal-lemniscate/ee-monotone-convergence-l222/",
  "summary_short": "`theorem` declaration in `TauLib.BookVI.Persistence.TemporalLemniscate`.",
  "declaration_id": "TauLib.BookVI.Persistence.TemporalLemniscate::ee_monotone_convergence",
  "declaration_slug": "ee-monotone-convergence-l222",
  "kind": "theorem",
  "name": "ee_monotone_convergence",
  "module_name": "TauLib.BookVI.Persistence.TemporalLemniscate",
  "module_url": "/corpus/taulib/docs/book-vi-persistence-temporal-lemniscate/",
  "source_line_start": 222,
  "source_line_end": 227,
  "registry_ids": [],
  "related_registry_items": [],
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookVI/Persistence/TemporalLemniscate.lean#L222-L227",
  "formal_status": "formalized",
  "declaration_role": "proof obligation",
  "formal_status_label": "formal proof obligation checked",
  "right_rail": {
    "related": [
      {
        "title": "TauLib.BookVI.Persistence.TemporalLemniscate",
        "url": "/corpus/taulib/docs/book-vi-persistence-temporal-lemniscate/"
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookVI/Persistence/TemporalLemniscate.lean#L222-L227",
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

- Module: [TauLib.BookVI.Persistence.TemporalLemniscate](/corpus/taulib/docs/book-vi-persistence-temporal-lemniscate/)
- Source path: [`TauLib/BookVI/Persistence/TemporalLemniscate.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookVI/Persistence/TemporalLemniscate.lean#L222-L227)
- Source range: L222-L227
- Kind: `theorem`
- Public role: `proof obligation`
- Formal status hint: `formal proof obligation checked`

## Registry Links

- No Registry IDs were detected in this declaration block.

## Immediate Comment / Docstring

```lean
No immediate Lean doc/comment block was detected for this declaration.
```

## Source Excerpt

```lean
theorem ee_monotone_convergence :
    ee_convergence.monotone_increasing = true ∧
    ee_convergence.limit_is_one = true ∧
    ee_convergence.hodge_stabilization = true ∧
    ee_convergence.poincare_lockin = true :=
  ⟨rfl, rfl, rfl, rfl⟩
```

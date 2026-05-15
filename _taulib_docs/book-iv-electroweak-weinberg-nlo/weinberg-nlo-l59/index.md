---
{
  "projection_kind": "taulib_declaration",
  "title": "weinbergNLO",
  "permalink": "/corpus/taulib/docs/book-iv-electroweak-weinberg-nlo/weinberg-nlo-l59/",
  "summary_short": "`def` declaration in `TauLib.BookIV.Electroweak.WeinbergNLO`.",
  "declaration_id": "TauLib.BookIV.Electroweak.WeinbergNLO::weinbergNLO",
  "declaration_slug": "weinberg-nlo-l59",
  "kind": "def",
  "name": "weinbergNLO",
  "module_name": "TauLib.BookIV.Electroweak.WeinbergNLO",
  "module_url": "/corpus/taulib/docs/book-iv-electroweak-weinberg-nlo/",
  "source_line_start": 59,
  "source_line_end": 60,
  "registry_ids": [],
  "related_registry_items": [],
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIV/Electroweak/WeinbergNLO.lean#L59-L60",
  "formal_status": "defined",
  "declaration_role": "definition",
  "formal_status_label": "definition",
  "right_rail": {
    "related": [
      {
        "title": "TauLib.BookIV.Electroweak.WeinbergNLO",
        "url": "/corpus/taulib/docs/book-iv-electroweak-weinberg-nlo/"
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIV/Electroweak/WeinbergNLO.lean#L59-L60",
        "external": true
      }
    ],
    "meta": {
      "type": "TauLib Declaration",
      "kind": "def",
      "role": "definition",
      "status": "definition"
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

- Module: [TauLib.BookIV.Electroweak.WeinbergNLO](/corpus/taulib/docs/book-iv-electroweak-weinberg-nlo/)
- Source path: [`TauLib/BookIV/Electroweak/WeinbergNLO.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIV/Electroweak/WeinbergNLO.lean#L59-L60)
- Source range: L59-L60
- Kind: `def`
- Public role: `definition`
- Formal status hint: `definition`

## Registry Links

- No Registry IDs were detected in this declaration block.

## Immediate Comment / Docstring

```lean
/-- The canonical NLO correction instance: 5/7 · ι³. -/
```

## Source Excerpt

```lean
def weinbergNLO : WeinbergNLO :=
  ⟨5, 7, 3, by native_decide, by native_decide, by native_decide⟩
```

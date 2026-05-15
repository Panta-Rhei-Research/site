---
{
  "projection_kind": "taulib_declaration",
  "title": "teich_lift",
  "permalink": "/corpus/taulib/docs/book-i-polarity-teichmueller-lift/teich-lift/",
  "summary_short": "`def` declaration in `TauLib.BookI.Polarity.TeichmuellerLift`.",
  "declaration_id": "TauLib.BookI.Polarity.TeichmuellerLift::teich_lift",
  "declaration_slug": "teich-lift",
  "kind": "def",
  "name": "teich_lift",
  "module_name": "TauLib.BookI.Polarity.TeichmuellerLift",
  "module_url": "/corpus/taulib/docs/book-i-polarity-teichmueller-lift/",
  "source_line_start": 72,
  "source_line_end": 73,
  "registry_ids": [],
  "related_registry_items": [],
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookI/Polarity/TeichmuellerLift.lean#L72-L73",
  "formal_status": "defined",
  "declaration_role": "definition",
  "formal_status_label": "definition",
  "right_rail": {
    "related": [
      {
        "title": "TauLib.BookI.Polarity.TeichmuellerLift",
        "url": "/corpus/taulib/docs/book-i-polarity-teichmueller-lift/"
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookI/Polarity/TeichmuellerLift.lean#L72-L73",
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

- Module: [TauLib.BookI.Polarity.TeichmuellerLift](/corpus/taulib/docs/book-i-polarity-teichmueller-lift/)
- Source path: [`TauLib/BookI/Polarity/TeichmuellerLift.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookI/Polarity/TeichmuellerLift.lean#L72-L73)
- Source range: L72-L73
- Kind: `def`
- Public role: `definition`
- Formal status hint: `definition`

## Registry Links

- No Registry IDs were detected in this declaration block.

## Immediate Comment / Docstring

```lean
/-- The Teichmüller omega-tail: canonical lift of residue r at prime p_{i+1}.
    i is 0-indexed (i=0 → prime p_1=2). -/
```

## Source Excerpt

```lean
def teich_lift (r i d : TauIdx) : OmegaTail :=
  ⟨d, teich_list r i d, teich_list_length r i d⟩
```

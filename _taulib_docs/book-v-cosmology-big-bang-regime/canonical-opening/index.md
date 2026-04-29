---
{
  "projection_kind": "taulib_declaration",
  "title": "canonical_opening",
  "permalink": "/verify/taulib/docs/book-v-cosmology-big-bang-regime/canonical-opening/",
  "summary_short": "`def` declaration in `TauLib.BookV.Cosmology.BigBangRegime`.",
  "declaration_id": "TauLib.BookV.Cosmology.BigBangRegime::canonical_opening",
  "declaration_slug": "canonical-opening",
  "kind": "def",
  "name": "canonical_opening",
  "module_name": "TauLib.BookV.Cosmology.BigBangRegime",
  "module_url": "/verify/taulib/docs/book-v-cosmology-big-bang-regime/",
  "source_line_start": 80,
  "source_line_end": 82,
  "registry_ids": [],
  "related_registry_items": [],
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookV/Cosmology/BigBangRegime.lean#L80-L82",
  "formal_status": "defined",
  "right_rail": {
    "related": [
      {
        "title": "TauLib.BookV.Cosmology.BigBangRegime",
        "url": "/verify/taulib/docs/book-v-cosmology-big-bang-regime/"
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookV/Cosmology/BigBangRegime.lean#L80-L82",
        "external": true
      }
    ],
    "meta": {
      "type": "TauLib Declaration",
      "kind": "def",
      "status": "defined"
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

- Module: [TauLib.BookV.Cosmology.BigBangRegime](/verify/taulib/docs/book-v-cosmology-big-bang-regime/)
- Source path: [`TauLib/BookV/Cosmology/BigBangRegime.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookV/Cosmology/BigBangRegime.lean#L80-L82)
- Source range: L80-L82
- Kind: `def`
- Formal status hint: `defined`

## Registry Links

- No Registry IDs were detected in this declaration block.

## Immediate Comment / Docstring

```lean
/-- The canonical temporal opening. -/
```

## Source Excerpt

```lean
def canonical_opening : TemporalOpening where
  first_tick := 1
  first_tick_is_one := by rfl
```

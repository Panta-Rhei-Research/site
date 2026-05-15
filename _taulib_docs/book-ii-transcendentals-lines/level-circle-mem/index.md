---
{
  "projection_kind": "taulib_declaration",
  "title": "level_circle_mem",
  "permalink": "/corpus/taulib/docs/book-ii-transcendentals-lines/level-circle-mem/",
  "summary_short": "`def` declaration in `TauLib.BookII.Transcendentals.Lines`.",
  "declaration_id": "TauLib.BookII.Transcendentals.Lines::level_circle_mem",
  "declaration_slug": "level-circle-mem",
  "kind": "def",
  "name": "level_circle_mem",
  "module_name": "TauLib.BookII.Transcendentals.Lines",
  "module_url": "/corpus/taulib/docs/book-ii-transcendentals-lines/",
  "source_line_start": 56,
  "source_line_end": 57,
  "registry_ids": [
    "II.D25"
  ],
  "related_registry_items": [
    {
      "id": "II.D25",
      "title": "Level Circle",
      "url": "/registry/object/II.D25/"
    }
  ],
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookII/Transcendentals/Lines.lean#L56-L57",
  "formal_status": "defined",
  "declaration_role": "data/computed value",
  "formal_status_label": "data/computed value",
  "right_rail": {
    "related": [
      {
        "title": "TauLib.BookII.Transcendentals.Lines",
        "url": "/corpus/taulib/docs/book-ii-transcendentals-lines/"
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookII/Transcendentals/Lines.lean#L56-L57",
        "external": true
      }
    ],
    "meta": {
      "type": "TauLib Declaration",
      "kind": "def",
      "role": "data/computed value",
      "status": "data/computed value"
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

- Module: [TauLib.BookII.Transcendentals.Lines](/corpus/taulib/docs/book-ii-transcendentals-lines/)
- Source path: [`TauLib/BookII/Transcendentals/Lines.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookII/Transcendentals/Lines.lean#L56-L57)
- Source range: L56-L57
- Kind: `def`
- Public role: `data/computed value`
- Formal status hint: `data/computed value`

## Registry Links

- `II.D25` — Level Circle

## Immediate Comment / Docstring

```lean
/-- [II.D25] Level circle at stage k: two points share the same
    D-residue mod primorial(k). -/
```

## Source Excerpt

```lean
def level_circle_mem (x y k : TauIdx) : Bool :=
  (from_tau_idx x).d % primorial k == (from_tau_idx y).d % primorial k
```

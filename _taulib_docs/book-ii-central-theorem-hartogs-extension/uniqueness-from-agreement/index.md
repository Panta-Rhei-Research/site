---
{
  "projection_kind": "taulib_declaration",
  "title": "uniqueness_from_agreement",
  "permalink": "/verify/taulib/docs/book-ii-central-theorem-hartogs-extension/uniqueness-from-agreement/",
  "summary_short": "`theorem` declaration in `TauLib.BookII.CentralTheorem.HartogsExtension`.",
  "declaration_id": "TauLib.BookII.CentralTheorem.HartogsExtension::uniqueness_from_agreement",
  "declaration_slug": "uniqueness-from-agreement",
  "kind": "theorem",
  "name": "uniqueness_from_agreement",
  "module_name": "TauLib.BookII.CentralTheorem.HartogsExtension",
  "module_url": "/verify/taulib/docs/book-ii-central-theorem-hartogs-extension/",
  "source_line_start": 274,
  "source_line_end": 277,
  "registry_ids": [
    "II.T37"
  ],
  "related_registry_items": [
    {
      "id": "II.T37",
      "title": "Hartogs Extension Uniqueness",
      "url": "/registry/object/II.T37/"
    }
  ],
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookII/CentralTheorem/HartogsExtension.lean#L274-L277",
  "formal_status": "formalized",
  "right_rail": {
    "related": [
      {
        "title": "TauLib.BookII.CentralTheorem.HartogsExtension",
        "url": "/verify/taulib/docs/book-ii-central-theorem-hartogs-extension/"
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookII/CentralTheorem/HartogsExtension.lean#L274-L277",
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

- Module: [TauLib.BookII.CentralTheorem.HartogsExtension](/verify/taulib/docs/book-ii-central-theorem-hartogs-extension/)
- Source path: [`TauLib/BookII/CentralTheorem/HartogsExtension.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookII/CentralTheorem/HartogsExtension.lean#L274-L277)
- Source range: L274-L277
- Kind: `theorem`
- Formal status hint: `formalized`

## Registry Links

- `II.T37` — Hartogs Extension Uniqueness

## Immediate Comment / Docstring

```lean
/-- [II.T37] Uniqueness structural core: two extensions that agree on all
    stages must agree on the bndlift extension.
    If reduce(x, k) = reduce(y, k), then bndlift at stage k gives the same
    stage-k data: reduce(bndlift(x,k), k) = reduce(bndlift(y,k), k). -/
```

## Source Excerpt

```lean
theorem uniqueness_from_agreement (x y k : TauIdx)
    (h : reduce x k = reduce y k) :
    reduce (bndlift x k) k = reduce (bndlift y k) k := by
  rw [extension_preserves_stage, extension_preserves_stage, h]
```

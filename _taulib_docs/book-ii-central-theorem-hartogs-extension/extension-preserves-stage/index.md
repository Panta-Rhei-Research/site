---
{
  "projection_kind": "taulib_declaration",
  "title": "extension_preserves_stage",
  "permalink": "/verify/taulib/docs/book-ii-central-theorem-hartogs-extension/extension-preserves-stage/",
  "summary_short": "`theorem` declaration in `TauLib.BookII.CentralTheorem.HartogsExtension`.",
  "declaration_id": "TauLib.BookII.CentralTheorem.HartogsExtension::extension_preserves_stage",
  "declaration_slug": "extension-preserves-stage",
  "kind": "theorem",
  "name": "extension_preserves_stage",
  "module_name": "TauLib.BookII.CentralTheorem.HartogsExtension",
  "module_url": "/verify/taulib/docs/book-ii-central-theorem-hartogs-extension/",
  "source_line_start": 265,
  "source_line_end": 268,
  "registry_ids": [
    "II.L12"
  ],
  "related_registry_items": [
    {
      "id": "II.L12",
      "title": "Extension in Split-Complex Codomain",
      "url": "/registry/object/II.L12/"
    }
  ],
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookII/CentralTheorem/HartogsExtension.lean#L265-L268",
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookII/CentralTheorem/HartogsExtension.lean#L265-L268",
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
- Source path: [`TauLib/BookII/CentralTheorem/HartogsExtension.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookII/CentralTheorem/HartogsExtension.lean#L265-L268)
- Source range: L265-L268
- Kind: `theorem`
- Formal status hint: `formalized`

## Registry Links

- `II.L12` — Extension in Split-Complex Codomain

## Immediate Comment / Docstring

```lean
/-- [II.L12] Extension preserves stage-k data: the reduction of the
    bndlift extension back to stage k recovers the original stage-k value.
    reduce(bndlift(x, k), k) = reduce(x, k).
    This follows from reduction_compat since bndlift(x, k) = reduce(x, k+1). -/
```

## Source Excerpt

```lean
theorem extension_preserves_stage (x k : TauIdx) :
    reduce (bndlift x k) k = reduce x k := by
  simp only [bndlift, reduce]
  exact Nat.mod_mod_of_dvd x (primorial_dvd (Nat.le_succ k))
```

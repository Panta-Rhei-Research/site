---
{
  "projection_kind": "taulib_declaration",
  "title": "bndlift_tower",
  "permalink": "/verify/taulib/docs/book-ii-central-theorem-hartogs-extension/bndlift-tower/",
  "summary_short": "`theorem` declaration in `TauLib.BookII.CentralTheorem.HartogsExtension`.",
  "declaration_id": "TauLib.BookII.CentralTheorem.HartogsExtension::bndlift_tower",
  "declaration_slug": "bndlift-tower",
  "kind": "theorem",
  "name": "bndlift_tower",
  "module_name": "TauLib.BookII.CentralTheorem.HartogsExtension",
  "module_url": "/verify/taulib/docs/book-ii-central-theorem-hartogs-extension/",
  "source_line_start": 281,
  "source_line_end": 285,
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
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookII/CentralTheorem/HartogsExtension.lean#L281-L285",
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookII/CentralTheorem/HartogsExtension.lean#L281-L285",
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
- Source path: [`TauLib/BookII/CentralTheorem/HartogsExtension.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookII/CentralTheorem/HartogsExtension.lean#L281-L285)
- Source range: L281-L285
- Kind: `theorem`
- Formal status hint: `formalized`

## Registry Links

- `II.T37` — Hartogs Extension Uniqueness

## Immediate Comment / Docstring

```lean
/-- [II.T37] BndLift is tower-coherent: reduce(bndlift(x, k+1), k) = reduce(x, k).
    This is the key structural property for Hartogs extension uniqueness. -/
```

## Source Excerpt

```lean
theorem bndlift_tower (x k : TauIdx) :
    reduce (bndlift x (k + 1)) k = reduce x k := by
  simp only [bndlift, reduce]
  have h : k ≤ k + 1 + 1 := Nat.le_add_right k 2
  exact Nat.mod_mod_of_dvd x (primorial_dvd h)
```

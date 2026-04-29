---
{
  "projection_kind": "taulib_declaration",
  "title": "same_equation",
  "permalink": "/verify/taulib/docs/book-v-cosmology-big-bang-regime/same-equation/",
  "summary_short": "`theorem` declaration in `TauLib.BookV.Cosmology.BigBangRegime`.",
  "declaration_id": "TauLib.BookV.Cosmology.BigBangRegime::same_equation",
  "declaration_slug": "same-equation",
  "kind": "theorem",
  "name": "same_equation",
  "module_name": "TauLib.BookV.Cosmology.BigBangRegime",
  "module_url": "/verify/taulib/docs/book-v-cosmology-big-bang-regime/",
  "source_line_start": 160,
  "source_line_end": 162,
  "registry_ids": [
    "V.P90"
  ],
  "related_registry_items": [
    {
      "id": "V.P90",
      "title": "Same-Equation Proposition",
      "url": "/registry/object/V.P90/"
    }
  ],
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookV/Cosmology/BigBangRegime.lean#L160-L162",
  "formal_status": "formalized",
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookV/Cosmology/BigBangRegime.lean#L160-L162",
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

- Module: [TauLib.BookV.Cosmology.BigBangRegime](/verify/taulib/docs/book-v-cosmology-big-bang-regime/)
- Source path: [`TauLib/BookV/Cosmology/BigBangRegime.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookV/Cosmology/BigBangRegime.lean#L160-L162)
- Source range: L160-L162
- Kind: `theorem`
- Formal status hint: `formalized`

## Registry Links

- `V.P90` — Same-Equation Proposition

## Immediate Comment / Docstring

```lean
/-- [V.P90] Same-equation proposition: the τ-Einstein equation
    R^H = κ_τ · T applies identically at all refinement depths.

    Only the boundary character's magnitude changes, not the
    equation's structure. Early ticks ≠ different physics. -/
```

## Source Excerpt

```lean
theorem same_equation (c1 c2 : RegimeBoundaryCharacter)
    (h1 : c1.same_equation = true) (h2 : c2.same_equation = true) :
    c1.same_equation = c2.same_equation := by rw [h1, h2]
```
